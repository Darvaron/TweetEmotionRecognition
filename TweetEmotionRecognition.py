from logic.controller import Controller


def main():
    print(
        'Only works with text in english, please take on count that these model doesn\'t work well in all type of data.')
    hashtag = input('Write the hashtag or word to be searched, e.g. #Twitter or Twitter: ')
    controller = Controller(hashtag)


if __name__ == "__main__":
    main()
