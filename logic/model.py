import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences


class Model():

    def __init__(self):
        '''
        Load tf model located at EmotionRModel folder and other requirements to predict emotions
        '''
        global padded_test

        # Model
        print('Loading model ...')
        self.modelPath = os.path.dirname(os.path.realpath(__file__))[:-5] + 'EmotionRmodel\EmotionRmodel'
        self.Emodel = tf.keras.models.load_model(self.modelPath)
        print('Model loaded successfully')

        # Tokenizer
        with open(os.path.dirname(os.path.realpath(__file__))[:-5] + 'resources\ptokenizer.pickle', 'rb') as handle:
            self.token = pickle.load(handle)

        # Dicts to convert index to class
        self.dict = {0: 'anger', 1: 'sadness', 2: 'fear', 3: 'love', 4: 'joy', 5: 'surprise'}

    def preprocess_tweet(self, tweet):
        '''
        Converts the tweet from text to a matrix ready to be used to predict
        :param tweet:
        :return:
        '''
        p_tweet = self.token.texts_to_sequences([tweet])
        return pad_sequences(p_tweet, maxlen=50, padding='post', truncating='post')

    def predict(self, tweet):
        '''
        Predicts the emotion
        :param tweet: tweet text
        :return: index of the predicted class
        '''
        pad_tweet = self.preprocess_tweet(tweet)
        p = self.Emodel.predict(np.expand_dims(pad_tweet[0], axis=0))[0]
        predicted_class_t = self.dict[np.argmax(p).astype('uint8')]
        return predicted_class_t

    def model_info(self):
        '''
        Prints information of the model
        :return:
        '''
        print(self.Emodel.summary())
