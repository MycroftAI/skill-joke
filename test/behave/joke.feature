Feature: mycroft-jokes

  Scenario Outline: Tell any joke
    Given an english speaking user
     When the user says "<tell me a joke>"
     Then "mycroft-joke" should reply with anything

  Examples: request any joke
    | tell me a joke |
    | tell me a joke |
    | make me laugh |
    | brighten my day |
    | got any jokes |

  Scenario Outline: Tell Chuck Norris joke
    Given an english speaking user
     When the user says "<tell me a chuck norris joke>"
     Then mycroft reply should contain "chuck norris"

  Examples: request a chuck norris joke
    | tell me a chuck norris joke |
    | tell me a chuck norris joke |
    | joke about chuck |
    | chuck norris joke |

  Scenario Outline: Tell neutral joke
    Given an english speaking user
     When the user says "<tell me a neutral joke>"
     Then "mycroft-joke" should reply with anything

  Examples: request a neutral joke
    | tell me a neutral joke |
    | tell me a neutral joke |
    | geeky joke |
    | do you have any non-offensive jokes |


