import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition_of(word):
    # return data.get(word.lower(), "The word doesn't exist. Please double check it.")
    word = word.lower()

    if word in data:
        show_definitions(data[word])
    elif word.title() in data:
        show_definitions(data[word.title()])
    elif word.upper() in data:
        show_definitions(data[word.upper()])
    else:
        matches = get_close_matches(word, data.keys());
        if len(matches) > 0:
            confirmation = input(f"Did you mean {matches[0]} instead? Y if Yes, or N if No: ")
            if confirmation.lower() == 'y':
                definition_of(matches[0])
                return

        show_definitions(["The word doesn't exist. Please double check it."])

def show_definitions(words):
    for word in words:
        print(word)

word = input("Enter word: ")
definition_of(word)
