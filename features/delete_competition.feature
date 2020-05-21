Feature: Delete competition
  In order to stop organizing a competition
  As a user
  I want to delete a competition I have created

  Background: There are registered users and competitions registered
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists competition registered by "user1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2010-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2010-05-22                | 17:00:00                  |
      | Competition2 | Competition1 description | 2000-05-01               | 17:00:00                 | 2010-05-03                | 17:00:00                  | 2010-05-09               | 17:00:00                 | 2020-05-13                | 17:00:00                  |

  Scenario: Delete owned competition
    Given I login as user "user1" with password "password"
    When I delete the competition with name "Competition1"
    Then I'm at "competition/"
    Then I'm viewing a list containing 1 competitions
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition2 | Competition1 description | 2000-05-01               | 17:00:00                 | 2010-05-03                | 17:00:00                  | 2010-05-09               | 17:00:00                 | 2020-05-13                | 17:00:00                  |
    And The list contains 1 competition

  Scenario: Try to delete not owned competition
    Given I login as user "user2" with password "password"
    When I want to delete the competition "Competition1"
    Then There is 403 Forbidden

  Scenario: Try to delete an owned competition but not logged in
    Given I'm not logged in
    When I want to delete the competition "Competition1"
    Then Need to login to have "competition/id/1/delete/" link available