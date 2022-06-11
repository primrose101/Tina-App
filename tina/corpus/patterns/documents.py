_documents = [
    # TOR, Transcript of Records
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "tor"}], "id": "TOR"},
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "transcript"},{"LOWER": "of"},{"LOWER": "record"}], "id": "TOR"},
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "transcript"},{"LOWER": "of"},{"LOWER": "records"}], "id": "TOR"},

    # Prospectus
    {"label": "Prospectus", "pattern": [{"LOWER": "prospectus"}], "id": "Prospectus"},

    # Study Load
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "study"}, {"LOWER": "load"}], "id": "STUDY"},

    # Report Card
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "report"}, {"LOWER": "card"}], "id": "CARD"},
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "my"}, {"LOWER": "grade"}], "id": "CARD"},
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "my"}, {"LOWER": "grades"}], "id": "CARD"},
    
    # Diploma
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "diploma"}], "id": "DIPLOMA"},
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "college"}, {"LOWER": "diploma"}], "id": "DIPLOMA"},

    # Good moral
    # {"label": "DOCUMENT", "pattern": [{"LOWER": "good"}, {"LOWER": "moral"}], "id": "MORAL"},

    # Year Book
    {"label": "Yearbook", "pattern": [{"LOWER":"yearbook"}], "id": "Yearbook"},

    # Proof of Payment
    {"label": "Proof of Payment", "pattern": [{"LOWER": "proof"}, {"LOWER": "of"}, {"LOWER": "payment"}], "id": "Proof of Payment"},

    # Promissory Note
    {"label": "Promissory Note", "pattern": [{"LOWER": "promissory"}, {"LOWER": "note"}], "id": "Promissory Note"}
]

DOCUMENTS = _documents