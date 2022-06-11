from .banks import BANKS
from .documents import DOCUMENTS
from .general import GENERAL
from .program.case import CASE
from .program.ccj import CCJ
from .program.ccs import CCS
from .program.cea import CEA
from .program.cmba import CMBA
from .program.cnahs import CNAHS
from .scholarship import SCHOLARSHIP

PATTERNS = GENERAL + BANKS + DOCUMENTS + SCHOLARSHIP + CASE + CCJ + CCS + CEA + CMBA + CNAHS
