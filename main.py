from ast import parse
from http.client import ResponseNotReady
import json
import re
from urllib import response

symptoms = {}
remedies = {
    'niacin': 0,
    'nac': 0,
    'ginko': 0,
    'quercetin': 0,
    'nattokinase': 0,
    'natto': 0,
    'zinc': 0,
    'probiotics':0,
    'prebiotics':0,
    'antihistamines':0,
}

def parse_text(input):
    parsed_text = re.findall(r"[\w']+|[.,!?;]", input.lower())
    for each in parsed_text:
        if each in remedies:
            remedies[each] += 1

def main():

    f = open('data/full.json')
    response_json = json.load(f)

    for i in range(len(response_json)):
        if not (i % 100):
            print("Entry ", i)

        print(i)

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