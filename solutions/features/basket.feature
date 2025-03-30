Feature: Shopping Basket Management

  As a customer
  I want to manage items in my shopping basket
  So that I can review and purchase them later

  Scenario: Adding an item to the basket
    Given I am a logged-in customer
    And I am viewing the product page for "Wireless Mouse", costing 25.99, with 10 in stock
    When I click the "Add to Basket" button
    Then "Wireless Mouse" should be in my basket
    And the basket should show a total price of "$25.99"

  Scenario: Adding the same item multiple times increases quantity
    Given I am a logged-in customer
    And I am viewing the product page for "Wireless Mouse", costing 25.99, with 10 in stock
    When I click the "Add to Basket" button twice
    Then my basket should show 1 line item for "Wireless Mouse" with quantity 2
    And the basket should show a total price of "$51.98"

  Scenario: Removing an item from the basket
    Given I am a logged-in customer
    And my basket contains 1 item with specs:
    | name            | price | stock |
    | Wireless Mouse  | 25.99 | 10    |
    When I remove "Wireless Mouse" from my basket
    Then my basket should be empty
    And the basket should show a total price of "$0.00"

  Scenario: Prevent adding out-of-stock item
    Given I am a logged-in customer
    And "Bluetooth Keyboard" is out of stock
    When I try to add "Bluetooth Keyboard" to my basket
    Then I should see a message "This item is out of stock!"
    And "Bluetooth Keyboard" should not be in my basket

  Scenario: Temporary basket for guest users
    Given I am not logged in
    And I add "Laptop Stand" to my basket
    When I view my basket
    Then I should see "Laptop Stand" in my basket

  Scenario: Merge guest basket with user account on login
    Given I am not logged in
    And I add "Laptop Stand" to my basket
    When I log in as "alice@example.com"
    And I view my basket
    Then I should see "Laptop Stand" in my basket
