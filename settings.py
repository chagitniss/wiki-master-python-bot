WRONG_GUESSES = 3
GOOD_GUESSES = 3
POINTS_PER_GOOD_GUESS = 10
POINTS_PER_WRONG_GUESS = -5


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

YES_ANSWERS = f"Now it's your turn.\nTry and guess {GOOD_GUESSES} important words about this title!\n" \
              f"Give me your first guess"

REPEATING_GUESS = ["You have already used this word. Try another guess.", "You can't use the same word twice!"]

TITLE_RESPONSES = ["hey, you are using the title!",
                  "You can't just reuse the title",
                  "I see what you did there...impossible!",
                  "No way I'm accepting that."]

COMMON_RESPONSES = ["C'mon, This word is way too common...",
                    "Nah, Be more original with your words.",
                    "I want some good content, Buddy. Too common",
                    "This word is toooooo common",
                    "Don't just give me every day words."]


SUCCESS_RESPONSES = ["Way to go! you'll finish in {} guesses.",
                     "Alrighty! only {} words to guess.",
                     "You Rock! guess me {} more.",
                     "Your Knowledge is astounding. only {} more words",
                     "I worship your brain! c'mon {} and you're done."]


WIN_MESSAGE = ["You win!!!!!\nYour score is {}.\nurl{}", "and that's a win! with a score of {}\nurl{}",
                 "BAM! win! with {} points this round.\nurl{}",
                 "clap your hands for this one! you won this round with {} points.\nurl{}",
                 "aaaaand you win! {} points earned this round! \nurl{}"]


LOSE_MESSAGE = ["Unfortunately, You failed this round.\n Your score is {}\nwould you like to hear about this jsa? url{}",
                "Bad news, game failure. You're out with a score of {}.\nwanna learn about it? url{}",
                "What a shame, you failed. maybe next round.\nyou got {} points.url{}",
                "So did you really know this one? I guess not, you failed! \n{} points for you. url{}"]


FAIL_MESSAGE = ["Nope! You're wrong. tries left: {}",
                "Wrong! watch out! only {} wrong guesses left",
                "That is a mistake... only {} more like that.",
                "Nah, Not a good guess this one. {} more mistakes",
                "You sure you know it? only {} errors left."]

HELP_MESSAGE = "Hello! I am the WikiMaster bot.\n" \
               "This game I suggest is for those who want to prove their knowledge at any price,\n" \
               "Even at a heavy price of playing against Wikipedia, the site that knows everything!\n" \
               "Guess three words related to the Wikipedia title I'll get you.\n" \
               "10 points for correct guessing.\n" \
               "watch out! You have only 3 options to make mistakes,\n" \
               "And five points are reduced for each mistake.\nclick to play!"
