class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ct=defaultdict(lambda :-1)
        n=len(words)
        flg=-1
        for i in range(n):
            ct[words[i]]=i
            if words[i]=="":
                flg=i
        lst=[]
        for i in range(n):
            for j in range(len(words[i])):
                if ct[words[i][j:][::-1]]!=-1 and i!=ct[words[i][j:][::-1]] and words[i][:j]==words[i][:j][::-1]:
                    if [ct[words[i][j:][::-1]],i] not in lst:
                        lst.append([ct[words[i][j:][::-1]],i])
                if ct[words[i][:j][::-1]]!=-1 and i!=ct[words[i][:j][::-1]] and words[i][j:]==words[i][j:][::-1]:
                    
                    lst.append([i,ct[words[i][:j][::-1]]])
        if "" in words:
            for i in range(n):
                if ""!=words[i] and words[i][::-1]==words[i]:
                    if [i,flg] not in lst:
                        lst.append([i,flg])
                    if [flg,i] not in lst:
                        lst.append([flg,i])
        return lst
