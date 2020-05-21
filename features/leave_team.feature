Feature: Leave Team
  In order to leave a team in which we are in
  As a user
  I want to leave the team

  Background: There are registered users and a team by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists competition registered by "user1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2030-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2070-05-22                | 17:00:00                  |
    And Exists team "team1" at competition "Competition1" by "user2"

  Scenario: Leave my team
    Given I login as user "user2" with password "password"
    When I leave team "team1" at competition "Competition1"
    Then There are 0 teams at competition "Competition1"

  Scenario: Try to leave a team but not logged in
    Given I'm not logged in
    When I want to leave at competition "Competition1"
    Then Redirect to login to have "competition/id/1/" link available
