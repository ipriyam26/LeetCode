/*
 * @lc app=leetcode id=841 lang=java
 *
 * [841] Keys and Rooms
 */

// @lc code=start
class Solution {
    boolean visited[];
       public void dfs(List<List<Integer>> rooms, int n){
        visited[n] = true;
        for(int i = 0; i < rooms.get(n).size(); i++){
            if(!visited[rooms.get(n).get(i)]){
                dfs(rooms, rooms.get(n).get(i));
            }
        }
       }
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n =rooms.size();
        visited = new boolean[n];
        visited[0] = true;
        dfs(rooms, 0);
        for (int i = 0; i < visited.length; i++) {
            if (!visited[i]) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

