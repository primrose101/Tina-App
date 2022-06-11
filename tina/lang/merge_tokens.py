# Merge Tokens

END_TOKEN = "__end__"
SETTINGS = "__settings__"

DEFAULT_ATTRS = {
    "IS_ALPHA": True,
    "LEMMA": ""
}

MERGE_TOKENS = {
    "ms": {
        "team": END_TOKEN,
        "teams": END_TOKEN,
        "account": END_TOKEN,
    },
    "i": {
        "d": END_TOKEN
    }
}

# MERGE_ATTRS = {
#     "ms team": {

#     },
#     "ms teams": {

#     },
# }