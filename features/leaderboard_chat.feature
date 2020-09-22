@leaderboard
Feature: Leaderboard
  @leaderboard.basic
  Scenario: Basics
    When Fendy says "@emojirade leaderboard"
    When Fendy says "@emojirade leaderboard weekly"
    When Fendy says "@emojirade leaderboard monthly"
    When Fendy says "@emojirade leaderboard all time"

  @leaderboard.with_on_date
  Scenario: With on_date
    When Dave says "@emojirade leaderboard weekly 20200701"
    When Dave says "@emojirade leaderboard monthly 20200615"
