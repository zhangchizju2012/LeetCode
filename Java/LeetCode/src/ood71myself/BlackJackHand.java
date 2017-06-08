package ood71myself;

import java.util.ArrayList;

public class BlackJackHand extends Hand<BlackJackCard>{
	// 注意这个和Hand的对比：public abstract class Hand <T extends Card> 
	// 这里没有<T extends Card>，Hand后直接跟了满足<T extends Card> 的东西
	// 测试一下这个BlackJackHand怎么用，像昨天那个solution一样
	// 对比昨天的line 6 是不是就不用加<>了，嗯是的，不用加了 extends Hand<BlackJackCard> 已经包含了这一信息
	
//	public BlackJackHand(ArrayList<BlackJackCard> cs) {
//		super(cs);
//		// TODO Auto-generated constructor stub
//	}

	@Override
	public int getPoint() {
		// TODO Auto-generated method stub
		return 0;
	}

}
