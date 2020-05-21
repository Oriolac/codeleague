Feature: Detail competition
  In order to know more about a competition
  As a user
  I want to be able t know the title and the description about the competition

  Background: There are some competitions
    Given Exists a user "user" with password "password"
    And Exists competition registered by "user"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2030-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2050-05-22                | 17:00:00                  |
      | Competition2 | Competition2 description | 2000-05-07               | 17:00:00                 | 2030-05-15                | 17:00:00                  | 2010-05-16               | 17:00:00                 | 2050-06-16                | 18:00:00                  |
      | Competition3 | Competition3 description | 2000-05-22               | 17:00:00                 | 2030-05-30                | 17:00:00                  | 2010-05-31               | 17:00:00                 | 2050-06-20                | 18:00:00                  |

  Scenario: Show competition information
    Given I login as user "user" with password "password"
    When I visit the competition with title "Competition1"
    Then I'm at "competition/id/1/"
    Then I view all the competition information of "Competition1"
      | title        | description              |
      | Competition1 | Competition1 description |

  Scenario: Try to see the information of a competition but not logged in
    Given I'm not logged in
    When I visit the competition with title "Competition1"
    Then Redirect to login to have "competition/id/1/" link available