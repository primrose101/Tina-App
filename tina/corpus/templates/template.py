import random

def display_warning(message) -> None:
    print(message)

class Template:
    def __init__(
        self,
        template_name: str,
        patterns: list,
        use_patterns: bool = True,
        use_default_generated: bool = False
    ):
        self.template_name = template_name
        self.patterns = patterns
        self.use_patterns = use_patterns
        self.use_default_generated = use_default_generated

        if self.use_patterns and self.use_default_generated:
            display_warning(
                'Skipping use_default_generated. '
                'If not intended, set use_pattern to False'
            )
    
    def get_pattern(
        self, 
        arguments: list = None,
        arguments_map: dict = None,
        default_arg: str = None
    ):
        if self.use_patterns:
            return random.choice(self.patterns)
        else:
            return self.generate_pattern(
                arguments=arguments,
                arguments_map=arguments_map,
                default_arg=default_arg
            )
            # FIX THIS


    def _get_pattern(self):
        return random.choice(self.patterns)

    def generate_pattern(
        self, 
        arguments: list = None,
        arguments_map: dict = None,
        default_arg: str = None
    ):
        """For templates that uses NER.
        Check first if default generator is to be used.
        If not return overrided function declared in child class.
        
        arguments (list): list of entity labels or ids
        """

        if (
            isinstance(arguments, list) and
            isinstance(arguments_map, dict) and
            isinstance(default_arg, str)
        ):
            if not self.use_default_generated:
                return self._generate_pattern(
                    arguments=arguments,
                    arguments_map=arguments_map,
                    default_arg=default_arg
                )

            content = self._get_pattern()
            original = content
            if arguments:
                for arg in arguments:
                    try:
                        content = content + arguments_map[arg]
                    except KeyError:
                        continue
            else:
                content = content + default_arg
            
            if content == original:
                content = content + default_arg

            return content
            
        raise Exception('Missing or empty arguments')
  
    def _generate_pattern(
        self, 
        arguments: list,
        arguments_map: dict,
        default_arg: str
    ):
        pass
