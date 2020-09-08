
import re


class Solution:
    def compute_top_k_frequent_words(self, k, keywords, reviews):
        
        # address edges cases 
        if not keywords or not k or not reviews :
            return []
        
       
       
        dic = {}
        for rev in reviews:
            words = re.findall(r'\w+', rev.lower())
            rev_set = set(words)
            for keyword in keywords:
                if keyword in rev_set:
                    dic[keyword] = dic.get(keyword, 0) + 1   
        keyword_freqs = sorted(dic.items(), key = lambda x: (-x[1], x[0]))[:k]
        return [w for w,_ in keyword_freqs]
      
    
            


sol = Solution()
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
print(sol.compute_top_k_frequent_words(k, keywords, reviews) == ["anacell", "betacellular"])


k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
print(sol.compute_top_k_frequent_words(k, keywords, reviews) == ["betacellular", "anacell"] )
