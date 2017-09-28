/**
 * @author zhangchi
 *
 * 2017年9月21日 下午10:13:44
 */
package amazon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

class Point {
	float x;
	float y;
}

/**
 * @author zhangchi
 * 2017年9月21日 下午10:13:44
 */
public class GetKClosestPoint {
	public Point[] getKClosest(Point[] points, Point origin, int k){
		HashMap<Float, ArrayList<Point>> dic = new HashMap<>();
		ArrayList<Float> distancList = new ArrayList<>();
		float distance;
		ArrayList<Point> temp;
		for(Point p:points){
			distance = calculate(p, origin);
			distancList.add(distance);
			if(dic.containsKey(distance)){
				dic.get(distance).add(p);
			}else {
				temp = new ArrayList<>();
				temp.add(p);
				dic.put(distance, temp);
			}
		}
		Collections.sort(distancList);
		Point[] result = new Point[k];
		int index = 0;
		for(float d:distancList){
			temp = dic.get(d);
			Point point = temp.remove(temp.size()-1);
			result[index] = point;
		}
		return result;
	}
	public float calculate(Point p, Point o){
		return (float)(Math.pow(Math.abs(o.x-p.x),2) + Math.pow(Math.abs(o.y-p.y),2));
	}
	public static void main(String[] args){

		
	}
}
