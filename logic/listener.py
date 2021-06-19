import logic.jsonHandler
import plots.plot as pl
from tweepy.streaming import StreamListener

counter_tweets = 0

class TwitterListener(StreamListener):

    def __init__(self, model, tweets):
        '''
        Constructor - Setup
        :param model: defines de RNN to be used
        :param tweets: show plots every (tweets)
        '''
        # super().__init__(self)
        self.model = model
        self.every_plot = tweets

    def on_data(self, raw_data):
        '''
        Predicts the emotion based on raw_data
        :param raw_data: Tweet data
        :return: Flag
        '''
        global counter_tweets
        try:
            tweet = logic.jsonHandler.get_text(raw_data)
            if tweet != '':
                # print('Tweet: {}'.format(tweet))
                emotion = self.model.predict(tweet)
                print('Predicted emotion: {}\n'.format(emotion))
                pl.labels.append(emotion)
                counter_tweets += 1
                if counter_tweets % self.every_plot == 0:
                    pl.plot_fig()

            return True
        except Exception as e:
            print('Error on data: {}'.format(e))

    def on_error(self, status_code):
        '''
        Prints error
        :param status_code: error
        '''
        print('On error: {}'.format(status_code))

    def on_status(self, status):
        try:
            return
        except Exception as e:
            print('Error on status: {}'.format(e))
