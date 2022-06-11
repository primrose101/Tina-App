from .template import Template


default_name = 'School ID'
default_link = 'https://bit.ly/IDPrinting-College (College). '
default_links = {
    'College': 'https://bit.ly/IDPrinting-College (College). ',
    'SHS': 'https://bit.ly/IDPrinting-SHS (SHS). ',
    'JHS': 'https://bit.ly/IDPrinting-JHS (JHS). ',
    'Elementary': 'https://bit.ly/IDPrinting-ELEM (Elementary). '
}

default_header = [
    'Please use the following links. ',
    'Here are the following links. '
]

class SchoolID(Template):
    def __init__(
        self,
        template_name: str = default_name,
        patterns: list = default_header,
        use_patterns: bool = False,
        use_default_generated: bool = True
    ):
        super().__init__(
            template_name=template_name,
            patterns=patterns,
            use_patterns=use_patterns,
            use_default_generated=use_default_generated
        )

    def get_pattern(
        self,
        arguments: list = [],
        arguments_map: dict = default_links,
        default_arg: str = default_link
    ):
        return super().get_pattern(
            arguments=arguments,
            arguments_map=arguments_map,
            default_arg=default_arg
        )
