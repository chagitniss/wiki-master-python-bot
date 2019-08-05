NUM_GUESSES = 3

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
NUMBERS = set("1234567890")


NUMBERS_RESPONSES = ["No way I'm accepting that.",
                     "Are you kidding? you can't guess numbers or letters....",
                     "Nope! i don't accept numbers and letters",
                     "Didn't I tell you? no numbers or letters"]

CHOOSE_VALUE = ["So have you heard about {!r}?",
                "Really? what about {!r}?",
                "If so, you might know something about {!r}?",
                "Okay, I'll look for something else. heard of {!r}?", ]

INVALID_ANSWERS = "Invalid answer.\nChoose 'yes' or 'no'."

YES_ANSWERS = f"Now it's your turn.\nTry and guess {NUM_GUESSES} important words about this title!\n" \
              f"Give me your first guess"

REPEATING_GUESS = ["You have already used this word. Try another guess.", "You can't use the same word twice!"]
Expectation_button_click = False  # 0 - free input 1 - Expectation button click

TITLE_RESPONSES = ["hey, you are using the title I gave you!",
                  "You can't just reuse the title",
                  "I see what you did there...impossible!",
                  "No way I'm accepting that."]