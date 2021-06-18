class Solution(object):
    
        
    def __init__(self):
        self.max_row = 0
        self.max_col = 0
        
        self.forest =[]
        
        self.tree_height_vertex_dict = {}
        self.vertex_neighbor_dict={}
                
            
            
            
    def sort_by_height(self):
        for i in range(self.max_row):
            for j in range(self.max_col):
                # print(i, j, self.max_row, self.max_col)
                tree_height = self.forest[i][j]
                if tree_height<=1: continue
                    
                self.tree_height_vertex_dict[tree_height]=(i,j)
                
                
    def build_neighbor_list(self):
        for i in range(self.max_row):
            for j in range(self.max_col):
                if self.forest[i][j]==0:
                    continue
                self.vertex_neighbor_dict[(i,j)]=[]
                
                if i-1>=0 and self.forest[i-1][j]>0:
                    self.vertex_neighbor_dict[(i,j)].append((i-1,j))
                
                if i+1<self.max_row and self.forest[i+1][j]>0:
                    self.vertex_neighbor_dict[(i,j)].append((i+1,j))
                
                if j-1>=0 and self.forest[i][j-1]>0:
                    self.vertex_neighbor_dict[(i,j)].append((i,j-1))
                    
                if j+1<self.max_col and self.forest[i][j+1]>0:
                    self.vertex_neighbor_dict[(i,j)].append((i,j+1))
        
    def bfs(self,start_vertex, target_vertex ) :
        
        q = [start_vertex]
        
        steps_required = 0
        
        visted_vertex_set = set()
        visted_vertex_set.add(start_vertex)
        
        while(len(q)>0):
            
            count_last_level_nodes = len(q)
            
            for i in range(count_last_level_nodes):
                
                current_vertex = q.pop(0)
                
                
                if current_vertex == target_vertex:
                    return steps_required
                
                for next_vertex in self.vertex_neighbor_dict[current_vertex]:
                    
                    if next_vertex in visted_vertex_set:
                        continue
                        
                    q.append(next_vertex)
                    visted_vertex_set.add(next_vertex)
            steps_required +=1
                    
        return -1
                    
                        
                
    
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if forest[0][0]==0:
            return -1
        
        self.max_row = len(forest)
        self.max_col = len(forest[0])
        self.forest = forest
        
        self.sort_by_height()
        self.build_neighbor_list()
        
        # print(self.vertex_neighbor_dict)
        
        total_steps_required = 0
        start_vertex = (0,0)
        
        
        
        
        for h in sorted(self.tree_height_vertex_dict.keys()):
            target_vertex = self.tree_height_vertex_dict[h]
            
            step_required = self.bfs(start_vertex, target_vertex)
            
            # print(start_vertex, target_vertex,step_required )
            
            if step_required==-1:
                return -1
            total_steps_required += step_required
            start_vertex = target_vertex
        if total_steps_required == 0:
            return -1
        else:
            return total_steps_required


if __name__ == '__main__':
    forest = [[1,2,3],[0,0,4],[7,6,5]]

    sol = Solution()
    print("input forest: ", forest)
    print("total cost for forest is", sol.cutOffTree(forest))