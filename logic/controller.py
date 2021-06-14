from logic.model import Model
from logic.twitterController import TwitterController


class Controller():

    def __init__(self, h):
        '''
        Class on charge of setting up the model and the twitterController as well
        :param h: hashtag or word to be searched
        '''
        self.model = Model()
        self.twitterC = TwitterController(h, self.model)
