import os
from logic.listener import TwitterListener
from tweepy import OAuthHandler
from tweepy import Stream


class TwitterController():

    def __init__(self, model):
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
        self.model = model

    def search(self, h):
        '''
        Searchs tweets with a given hashtag or keyword filtering only tweets in english
        :param h: hashtag or keyword
        '''
        # Streaming setup
        self.listener = TwitterListener(self.model)
        self.stream = Stream(self.auth, self.listener)

        print('Searching: {}'.format(h))
        self.stream.filter(track=[h], languages=['en'])

# class MyStream(Stream):
#
#     def on_status(self, status):
#         if hasattr(status, "retweeted_status"):  # Check if Retweet
#             try:
#                 print(status.retweeted_status.extended_tweet["full_text"])
#             except AttributeError:
#                 print(status.retweeted_status.text)
#         else:
#             try:
#                 print(status.extended_tweet["full_text"])
#             except AttributeError:
#                 print(status.text)
