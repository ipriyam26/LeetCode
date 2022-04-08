/*
 * @lc app=leetcode id=19 lang=cpp
 *
 * [19] Remove Nth Node From End of List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* ptr =head ;
        int len=0;
        while(ptr){
            ptr = ptr->next;
            len++;
        }
        if(len==n){
            return head->next;
        }
        ptr = head;
        for (int i = 1; i < len-n; i++)
        {
           ptr=ptr->next;
        }
        ptr->next=ptr->next->next;
        return head;
        

    }
};
// @lc code=end

