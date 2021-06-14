class Solution(object):
    def __init__(self):
        self.sub_str_lengths = {}
        self.input_str=""
        self.max_index = (-1,-1)
            
             
            
        
        
        
        
    def print_table(self, table):
        print("-------------")
        for row in table:
            print(row)
        print("-------------")
            
            
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        :type s: str
        :rtype: str
        """
        
        if not s or len(s)==0:
            return ""
        if len(s)==1:
            return s
        
        dp_table = []
        
        for i in range(len(s)):
            l = [False]*len(s)
            dp_table.append(l)
            
        
        
        # self.print_table(dp_table)
        
        
        for i in range(len(s)):
            dp_table[i][i]=True
            
            
         
        # self.print_table(dp_table)
        
        max_palin_length = 1
        max_palin_start = 0
        
        for j in range(1, len(s)):
            i = j-1
            if s[i]==s[j]:
                dp_table[i][j]=True
                max_palin_length=2
                max_palin_start= i
        # self.print_table(dp_table)
        
        
        
        count = 3
        
        while(count<=len(s)):
            for i in range(0, len(s)-count+1):
                j = i+count-1
                if i+1<len(s) and j-1>=0 and dp_table[i+1][j-1] and s[i]==s[j]:
                    dp_table[i][j]=True
                    max_palin_length=count
                    max_palin_start=i
            count+=1
            
        # self.print_table(dp_table)
        
        
        
        return s[max_palin_start: max_palin_start+max_palin_length]


if __name__ == '__main__':
    s = "babad"
    sol = Solution()
    print("input string:" ,s)
    print("longestPalindrome: ", sol.longestPalindrome(s))
