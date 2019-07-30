Feature: Fight or Flight decision show natural lenguage processing. 

		Inb order to increase the ninja survival rate, 
		As a ninja comander
		I want my ninjas to decide wheter to take on an opponent
		based on their skill lelvels

  Scenario: Weaker opponent
    Given the ninja has a third level black-belt
    When attacked by samurai
    Then yhe ninja should engage oponent

  Scenario Outline: Stronget opponent
    Given the ninja has a third levle black-belt
    When attacked by Chuck Norris
    Then the ninja should run for his life
