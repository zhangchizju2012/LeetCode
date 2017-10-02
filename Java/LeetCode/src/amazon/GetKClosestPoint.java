/**
 * @author zhangchi
 *
 * 2017年9月21日 下午10:13:44
 */
package amazon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.PriorityQueue;

class Point {
	float x;
	float y;
	/**
	 * 
	 */
	public Point(float a, float b) {
		// TODO Auto-generated constructor stub
		x = a;
		y = b;
	}
}

public class GetKClosestPoint {
	public Point[] getKClosest(Point[] points, Point origin, int k){
		if(points==null || k >= points.length){
			return points;
		}
		PriorityQueue<Point> temp = new PriorityQueue<Point>(new Comparator<Point>() {
			@Override
			public int compare(Point o1, Point o2) {
				// TODO Auto-generated method stub
				return Double.compare(calculate(o1, origin), calculate(o2, origin));
			}
		});
		for(Point item : points){
			temp.offer(item);
		}
		Point[] result = new Point[k];
		for(int i = 0;i<k;i++){
			result[i] = temp.poll();
		}
		return result;
	}
	public float calculate(Point a, Point b){
		return (a.x-b.x) * (a.x-b.x) + (a.y-b.y) * (a.y-b.y);
	}
	
}

//public class GetKClosestPoint {
//	public Point[] getKClosest(Point[] points, Point origin, int k){
//		
//		return null;
//		
//	}
//	public static void main(String[] args){
//		PriorityQueue<Integer> test = new PriorityQueue<Integer>(new 
//	Comparator<Integer>() {
//			@Override
//			public int compare(Integer o1, Integer o2) {
//				// TODO Auto-generated method stub
//				return Double.compare(o2,o1);
//			}
//		});
//		test.offer(1);
//		test.offer(0);
//		test.offer(2);
//		while(test.size()>0){
//			System.out.println(test.poll());
//		}
//	}
//	
//}

///**
// * @author zhangchi
// * 2017年9月21日 下午10:13:44
// */
//public class GetKClosestPoint {
//	public Point[] getKClosest(Point[] points, Point origin, int k){
//		HashMap<Float, ArrayList<Point>> dic = new HashMap<>();
//		ArrayList<Float> distancList = new ArrayList<>();
//		float distance;
//		ArrayList<Point> temp;
//		for(Point p:points){
//			distance = calculate(p, origin);
//			distancList.add(distance);
//			if(dic.containsKey(distance)){
//				dic.get(distance).add(p);
//			}else {
//				temp = new ArrayList<>();
//				temp.add(p);
//				dic.put(distance, temp);
//			}
//		}
//		Collections.sort(distancList);
//		Point[] result = new Point[k];
//		int index = 0;
//		for(float d:distancList){
//			if(index<k){
//				temp = dic.get(d);
//				Point point = temp.remove(temp.size()-1);
//				result[index] = point;
//				index += 1;
//			}
//		}
//		return result;
//	}
//	public float calculate(Point p, Point o){
//		return (float)(Math.pow(Math.abs(o.x-p.x),2) + Math.pow(Math.abs(o.y-p.y),2));
//	}
//	public static void main(String[] args){
//
//		
//	}
//}
