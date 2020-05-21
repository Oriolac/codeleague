Feature: Edit competition
  In order to keep updated the information of a competition for the users
  As a user
  I want to edit a competition register I created

  Background: There are registered users and a competition by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists competition registered by "user1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2030-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2070-05-22                | 17:00:00                  |

  Scenario: Edit owned competition registry description
    Given I login as user "user1" with password "password"
    When I edit the competition with name "Competition1"
      | description                 |
      | description of Competition1 |
    Then I'm at "competition/id/1/"
    Then I view all the competition information of "Competition1"
      | title        | description              |
      | Competition1 | Competition1 description |
    And there are 1 competitions

  Scenario: Try to edit competition but not logged in
    Given I'm not logged in
    When I want to edit the competition with name "Competition1"
    Then Need to login to have "competition/id/1/edit/" link available

  Scenario: Try to edit competition but not the owner no edit button
    Given I login as user "user2" with password "password"
    When I want to edit the competition with name "Competition1"
    Then There is 403 Forbidden