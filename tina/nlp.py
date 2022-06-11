from spacy import load

from .corpus.patterns import PATTERNS
from .lang.stopwords import EXCLU, STOPWORDS
from .pipelines import custom_tokenizer, merger


class NLP:
    def __init__(
        self,
        language = 'en_core_web_trf',
        stopwords = STOPWORDS,
        excluded_stopwords = EXCLU,
        add_entity_ruler = True,
        patterns = PATTERNS,
        tokenizer = custom_tokenizer
    ):
        self.__instance = load(language)
        self.__instance.Defaults.stop_words |= stopwords
        self.__instance.Defaults.stop_words -= excluded_stopwords

        for item in excluded_stopwords:
            try:
                self.__instance.vocab[item].is_stop = False
            except KeyError as e:
                continue
        
        if add_entity_ruler:
            entity_ruler = self.__instance.add_pipe('entity_ruler', before='ner')
            entity_ruler.add_patterns(patterns)
        
        self.__instance.tokenizer = tokenizer(self.__instance)
        self.__instance.add_pipe("merger", name="tokenmerger", before='entity_ruler')
    
    @property
    def Instance(self):
        return self.__instance
