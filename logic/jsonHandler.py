import json
import re
import time

not_identified = []
counter_not_identified = 0


def transform_word(string_v):
    '''
    Trasforms string_v into a valid str to make predictions using the model
    :param string -- char from word or entire tweet
    :param case -- case to be analyzed
    :return: case_number -- represents the case of the given tweet or word
    :return: transformed -- transformed word to be used by the model
    '''

    global not_identified, counter_not_identified

    # case: -1 default, 1 word, 2 user, 3 url, 4 hashtag
    case_number = -1

    # Removing special chars at the end
    invalid = [',', '\'', '.', ';', ':', '‘', '’', '"', "'", '!']

    try:
        if string_v[-1] in invalid:
            string_v = string_v[:-1]
    except:
        print('Non valid -1 char: {}'.format(string_v))

    word = re.search('^([a-z])+$', string_v)  # word
    if word:
        case_number = 1
    else:
        user = re.search('^([@])([a-zA-Z0-9_]){5,16}$', string_v)  # user

        if user:
            case_number = 2
        else:
            url = re.search(
                r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",
                string_v)  # url
            if url:
                case_number = 3
            else:
                hashtag = re.search('^(#)([a-zA-Z0-9_])+$', string_v)  # hashtag
                if hashtag:
                    case_number = 4
                else:
                    # print('Word: {} not identified'.format(string_v))
                    not_identified.append(string_v)
                    counter_not_identified += 1
                    if counter_not_identified % 10 == 0:
                        print('\nWords don\'t identified:\nnot identified: {}\n'.format(not_identified))
                        time.sleep(3)
                    # raise Exception('Word {} not identified: '.format(string_v))
    case_dict = {
        -1: string_v,
        1: string_v,
        2: '<usermention>',
        3: '<url>',
        4: '<hashtag>'
    }
    transformed = case_dict[case_number]

    return transformed


def get_text(tweet):
    '''
    Extracts relevant data from a tweet, it looks up if there's any of the required words (i, and, ...) of the tweet,
    if don't ignores it, deletes words that contains some special characters such as / @ ... and so on,
    if the final text doesn't have more tan 5 words it won't be returned
    :param tweet: json file in string
    :return: processed text ready to be used on the RNN
    '''
    # print('Loading tweet ...\n')

    tweet_json = json.loads(tweet)

    '''
    Falta arreglar la siguiente sección de código y sección not identified y error 
     raise ProtocolError("Connection broken: %r" % e, e)
    urllib3.exceptions.ProtocolError: ('Connection broken: IncompleteRead(0 bytes read)', IncompleteRead(0 bytes read))
    '''
    ##################################################################################
    # if hasattr(tweet_json, "retweeted_status"):  # Check if Retweet
    try:
        print('A')
        original = tweet_json["retweeted_status"]['extended_tweet']["full_text"]
    except:
        try:
            print('B')
            original = tweet_json["retweeted_status"]["text"]
        # else:
        except:
            try:
                print('C')
                original = tweet_json['extended_tweet']["full_text"]
            except:
                print('D')
                original = tweet_json["text"]
    ##################################################################################
    # try:
    # #if 'extended_tweet' in tweet_json:  # If it contains text
    #     original = tweet_json['extended_tweet']['full_text']
    #     #print('Extended ', end='')
    # except:
    # #else:
    #     original = tweet_json['text']

    text = original.lower().split(' ')
    text = [w.replace('\n', ' ') for w in text[:-1]] + [text[-1].replace('\n', '')]  # replaces \n
    transformed_text = [transform_word(w) for w in text]
    transformed_text = ' '.join(transformed_text)
    print('Tweet: {}'.format(original))
    # print('Transformed: {}'.format(transformed_text))

    return transformed_text

# def get_text(tweet):
#     '''
#     Extracts relevant data from a tweet, it looks up if there's any of the required words (i, and, ...) of the tweet,
#     if don't ignores it, deletes words that contains some special characters such as / @ ... and so on,
#     if the final text doesn't have more tan 5 words it won't be returned
#     :param tweet: json file in string
#     :return: processed text ready to be used on the RNN
#     '''
#     tweet_json = json.loads(tweet)
#     text = ''
#     if 'text' in tweet_json:  # If it contains text
#         text = tweet_json['text']
#         # print(tweet_json)
#         listwords = text.split(' ')
#         not_allowed = ['\n', 'chart']
#         flag_n = any(na in w for w in listwords for na in not_allowed)
#         if not flag_n: # si no tiene palabras / caracteres no deseados
#             special_char = ['/', '@', 'RT', '…', '//']
#             required_words = ['a', 'the', 'i', 'you', 'u', 'and']
#
#             if any(rw in w for rw in required_words for w in listwords):  # if contains required words
#                 text = [w for w in listwords if not any(ch in w for ch in special_char)]  # deletes special characters
#                 if len(text) > 10:  # if the text is longer than 5 words
#                     text = ' '.join(text)
#                 else:
#                     text = ''
#         else:
#             text = ''
#     return text
