Feature: List all competitions of a category
  In order to find out the competitions about topics we like the most
  As a user
  I want to list all the competitions that belong to a category

  Background: There are 2 competitions of a category registered by same user
    Given Exists a user "user" with password "password"
    And Exists a category "category1" with description "category1 description"
    And Exists a category "category2" with description "category2 description"
    And Exists competition registered by "user"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 | categories |
      | Competition1 | Competition1 description | 2010-05-09               | 17:00:00                 | 2030-05-20                | 17:00:00                  | 2015-05-21               | 17:00:00                 | 2040-05-22                | 17:00:00                  | category1  |
      | Competition2 | Competition2 description | 2010-05-07               | 17:00:00                 | 2030-05-15                | 17:00:00                  | 2015-05-16               | 17:00:00                 | 2040-06-16                | 18:00:00                  | category1  |
      | Competition3 | Competition3 description | 2010-05-22               | 17:00:00                 | 2030-05-30                | 17:00:00                  | 2015-05-31               | 17:00:00                 | 2040-06-20                | 18:00:00                  | category2  |

  Scenario: List all competitions that belong to a category
    Given I login as user "user" with password "password"
    When I list all competitions of category "category1"
    Then I'm at "category/"
    Then I'm viewing a list containing all the competitions from category "category1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 | categories |
      | Competition1 | Competition1 description | 2010-05-09               | 17:00:00                 | 2030-05-20                | 17:00:00                  | 2015-05-21               | 17:00:00                 | 2040-05-22                | 17:00:00                  | category1  |
      | Competition2 | Competition2 description | 2010-05-07               | 17:00:00                 | 2030-05-15                | 17:00:00                  | 2015-05-16               | 17:00:00                 | 2040-06-16                | 18:00:00                  | category1  |

  Scenario: Try to list all competition of a category but not logged in
    Given I'm not logged in
    When I want to list all competitions of category "category1"
    Then Need to login to have "category/" link available