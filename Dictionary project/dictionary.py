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
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no\n")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("There is some spelling mistake please check and retry.")
        else:
            return("Entered wrong key, Just type y or n\n")
    else:
        print("There is some spelling mistake please check and retry.")

word = input("Enter word that you want to search.\n")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)