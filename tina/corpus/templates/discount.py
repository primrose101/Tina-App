from .template import Template


default_name = 'Discount'

pattern_list = [
    'For Sibling Discounts, kindly refer to this link https://bit.ly/CITU-SDP2021. Also, there is a 20 percent discount for those who will pay their tuition in full. Thank you and Stay safe!'
]

class Discount(Template):
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
