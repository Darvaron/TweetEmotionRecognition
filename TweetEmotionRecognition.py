print('Loading ...')
from logic.twitterController import TwitterController


def main():
    controller = TwitterController()
    print(
        'Only works with tweets in english, please take on count that this model doesn\'t work well in all type of data.')
    hashtag = input('Write the hashtag or word to be searched, e.g. #Twitter or Twitter: ')
    tweets = int(input('how often show plots? (in tweets) e.g. 50: '))
    print('\n')
    controller.search(hashtag, tweets)


if __name__ == "__main__":
    main()
