import re
from functools import reduce

log_string = 'fhjkdfhjdfhjkdfhMEM:30-hfjkhfjksadhfjkMEM:40'

memory_occurance = re.findall('MEM:[0-9]{1,}', log_string)

print(memory_occurance)

print(reduce(lambda x,y: x+y, list(map(lambda x :int(x[4:]), memory_occurance))) / len(memory_occurance))

