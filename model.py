import csv
import re
from collections import defaultdict
from random import randrange
import wikipedia
import settings
import random


def get_titles():
    with open("minimal_data.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        rows = [row for idx, row in enumerate(reader)]
        return rows


def common_words_parser():
    common_words = set()
    with open("common_words.txt", 'r') as f:
        for word in f:
            common_words.add(word[:-1])
    return common_words


def extract_win_gifs():
    win_gifs = []
    with open("win_gifs.txt", "r") as f:
        for url in f.readlines():
            win_gifs.append(url)
    return win_gifs


def extract_fail_gifs():
    fail_gifs = []
    with open("fail_gifs.txt", "r") as f:
        for url in f.readlines():
            fail_gifs.append(url)
    return fail_gifs


class DB:

    def __init__(self):
        # wikipedia.set_lang("he")
        wikipedia.set_lang("en")
        self.titles = get_titles()
        self.common_words = common_words_parser()
        self.win_gifs = extract_win_gifs()
        self.fail_gifs = extract_fail_gifs()

    def get_random_title(self):
        rand = randrange(1, 955)
        title = self.titles[rand][0]
        return title

    def get_page_summary(self, title)->str:
        page_content = wikipedia.summary(title)
        return page_content

    def get_random_win_gif(self):
        return random.choice(self.win_gifs)

    def get_random_fail_gif(self):
        return random.choice(self.fail_gifs)


class Game:

    def __init__(self):
        self.users_info_dict = defaultdict()
        self.db = localDB()

    def add_user(self, id):
        self.users_info_dict[id] = defaultdict()
        self.users_info_dict[id]['state'] = "button_click"
        self.users_info_dict[id]['good_guesses'] = 0
        self.users_info_dict[id]['wrong_guesses'] = 0
        self.users_info_dict[id]['score'] = 0
        self.users_info_dict[id]['played_guesses'] = []

    def get_page_title(self, id):
        self.users_info_dict[id]['page_title'] = self.db.get_random_title()
        return self.users_info_dict[id]['page_title']

    def get_page_content(self, id):
        content = wikipedia.page(self.users_info_dict[id]['page_title'])
        self.users_info_dict[id]['page_content'] = content

    def get_info(self, id):
        return wikipedia.summary(self.users_info_dict[id]['page_title'], sentences=3) + '\n' + self.users_info_dict[id][
            'page_content'].url

    def text_search(self, text, page_content):
        if re.search(r"\b" + re.escape(text) + r"\b", page_content):
            return True
        return False

    def test_button_click(self, word, id):  # when user click button
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

        if text in self.db.common_words:
            return random.choice(settings.COMMON_RESPONSES)

        # ------ finally, good word ----------
        if self.text_search(text, self.users_info_dict[id]['page_content'].content.lower()):  # The word does appear
                                                                                            # on the Wikipedia page
            [self.users_info_dict[id]['played_guesses'].append(w) for w in split]
            self.users_info_dict[id]["score"] += settings.POINTS_PER_GOOD_GUESS

            self.users_info_dict[id]["good_guesses"] += 1

            if self.users_info_dict[id]["good_guesses"] == settings.GOOD_GUESSES:  # win the game!
                curr_score = self.users_info_dict[id]['score']
                link = self.db.get_random_win_gif()
                return random.choice(settings.WIN_MESSAGE).format(curr_score, link)

            remained_guesses = settings.GOOD_GUESSES - self.users_info_dict[id]['good_guesses']
            return random.choice(settings.SUCCESS_RESPONSES).format(remained_guesses)

        else:  # The word does not appear on the Wikipedia page
            self.users_info_dict[id]["wrong_guesses"] += 1
            self.users_info_dict[id]["score"] += settings.POINTS_PER_WRONG_GUESS

            if self.users_info_dict[id]['wrong_guesses'] == settings.WRONG_GUESSES:  # fail the game...
                curr_score = self.users_info_dict[id]['score']
                link = self.db.get_random_fail_gif()
                return random.choice(settings.LOSE_MESSAGE).format(curr_score, link)

            curr_score = settings.WRONG_GUESSES - self.users_info_dict[id]['wrong_guesses']
            return random.choice(settings.FAIL_MESSAGE).format(curr_score)





