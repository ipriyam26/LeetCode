import java.util.Stack;

/*
 * @lc app=leetcode id=735 lang=java
 *
 * [735] Asteroid Collision
 */

// @lc code=start
// class Solution {

//     public int[] asteroidCollision(int[] asteroids) {
//         int asteroidLength = asteroids.length;
//         if (asteroidLength == 0 || asteroidLength == 1) {
//             return asteroids;

//         }
//         Stack<Integer> collisions = new Stack<Integer>();
//         int i = 1;
//         int count = 1;
//         collisions.push(asteroids[0]);
//         while (i < asteroidLength) {
//             int asteroid = asteroids[i];

//             if (isOppositeSign(asteroid, collisions.peek())) {
//                 if (Math.abs(asteroid) > Math.abs(collisions.peek())) {
//                     collisions.pop();
//                     collisions.push(asteroid);

//                 }
//                 else if(Math.abs(asteroid) == Math.abs(collisions.peek())){
//                     collisions.pop();
//                     count--;
//                 }
//             } else {
//                 collisions.push(asteroid);
//                 count++;
//             }

//             i++;
//         }
//         int j = 0;
//         Stack<Integer> n = new Stack<Integer>();
//         while (!collisions.isEmpty()) {
//             n.push(collisions.pop());
//         }
//         int[] ans = new int[count];
//         while (!n.isEmpty()) {
//             ans[j] = n.pop();
//             j++;
//         }
//         return ans;
//     }

//     public boolean isOppositeSign(int a, int b) {
//         if (a * b >= 0) {
//             return false;
//         } else {
//             return true;
//         }
//     }
// }

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        LinkedList<Integer> stack = new LinkedList<>();
        
        List<Integer> result = new ArrayList<>();
        
        for(int asteroid: asteroids) {
            if(asteroid<0) {
                while(!stack.isEmpty() && -asteroid > stack.peekLast()) {
                    stack.removeLast();
                }
                
                if(stack.isEmpty()) {
                    result.add(asteroid);
                } else if(stack.peekLast() == -asteroid) {
					stack.removeLast();
				}

            } else stack.add(asteroid);
        }
        
        result.addAll(stack);
        
        return result.stream().mapToInt(x -> x).toArray();
    }
}
// @lc code=end
