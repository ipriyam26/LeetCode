/*
 * @lc app=leetcode id=130 lang=java
 *
 * [130] Surrounded Regions
 */

// @lc code=start
class Solution {
    class UnionFind{
    int[] size;
    int[] id;
    
        public UnionFind(int size){
            this.id = new int[size];
            this.size = new int[size];
            for(int i = 0; i < size; i++){
                this.id[i] = i;
                this.size[i] = 1;
            }
        }
    
        public  int find(int x){
    
            int root = x;
            while(root != id[root]){
                root = id[root];
            }
            //compress path
            while(x != root){
                int temp = id[x];
                id[x] = root;
                x = temp;
            }
            return root;
    
        }
        public void union(int x, int y){
            int rootX = find(x);
            int rootY = find(y);
            if(rootX == rootY){
                return;
            }
            if(size[rootX] > size[rootY]){
                id[rootY] = rootX;
                size[rootX] += size[rootY];
            }else{
                id[rootX] = rootY;
                size[rootY] += size[rootX];
            }
        }
        public boolean connected(int x, int y){
            return find(x) == find(y);
        }
        public int findLargestComponent(){
            int max = 0;
            for(int i = 0; i < size.length; i++){
                max = Math.max(max, size[i]);
            }
            return max;
        }
    
    
    }
    public void solve(char[][] board) {
        int n = board.length;
        int m = board[0].length;
        UnionFind UF = new UnionFind(n*m+1);

      for (int i = 0; i < n; i++) {
          for (int j = 0; j < m; j++) {
              if(j==0||j==m-1||i==0||i==n-1){
                  UF.union(i*m+j, n*m);
              }
              else if(board[i][j]=='O'){
                  if(board[i-1][j]=='O'){
                      UF.union((i-1)*m+j,    i*m+j);
                  }
                  if(board[i+1][j]=='O'){
                      UF.union((i+1)*m+j,i*m+j );
                  }
                  if(board[i][j-1]=='O'){
                      UF.union(i*m+(j-1), i*m+j);
                  }
                  if(board[i][j+1]=='O'){
                      UF.union(i*m+(j+1), i*m+j);
                  }
              }
          }
      }

      for (int i = 0; i < n; i++) {
          for (int j = 0; j < m; j++) {
              if(!UF.connected(i*m+j, n*m)){
                  board[i][j] ='X';
              }
          }
      }

        
    }
}
// @lc code=end

