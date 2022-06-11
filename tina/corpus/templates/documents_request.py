from .template import Template


default_name = 'Request Documents'
default_link = 'bit.ly/REQUEST-URO-Docus'
default_links = {
    'College': 'bit.ly/REQUEST-URO-Docus (Request Documents). ',
    'SHS': 'bit.ly/REQUEST-URO-Docus-HighSchool (SHS/JHS). ',
    'JHS': 'bit.ly/REQUEST-URO-Docus-HighSchool (SHS/JHS). ',
    'Prospectus': 'https://bit.ly/3hfky3C',
    'Yearbook': 'https://docs.google.com/forms/d/e/1FAIpQLSd2v1cSVj5nbrd39ArTwiyJB086qvL2BxnruO42DlvHfzya7g/viewform (Yearbook). ',
    'Proof of Payment': 'http://bit.ly/CITU_ProofOfPayment (Proof of Payment). ',
    'Promissory Note': 'http://bit.ly/PNApplication2021 (Promissory Note). '
}

default_header = [
    'Please use the following links. ',
    'Here are the following links. '
]

class Documents(Template):
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
