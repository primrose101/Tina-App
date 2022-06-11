_bsn = [ 
    #BS Nursing
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BS'}, {'ORTH': 'Nursing'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BS'}, {'ORTH': 'in'}, {'ORTH': 'Nursing'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BSN'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'Nursing'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'nursing'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'bsn'}]},
]

_bspharma = [ 
    #BS Pharmacy
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BS'}, {'ORTH': 'Pharmacy'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BS'}, {'ORTH': 'in'}, {'ORTH': 'Pharmacy'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'BSPHARMA'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'PHARMACY'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'pharmacy'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'bspharma'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'pharma'}]},
]

_midwifery = [ 
    #Diploma in Midwifery
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'Diploma'}, {'ORTH': 'in'}, {'ORTH': 'Midwifery'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'MIDWIFERY'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'Midwifery'}]},
    {'label': 'PROGRAM', 'pattern': [{'ORTH': 'midwifery'}]},
]

CNAHS = _bsn + _bspharma + _midwifery