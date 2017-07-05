package com.java1234.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HelloWorldServlet extends HttpServlet{

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
		//请求来了向页面输出东西（此处输出了html file）
		response.setCharacterEncoding("gbk");
		PrintWriter out=response.getWriter();
		out.println("<html>");
		out.println("<head><title>你好呀</title></head>");
		out.println("Servlet 你好");
		out.println("</html>");
		out.close();
	}
	
}
