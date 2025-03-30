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
