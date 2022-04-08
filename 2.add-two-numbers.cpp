/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
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
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    // int createLinkedList(){

    // }
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *l3 = new ListNode();
        int val;
        ListNode *curr = l3;
        int carry = 0;
        while (l1 || l2 || carry)
        {
            if (l1 != NULL)
            {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL)
            {
                carry += l2->val;
                l2 = l2->next;
            }
            val = carry%10;
            curr->next = new ListNode(val);
            carry = carry/10;
            curr=curr->next ;
        }
        return l3->next;
    }
};
// @lc code=end
