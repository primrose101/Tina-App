from .template import Template


default_name = 'Subject'
default_link = 'https://bit.ly/ETO-REQUEST-ChangingCourses'
default_links = {
    'Default': 'https://bit.ly/ETO-REQUEST-ChangingCourses (Enroll, Drop, Change). ',
    'Accredit': 'https://bit.ly/CourseAccreditation (Accreditation). '
}

default_header = [
    'Please use the following links. ',
    'Here are the following links. '
]

class Subject(Template):
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
