package com.java1234.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;

import com.java1234.model.BookType;

/**
 * 图书类别Dao类
 * @author zhangchi
 *
 */

public class BookTypeDao {

	public int add(Connection con, BookType bookType) throws Exception{
		String sql = "insert into t_bookType values(null,?,?)";
		PreparedStatement pstmt = con.prepareStatement(sql);
		pstmt.setString(1, bookType.getBookTypeName());
		pstmt.setString(2, bookType.getBookTyepDesc());
		return pstmt.executeUpdate();
	}
}
