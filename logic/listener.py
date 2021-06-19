import logic.jsonHandler
from tweepy.streaming import StreamListener


class TwitterListener(StreamListener):

    def __init__(self, model):
        '''
        Constructor - Setup
        :param model: defines de RNN to be used
        '''
        self.model = model

    def on_data(self, raw_data):
        '''
        Predicts the emotion based on raw_data
        :param raw_data: Tweet data
        :return: Flag
        '''
        tweet = logic.jsonHandler.get_text(raw_data)
        if tweet != '':
            #print('Tweet: {}'.format(tweet))
            print('Predicted emotion: {}\n'.format(self.model.predict(tweet)))
        return True

    def on_error(self, status_code):
        '''
        Prints error
        :param status_code: error
        '''
        print(status_code)
