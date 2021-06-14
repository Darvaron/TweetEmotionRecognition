import json


def get_text(tweet):
    '''
    Extracts relevant data from a tweet, it looks up if there's any of the required words (i, and, ...) of the tweet,
    if don't ignores it, deletes words that contains some special characters such as / @ ... and so on,
    if the final text doesn't have more tan 5 words it won't be returned
    :param tweet: json file in string
    :return: processed text ready to be used on the RNN
    '''
    tweet_json = json.loads(tweet)
    text = ''
    if 'text' in tweet_json:  # If it contains text
        text = tweet_json['text']
        # print(tweet_json)
        listwords = text.split(' ')
        special_char = ['/', '@', 'RT', '...']
        required_words = ['a', 'the', 'i', 'you', 'u', 'and']
        if any(rw in w for rw in required_words for w in listwords):  # if contains required words
            text = [w for w in listwords if not any(ch in w for ch in special_char)]  # deletes special characters
            if len(text) > 5:  # if the text is longer than 5 words
                text = ' '.join(text)
            else:
                text = ''
    return text
