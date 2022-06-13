from .template import Template


default_name = 'Tuition'

pattern_list = [
    'An estimate of the fees is computed as follows: = P835.00 per unit cost x no. of units enrolled (all colleges except, nursing P918.50) = Add miscellaneous fee of around P6K (subject to change in the coming academic year). Also, here is the link for your payment options: https://bit.ly/citupaymentoptions. Thank you and Stay safe!'
]

class Tuition(Template):
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
