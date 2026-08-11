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
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr)
        {
            return head;
        }
        ListNode* nextNode = head->next;
        ListNode* current = head;
        ListNode* newNext = nullptr;
        head->next = nullptr;
        while (nextNode != nullptr)
        {
            newNext = nextNode->next;
            nextNode->next = current;
            current = nextNode;
            nextNode = newNext;
        }
        return current;
    }
};
