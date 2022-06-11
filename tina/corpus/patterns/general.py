_general = [
    # School ID dd-dddd-dd
    {"label": "ID", "pattern": [{"SHAPE": "dd"}, {"ORTH": "-"}, {"SHAPE": "dddd"}, {"ORTH": "-"}, {"SHAPE": "ddd"}], "id": "ID"},

    # Courses
    {"label": "COURSE", "pattern": [{"SHAPE": "XXddd"}], "id": "COURSE"},
    {"label": "COURSE", "pattern": [{"SHAPE": "xxddd"}], "id": "COURSE"},
    {"label": "COURSE", "pattern": [{"SHAPE": "XXdddd"}], "id": "COURSE"},
    {"label": "COURSE", "pattern": [{"SHAPE": "xxdddd"}], "id": "COURSE"},

    # Verbs
    {"label": "Accredit", "pattern": [{"LOWER": "accredit"}], "id": "Accredit"},
    {"label": "Accredit", "pattern": [{"LOWER": "accreditation"}], "id": "Accredit"},
    {"label": "Default", "pattern":[{"LOWER":"enrol"}], "id": "Default"},
    {"label": "Default", "pattern":[{"LOWER":"enroll"}], "id": "Default"},
    {"label": "Default", "pattern":[{"LOWER":"change"}], "id": "Default"},
    {"label": "Default", "pattern":[{"LOWER":"drop"}], "id": "Default"},

    # Year LEVEL
    {"label": "SHS", "pattern":[{"LOWER":"shs"}], "id": "SHS"},
    {"label": "SHS", "pattern":[{"LOWER":"senior"}, {"LOWER": "high"}], "id": "SHS"},
    {"label": "SHS", "pattern":[{"LOWER":"senior"}, {"LOWER": "high"}, {"LOWER": "school"}], "id": "SHS"},
    
    {"label": "JHS", "pattern":[{"LOWER":"jhs"}], "id": "JHS"},
    {"label": "JHS", "pattern":[{"LOWER":"junior"}, {"LOWER": "high"}], "id": "JHS"},
    {"label": "JHS", "pattern":[{"LOWER":"junior"}, {"LOWER": "high"}, {"LOWER": "school"}], "id": "JHS"},

    {"label": "JHS", "pattern":[{"LOWER":"elementary"}], "id": "Elementary"},
    {"label": "JHS", "pattern":[{"LOWER":"college"}], "id": "College"},

    # Student Year LEVEL
    {"label": "Freshmen", "pattern":[{"LOWER":"freshmen"}], "id": "Freshmen"},
    {"label": "Freshmen", "pattern":[{"LOWER":"freshman"}], "id": "Freshmen"},

    {"label": "Transferees", "pattern":[{"LOWER":"transfere"}], "id": "Transferees"},
    {"label": "Transferees", "pattern":[{"LOWER":"transferee"}], "id": "Transferees"},
    
    {"label": "Returnee", "pattern":[{"LOWER":"returne"}], "id": "Returnee"},
    {"label": "Returnee", "pattern":[{"LOWER":"returnee"}], "id": "Returnee"}
]

GENERAL = _general