from spacy.language import Language
from spacy.tokens import Doc, Token

from ..lang.merge_tokens import DEFAULT_ATTRS, END_TOKEN, MERGE_TOKENS

_LEMMA = "LEMMA"
_append = lambda l: " ".join(c for c in l)

def check_token(token: Token, doc: Doc):
    start = token.i
    stop = len(doc)

    tracker = []
    current_path = MERGE_TOKENS
    for index in range(start, stop):
        current_token = doc[index]
        if current_token.text in current_path:
            tracker.append(current_token)
            current_path = current_path[current_token.text]

            if current_path == END_TOKEN:
                return tracker
        else:
            return []

@Language.component("merger")
def merger(doc):
    with doc.retokenize() as retokenzier:
        for token in doc:
            path = check_token(token, doc)

            if path:
                start = path[0].i
                end = path[len(path)-1].i

                attrs = DEFAULT_ATTRS
                attrs[_LEMMA] = _append([tok.text for tok in path])
                
                retokenzier.merge(doc[start:end + 1], attrs=attrs)

    return doc
