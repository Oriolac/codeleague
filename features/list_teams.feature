Feature: List all teams in a competition
  In order to keep myself up to date about teams registered in a competition
  As a user
  I want to list all the teams of a competition

  Background: There are registered users and 3 teams of a competition
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists a user "user3" with password "password"
    And Exists competition registered by "user1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2010-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2030-05-22                | 17:00:00                  |
    And Exists team "team1" at competition "Competition1" by "user2"
    And Exists team "team2" at competition "Competition1" by "user3"

  Scenario: List all teams of a competition
    Given I login as user "user1" with password "password"
    When I visit the competition with title "Competition1"
    Then I'm viewing a list containing all the teams of the competition
      | name   |
      | team1  |
      | team2  |

  Scenario: Try to list teams of a competition but not logged in
    Given I'm not logged in
    When I visit the competition with title "Competition1"
    Then Redirect to login to have "competition/id/1/" link available

