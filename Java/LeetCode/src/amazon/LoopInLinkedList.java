/**
 * @author zhangchi
 *
 * 2017年9月29日 下午10:57:29
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月29日 下午10:57:29
 */
public class LoopInLinkedList {
	public ListNode detectCycle(ListNode head) {
        if(head == null){return null;}
        ListNode slow = head;
        ListNode fast = head;
        ListNode later = head;
        if(slow.next != null){
            slow = slow.next;
        }else{
            return null;
        }
        if(fast.next.next != null){
            fast = fast.next.next;
        }else{
            return null;
        }
        while(fast != slow){
            if(fast.next != null && fast.next.next != null){
                fast = fast.next.next;
            }else{
                return null;
            }
            slow = slow.next;
        }
        while(later != fast){
            later = later.next;
            fast = fast.next;
        }
        return later;
    }
}
