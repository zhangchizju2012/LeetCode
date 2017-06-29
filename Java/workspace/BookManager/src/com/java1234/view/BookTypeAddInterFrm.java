package com.java1234.view;

import java.awt.EventQueue;

import javax.swing.JInternalFrame;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.LayoutStyle.ComponentPlacement;

import com.java1234.dao.BookTypeDao;
import com.java1234.model.BookType;
import com.java1234.util.DbUtil;
import com.java1234.util.StringUtil;

import javax.swing.JTextArea;
import javax.swing.JButton;
import javax.swing.ImageIcon;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.awt.event.ActionEvent;

public class BookTypeAddInterFrm extends JInternalFrame {
	private JTextField bookTypeNameTxt;
	private JTextArea bookTypeDescTxt;
	private DbUtil dbUtil = new DbUtil();
	private BookTypeDao bookTypeDao = new BookTypeDao();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					BookTypeAddInterFrm frame = new BookTypeAddInterFrm();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public BookTypeAddInterFrm() {
		setClosable(true);
		setIconifiable(true);
		setTitle("图书类别添加");
		setBounds(100, 100, 450, 300);
		
		JLabel label = new JLabel("图书类别名称：");
		
		JLabel label_1 = new JLabel("图书类别描述：");
		
		bookTypeNameTxt = new JTextField();
		bookTypeNameTxt.setColumns(10);
		
		bookTypeDescTxt = new JTextArea();
		
		JButton button = new JButton("添加");
		button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				bookTypeAddActionPerformed(e);
			}
		});
		button.setIcon(new ImageIcon(BookTypeAddInterFrm.class.getResource("/images/add.png")));
		
		JButton button_1 = new JButton("重置");
		button_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				resetValueActionPerformed(e);
			}
		});
		button_1.setIcon(new ImageIcon(BookTypeAddInterFrm.class.getResource("/images/reset.png")));
		GroupLayout groupLayout = new GroupLayout(getContentPane());
		groupLayout.setHorizontalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addGroup(groupLayout.createSequentialGroup()
					.addGroup(groupLayout.createParallelGroup(Alignment.LEADING)
						.addGroup(groupLayout.createSequentialGroup()
							.addGap(76)
							.addGroup(groupLayout.createParallelGroup(Alignment.LEADING)
								.addGroup(groupLayout.createSequentialGroup()
									.addComponent(label_1)
									.addPreferredGap(ComponentPlacement.RELATED)
									.addComponent(bookTypeDescTxt, GroupLayout.PREFERRED_SIZE, 205, GroupLayout.PREFERRED_SIZE))
								.addGroup(groupLayout.createSequentialGroup()
									.addComponent(label)
									.addPreferredGap(ComponentPlacement.RELATED)
									.addComponent(bookTypeNameTxt, GroupLayout.PREFERRED_SIZE, 192, GroupLayout.PREFERRED_SIZE))))
						.addGroup(groupLayout.createSequentialGroup()
							.addGap(62)
							.addComponent(button)
							.addGap(59)
							.addComponent(button_1)))
					.addContainerGap(48, Short.MAX_VALUE))
		);
		groupLayout.setVerticalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addGroup(groupLayout.createSequentialGroup()
					.addGap(46)
					.addGroup(groupLayout.createParallelGroup(Alignment.BASELINE)
						.addComponent(label)
						.addComponent(bookTypeNameTxt, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
					.addGap(34)
					.addGroup(groupLayout.createParallelGroup(Alignment.BASELINE)
						.addComponent(label_1)
						.addComponent(bookTypeDescTxt, GroupLayout.PREFERRED_SIZE, 85, GroupLayout.PREFERRED_SIZE))
					.addGap(18)
					.addGroup(groupLayout.createParallelGroup(Alignment.BASELINE)
						.addComponent(button)
						.addComponent(button_1))
					.addContainerGap(16, Short.MAX_VALUE))
		);
		getContentPane().setLayout(groupLayout);

	}
	/*
	 * 图书类别添加事件处理
	 */
	private void bookTypeAddActionPerformed(ActionEvent evt) {
		// TODO Auto-generated method stub
		String bookTypeName = this.bookTypeNameTxt.getText();
		String bookTypeDesc = this.bookTypeDescTxt.getText();
		if(StringUtil.isEmpty(bookTypeName)){
			JOptionPane.showMessageDialog(null, "图书类别名称不能为空！");
			return;
		}
		BookType bookType = new BookType(bookTypeName,bookTypeDesc);
		Connection con = null;
		try{
			con = dbUtil.getCon();
			int n = bookTypeDao.add(con, bookType);
			if(n==1){
				JOptionPane.showMessageDialog(null, "图书类别添加成功！");
				resetValue();
			}else{
				JOptionPane.showMessageDialog(null, "图书类别添加失败！");
			}
		}catch(Exception e){
			e.printStackTrace();
			JOptionPane.showMessageDialog(null, "图书类别添加失败！");
		}finally {
			try {
				dbUtil.closeCon(con);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

	/*
	 * 重置事件处理
	 */
	private void resetValueActionPerformed(ActionEvent evt) {
		// TODO Auto-generated method stub
		this.resetValue();
	}

	/*
	 * 重置表单
	 */
	private void resetValue(){
		this.bookTypeNameTxt.setText("");
		this.bookTypeDescTxt.setText("");
	}
}
