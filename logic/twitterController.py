import os
from logic.listener import TwitterListener
from tweepy import OAuthHandler
from tweepy import Stream
from logic.model import Model


class TwitterController():

    def __init__(self):
        '''
        Constructor - setup and authentication process
        :param model: RNN
        '''

        # Authentitacion process
        self.tokens_dir = os.path.dirname(os.path.realpath(__file__))[:-27] + 'TOKENS.txt'

        with open(self.tokens_dir) as f:
            tokens = f.readlines()

        self.auth = OAuthHandler(tokens[0][:-1], tokens[1][:-1])
        self.auth.set_access_token(tokens[2][:-1], tokens[3])
        self.model = Model()

    def search(self, h, tweets):
        '''
        Searchs tweets with a given hashtag or keyword filtering only tweets in english
        :param h: hashtag or keyword
        :param tweets: number of tweets between plots
        '''
        # Streaming setup
        try:
            self.listener = TwitterListener(self.model, tweets)
            self.stream = Stream(self.auth, self.listener)
            print('Searching: {}'.format(h))
            self.stream.filter(track=[h], languages=['en'])
        except Exception as e:
            print('Error: {}'.format(e))
            #Known issue ('Connection broken: IncompleteRead(0 bytes read)', IncompleteRead(0 bytes read)) tweepy