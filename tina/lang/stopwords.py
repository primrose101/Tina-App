# Stop words
_tagalog = set(
"""
akin aking ako alin am amin aming ang ano anumang apat at atin ating ay

bababa bago bakit bilang

dahil dalawa dapat din dito doon

gagawin gayunman ginagawa ginawa ginawang gumawa gusto

habang hanggang hindi huwag

iba ibaba ibabaw ibig ikaw ilagay ilalim ilan inyong isa isang itaas ito iyo iyon iyong

ka kahit kailangan kailanman kami kanila kanilang kanino kanya kanyang kapag kapwa karamihan katiyakan katulad kaya kaysa ko kong kulang kumuha kung

laban lahat lamang likod lima

maaari maaaring maging mahusay makita marami marapat masyado may mayroon mga minsan mismo mula muli 

na nabanggit naging nagkaroon nais nakita namin napaka narito nasaan ng ngayon ni nila nilang nito niya niyang noon 

o 

pa paano pababa paggawa pagitan pagkakaroon pagkatapos palabas pamamagitan panahon pangalawa para paraan pareho pataas pero pumunta pumupunta

sa saan sabi sabihin sarili sila sino siya 

tatlo tayo tulad tungkol 

una 

walang
""".split()
)


_bisaya = set(
"""
ako amua ato 

busa buhaton batok

dili

hangtod

ikaw ila ilang imo imong iya iyang 

kaayo kana kaniya kaugalingon kay kini kinsa kita kamo mao kaniadto kinahanglan

lamang 

mahimong mga mismo nahimo 

nga 

pareho pud 

sila siya 

ngano

sa

tungod tanan

unta unsaon ubos uban unsa
""".split()
)


_eng = set(
"""
ll ve m
like
""".split()
)

_greetings = set(
"""
good day morning afternoon evening
bless
thank thanks
best
regards
hope hear soon
god
hello hi
""".split()
)

_honorifics = set(
"""
mr sir 
mrs miss ms madam madame maam mam
""".split()
)

_months = set(
"""
january jan
febuary feb
march mar
april apr
may 
june
july
august aug
september sept
october oct
november nov
december dec
""".split()
)

_days = set(
"""
sunday sun
monday mon
tuesday tues tue tu
wednesday wed
thursday thurs thur
friday fri
saturday sat
""".split()
)

EXCLU = set(
"""
how
down
""".split()
)

STOPWORDS = _tagalog | _bisaya | _eng | _greetings | _honorifics | _months | _days


