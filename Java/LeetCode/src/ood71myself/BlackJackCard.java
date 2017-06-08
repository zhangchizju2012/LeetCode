package ood71myself;

public class BlackJackCard extends Card {
	public BlackJackCard(int v, int c){
		super(v, c);
	}
	public int getPoint(){
		return Math.min(value, 10);
	}
	public boolean isAce(){
		if(value==1){
			return true;
		}else{
			return false;
		}
	}
	public boolean isFace(){
		if(13>=value && value>=11){
			return true;
		}else{
			return false;
		}
	}
}
