from ast import parse
from http.client import ResponseNotReady
import json
import re
from urllib import response
from naive import scoring
from entities import remedies, index_to_struct
from nltk.tokenize import word_tokenize

def parse_text(input):
    parsed_text = word_tokenize(input)
    matched = set()
    for each in parsed_text:
        if each in remedies:
            matched.add(each)
            remedies[each] += 1

    for each in matched:
        sentiment = scoring(parsed_text, each, 5)
        print("Sentence: ", input)
        print("Target Word: ", each)
        print("Score: ", sentiment)
        print()

def main():

    f = open('data/full.json')
    response_json = json.load(f)

    for i in range(len(response_json)):
        if not (i % 100):
            print("Entry ", i)

        if "title" in response_json[i]:
            parse_text(response_json[i]['title'])

        if "selftext" in response_json[i]:
            parse_text(response_json[i]['selftext'])
        
        if "body" in response_json[i]:
            parse_text(response_json[i]['body'])

    print("Analysed submissions: ", len(response_json))
    print("Remedy counts: ", remedies)




if __name__ == "__main__":
    main()