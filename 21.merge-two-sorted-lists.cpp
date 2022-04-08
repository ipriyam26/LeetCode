/*
 * @lc app=leetcode id=21 lang=cpp
 *
 * [21] Merge Two Sorted Lists
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *ptr1 = list1;
        ListNode *ptr2 = list2;
        ListNode *list3 = new ListNode();
        ListNode *ptr3 = list3;
        while (ptr1&&ptr2)
        {
            if(ptr1->val<=ptr2->val){
                ptr3->next = ptr1;
                ptr3=ptr3->next;
                ptr1=ptr1->next;
                
            }
            else{
                ptr3->next = ptr2;
                ptr3=ptr3->next;
                ptr2=ptr2->next;
            }
        }
        if(ptr1){
            ptr3->next = ptr1;
        }else
        {
            ptr3->next=ptr2;
        }
        return list3->next;

    }
};
// @lc code=end

//[1,2,3,3,4,5]
//[0,2,4,4,6,6]

