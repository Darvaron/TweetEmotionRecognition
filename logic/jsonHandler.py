import json
import re
import plots.plot as pl

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

    # Removing special chars

    remove = ['...', '’', "'", '“', '”', '.”', '(', '"', ')', '!', '?']

    for r in remove:
        string_v = string_v.replace(r, '')

    # case: -1 default, 1 word, 2 user, 3 url, 4 hashtag
    case_number = -1

    # Removing special chars at the end
    invalid = [',', '\'', '.', ';', ':', '‘', '’', '"', "'", '!']

    try:
        if string_v[-1] in invalid:
            string_v = string_v[:-1]
    except:
        # print('Non valid -1 char: {}'.format(string_v))
        pass

    word = re.search('^([a-z])+$', string_v)  # word
    if word:
        case_number = 1
    else:
        user = re.search('^([.])?([@])([a-zA-Z0-9_]){5,16}$', string_v)  # user

        if user:
            case_number = 2
        else:
            url = re.search(
                r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",
                string_v)  # url
            if url:
                case_number = 3
            else:
                hashtag = re.search('^(#)([a-zA-Z0-9_\\ ])+$', string_v)  # hashtag
                if hashtag:
                    case_number = 4
                else:
                    # print('Word: {} not identified'.format(string_v))
                    not_identified.append(string_v)
                    counter_not_identified += 1
                    if counter_not_identified % 10 == 0:
                        # print('\nWords don\'t identified:\nnot identified: {}\n'.format(not_identified))
                        # time.sleep(3)
                        pass
                    # raise Exception('Word {} not identified: '.format(string_v))
    case_dict = {
        -1: string_v,
        1: string_v,
        2: '<usermention>',
        3: '<url>',
        4: '<hashtag>'
    }
    transformed = case_dict[case_number]

    '''
    There are know issues for this method, such as some # are not correctly identified, however it does a nice job,
    good enough for this purpose
    '''

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

    if 'retweeted_status' in tweet_json:
        if 'extended_tweet' in tweet_json['retweeted_status']:
            # print('Case 1.')
            original = tweet_json['retweeted_status']['extended_tweet']['full_text']
        else:
            # print('Case 2.')
            original = tweet_json['retweeted_status']['text']
    else:
        if 'extended_tweet' in tweet_json:
            # print('Case 3.')
            original = tweet_json['extended_tweet']['full_text']
        else:
            # print('Case 4.')
            original = tweet_json['text']

    pl.tweets_saved.append(original)

    text = original.lower().split(' ')
    # separable = ['?', '"', '“', '”', '!']
    # text = [w.replace(ch, ' '+ch) for ch in separable for w in text] # separates separable symbols from the word
    text = [w.replace('\n', ' ') for w in text[:-1]] + [text[-1].replace('\n', '')]  # replaces \n
    # text = [w.replace('\xa0', ' ') for w in text[:-1]] + [text[-1].replace('\xa0', '')] # replaces \xa0
    text = ' '.join(text).split(' ')  # Fixing last line spaces
    transformed_text = [transform_word(w) for w in text if w not in ['']]  # delete symbols
    transformed_text = ' '.join(transformed_text)
    print('Tweet: {}'.format(original))
    # print('Transformed: {}'.format(transformed_text))

    return transformed_text
