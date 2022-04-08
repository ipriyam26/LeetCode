import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Stack;

/*
 * @lc app=leetcode id=496 lang=java
 *
 * [496] Next Greater Element I
 */

// @lc code=start
class Solution {
//     public int[] nextGreaterElement(int[] nums1, int[] nums2) {
// int arr[] = new int[nums1.length];
// int k =0;
//         //Brute force
//         for (int i : nums1) {
//             //Find the element in array nums2
//             int j=0;
//             while (j<nums2.length) {
//                 if(i==nums2[j]){
//                     break;
//                 }
//                 j++;
//             }
//             while(j<nums2.length){
//                 if(nums2[j]>i){
//                     arr[k] = nums2[j];
//                     break;
//                 }
//             }
//             if(j==nums2.length){
//                 arr[k]=-1;
//             }
//             k++;
        
//         }
//         return arr;
//     }



public int[] nextGreaterElement(int[] nums1, int[] nums2)
{
     Map map = new HashMap<Integer,Integer>();
    for (int num : nums1) {
        map.put(num,0 );
    }
    int i =0;
    while(i<nums2.length){
        if(map.containsKey(nums2[i])){
            int j =i;
            while(j<nums2.length){
                if(nums2[j]>nums2[i]){
                   map.put(nums2[i],nums2[j]); 
                    break;

                }
                j++;
            }
            if(j==nums2.length){
                map.put(nums2[i],-1); 
            }
        }
        i++;
    }
    int k =0;
    int arr[] = new int[k]  ;
    for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
       arr[k]=entry.getValue(); 
    } 
 
    
    return arr;
}
}
// @lc code=end

