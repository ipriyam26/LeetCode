import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=128 lang=java
 *
 * [128] Longest Consecutive Sequence
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


}

    public int longestConsecutive(int[] nums) {
        UnionFind uf = new UnionFind(nums.length);
        Map<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if(map.containsKey(nums[i])){
                continue;
            }
            if(map.containsKey(nums[i] - 1)){
                uf.union(i, map.get(nums[i] - 1));
            }
            if(map.containsKey(nums[i] + 1)){
                uf.union(i, map.get(nums[i] + 1));
            }
            map.put(nums[i], i);
        }
        return uf.findLargestComponent();
        
    }
}
// @lc code=end

