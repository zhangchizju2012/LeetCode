package ood71myself;

//public class BlackJackDeck extends Deck<BlackJackCard>{
public class BlackJackDeck extends Deck<BlackJackCard, BlackJackHand>{

	@Override
	public void initialize() {
		// TODO Auto-generated method stub
		for(int i=1;i<=13;i++){
			for(int j=1;j<=4;j++){
				BlackJackCard c = new BlackJackCard(i, j);
				cards.add(c);
			}
		}
	}

	@Override
	// 注意这里是BlackJackHand[]而不是Hand<T>[]
	public BlackJackHand[] givePlayerInitialCard(int playerNumber) {
		// TODO Auto-generated method stub
		if(playerNumber>26){
			System.out.println("We don't have enough cards.");
			return null;
		}else{
			BlackJackHand[] bj = new BlackJackHand[playerNumber];
			for(int i=0;i<playerNumber;i++){
				bj[i] = new BlackJackHand();
				bj[i].setPlayerName(i);
				bj[i].addCard(getNextCard());
			}
			for(int i=0;i<playerNumber;i++){
				bj[i].addCard(getNextCard());
			}
			return bj;
		}
	}

}
