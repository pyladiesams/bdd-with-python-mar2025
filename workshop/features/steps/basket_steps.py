from behave import given, then, when
from src.webshop.models import Basket, Product, User


@given("I am a logged-in customer")
def step_impl(context):
    context.user = User(name="Mike", basket=Basket())


@given(
    'I am viewing the product page for "{product_name}", costing {price}, with {stock} in stock'
)
def step_impl(context, product_name: str, price: float, stock: int):
    context.current_product = Product(name=product_name, price=price, stock=stock)


@when('I click the "Add to Basket" button')
def step_impl(context):
    context.user.basket.add(context.current_product)


@then('"{product_name}" should be in my basket')
def step_impl(context, product_name: str):
    assert product_name in context.user.basket.items
    assert context.user.basket.items[product_name] == 1


@then('the basket should show a total price of "${price:f}"')
def step_impl(context, price: float):
    assert context.user.basket.total == price
