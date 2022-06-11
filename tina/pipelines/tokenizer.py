from spacy.lang import en, punctuation, tokenizer_exceptions
from spacy.util import compile_prefix_regex, compile_infix_regex, compile_suffix_regex

from spacy.language import Language
from spacy.tokenizer import Tokenizer

_infixes = en.punctuation.TOKENIZER_INFIXES
_token_exceptions = en.tokenizer_exceptions.TOKENIZER_EXCEPTIONS

_prefixes = punctuation.TOKENIZER_PREFIXES
_suffixes = punctuation.TOKENIZER_SUFFIXES
_url = tokenizer_exceptions.URL_MATCH

_custom_infixes = (
    [
        r"(?<=No\.)/(?=INVOICE)",
        r"(?<=[a-z]):(?=[0-9])",
        r"(?<=[a-z])\?(?=\w)",
        # r"(?<=[a-z])\.(?=[a-z]+\s)",
        r"(?<=[a-z])\((?=[A-Za-z0-9]+)"
    ]
)

_custom_suffix = (
    [
        r"(?<=[A-Za-z])\/"
    ]
)

_infixes += _custom_infixes
_suffixes += _custom_suffix

def custom_tokenizer(nlp: Language):
    infix_re = compile_infix_regex(_infixes)
    prefix_re = compile_prefix_regex(_prefixes)
    suffix_re = compile_suffix_regex(_suffixes)

    tokenizer = Tokenizer(
        nlp.vocab,
        rules=_token_exceptions,
        prefix_search=prefix_re.search,
        suffix_search=suffix_re.search,
        infix_finditer=infix_re.finditer,
        url_match = _url,
        token_match=nlp.tokenizer.token_match
    )
    
    return tokenizer