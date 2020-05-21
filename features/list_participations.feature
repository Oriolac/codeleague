Feature: List user participations
  In order to know in which competitions I have participated
  As a user
  I want to list all the competitions I have participated

  Background: There are some competitions with teams registered by same user
    Given Exists a user "user" with password "password"
    And Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists competition registered by "user"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2010-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2070-05-22                | 17:00:00                  |
      | Competition2 | Competition2 description | 2000-05-07               | 17:00:00                 | 2010-05-15                | 17:00:00                  | 2010-05-16               | 17:00:00                 | 2070-06-16                | 18:00:00                  |
      | Competition3 | Competition3 description | 2000-05-22               | 17:00:00                 | 2010-05-30                | 17:00:00                  | 2010-05-31               | 17:00:00                 | 2070-06-20                | 18:00:00                  |
    And Exists team "team1" at competition "Competition1" by "user1"
    And Exists team "team2" at competition "Competition2" by "user1"

  Scenario: List all competitions in which we have participated
    Given I login as user "user1" with password "password"
    When I view participations of user "user1"
    Then I'm at "accounts/u/2/participations/"
    Then I'm viewing a list of all competitions "user1" has participated
      | title        |
      | Competition1 |
      | Competition2 |

  Scenario: Try to list all participations in which we have participated but not logged in
    Given I'm not logged in
    When I view participations of user "user1"
    Then Need to login to have "accounts/u/2/participations/" link available