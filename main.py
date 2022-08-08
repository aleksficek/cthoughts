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

    f = open('data/submissions.json')
    response_json = json.load(f)

    response_json[0]['title']
    response_json[0]['selftext']

    for i in range(len(response_json)):
        print(i)

        parse_text(response_json[i]['title'])

        if "selftext" in response_json[i]:
            parse_text(response_json[i]['selftext'])

        
    print("Analysed submissions: ", len(response_json))
    print("Remedy counts: ", remedies)




if __name__ == "__main__":
    main()