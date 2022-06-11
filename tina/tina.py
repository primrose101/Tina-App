from .model import Model
from .nlp import NLP
from .preprocess import Preprocess
from .sender import Sender

class Tina:
    def __init__(
        self,
        min_len: int = 2
    ):
        self.__preprocess = Preprocess(min_len=min_len)
        self.nlp = NLP()
        self.model = Model()
        self.sender = Sender()

    @property
    def Nlp(self):
        return self.nlp.Instance
    
    @property
    def Mdel(self):
        return self.model.Mdel

    def preprocess(self, message):
        token, entities = self.__preprocess.preprocess(
            message=message,
            spacy_nlp=self.Nlp
        )
        
        return token, entities
    
    def predict(self, tokens):
        return self.model.predict(
            tokens=tokens,
            model=self.model.model
        )

    def get_reply(
        self,
        category: str,
        arguments:list = []
    ):
        return self.sender.get_reply(
            category=category,
            arguments=arguments
        )
    
    def block(
        self,
        message: str
    ):
        tokens, entities = self.preprocess(message)
        prediction = self.predict(tokens)
        
        print(prediction)
        print(entities)

        if prediction:
            category = prediction[0][0]
            prob = prediction[0][1]

            if prob >= .75:
                return self.get_reply(category=category, arguments=entities)
            if prob >= .50:
                return "I'm confused. Can you rephrase that?"
        return "I don't understand"