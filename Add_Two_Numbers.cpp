class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* random = new ListNode();
        ListNode* temp = random;
        int carry {0};
        while(l1 != nullptr || l2 != nullptr || carry){
            int sum{carry};
            if(l1 != nullptr){
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2 != nullptr){
                sum += l2->val;
                l2 = l2->next;
            }
            carry = sum / 10;
            ListNode* newNode = new ListNode(sum%10);
            temp->next = newNode;
            temp = temp->next;
        }
        return random->next;
    }
};