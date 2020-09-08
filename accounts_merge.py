class Solution(object):
    def accountsMerge(self, accounts):
        """
        
        :type accounts: List[List[str]]
        :rtype: List[List[str]]]
         n = len(accounts)
        email2name = dict()
        
        TODO https://leetcode.com/problems/accounts-merge/submissions/
        
        
        """
        n = len(accounts)
        email2name = dict()
        
        email2index = collections.defaultdict()
        uf = UnionFind(n)
        
        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                if email not in email2index:
                    email2name[email] = name
                    email2index[email] = i
                
                
                uf.union(email2index[account[1]],email2index[email])
                
        emailgroup= collections.defaultdict(list)
        for email in email2index:
            emailgroup[uf.find(email2index[email])].append(email)
        res = list()
        
        for item, emails in emailgroup.items():
            res.append([email2name[emails[0]]] + sorted(emails))
        return res
        
class UnionFind(object):
    
    def __init__(self, size):
        self.father = dict()
        
        for i in range(size):
            self.father[i] = i
            

    def find(self, x):
        if self.father[x] == x:
            return x
        
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
      