import re
from collections import Counter

def word_count(text):
    count = Counter(re.findall('[a-z0-9]+', text.lower()))

    return count
