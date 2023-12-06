Feature: Check the Login functionality

  Background:
    Given login: I am a user on the login page

  @login
  Scenario: Login is successful with valid credentials
    When login: I fill in an email "testare_web@gmail.com"
    When login: I fill in a password "testare1234"
    When login: I click the login button
    Then base: I can see my account in the menu


  @login
  Scenario: Check when email is inncorect
    When login: I fill in an email "tre_web@gil.om"
    When login: I fill in a password "tessare1234"
    When login: I click the login button
    Then login: I verify the email is wrong validation message "Invalid email address or password."