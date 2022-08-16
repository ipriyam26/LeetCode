import java.util.Arrays;

/*
 * @lc app=leetcode id=947 lang=java
 *
 * [947] Most Stones Removed with Same Row or Column
 */

// @lc code=start
class Solution {

    class UnionFind{
    int[] size;
    int[] id;
    int count;
    
        public UnionFind(int size){
            this.id = new int[size];
            this.size = new int[size];
            for(int i = 0; i < size; i++){
                this.id[i] = i;
                this.size[i] = 0;
            }
            this.count =size;
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
            this.count--;
        }
        public int getNumberOfComponents(){
            return this.count;
        }
       
    
    
    }
    private boolean isConnected(int[] p1, int[] p2){
        return p1[0] == p2[0] || p1[1] == p2[1];
    }
    public int removeStones(int[][] stones) {

        int n = stones.length;
        UnionFind uf = new UnionFind(n);


        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected(stones[i], stones[j]))
                    uf.union(i, j);
            }
        }
        return n - uf.getNumberOfComponents();





        
    }
}
// @lc code=end

