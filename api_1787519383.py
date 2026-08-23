import hashlib

import json

import os

import random

import string

from typing import Dict, List

class JokeGenerator:

    def __init__(self, db_file: str = 'jokes.db'):

        self.db_file = db_file

        self.jokes = self.load_jokes()

    def load_jokes(self) -> Dict[str, str]:

        if os.path.exists(self.db_file):

            with open(self.db_file, 'r') as f:

                return json.load(f)

        else:

            return {}

    def save_jokes(self) -> None:

        with open(self.db_file, 'w') as f:

            json.dump(self.jokes, f)

    def generate_joke(self) -> str:

        # Simple joke generation using templates

        templates = [

            '{} को {} कहा जाता है क्योंकि {}',

            '{} क्योंकि {} है {}',

            '{} जब {} हो जाता है तो {}',

        ]

        subjects = ['आदमी', 'औरत', 'बच्चा', 'कुत्ता', 'बिल्ली']

        verbs = ['हंसता', 'रोता', 'चलता', 'दौड़ता', 'सोता']

        objects = ['पानी', 'आग', 'हवा', 'मिट्टी', 'पेड़']

        template = random.choice(templates)

        joke = template.format(

            random.choice(subjects),

            random.choice(verbs),

            random.choice(objects),

        )

        return joke

    def generate_unique_joke(self) -> str:

        while True:

            joke = self.generate_joke()

            joke_hash = hashlib.sha256(joke.encode()).hexdigest()

            if joke_hash not in self.jokes.values():

                return joke, joke_hash

    def add_joke(self, joke: str, joke_hash: str) -> None:

        joke_id = str(len(self.jokes) + 1)

        self.jokes[joke_id] = joke_hash

        self.save_jokes()

    def get_joke(self) -> str:

        if self.jokes:

            joke_id = random.choice(list(self.jokes.keys()))

            joke_hash = self.jokes[joke_id]

            # For simplicity, we'll just generate a new joke if we can't find the old one

            joke = self.generate_joke()

            return joke

        else:

            joke, joke_hash = self.generate_unique_joke()

            self.add_joke(joke, joke_hash)

            return joke

    def validate_joke(self, joke: str) -> bool:

        # Simple validation: check if joke is not empty and has a valid hash

        if not joke:

            return False

        joke_hash = hashlib.sha256(joke.encode()).hexdigest()

        return joke_hash not in self.jokes.values()

def main():

    generator = JokeGenerator()

    while True:

        joke = generator.get_joke()

        print(joke)

if __name__ == '__main__':

    main()