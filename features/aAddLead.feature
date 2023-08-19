Feature: Adding Lead
  Scenario: Add lead with mandatory fields
    Given user navigates to login page
    When user enters login details mail as "manoj.assetmonk@gmail.com" and password as "Propflo@1234"
    And click login button
    And click on sales and inside that clicks leads
    And click Add Lead option
    And enters mandatory fields in add leads page
    |firstname  |lastname      |  mobile         |email             | description |
    |RGV   |  kumar    | 9177731192    | rgv@gmail.com  |eager to buy |
    And click on save button
    Then the lead details should added successfully

  Scenario: create task
    When click on tasks bar
    And click on create task
    And write task and set task details
    | textbox              | time       |
    | site visit tomorrow  | 1530       |
    And click task save
    Then ckeck task is created or not

  Scenario: Add notes
    When clickon Notes taskbar
    And click on create notes
    And write description in notes and save
    |notesDescription|
    |today he is busy tommorow site vist wee can go |
    Then check the note is created or not