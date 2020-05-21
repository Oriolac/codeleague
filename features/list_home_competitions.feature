Feature: List competitions
  In order to keep myself up to date about competitions which will be held recently
  As a user
  I want to list the 6 competitions that are in progress and will be the next to end

  Background: There are 7 registered competitions by same user
    Given Exists a user "user" with password "password"
    And Exists competition registered by "user"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2000-05-09               | 17:00:00                 | 2010-05-20                | 17:00:00                  | 2010-05-21               | 17:00:00                 | 2050-05-22                | 17:00:00                  |
      | Competition2 | Competition2 description | 2000-05-07               | 17:00:00                 | 2010-05-15                | 17:00:00                  | 2010-05-16               | 17:00:00                 | 2050-06-16                | 18:00:00                  |
      | Competition3 | Competition3 description | 2000-05-22               | 17:00:00                 | 2010-05-30                | 17:00:00                  | 2010-05-31               | 17:00:00                 | 2050-06-20                | 18:00:00                  |
      | Competition4 | Competition4 description | 2000-05-23               | 17:00:00                 | 2010-05-27                | 17:00:00                  | 2010-05-28               | 17:00:00                 | 2050-05-29                | 17:00:00                  |
      | Competition5 | Competition5 description | 2000-05-26               | 17:00:00                 | 2010-05-30                | 17:00:00                  | 2010-05-31               | 17:00:00                 | 2050-06-01                | 18:00:00                  |
      | Competition6 | Competition6 description | 2000-06-02               | 17:00:00                 | 2010-06-05                | 17:00:00                  | 2010-06-06               | 17:00:00                 | 2050-06-06                | 18:00:00                  |
      | Competition7 | Competition7 description | 2000-06-12               | 17:00:00                 | 2010-06-20                | 17:00:00                  | 2010-06-21               | 17:00:00                 | 2050-06-24                | 18:00:00                  |


  Scenario: List 6 competitions that will be the most recent to end
    Given I login as user "user" with password "password"
    When I am at "league:home" page
    And The list contains 6 competitions
      | title        |
      | Competition1 |
      | Competition2 |
      | Competition3 |
      | Competition4 |
      | Competition5 |
      | Competition6 |

  Scenario: Try to list 6 most recent to end competitions but not logged in
    Given I'm not logged in
    When I am at "league:home" page
    Then There is no competitions at page
      | title        |
      | Competition1 |
      | Competition2 |
      | Competition3 |
      | Competition4 |
      | Competition5 |
      | Competition6 |
