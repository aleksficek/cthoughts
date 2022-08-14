import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')

from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment(parsed_review): #passes the parsed review 
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(parsed_review)
    compound = score.get('compound')
    return compound #returns the sentiment score

def scoring(word_tokens, keyword, limit=3):
    # word_tokens = word_tokenize(body) #tokenizes each review
    position = 0 #position in the review where the feature is found
    keyword_list = []
    for word in word_tokens: #for each word in the review
        if(word.find(keyword)>-1):
            keyword_list.append(position) 
        position = position + 1

    limited_sentence_list = []
    for item in range(len(word_tokens)):
        if(abs(item - keyword_list[0]) <= limit): 
            limited_sentence_list.append(word_tokens[item])
    parsed_review = ' '.join(limited_sentence_list)
    return get_sentiment(parsed_review)


def main():
    limit = 3 #the number of words on either side of the feature word used to create the window
    attribute = "cushion" #desired feature 
    reviews_list = ["I love the cushion, but hate the support.", "Even though the shoe was durable, it had very little cushion and made my feet sore after runs."] #list of product reviews
    attribute_position_list = [] #list of positions where the feature word was found in each review
    review_with_attribute_list = [] #list of review containing the feature word

    for review in reviews_list:
        word_tokens = word_tokenize(review) #tokenizes each review
        position = 0 #position in the review where the feature is found
        for word in word_tokens: #for each word in the review
            if(word.find(attribute)>-1):
                attribute_position_list.append(position) 
                review_with_attribute_list.append(word_tokens) 
            position = position + 1

    index = 0 #keeps track of which review is being parsed

    for review in review_with_attribute_list:
        limited_sentence_list = [] #list of words within the window 
        for item in range(len(review)):
            if(abs(item - attribute_position_list[index]) <= limit): 
                limited_sentence_list.append(review[item])
        parsed_review = ' '.join(limited_sentence_list)
        print(parsed_review)

        print(get_sentiment(parsed_review))
        index = index + 1

if __name__ == "__main__":
    main()