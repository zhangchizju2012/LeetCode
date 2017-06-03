package music;

import javax.sound.midi.*;
import javax.swing.*;

import java.awt.*;

public class MiniMusicPlayer {
	MyDrawPanel mp;//it's important to be put outside
	public static void main(String[] args){
		MiniMusicPlayer mmp = new MiniMusicPlayer();
		mmp.go();
	}
	public void go(){
		draw();
		try{
			Sequencer player = MidiSystem.getSequencer();
			player.open();
			
			Sequence seq = new Sequence(Sequence.PPQ, 4);
			
			int[] eventIWant = {127};// 这个参数还没搞懂
			player.addControllerEventListener(mp, eventIWant);
			//player是监听的，一旦监听到满足条件的行为就会导致：action真正执行
			// see line 8, can't be new MyDrawPanel();
			// 明天再对比这个位置的mp和SimpleGUI.java中同样位置的new Button1Listen()，搞清楚为什么
			Track track = seq.createTrack();
			
			for(int i = 5; i < 61; i += 4){
				track.add(makeEvent(144, 1, i, 100, i));
				track.add(makeEvent(176, 1, 127, 0, i));
				track.add(makeEvent(128, 1, i, 100, i+2));
			}
			player.setSequence(seq);
			player.start();
			System.out.println("success");
			
		}catch(Exception ex){
			System.out.println("error");
		}
	}
	public void draw(){
		JFrame frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		mp = new MyDrawPanel();// see line 8, can't be MyDrawPanel mp = new MyDrawPanel()
		frame.getContentPane().add(mp);
		
		frame.setSize(300, 300);
		frame.setVisible(true);
	}
	public MidiEvent makeEvent(int a, int b, int c, int d, int e){
		MidiEvent event = null;
		try{
			ShortMessage message = new ShortMessage();
			message.setMessage(a, b, c, d);
			event = new MidiEvent(message, e);
		}catch(Exception ex){
			System.out.println("error");
		}
		return event;	
	}
	class MyDrawPanel extends JPanel implements ControllerEventListener{
		private static final long serialVersionUID = 7672070056814354519L;
		public void paintComponent(Graphics g){
			int red = (int)(Math.random()*255);
			int green = (int)(Math.random()*255);
			int blue = (int)(Math.random()*255);	
			Color randomColor = new Color(red, green, blue);
			g.setColor(randomColor);//set了之后就会对后面的产生作用，重新set就会对再之后的产生作用
			g.fillRect(0, 0, this.getWidth(), this.getWidth());
			
			red = (int)(Math.random()*255);
			green = (int)(Math.random()*255);
			blue = (int)(Math.random()*255);	
			randomColor = new Color(red, green, blue);
			g.setColor(randomColor);
			g.fillOval(70, 70, 100, 100);
		}
		@Override
		public void controlChange(ShortMessage event) {
			// TODO Auto-generated method stub
			repaint();
		}
		
	}
}
