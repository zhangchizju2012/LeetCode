package com.java1234.model;

/**
 * 图书类别实体
 * @author zhangchi
 *
 */
public class BookType {
	
	private int id; //编号
	private String bookTypeName; //名称
	private String bookTyepDesc; //备注
	public BookType() {
		super();
		// TODO Auto-generated constructor stub
	}
	public BookType(String bookTypeName, String bookTyepDesc) {
		super();
		this.bookTypeName = bookTypeName;
		this.bookTyepDesc = bookTyepDesc;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getBookTypeName() {
		return bookTypeName;
	}
	public void setBookTypeName(String bookTypeName) {
		this.bookTypeName = bookTypeName;
	}
	public String getBookTyepDesc() {
		return bookTyepDesc;
	}
	public void setBookTyepDesc(String bookTyepDesc) {
		this.bookTyepDesc = bookTyepDesc;
	}
}
