import csv
from random import randrange
import wikipedia
import settings
import random



# wikipedia.set_lang("he")
wikipedia.set_lang("en")

global row

with open("minimal_data.csv", "r", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=",")
    row = [row for idx, row in enumerate(reader)]


def get_random_title():

    rand = randrange(1, 955)
    title = row[rand][0]

    return title


def get_page_content(title)->str:
    page_content = wikipedia.summary(title)
    return page_content


def test_word(word):
    word = word.lower()

    if settings.Expectation_button_click:

        if word == "yes":
            settings.Expectation_button_click = False
            settings.page_content = get_page_content(settings.page_title)
            return settings.YES_ANSWERS

        elif word == "no":
            settings.page_title = get_random_title()
            message = random.choice(settings.CHOOSE_VALUE).format(settings.page_title)
            return message

        else:
            return settings.INVALID_ANSWERS

    else:
        return None





