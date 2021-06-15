class Solution(object):
    def __init__(self):
        self.src_color=0
        self.dest_color =0
        self.vertex_neighbor_dict = {}
        self.max_rows = 0
        self.max_cols = 0
        self.visited = set()
        self.image= []
        
    def make_adjacency_list(self, image):
        for i in range(self.max_rows):
            for j in range(self.max_cols):
                self.vertex_neighbor_dict[(i,j)] = [] 
                
                if i-1>=0 and image[i][j]==image[i-1][j]:
                    self.vertex_neighbor_dict[(i,j)].append((i-1,j))
                    
                if j-1>=0 and image[i][j]==image[i][j-1]:
                    self.vertex_neighbor_dict[(i,j)].append((i,j-1))
                    
                if i+1<self.max_rows and image[i][j]==image[i+1][j]:
                    self.vertex_neighbor_dict[(i,j)].append((i+1,j))
                    
                if j+1<self.max_cols and  image[i][j]==image[i][j+1]:
                    self.vertex_neighbor_dict[(i,j)].append((i,j+1))
    def dfs(self, v):
        if v in self.visited:
            return
        self.visited.add(v)
        
        if self.image[v[0]][v[1]] == self.src_color:
            self.image[v[0]][v[1]]=self.dest_color
                                                                
        for n in self.vertex_neighbor_dict[v]:
            if n not in self.visited:
                self.dfs(n)
                                                                
                                                        
                                                                
                                                            
    def print_vertex_n_dict(self):
        for v in self.vertex_neighbor_dict:
            print(v)
            print(self.vertex_neighbor_dict[v])
            print("-------")
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.dest_color=newColor
        self.src_color=image[sr][sc]
        self.max_rows = len(image)
        self.max_cols = len(image[0])
        self.image = image
        self.make_adjacency_list(image)
        # self.print_vertex_n_dict()
        src_vertex = ((sr, sc))
        self.dfs(src_vertex)
        # print(self.image)
        return self.image
                            

if __name__ == '__main__':
    input_image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    sol = Solution()
    new_image = sol.floodFill(input_image, sr, sc, newColor)

    print("input_image: ", input_image)
    print("output_image: ", new_image)
