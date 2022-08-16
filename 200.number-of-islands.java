import java.util.HashSet;

/*
 * @lc app=leetcode id=200 lang=java
 *
 * [200] Number of Islands
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
            this.count--;
            if (size[rootX] > size[rootY]) {
                id[rootY] = rootX;
                size[rootX] += size[rootY];
            } else {
                id[rootX] = rootY;
                size[rootY] += size[rootX];
            }
        }

        public int findLargestComponent() {
            int max = 0;
            for (int i = 0; i < size.length; i++) {
                max = Math.max(max, size[i]);
            }
            return max;
        }
        public void increaseCount(){
            this.count++;
        }

       
    }

    public int numIslands(char[][] grid) {
        int m = grid[0].length;
        int n = grid.length;
        UnionFind uf = new UnionFind(n * m + 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    uf.increaseCount();
                    if (i > 0 && grid[i - 1][j] == '1') {
                        uf.union(i * m + j, (i - 1) * m + j);
                    }
                    if (j > 0 && grid[i][j - 1] == '1') {
                        uf.union(i * m + j, i * m + j - 1);
                    }
                }
            }
        }
        return uf.count;

    }
}
// @lc code=end
