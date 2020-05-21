Feature: Register Team
  In order to create a team
  As a user
  I want to register a team in the corresponding competition along with its name

  Background: There are registered users and a competition by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists a user "user3" with password "password"
    And Exists competition registered by "user1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2022-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2023-05-22                | 17:00:00                  |

  Scenario: Register a team
    Given I login as user "user2" with password "password"
    When I register team "team1" at competition "Competition1"
    Then I'm at "competition/id/1/"
    Then There are 1 teams at competition "Competition1"

  Scenario: Try to register a team but not logged in
    Given I'm not logged in
    When I want to register a team at competition "Competition1"
    Then Need to login to have "competition/id/1/create-team/" link available
