package music;

import javax.sound.midi.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BeatBox {
	JCheckBox[] cbArray;
	Sequencer player;
	Sequence seq;
	Track track;
	public static void main(String[] args){
		BeatBox bb = new BeatBox();
		bb.draw();
		bb.midiGo();
	}
	public void midiGo(){
		try{
			player = MidiSystem.getSequencer();
			player.open();
			seq = new Sequence(Sequence.PPQ, 4);
			track = seq.createTrack();
			}catch(Exception ex){
				System.out.println("error");
		}
	}
	public void draw(){
		JFrame frame = new JFrame();
		frame.setTitle("Cyber BeatBox");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		frame.getContentPane().add(BorderLayout.WEST, addLeftPanel());
		frame.getContentPane().add(BorderLayout.EAST, addRightPanel());
		frame.getContentPane().add(BorderLayout.CENTER, addMiddlePanel());
		frame.setSize(760, 480);
		frame.setVisible(true);
	}
	public Box addLeftPanel(){
		Box nameBox = new Box(BoxLayout.Y_AXIS);
		//JPanel panel = new JPanel();
		//panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
		String[] instrumentList = {"Bass Drum","Closed Hi-Hat","Open Hi-Hat","Acoustic Snare",
				"Crash Cymbal","Hand Clap","High Tom","Hi Bongo","Maracas","Whistle","Low Conga",
				"Cowbell","Vibraslap","Low-mid Tom","High Agogo","Open Hi Conga"};
		for(int i=0; i<instrumentList.length; i++){
			JLabel label = new JLabel(instrumentList[i]);
			nameBox.add(label);
		}
		return nameBox;
	}
//	public Box addRightPanel(){
//		Box b = new Box(BoxLayout.Y_AXIS);
//		//JPanel panel = new JPanel();
//		//panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
//		String[] commandList = {"Start","Stop","Tempo Up","Tempo Down"};
//		for(int i=0; i<commandList.length; i++){
//			JButton button = new JButton(commandList[i]);
//			b.add(button);
//		}
//		return b;
//	}
	public Box addRightPanel(){
		Box b = new Box(BoxLayout.Y_AXIS);
		//JPanel panel = new JPanel();
		//panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
		//String[] commandList = {"Start","Stop","Tempo Up","Tempo Down"};
		//for(int i=0; i<commandList.length; i++){
		JButton startButton = new JButton("Start");
		startButton.addActionListener(new StartButtonListen());
		b.add(startButton);
		
		JButton stopButton = new JButton("Stop");
		stopButton.addActionListener(new StopButtonListen());
		b.add(stopButton);
		
		JButton tempoUpButton = new JButton("Tempo Up");
		tempoUpButton.addActionListener(new TempoUpListen());
		b.add(tempoUpButton);
		
		JButton tempoDownButton = new JButton("Tempo Down");
		tempoDownButton.addActionListener(new TempoDownListen());
		b.add(tempoDownButton);
				
		return b;
	}
	public JPanel addMiddlePanel(){
		GridLayout grid = new GridLayout(16, 16);
		grid.setVgap(1);
		grid.setHgap(2);
		JPanel panel = new JPanel(grid);
		cbArray = new JCheckBox[256];
		for(int i=0; i<256; i++){
			JCheckBox check = new JCheckBox();
			cbArray[i] = check;
			panel.add(check);
		}
		return panel;
	}
	class StartButtonListen implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			System.out.println("start");
			int[] instruments = {35,42,46,38,49,39,50,60,70,72,64,56,58,47,67,63};
			for(int i=0; i<16; i++){
				for(int j=0; j<16; j++){
					if(cbArray[i*16+j].isSelected()){
						track.add(makeEvent(144, 9, instruments[i], 100, j));
						track.add(makeEvent(128, 9, instruments[i], 100, j+1));
					}
				}
			}
			try{
				track.add(makeEvent(176, 1, 127, 0, 16));//16拍有事件才能重复播放
				player.setSequence(seq);
				player.setLoopCount(Sequencer.LOOP_CONTINUOUSLY);//使能够无穷循环
				player.start();
				System.out.println("success");
			}catch(Exception ex){
				System.out.println("error");
			}
		}
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
	class StopButtonListen implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			System.out.println("stop");
			player.stop();
		}
	}
	class TempoUpListen implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			System.out.println("tempo up");
		}
	}
	class TempoDownListen implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			System.out.println("tempo down");
		}
	}
}
