from .template import Template


default_name = 'Discount'

pattern_list = [
    'For Sibling Discounts: https://bit.ly/CITU-SDP2021. Full-Payment: 20%. Basta You: 0%'
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
