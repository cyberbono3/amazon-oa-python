

"""
Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]



result = set()
for i in range(len(s) - k + 1):
    window = s[i:i+k]
    if len(window)  == len(set(window)):
        res.add("".join(window))
        

Input: s = "abacab", k = 3
Output: ["bac", "cab"]

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.


res = set()
P(n*k)
for i in range(n-k+1):  O(n)
    window = s[i:i+k]
    if len(window) == len(set(window)) O(k)
        # characters are all unique
        res.add("".join(window))
    
return list(res)

            0 1 2 3 4 5
Input: s = "a b a c a b", k = 3

                  ^   ^
Output: ["bac", "cab"]

dic = {a:2, c:1}
start = 1  , end = 3
result = {"bac", "cab"}

if end -start + 1 == k 
    if len(dic) == k:
        result.add("".join(s[start: end+1]))
    if dic[s[start]] > 1:
        dic[s[start]] -= 1
    else:
        del dic[s[start]]
    start += 1
    


"""     
class Solution: 
    def compute_unique_substrings(self, s, k):
        if not s or not k:
            return []
        start, dic, result = 0, {}, set()
        for i, char in enumerate(s):
            dic[char] = dic.get(char, 0) + 1
            if i - start + 1 == k:
                if len(dic) == k:
                    result.add("".join(s[start:i+1]))
                if dic[s[start]] > 1:
                    dic[s[start]] -= 1
                else:
                    del dic[s[start]]
                start += 1
        return list(result)
            
        
       
      
sol = Solution()
print(sol.compute_unique_substrings("abcabc", 3) == ["abc", "bca", "cab"])
print(sol.compute_unique_substrings("abacab", 3) == ["bac", "cab"])
print(sol.compute_unique_substrings("awaglknagawunagwkwagl", 4) == ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"])



        
    