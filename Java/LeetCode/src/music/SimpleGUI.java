package music;

import java.awt.event.*;
import javax.swing.*;
import java.awt.*;

class MyDrawPanel extends JPanel{
	private static final long serialVersionUID = 1L;
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
}

//public class SimpleGUI implements MouseListener {
public class SimpleGUI implements ActionListener {
	JButton button;
	JButton button2;
	JLabel label;
	MyDrawPanel mp;
	int count = 0;
	public static void main(String[] args){
		SimpleGUI sg = new SimpleGUI();
		sg.go();
	}
		
	public void go(){
		JFrame frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		button = new JButton("change color");
		button2 = new JButton("change label");
		frame.getContentPane().add(BorderLayout.SOUTH, button);
		frame.getContentPane().add(BorderLayout.EAST, button2);
		
		mp = new MyDrawPanel();
		frame.getContentPane().add(mp);
		
		label = new JLabel();
		label.setText("I'm a label.");
		frame.getContentPane().add(BorderLayout.WEST, label);
		
		frame.setSize(500, 500);
		frame.setVisible(true);
		button.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(count%2==1){
			button.setText("change");
		}else{
			button.setText("click me");
		}
		count += 1;
		mp.repaint();
	}
}
