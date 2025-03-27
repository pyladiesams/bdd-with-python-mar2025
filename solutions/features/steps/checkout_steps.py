from behave import given, when, then
from behave.model import Row
from src.webshop.models import Basket, User, Product
import math


@given("a catalogue")
def step_impl(context):
    context.catalogue = {
        row["name"]: Product.model_validate(row)
        for row in map(Row.as_dict, context.table)
    }
    
@given("shipping costs")
def step_impl(context):
    context.shipping_costs = {
        row["country"]: row for row in
        map(Row.as_dict, context.table)
    }
    
@given("tax rates")
def step_impl(context):
    context.tax_rates = {
        row["country"]: row for row in
        map(Row.as_dict, context.table)
    }
    
@given("Customer Mike is a '{customer_type}' user residing in '{country}'")
def step_impl(context, customer_type: str, country: str):
    context.user = User(
        name="mike@example.com",
        is_vip=customer_type=="vip",
        country=country,
        basket=Basket()
    )
    
@when("he adds '{products}' to his basket")
def step_impl(context, products: str):
    items = products.split(",")
    for item in items:
        context.user.basket.add(
            context.catalogue[item]
        )
        

@when("checks out")
def step_impl(context):
    user: User = context.user
    context.total_payable = user.checkout(
        tax_rates=context.tax_rates,
        shipping_costs=context.shipping_costs
    )
    

@then("he sees '{amount:f}'")
def step_impl(context, amount: float):
    assert math.isclose(context.total_payable, amount), "Expected %f, got %f" % (
        context.total_payable, amount
        )