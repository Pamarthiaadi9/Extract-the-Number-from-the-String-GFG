class Solution:
    def ExtractNumber(self,sentence):
        #code here
        s = sentence.split()
        m = -1
        for i in s:
            if i[0].isdigit() and '9' not in i:
                m = max(m,int(i))
        return m if m != -1 else -1
