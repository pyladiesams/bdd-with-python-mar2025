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


@when('I click the "Add to Basket" button twice')
def step_impl(context):
    context.user.basket.add(context.current_product)
    context.user.basket.add(context.current_product)


@then(
    'my basket should show {n_items:d} line item for "{product_name}" with quantity {quantity:d}'
)
def step_impl(context, n_items: int, product_name: str, quantity: int):
    assert len(context.user.basket.items) == n_items
    assert product_name in context.user.basket.items
    assert context.user.basket.items[product_name] == quantity


@given("my basket contains 1 item with specs")
def step_impl(context):
    for row in context.table:
        print(row)
        context.user.basket.add(
            Product(name=row["name"], price=row["price"], stock=row["stock"])
        )


@when('I remove "{product_name}" from my basket')
def step_impl(context, product_name: str):
    context.user.basket.remove(product_name)


@then("my basket should be empty")
def step_impl(context):
    assert len(context.user.basket.items) == 0


@given('"Bluetooth Keyboard" is out of stock')
def step_impl(context):
    context.current_product = Product(name="Bluetooth Keyboard", price=30.99, stock=0)


@when('I try to add "Bluetooth Keyboard" to my basket')
def step_impl(context):
    try:
        context.user.basket.add(context.current_product)
    except Exception as e:
        context.error = e


@then('I should see a message "{message}"')
def step_impl(context, message: str):
    assert hasattr(context, "error"), "No error raised!"
    assert context.error.args[0] == message, "Wrong message: %s" % context.error


@then('"{product_name}" should not be in my basket')
def step_impl(context, product_name: str):
    assert product_name not in context.user.basket.items


@given("I am not logged in")
def step_impl(context):
    context.user = User(name="non-user", is_logged_in=False, basket=Basket())


@given('I add "Laptop Stand" to my basket')
def step_impl(context):
    context.user.basket.add(Product(name="Laptop Stand", price=10.99, stock=3))


@when("I view my basket")
def step_impl(context):
    context.items_list = context.user.basket.show()


@then('I should see "Laptop Stand" in my basket')
def step_impl(context):
    assert "Laptop Stand" in context.items_list


@when('I log in as "alice@example.com"')
def step_impl(context):
    context.user.with_name("alice@example.com")
