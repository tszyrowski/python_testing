
Feature: Show table as data passed to test function
  I want to make example of using data 

  Scenario: using different users scenario
    Given a set of specific users
    		| name			| department 	|
    		| Barry			| Beer Cans		|
    		| Pudey			| Silly Walks |
    		| Two-Lump 	| Silly Walks |
    		
    When we count the number of people in each department
    Then we eill find two people in "Silly Wals"
    But we will find one person in "Beer Cans"
