Feature: Login

    Scenario: Successful Login
        Given The user is on the login page
        When they enter valid credentials
        Then they should see their dashboard
