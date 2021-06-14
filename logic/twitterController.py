import os
from logic.listener import TwitterListener
from tweepy import OAuthHandler
from tweepy import Stream


class TwitterController():

    def __init__(self, h, model):
        '''
        setup and authentication process
        :param h: Word or hashtag to be used
        :param model: RNN
        '''

        # Authentitacion process
        self.tokens_dir = os.path.dirname(os.path.realpath(__file__))[:-27] + 'TOKENS.txt'

        with open(self.tokens_dir) as f:
            tokens = f.readlines()

        self.auth = OAuthHandler(tokens[0][:-1], tokens[1][:-1])
        self.auth.set_access_token(tokens[2][:-1], tokens[3])

        # Streaming setup
        self.listener = TwitterListener(model)
        self.stream = Stream(self.auth, self.listener)
        self.search(h)

    def search(self, h):
        '''
        Searchs tweets with a given hashtag or keyword filtering only tweets in english
        :param h: hashtag or keyword
        '''
        print('Searching: {}'.format(h))
        self.stream.filter(track=[h], languages=['en'])
