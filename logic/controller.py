from logic.model import Model
from logic.twitterController import TwitterController


class Controller():

    def __init__(self):
        '''
        Method on charge of setting up the model and the twitterController as well
        '''
        self.twitterC = TwitterController(Model())

    def search(self, h):
        '''
        Reference TwitterController.search()
        :param h: Hashtag or word to search
        :return: None
        '''
        self.twitterC.search(h)
