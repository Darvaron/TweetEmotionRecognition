print('Loading ...')

from logic.controller import Controller
from logic.jsonHandler import get_text


def main():
    #get_text('This is a test of @Darvaron, check it out at www.google.com, this is #awesome :)')
    controller = Controller()
    print(
        'Only works with tweets in english, please take on count that this model doesn\'t work well in all type of data.')
    hashtag = input('Write the hashtag or word to be searched, e.g. #Twitter or Twitter: ')
    print('\n')
    controller.search(hashtag)


if __name__ == "__main__":
    main()
