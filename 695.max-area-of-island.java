import java.util.Arrays;

/*
 * @lc app=leetcode id=695 lang=java
 *
 * [695] Max Area of Island
 */

// @lc code=start
class Solution {
    class UnionFind {
        int[] size;
        int[] id;

        int count=0;

        public UnionFind(int size) {

            this.id = new int[size];
            this.size = new int[size];
            for (int i = 0; i < size; i++) {
                this.id[i] = i;
                this.size[i] = 1;

            }
        }

        public int find(int x) {

            int root = x;
            while (root != id[root]) {
                root = id[root];
            }
            // compress path
            while (x != root) {
                int temp = id[x];
                id[x] = root;
                x = temp;
            }
            return root;

        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY) {
                return;
            }

            if (size[rootX] > size[rootY]) {
                id[rootY] = rootX;
                size[rootX] += size[rootY];
            } else {
                id[rootX] = rootY;
                size[rootY] += size[rootX];
            }
        }

        public int findLargestComponent() {
            System.out.println(Arrays.toString(size));
            int max = 0;
            for (int i = 0; i < size.length; i++) {
                max = Math.max(max, size[i]);
            }
int cpp=0;
            for (int i = 0; i < id.length; i++) {
                if(id[i]==max){
cpp++;
                }
            }
            return cpp;
        }
        public void increaseCount(){
            this.count++;
        }

        public void printTheId(){
            
            System.out.println(Arrays.toString(id));
        }
       
    }
    public int maxAreaOfIsland(int[][] grid) {
        int m = grid[0].length;
        int n = grid.length;
        UnionFind uf = new UnionFind(n * m + 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {

                    if (i > 0 && grid[i - 1][j] == '1') {
                        uf.union(i * m + j, (i - 1) * m + j);
                    }
                    if (j > 0 && grid[i][j - 1] == '1') {
                        uf.union(i * m + j, i * m + j - 1);
                    }
                    if(i<n-1 && grid[i+1][j]=='1'){
                        uf.union(i * m + j, (i + 1) * m + j);
                        
                    }
                    if(j<m-1&& grid[i][j+1]=='1'){
                        uf.union(i * m + j, i * m + j + 1);

                    }
                }
            }
        }
        uf.printTheId();
        return uf.findLargestComponent(); 
    }
}
// @lc code=end

