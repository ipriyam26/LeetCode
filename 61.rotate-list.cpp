/*
 * @lc app=leetcode id=61 lang=cpp
 *
 * [61] Rotate List
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
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {

        ListNode* ptr = head;
        if(head==NULL){
            return head;
        }
        if(k==0){
            return head;
        }

        int len=1;
        while(ptr->next!=NULL){
            len++;
            ptr=ptr->next;
        }

        int r = k%len;
        ptr->next = head;
        ListNode* ptr2 = head;
        int i=1;
        while(i<len-r){
            ptr2=ptr2->next;
            i++;
        }
        ptr = ptr2->next;
        ptr2->next = NULL;
        return ptr;

    }
};
// @lc code=end

