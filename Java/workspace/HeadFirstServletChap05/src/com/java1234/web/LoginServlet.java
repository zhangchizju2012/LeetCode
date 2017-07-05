package com.java1234.web;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.jasper.tagplugins.jstl.core.Out;

import com.java1234.dao.UserDao;
import com.java1234.model.User;
import com.java1234.util.DbUtil;

public class LoginServlet extends HttpServlet{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	// servlet是作为请求的处理者, get:appends form data into the URL in name/value pairs
	// post: appends form data inside the body of the HTTP request. not shown in URL 

	@Override
	// 根据请求种类来选择doGet还是doPost,helloWorld这个例子是doGet
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doPost(request, response);
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//这部分是自己写的
		
		String userName = request.getParameter("userName");
		String password = request.getParameter("password");
		User user = new User(userName, password);
		UserDao userDao = new UserDao();
		Connection con = null;
		DbUtil dbUtil = new DbUtil();
		User resultUser = null;
		try {
			con = dbUtil.getCon();
			if(con!=null){
				resultUser = userDao.login(con, user);
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
			try {
				dbUtil.closeCon(con);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		response.setCharacterEncoding("gbk");
		PrintWriter out=response.getWriter();
		if(resultUser!=null){
			out.println("登录成功");
		}else{
			out.println("登录失败");
		}
	}
	
}
