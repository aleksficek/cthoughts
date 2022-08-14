from ast import parse
from http.client import ResponseNotReady
import json
from operator import index
import re
from urllib import response
from naive import scoring
from entities import remedies, index_to_struct, name_to_index
from nltk.tokenize import word_tokenize

def parse_text(input):
    parsed_text = word_tokenize(input)
    matched = set()
    for each in parsed_text:
        if each in name_to_index:
            matched.add(each)
            index_to_struct[name_to_index[each]].count += 1

    for each in matched:
        sentiment = scoring(parsed_text, each, 5)
        index_to_struct[name_to_index[each]].scores.append(sentiment)
        # print("Sentence: ", input)
        # print("Target Word: ", each)
        # print("Score: ", sentiment)
        # print()

def final_scores():
    for structs in index_to_struct.values():
        scores = structs.scores
        print(structs.names[0] + " mean sentiment score: " + str(round(sum(scores) / len(scores), 2)) + " out of " + str(len(scores)))

def main():
    f = open('data/full.json')
    response_json = json.load(f)

    for i in range(len(response_json)):
        if not (i % 2000):
            print("Entry ", i)

        if "title" in response_json[i]:
            parse_text(response_json[i]['title'])

        if "selftext" in response_json[i]:
            parse_text(response_json[i]['selftext'])
        
        if "body" in response_json[i]:
            parse_text(response_json[i]['body'])

    print("Analysed submissions: ", len(response_json))
    final_scores()




if __name__ == "__main__":
    main()