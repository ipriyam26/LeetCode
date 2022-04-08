/*
 * @lc app=leetcode id=202 lang=java
 *
 * [202] Happy Number
 */

// @lc code=start
class Solution {
    public boolean isHappy(int n) {

        int fast = n;
        int slow =n;
        do{
            fast = squaredDigitSum(squaredDigitSum(fast));
            slow = squaredDigitSum(slow);
            if(fast==1 ){
                return true;
            }
        }while(slow!=fast);

        return false;
        
    }
    public int squaredDigitSum(int n){
        int sum=0;
        int d =n;
        while(n!=0){
            sum += (n%10)*(n%10);
            n=n/10;

        }
        // System.out.println(d+" : "+sum);
        return sum;

    }
}
// @lc code=end