# ALL = {'sat', 'whither', 'bababa', 'muli', 'three', 'onto', 'iba', 'tayo', 'batok', 'here', 'six', 'cannot', 'lahat', 'whatever', 'on', 'keep', 'pa', 'while', 'and', '’ve', 'masyado', 'nabanggit', 'an', 'sino', 'anywhere', 'everywhere', 'a', 'saturday', 'anyone', 'inyong', 'ever', 'does', 'mostly', 'una', 'ourselves', 'kailanman', 'kana', 'ikaw', 'busa', "n't", 'katulad', 'yourself', 'tulad', '’m', 'marapat', 'pumunta', 'aming', 'nine', 'her', 'paano', 'naging', 'amongst', 'used', 'din', 'everyone', 'pagkakaroon', 'be', 'anything', 'becomes', 'was', 'various', 'hereafter', 'else', "'s", 'ginawang', 'it', 'laban', 'make', 'tatlo', 'do', 'miss', 'first', 'ni', 'has', 'that', 'if', 'alin', 'hope', 'indeed', 'madam', 'like', 'sa', 'through', 'always', 'of', 'have', 'amua', 'hi', 'among', 'panahon', 'yet', 'whoever', 'ko', 'sabi', '‘d', 'yours', 'them', 'until', 'isang', 'apat', 'mga', 'ten', 'two', 'former', 'this', 'go', 'none', 'febuary', 'done', 'napaka', 'move', 'several', 'i', 'latterly', 've', 'front', 'kahit', 'or', 'top', 'pumupunta', 'kinsa', 'mon', 'few', 'beside', 'ngano', 'somewhere', 'thereafter', 'four', 'they', 'hanggang', 'pababa', 'had', 'twelve', 'hereupon', 'aug', 'nagkaroon', 'regards', 'towards', 'thence', 'same', 'ilagay', 'kaysa', 'pangalawa', 'ilan', 'are', 'much', 'herself', 'other', 'been', 'just', 'december', 'kanila', 'behind', 'but', 'iyang', 'than', 'kaniadto', 'him', 'serious', 'to', 'iyong', 'since', 'up', 'kanilang', 'july', 'due', 'thereby', 'unsa', 'hello', 'put', 'soon', 'whereby', '’re', 'aking', 'dili', 'may', 'nevertheless', 'march', 'she', 'what', 'us', 'whereupon', 'anumang', 'akin', 'ito', 'mam', 'show', 'mine', 'now', 'eight', 'itaas', 'ilalim', 'mula', 'hers', 'kumuha', 'latter', 'dahil', 'ako', 'wherein', 'mr', 'every', 'atin', 'pareho', 'morning', 'thur', 'kini', 'ours', 'otherwise', '‘m', 'call', 'thurs', 'kailangan', 'least', 'although', 'is', 'along', 'nga', 'pamamagitan', 'nothing', 'as', 'bless', 'god', 'say', 'became', 'off', 'whether', 'last', 'dec', 'where', 'doon', 'across', 'isa', 'though', 'full', 'see', 'tungkol', 'madame', 'buhaton', 'please', 'kong', 'll', 'mar', 'we', 'more', 'noon', 'however', 'their', 'further', 'amount', 'fifteen', 'nila', 'n’t', 'nais', 'from', 'take', 'out', 'whence', 'unta', 'siya', 'upon', "'re", 'something', '’s', 'ginawa', '’ll', 'kapag', 'nilang', 'his', 'someone', 'ibaba', 'could', 'nakita', 'at', 'feb', 'another', 'might', 'evening', 'niya', 'day', 'becoming', 'already', 'karamihan', 'jan', 'september', 'about', 'most', 'ng', 'seeming', 'sixty', 'nasaan', 'iya', 'doing', 'hence', 'tue', 'sunday', 'anyhow', 'ca', 'mismo', 'sometime', 'enough', 'mahimong', 'beforehand', 'your', 'nov', 'down', 'ang', 'june', 'o', 'mayroon', 'kulang', 'when', 'uban', 'toward', 'being', 'sept', 'anyway', 'apr', 'should', 'narito', 'whole', 'those', 'only', 'after', 'yourselves', 'mahusay', 'he', 'nor', 'wed', 'made', 'kaya', 'am', 'mrs', 'ibabaw', 'nito', 'alone', 'meanwhile', 'kita', 'ibig', 'paggawa', 'likod', 'oct', 'sabihin', 'ka', 'can', 'hear', 'themselves', 'therein', 'even', 'noone', 'monday', 'also', 'beyond', 'some', 'dapat', 'therefore', 'wednesday', 'sila', 'under', 'ngayon', 'saan', 'tanan', 'there', 'maging', 'unless', 'wherever', 'ilang', 'fifty', 'will', 'palabas', 'pero', 'imo', "'d", 'the', 'during', 'ila', 'hangtod', 'myself', 'whom', 'dito', 'august', 'really', 'thus', 'well', 'tungod', 'around', 'formerly', 'kanino', 'thru', 'ano', 'november', 'pud', 'neither', 'less', 'amin', 'together', 'ay', 'gumawa', 'hindi', 'katiyakan', 'iyon', 'one', 'five', 'our', 'such', 'quite', 'besides', 'into', 'para', 'except', 'did', 'seemed', 'between', 'how', 'sir', 'both', 'itself', '‘ve', 'back', 'seems', 'still', 'own', 'afternoon', 'kaayo', 'because', 'kung', 'hereby', 'third', 'kaugalingon', 'using', 'somehow', 'makita', 'these', 'namin', 'get', 'you', 'not', 'then', 'january', 'below', 'side', 'twenty', 'kanya', 'again', 'pagkatapos', 'ms', 'kapwa', '‘re', 'dalawa', 'were', 'next', 'why', 'marami', 'thanks', 'seem', 're', 'any', 'each', '‘ll', 'lamang', "'ve", 'sarili', 'minsan', 'would', 'by', 'with', 'good', 'moreover', 'above', 'huwag', 'thank', 'before', 'tu', 'elsewhere', 'pagitan', 'perhaps', '’d', 'friday', 'kamo', 'nahimo', 'nowhere', 'very', 'gagawin', 'kami', 'which', 'often', 'lima', "'m", 'kinahanglan', 'over', 'tuesday', 'too', 'against', 'pataas', 'no', 'niyang', 'its', 'october', 'sometimes', 'nobody', 'whereafter', "'ll", 'must', 'ato', 'paraan', 'herein', 'so', 'thursday', 'whereas', 'bottom', 'via', 'iyo', 'me', 'kanyang', 'walang', 'ating', 'unsaon', 'afterwards', 'n‘t', 'gusto', 'per', 'name', 'everything', 'fri', 'na', 'regarding', 'once', 'my', 'best', 'all', 'part', '‘s', 'almost', 'rather', 'for', 'never', 'm', 'forty', 'in', 'many', 'bago', 'whose', 'without', 'kay', 'mao', 'throughout', 'become', 'whenever', 'empty', 'gayunman', 'bakit', 'himself', 'hundred', 'ginagawa', 'eleven', 'april', 'tues', 'thereupon', 'either', 'namely', 'within', 'sun', 'habang', 'maaaring', 'who', 'give', 'ubos', 'maam', 'others', 'bilang', 'maaari', 'kaniya', 'imong'}