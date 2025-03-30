Feature:
    As a customer,
    When I check out, I want to see the total payable amount,
    depending on my status, residence and tax obligations.

    Background: Example catalogue, tax and shipping specifications
        Given a catalogue
            | name                      | price | stock | category    |
            | Wireless Mouse            | 29.99 | 10    | electronics |
            | Automate the Boring Stuff | 50.99 | 10    | books       |

        And shipping costs
            | country | not_vip | vip  |
            | NL      | 2.99    | 0    |
            | DE      | 6.99    | 0    |
            | UK      | 10.99   | 2.99 |

        And tax rates
            | country | books     | electronics     |
            | NL      | 0.1       | 0.1             |
            | DE      | 0.05      | 0.15            |
            | UK      | 0.1       | 0.125           |

    Scenario Outline: Checkout Registered Users
        Given Customer Mike is a '<type>' user residing in '<country>'
        When he adds '<products>' to his basket
        And checks out
        Then he sees '<amount>'

        Examples:
            | type     | country | products                                 | amount |
            | standard | NL      | Wireless Mouse,Automate the Boring Stuff | 92.07  |
            | vip      | DE      | Wireless Mouse,Automate the Boring Stuff | 88.03  |
            | standard | UK      | Automate the Boring Stuff                | 67.08  |

