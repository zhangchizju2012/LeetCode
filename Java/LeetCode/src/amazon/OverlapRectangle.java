/**
 * @author zhangchi
 *
 * 2017年10月1日 下午5:29:49
 */
package amazon;

/**
 * @author zhangchi
 * 2017年10月1日 下午5:29:49
 */
public class OverlapRectangle {
	public boolean doOverlap(Point l1, Point r1, Point l2, Point r2){
		if(r1.x<=l2.x || r1.y>=l2.y || r2.x<=l1.x || r2.y>= l1.y){
			return false;
		}else{
			return true;
		}
	}
	public float computeArea(Point l1, Point r1, Point l2, Point r2){
		if(doOverlap(l1, r1, l2, r2)==false){
			return (r1.x-l1.x) * (l1.y - r1.y) + (r2.x-l2.x) * (l2.y - r2.y);
		}else{
			float innerL = Math.max(l1.x, l2.x);
			float innerR = Math.min(r1.x, r2.x);
			float innerT = Math.min(l1.y, l2.y);
			float innerB = Math.max(r1.y, r2.y);
			return (r1.x-l1.x) * (l1.y - r1.y) + (r2.x-l2.x) * (l2.y - r2.y) 
					- (innerR-innerL)*(innerT-innerB);
		}
	}
	public static void main(String[] args){
		Point l1 = new Point(-3,4);
		Point r1 = new Point(3,0);
		//Point l2 = new Point(0,2);
		//Point r2 = new Point(9,-1);
		Point l2 = new Point(-9,2);
		Point r2 = new Point(0,-1);
		OverlapRectangle overlapRectangle = new OverlapRectangle();
		System.out.println(overlapRectangle.computeArea(l1, r1, l2, r2));
	}
}
