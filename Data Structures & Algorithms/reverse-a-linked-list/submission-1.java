/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) { return null; }
        ListNode prev = null, nex = head.next;
        while (!(head == null)) {
            head.next = prev;
            prev = head;
            head = nex;
            if (nex != null) nex = nex.next;
        }
        return prev;
    }
}
