import random

import json

# Jokes dataset

jokes = [

    {"id": 1, "joke": "Why don't scientists trust atoms? Because they make up everything."},

    {"id": 2, "joke": "Why was the math book sad? Because it had too many problems."},

    {"id": 3, "joke": "Why did the scarecrow win an award? Because he was outstanding in his field."},

    {"id": 4, "joke": "What do you call a fake noodle? An impasta."},

    {"id": 5, "joke": "Why did the bicycle fall over? Because it was two-tired."},

]

# API endpoint to generate a random joke

def generate_joke():

    random_joke = random.choice(jokes)

    return json.dumps(random_joke)

# Example usage

if __name__ == "__main__":

    print(generate_joke())