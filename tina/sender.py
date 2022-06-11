from .corpus.templates import (Balance, Bridging, CancelEnrollment, Discount,
                               Documents, Enrollment, Inc, Office, Programs,
                               Scholarship, SchoolID, ShiftProgram, Subject,
                               SubmitDocument, Tuition)

# [
# 'FAO', 'balance', 'discount', 'documents', 'REGISTRAR',
# 'school_id', 'ETO', 'cancel_enrollment', 'enrollment',
# 'submit_documents', 'inquire_programs', 'shift_program', 'ETEEAP',
# 'TSG', 'scholarship', 'subject', 'bridging_subject', 'tuition',
# 'grade_inc_concens'
# ]


class Sender:
    def __init__(
        self,
        dispatcher: dict = None
    ):
        if dispatcher is None:
            self.dispatcher = {
                'FAO': Office('FAO').get_pattern,
                'REGISTRAR': Office('REGISTRAR').get_pattern,
                'ETO': Office('ETO').get_pattern,
                'ETEEAP': Office('ETEEAP').get_pattern,
                'TSG': Office('TSG').get_pattern,
                'balance': Balance().get_pattern,
                'discount': Discount().get_pattern,
                'documents': Documents().get_pattern,
                'school_id': SchoolID().get_pattern,
                'cancel_enrollment': CancelEnrollment().get_pattern,
                'enrollment': Enrollment().get_pattern,
                'submit_documents': SubmitDocument().get_pattern,
                'inquire_programs': Programs().get_pattern,
                'shift_program': ShiftProgram().get_pattern,
                'scholarship': Scholarship().get_pattern,
                'subject': Subject().get_pattern,
                'bridging_subject': Bridging().get_pattern,
                'tuition': Tuition().get_pattern,
                'inc_marks': Inc().get_pattern
            }
        else:
            self.dispatcher = dispatcher

    def get_reply(
        self, 
        category:str,
        arguments:list = []
    ):
        return self.dispatcher[category](arguments=arguments)
