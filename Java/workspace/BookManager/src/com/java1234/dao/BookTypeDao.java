package com.java1234.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import com.java1234.model.BookType;
import com.java1234.util.StringUtil;

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
	/**
	 * 查询图书类别集合
	 * @param con
	 * @param bookType
	 * @return
	 * @throws Exception
	 */
	
	public ResultSet list(Connection con, BookType bookType) throws Exception{
		StringBuffer sb = new StringBuffer("Select * from t_bookType");
		if(StringUtil.isNotEmpty(bookType.getBookTypeName())){
			sb.append(" and bookTypeName like '%"+bookType.getBookTypeName()+"%'");//这里的and是为了避免出现多个情况，where .. and ..,不过这里并没有出现这种情况
		}
		PreparedStatement pstmt = con.prepareStatement(sb.toString().replaceFirst("and", "where"));
		return pstmt.executeQuery();
	}
	/**
	 * 删除图书类别
	 * @param con
	 * @param bookType
	 * @return
	 * @throws Exception
	 */
	public int delete(Connection con, BookType bookType) throws Exception{
		String sql = "DELETE FROM t_bookType WHERE id=?";
		PreparedStatement pstmt = con.prepareStatement(sql);
		pstmt.setInt(1, bookType.getId());
		return pstmt.executeUpdate();
	}
	
	/**
	 * 修改图书类别
	 * @param con
	 * @param bookType
	 * @return
	 * @throws Exception
	 */
	public int edit(Connection con, BookType bookType) throws Exception{
		String sql = "UPDATE t_bookType SET bookTypeName=?, bookTypeDesc=? WHERE id=?";
		PreparedStatement pstmt = con.prepareStatement(sql);
		pstmt.setString(1,bookType.getBookTypeName());
		pstmt.setString(2, bookType.getBookTyepDesc());
		pstmt.setInt(3, bookType.getId());
		return pstmt.executeUpdate();	
	}
}
