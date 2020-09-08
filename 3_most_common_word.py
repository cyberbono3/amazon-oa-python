
# https://leetcode.com/problems/most-common-word/

import re
from collections import Counter

def find_most_common_word(paragraph, banned):
    words = re.findall(r'\w+', paragraph.lower())
    allowed_words = [w for w in words if w not in set(banned)]
    return Counter(allowed_words).most_common()[0][0]
    
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(find_most_common_word(paragraph, banned))
  
    