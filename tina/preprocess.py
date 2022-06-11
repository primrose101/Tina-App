import contractions

class Preprocess:
    def __init__(
        self,
        min_len: int = 2
    ):
        self.min_len = min_len

    def tokenize(self, doc, min_len = None):
        if min_len is None:
            min_len = self.min_len
        
        tokens = [tok for tok in doc if len(tok.text) >= min_len]
        tokens = [
            tok for tok in tokens 
            if not tok.is_stop and 
                not tok.is_punct and
                not tok.like_url and
                not tok.like_email and
                not tok.like_num and
                tok.is_alpha
        ]
        
        tokens = [tok.lemma_ for tok in tokens]
        return tokens
    
    def get_entities(self, doc):
        return [ent.label_ for ent in doc.ents]
    
    def preprocess(self, message: str, spacy_nlp):
        expanded = contractions.fix(message)
        document = spacy_nlp(expanded)

        tokens = self.tokenize(document)
        entities = self.get_entities(document)
        
        return tokens, entities