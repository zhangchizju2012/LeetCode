/**
 * @author zhangchi
 *
 * 2017年9月27日 下午11:19:41
 */
package amazon;


//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}


/**
 * @author zhangchi
 * 2017年9月27日 下午11:19:41
 */
public class MergeTwoSortedLists {
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode temp = result;
        while(l1 != null && l2 != null){
            if(l1.val < l2.val){
                temp.next = l1;
                l1 = l1.next;
            }else{
                temp.next = l2;
                l2 = l2.next;
            }
            temp = temp.next;
        }
        if(l1 == null){
            temp.next = l2;
        }else{
            temp.next = l1;
        }
        return result.next;
    }
}
