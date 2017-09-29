/**
 * @author zhangchi
 *
 * 2017年9月28日 下午3:46:21
 */
package amazon;

//import java.util.LinkedHashSet;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * @author zhangchi
 * 2017年9月28日 下午3:46:21
 */
public class LRUCacheCountMiss {
	public int Solution(int[] array, int size) {
		int length = array.length;
		int result = 0;
		LinkedHashMap<Integer, Integer> temp = new LinkedHashMap<Integer, Integer>(){
			@Override
			public boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest){
				return this.size() > size;
			}
		};
		for(int i=0;i<length;i++){
			int value = array[i];
			if(temp.containsKey(value)){
				// 更新位置
				temp.remove(value);
				temp.put(value,0);
			}else{
				result += 1;
				temp.put(value,0);
			}
			System.out.println(temp);
		}
		return result;
	}
	public static void main(String[] args){
		LRUCacheCountMiss l = new LRUCacheCountMiss();
		int[] array = {1,2,3,4,5,4,1};
		System.out.println(l.Solution(array, 4));
	}
}
