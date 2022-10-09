class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = set()
        for i in range(len(emails)):
            e = ''
            at = emails[i].index('@')
            front = emails[i][:at]
            end = emails[i][at:]
            
            for i in front:
                if i == '.':
                    continue
                elif i == '+':
                    break
                else:
                    e += i
            e += end
            
            dic.add(e)
        
        return len(dic)
        