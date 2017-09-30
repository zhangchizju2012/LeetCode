/**
 * @author zhangchi
 *
 * 2017年9月29日 下午10:53:42
 */
package amazon;

/**
 * @author zhangchi
 * 2017年9月29日 下午10:53:42
 */
public class HasCycle {
	public boolean hasCycle(ListNode head) {
        if(head == null){return false;}
        ListNode slow = head;
        ListNode fast = head;
        if(slow.next != null){
            slow = slow.next;
        }else{
            return false;
        }
        if(fast.next.next != null){
            fast = fast.next.next;
        }else{
            return false;
        }
        while(fast != slow){
            if(fast.next != null && fast.next.next != null){
                fast = fast.next.next;
            }else{
                return false;
            }
            slow = slow.next;
        }
        return true;
    }
}
