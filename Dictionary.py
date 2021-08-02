import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("\nDid you mean %s instead\n" %get_close_matches(word, data.keys())[0])
        decide = input("\nPress y for yes or n for no\n")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("\npugger your paw steps on wrong keys \n")
        else:
            return("\nYou have entered wrong input please enter just y or n\n")
    else:
        print("\npugger your paw steps on wrong keys\n")



word = input("\nEnter the word you want to search\n")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



