from .template import Template


default_name = 'Shift Program'

pattern_list = [
    'Please use this link: https://cit.edu/colleges/'
]

class Programs(Template):
    def __init__(
        self,
        template_name: str = default_name,
        patterns: list = pattern_list,
        use_patterns: bool = True,
        use_default_generated: bool = False
    ):
        super().__init__(
            template_name=template_name,
            patterns=patterns,
            use_patterns=use_patterns,
            use_default_generated=use_default_generated
        )
