import csv
from collections import defaultdict
from random import randrange
import wikipedia
import settings
import random


def get_titles():
    with open("minimal_data.csv", "r", encoding='utf-8') as f:
        reader = csv.reader( f, delimiter=",")
        rows = [row for idx, row in enumerate(reader)]
        return rows


class Pages:

    def __init__(self):
        # wikipedia.set_lang("he")
        wikipedia.set_lang("en")
        self.titles = get_titles()

    def get_random_title(self):
        rand = randrange(1, 955)
        title = self.titles[rand][0]
        return title

    def get_page_summary(self, title)->str:
        page_content = wikipedia.summary(title)
        return page_content


class Game:

    def __init__(self):
        self.users_info_dict = defaultdict()
        self.pages = Pages()

    def add_user(self, id):
        self.users_info_dict[id] = defaultdict()
        self.users_info_dict[id]['state'] = "button_click"
        self.users_info_dict[id]['good_guesses'] = 0
        self.users_info_dict[id]['wrong_guesses'] = 0
        self.users_info_dict[id]['score'] = 0
        self.users_info_dict[id]['played_guesses'] = []

    def get_page_title(self, id):
        self.users_info_dict[id]['page_title'] = self.pages.get_random_title()
        return self.users_info_dict[id]['page_title']

    def get_page_content(self, id):
        content = wikipedia.page(self.users_info_dict[id]['page_title'])
        self.users_info_dict[id]['page_content'] = content

    def test_button_click(self, word, id):  #when user click button
        word = word.lower()

        if self.users_info_dict[id]['state'] == "button_click":

            if word == "yes":
                self.users_info_dict[id]['state'] = "playing"
                self.get_page_content(id)
                return settings.YES_ANSWERS

            elif word == "no":
                self.get_page_title(id)
                page_title = self.users_info_dict[id]['page_title']
                message = random.choice(settings.CHOOSE_VALUE).format(page_title)
                return message

            else:
                return settings.INVALID_ANSWERS

        else:
            return "Clicking a button is invalid now."

    def test_word(self, text, id):
        text = text.lower()

        if self.users_info_dict[id]['state'] == "button_click":
            return settings.INVALID_ANSWERS

        if text in settings.LETTERS or set(text).issubset(settings.NUMBERS):
            return random.choice(settings.NUMBERS_RESPONSES)

        split = text.split()
        for w in split:
            if w in self.users_info_dict[id]['played_guesses']:
                return random.choice(settings.REPEATING_GUESS)

        for k in self.users_info_dict[id]['page_title'].lower().split():
            if text == k:
                return random.choice(settings.TITLE_RESPONSES)

        else:
            return text



