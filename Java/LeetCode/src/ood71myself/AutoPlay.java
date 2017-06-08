package ood71myself;

import java.util.ArrayList;

public class AutoPlay {
	public static void main(String[] args){
		AutoPlay a = new AutoPlay();
		a.game();
	}
	public void game(){
		BlackJackDeck bjd = new BlackJackDeck();
		bjd.initialize();
		bjd.shuffle();
		BlackJackHand[] players = bjd.givePlayerInitialCard(20);
		ArrayList<BlackJackHand> winners = new ArrayList<>();
		for(BlackJackHand player:players){
			if(player.isBlackJack()){
				winners.add(player);
			}
		}
		if(winners.size()>0){
			System.out.println("Black Jack");
			for(BlackJackHand winner:winners){
				System.out.print(winner.getPlayerName());
				System.out.print(": ");
				for(BlackJackCard card:winner.getCards()){
					card.print();
				}
				System.out.println();
			}
		}else{
			boolean label = true;
			while(label){
				label = false;
				for(BlackJackHand player:players){
					if(player.getPoint()<16 && bjd.left()){
						player.addCard(bjd.getNextCard());
						label = true;
					}
				}
			}
			int maxValue = Integer.MIN_VALUE;
			for(BlackJackHand player:players){
				if(player.isExplosion() == false){
					if(player.getPoint()>maxValue){
						maxValue = player.getPoint();
						winners.clear();
						winners.add(player);
					}else if (player.getPoint() == maxValue) {
						winners.add(player);
					}
				}
			}
			if(winners.size()>0){
				for(BlackJackHand winner:winners){
					System.out.print(winner.getPlayerName());
					System.out.print("(");
					System.out.print(winner.getPoint());
					System.out.print(")");
					System.out.print(": ");
					for(BlackJackCard card:winner.getCards()){
						card.print();
					}
					System.out.println();
				}
			}else{
				System.out.println("全是渣渣");
			}
		}
	}
}
