# FAO = 'accounting@cit.edu'
# CREATE = 'create@cit.edu'
# ETEEAP = 'technical.eteeap@cit.edu'
# ETO = 'eto@cit.edu'
# IMDC = 'imdc@cit.edu'
# IMPO = 'impo@cit.edu'
# INFO = 'info@cit.edu'
# OAS = 'oas@cit.edu'
# REGISTRAR_C = 'registrar@cit.edu'
# REGISTRAR_HS = 'hs.registrar@cit.edu'
# SAO = 'sao@cit.edu'
# TSG = 'tsg@cit.edu'

from .template import Template

endl = '\n'
replace_tag = '<>'

default_name = 'Emails'
default_emails = {
    'FAO': 'accounting@cit.edu',
    'REGISTRAR': 'registrar@cit.edu(College) or hs.registrar@cit.edu(Highschool)',
    'ETO': 'eto@cit.edu',
    'ETEEAP': 'technical.eteeap@cit.edu',
    'TSG': 'tsg@cit.edu'
}

default_header = 'Sorry for any inconvenience in our system. '
default_footer = 'Please also include your student details if possible.'
default_body = [
    'You may forward your concern to <>. ',
    'You may directly send your concern to <>. ',
    'You may directly email to <>. ',
    'Email your concern to <>. ',
    'Kindly email your concern to <>. '
]

def generate_pattern():
    pattern_list = {office:[] for office in default_emails}
    categories = [office for office in default_emails]
    for office in default_emails:
        for body in default_body:
            content = (
                default_header +
                body.replace(replace_tag, default_emails[office]) +
                default_footer
            )
            pattern_list[office].append(content)

    return pattern_list, categories

pattern_list, categories = generate_pattern()

class Office(Template):
    def __init__(
        self,
        template_name: str,
        patterns: list = pattern_list,
        use_patterns: bool = True,
        use_default_generated: bool = False
    ):
        super().__init__(
            template_name=template_name,
            patterns=patterns[template_name],
            use_patterns=use_patterns,
            use_default_generated=use_default_generated
        )
