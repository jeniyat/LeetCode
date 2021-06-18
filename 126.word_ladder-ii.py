class Solution(object):
    def __init__(self):
        self.next_word_dict = {}
        self.word_list = set()
        
        self.visited = set()
        self.word_distance = {}
        self.parent_dict = {}
        
        self.resultant_path= []
        
    def make_next_word_dict(self):
        for word in self.word_list:
            self.next_word_dict[word]=set()
            for i in range(len(word)):
                for char in set('abcdefghijklmnopqrstuvwxyz')-set(word[i]):
                    new_word = word[:i]+char+word[i+1:]
                    if new_word in self.word_list:
                        self.next_word_dict[word].add(new_word)
                        
    def init_word_distance(self): 
        for word in self.word_list:
            self.word_distance[word]=float('inf')
            
        
            
    def bfs(self, start_word, end_word):
        word_queue = [start_word]
        self.word_distance[start_word]=0
        # print(self.next_word_dict)
        
        while(len(word_queue)>0):
            current_word = word_queue.pop(0)
            self.visited.add(current_word)
            
            for next_word in self.next_word_dict[current_word]:
                
                if self.word_distance[current_word] + 1 <  self.word_distance[next_word]:
                        self.word_distance[next_word] = self.word_distance[current_word] + 1
                        word_queue.append(next_word)
                        self.parent_dict[next_word]=set()
                        self.parent_dict[next_word].add(current_word)
                        
                if self.word_distance[current_word] + 1 ==  self.word_distance[next_word]:
                    self.parent_dict[next_word].add(current_word)
                        
                        
    
    
    def dfs(self, current_word, beginWord, path):
        
        if current_word==beginWord:
            # if you reach the end word add in the front of the path & return 
            path = [current_word]+path
            self.resultant_path.append(path)
        else:
            for prev_word in self.parent_dict[current_word]:
                self.dfs(prev_word, beginWord, [current_word]+path)
        
    
    
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.word_list=set(wordList)
        self.word_list.add(beginWord)
        
        if endWord not in self.word_list:
            return []
        self.make_next_word_dict()
        self.init_word_distance()
        
        #use bfs to find the optimal parent
        self.bfs(beginWord, endWord)
        if endWord not in self.visited:
            return []
        #use dfs to find the path from end to begin word
        self.dfs(endWord, beginWord, [])
        return self.resultant_path
        

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sol = Solution()
    ladders = sol.findLadders(beginWord, endWord, wordList)
    print(ladders)
