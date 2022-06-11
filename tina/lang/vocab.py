general = (
"""
inquire request ask
""".split()
)

balance_inquiry = (
"""
need settle withdraw
exact deficient deficiency
total outstanding balance tuition activation fee
forward process excess payment
assessment
remain remaining 
semester semestral
official statement
student account
other
""".split()
)

balance_forward = (
"""
forward transfer withdraw advance refund overpay
possible
previous upcoming incoming
excess total balance amount tuition subsidy activation fee bill money
negative
payment account
current midyear summer semester sy term
""".split()
)

discount_full = (
"""
avail discount deduct deduction
pay payment full tuition
option
year
""".split()
)

discount_sibling = (
"""
apply file avail discount sibling privilege program
requirement
""".split()
)

documents = (
"""
obtain pass submit upload
copy
hard hardcopy
soft softcopy
sign certify
slip

form certificate
authenticate authenticated
alumni id fee
course evaluation
course outline
diploma
inc completion mark grade
syllabus prospectus
report card
statement account
study load studyload
tor transcript record
yearbook year book
""".split()
)

accounts = (
"""
create make reset unblock
receive email address link
aim 
outlook 
ms microsoft team teams msteam msteams
moodle moodles 
wildcat lair
institutional
default
account detail details
university

cant unable work log login open
recover forgot forget
incorrect incorrectly password username
activate access accessing

clarify spell mispelle edit change
typo typographical

invalid wrong credential

add instructor class
""".split()
)

enrollment = (
"""
how update withdraw cancel
enrol enroll enrollment
confirm confirmation email
admission number
application deadline
transfer shift change
reserve reservation slot
status

process procedure step submit
requirement requirements

activation fee

upcoming incoming exact start schedule
summer semester sy term
shs jhs senior junior high college

bachelor degree
bridge class course subject subjects
program

entrance admission test exam examination

irregular returnee shiftee transferee transferees
""".split()
)

payment = (
"""
pay payment payments refund option
reflect confirm confirmation deduct
deficiency
semester sy term

settle proof
tuition activation enrollment fee

through thru
how use method
dragonpay
gcash

promissory note
""".split()
)

profile = (
"""
how get upload student id
update error year level
""".split()
)

scholarship = (
"""
inquire
avail apply academic scholarship program offer
qualification application requirement requirements
deadline

freshman ched

shs jhs senior junior high college
""".split()
)

subjects = (
"""
cross enrollee student
drop withdraw cancel add overload class course subject subjects
know change conflict section
credit accredit accredited

schedule
""".split()
)

eteeap = (
"""
eteeap program
""".split()
)

tuition = (
"""
inquire know
tuition enroll enrollment activation subsidy bill fee
down payment payments
official officially enrolled

school year
""".split()
)

program = (
"""
ab art arts beed bio biology bsed communication design education elementary english raphics language mathematic media multimedia psych psychology science secondary

bscomsci bscs bsit computational computer cs information tech technology

arch architecture bsarch bsce bsche bsece bsee bsie bsme ce chemical civil cpe ece ee electrical electronics engineer engineerin engineering industrial mech mechanical mechatronics mining

accountancy accounting administration ais analytics banking bfm bsa bsaod bsba bshm bshrm bsoad bstm business economics estate finance financial gbm hospitality hotel hr hrdm human management manangement marketing mkm mm office om operations restaurant tourism

bsn medical nursing pharma pharmacy

criminology

ba bachelor bs bsmare degree general geology ma major political public rad real resource system
""".split()
)

ALL = list(set(general | balance_inquiry | balance_forward | discount_full | discount_sibling | documents | accounts | enrollment | payment | profile | scholarship | subjects | eteeap | program | tuition))

# Hybrid Yarn:
# "Enrollment Activate Account" enrollment & account
# "Enrollment Unblock Account" enrollment & account
# "Enrollment Fee" enrollment & payment
# "Subject Not Added in Class" subjects & accounts
# "Tuition How to Pay" tuition & payments
# "Tuition Promissorry" tuition & payments