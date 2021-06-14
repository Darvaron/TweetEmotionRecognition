import os, pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class model():

    def __init__(self):
        global padded_test

        self.modelPath = os.path.dirname(os.path.realpath(__file__))[:-5] + 'EmotionRmodel\EmotionRmodel'
        self.Emodel = tf.keras.models.load_model(self.modelPath)
        #self.model_info()
        print('Model loaded successfully')

        with open(os.path.dirname(os.path.realpath(__file__))[:-5]+'resources\ptokenizer.pickle', 'rb') as handle:
            self.token = pickle.load(handle)

        #seq_test = self.preprocess_tweet('im feeling rather rotten so im not very ambitious right now')
        #print(seq_test[0])

        self.dict = {0: 'anger', 1: 'sadness', 2: 'fear', 3: 'love', 4: 'joy', 5: 'surprise'}


    def preprocess_tweet(self, tweet):
        p_tweet = self.token.texts_to_sequences([tweet])
        return pad_sequences(p_tweet, maxlen=50, padding='post', truncating='post')

    def predict(self, tweet):
        pad_tweet = self.preprocess_tweet(tweet)
        p = self.Emodel.predict(np.expand_dims(pad_tweet[0], axis=0))[0]
        predicted_class_t = self.dict[np.argmax(p).astype('uint8')]
        return predicted_class_t

    def model_info(self):
        print(self.Emodel.summary())
