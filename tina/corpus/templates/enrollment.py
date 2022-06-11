from .template import Template


default_name = 'Enrollment'
default_link = 'https://bit.ly/RequirementSubmission-Freshmen'
default_links = {
    'Freshmen': 'https://bit.ly/RequirementSubmission-Freshmen (Freshmen). ',
    'Transferees': 'https://bit.ly/RequirementSubmission-Transferees (Transferee). ',
    'Returnee': 'https://docs.google.com/forms/d/e/1FAIpQLSfeZSfYvmJQpp2EZiebyVToJGqfiUJfnE-f9H1YwLqrwslIpQ/viewform (Returnee). '
}

default_header = [
    'Please use the following links. ',
    'Here are the following links. '
]

class Enrollment(Template):
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
