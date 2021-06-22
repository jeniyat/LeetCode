class TrieNode:
    def __init__(self):
        self.childern = {}
        self.word = None

        
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def add_word(self, word):
        node = self.root
        
        for char in word:
            if char not in node.childern:
                node.childern[char]=TrieNode()
            node=node.childern[char]
            
        node.word = word
        
    def is_prefix(self, word):
        node = self.root
        
        for char in word:
            if char not in node.childern:
                return False
            node=node.childern[char]
        return True
            
    

class Solution(object):
    def __init__(self):
        self.trie_tree = Trie()
        self.resulted_words = []
        self.board = []
        self.word_list = []
        self.max_row = 0
        self.max_col = 0
        
        
    def build_trie_tree(self):
        for word in self.word_list:
            self.trie_tree.add_word(word)
     
    
    
    def dfs(self, row, col, node, visited):
        if node.word:
            self.resulted_words.append(node.word)
            node.word=None # to avoid duplicates
            
        if row<0 or row>=self.max_row or col<0 or col>=self.max_col:
            return 
        
        if self.board[row][col] not in node.childern:
            return 
        
        visited.add((row, col))
        
        # self.board[row][col] = 0 # to mark current postion as in processing
        
        neighbor_list = [(row+1, col), (row-1,col), (row, col-1), (row, col+1)]
        
        for neighbor in neighbor_list:
            neighbor_row = neighbor[0]
            neighbor_col = neighbor[1]
            
            
            
            if (neighbor_row, neighbor_col) in visited:
                continue
            else:
                self.dfs(neighbor_row, neighbor_col, node.childern[self.board[row][col]], visited)
        
        # self.board[row][col] = current_board_char
        visited.remove((row, col))
        
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.board = board
        self.max_row=len(board)
        self.max_col=len(board[0])
        
        self.word_list=words
        self.build_trie_tree()
        
        for i in range(self.max_row):
            for j in range(self.max_col):
                self.dfs(i, j, self.trie_tree.root, set())
                
        return self.resulted_words


if __name__ == '__main__':
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    valid_word = ["oath","pea","eat","rain"]
    sol = Solution()
    sol.findWords(board, valid_word)
