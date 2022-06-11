_bscs = [ 
    #BS Computer Science
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BS'}, {'ORTH': 'Computer'}, {'ORTH': 'Science'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BS'}, {'ORTH': 'in'}, {'ORTH': 'Computer'}, {'ORTH': 'Science'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'bscs'}]},
]

_bsit = [ 
    #BS Information Technology
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BS'}, {'ORTH': 'Information'}, {'ORTH': 'Technology'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BS'}, {'ORTH': 'in'}, {'ORTH': 'Information'}, {'ORTH': 'Technology'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'bsit'}]},
]

CCS = _bscs + _bsit