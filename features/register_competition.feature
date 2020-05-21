Feature: Register competition
  In order to organize a competition
  As a user
  I want to register a competition along with its title, description, date when inscriptions start, date when
  inscriptions finish, date when competition starts, date when competitions finishes, categories, files and owner
  must be set to me

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a competition without file
    Given I login as user "user" with password "password"
    When I register a competition as "user"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2010-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2030-05-22                | 17:00:00                  |
    Then I'm at "competition/id/1/"
    Then I'm viewing the details page for the first competition
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2010-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2030-05-22                | 17:00:00                  |
    And There are 1 competitions


  Scenario: Try to register a competition but not logged in
    Given I'm not logged in
    When I want to register a competition
    Then Need to login to have "competition/create/" link available





