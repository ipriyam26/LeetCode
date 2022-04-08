/*
 * @lc app=leetcode id=82 lang=cpp
 *
 * [82] Remove Duplicates from Sorted List II
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
class Solution
{
public:
    // ListNode* deleteDuplicates(ListNode* head) {
    //     ListNode* ptr = head;
    //     ListNode* ptr2 = ptr;
    //     while (ptr)
    //     {
    //         if(ptr->val==ptr->next->val&&ptr->next!=NULL){
    //             while (ptr->val==ptr->next->val&&ptr->next!=NULL)
    //             {
    //                 ptr=ptr->next;
    //             }
    //             ptr2->next = ptr->next;

    //         }
    //         else{
    //             ptr2=ptr2->next;

    //         }
    //         ptr=ptr->next;
    //     }

    //     return head;
    // }

    ListNode *deleteDuplicates(ListNode *head)
    {

        ListNode *dummy = new ListNode(0, head);
        ListNode *prev = dummy;

        while (head != NULL)
        {

            if (head->next != NULL && head->val == head->next->val)
            {

                while (head->next != NULL && head->val == head->next->val)
{                    head = head->next;
}
                prev->next = head->next;
            }

            else
{                prev = prev->next;
}
            head = head->next;
        }

        return dummy->next;
    }
};
// @lc code=end
