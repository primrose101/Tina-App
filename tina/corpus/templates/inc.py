from .template import Template


default_name = 'INC Mark'

pattern_list = [
    'You have to file for the INC completion. Email your Instructor if you already complied your lacking requirements and if so inform your instructor that you are going to file for the completion. For reference see attached link: https://docs.google.com/spreadsheets/d/1d86xht6hTU1q0KQ13QGaR0fkI4VtQebxMnlBvmN2kuc/edit?usp=sharing'
]

class Inc(Template):
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
