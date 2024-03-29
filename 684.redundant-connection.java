

/*
 * @lc app=leetcode id=684 lang=java
 *
 * [684] Redundant Connection
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
        public int findLargestComponent(){
            int max = 0;
            for(int i = 0; i < size.length; i++){
                max = Math.max(max, size[i]);
            }
            return max;
        }
        public boolean isConnected(int x,int y){
            return find(x)==find(y);
        }
    
    
    }

    public int[] findRedundantConnection(int[][] edges) {

      
       UnionFind uf = new UnionFind(edges.length+1);
       for (int i = 0; i < edges.length; i++) {
           if(uf.isConnected(edges[i][0], edges[i][1])){
return edges[i];
           }
           else{
               uf.union(edges[i][0], edges[i][1]);
           }
       }
       return edges[0];

    }
}

// @lc code=end
