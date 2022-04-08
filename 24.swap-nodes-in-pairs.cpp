/*
 * @lc app=leetcode id=24 lang=cpp
 *
 * [24] Swap Nodes in Pairs
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
    ListNode *swapPairs(ListNode *head)
    {
        ListNode *newHead = new ListNode();
        ListNode *previous = newHead;
        ListNode *ptr2;
        ListNode *nextPtr = previous;
        int i = 1;
        while (head!=NULL)
        {

            ptr2 = head;
            head=head->next;
                ptr2->next = NULL;

            if (i % 2 == 1)
            {
                nextPtr->next = ptr2;
                nextPtr = nextPtr->next;
                
            }
            else
            {
                previous->next = ptr2;
                ptr2->next = nextPtr;
                previous = nextPtr;
            }
            
            
            i++;
        }
        return newHead->next;
    }
};
// @lc code=end
