import collections

import numpy
from keras.models import load_model

MODEL_PATH = r'C:/Users/georg/Desktop/Tina/Tina/tina/model/model.h5'
CATEGORIES_PATH = r'C:/Users/georg/Desktop/Tina/Tina/tina/model/categories.npy'
VOCABS_PATH = r'C:/Users/georg/Desktop/Tina/Tina/tina/model/vocabs.npy'

ERROR_THRESHOLD = 0.25

class Model:
    def __init__(
        self,
        model_path: str = MODEL_PATH,
        categories_path: str = CATEGORIES_PATH,
        vocabs_path: str = VOCABS_PATH
    ) -> None:
        """

        """
        try:
            self.model = load_model(model_path)
            self.categories = numpy.load(categories_path, allow_pickle=True)
            self.vocabs = numpy.load(vocabs_path,allow_pickle=True)
        except:
            print("## Failed to load model ##")
    
    @property
    def Mdel(self):
        return self.model
    
    def to_bow(self, tokens: list, vocabs:dict = None):
        """Creates a bag of words"""

        if vocabs is None:
            vocabs = self.vocabs
        
        frequency = dict(collections.Counter(tokens))
        bag = list()

        for word in vocabs:
            if (word not in tokens) or (word not in frequency): bag.append(0)
            else: bag.append(frequency[word])
        return(numpy.array(bag))
    
    def predict(
        self, 
        tokens: list, 
        model,
        vocabs:dict = None, 
        categories:list = None
        ):
        """Predicts the category"""

        if vocabs is None:
            vocabs = self.vocabs
        
        if categories is None:
            categories = self.categories

        bag = self.to_bow(tokens, vocabs)
        predictions = model.predict(numpy.array([bag]))
        predictions = dict(zip(categories, predictions[0]))

        sorted_predictions = list({k: v for k, v in sorted(predictions.items(), key=lambda item: item[1], reverse = True)}.items())[:3]
        sorted_predictions = [(item[0], item[1]) for item in sorted_predictions if item[1] >= ERROR_THRESHOLD]

        return sorted_predictions

        # bag = self.to_bow(tokens, vocabs)
        # predictions = model.predict(numpy.array([bag]))[0]

        # plausible_predictions = [[index,range] for index,range in enumerate(predictions) if range >= ERROR_THRESHOLD]
        # plausible_predictions.sort(key=lambda x: x[1], reverse=True)

        # return_list = [(self.categories[pred[0]], pred[1]) for pred in plausible_predictions]
        # return return_list