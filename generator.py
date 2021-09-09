#!/usr/bin/env python3

from aitextgen import aitextgen

def generate_demographics():
    return {
        'first_name' : "John",
        'last_name' : "Smith",
        'pronoun' : "he",
        'pronoun_posessive' : "his",
        'city' : "Austin",
    }

def run_model():

    demographics = generate_demographics()

    ai = aitextgen()

    for _ in range(10):
        raw_text = f"{demographics['first_name']}'s wife told me {demographics['pronoun']} drove her to the abortion clinic in {demographics['city']}. Apparently she had sex with {demographics['first_name']} out of wedlock, and decided not to keep the baby."
        generated = ai.generate(n=10, prompt=raw_text, return_as_list=True)
        for example in generated:
            example = example.lstrip(raw_text)
            relevant = example.strip().splitlines()[0]
            print(relevant)

if __name__ == '__main__':
    run_model()
