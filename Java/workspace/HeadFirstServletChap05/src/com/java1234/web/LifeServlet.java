package com.java1234.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class LifeServlet extends HttpServlet{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	// servlet是作为请求的处理者, get:appends form data into the URL in name/value pairs
	// post: appends form data inside the body of the HTTP request. not shown in URL 

	// 服务阶段调用doGet, doPost
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		System.out.println("service");
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		System.out.println("service");
	}

	@Override
	// 销毁调用destroy()，关闭的时候调用（或者长时间不用）
	public void destroy() {
		System.out.println("servlet销毁");
	}

	@Override
	// 实例化调用init(),只执行一次（第一次请求服务的时候实例化，再请求一次就不初始化了） 
	// 类加载就是.xml文件里注释的流程信息(容器启动的时候就有)
	public void init() throws ServletException {
		System.out.println("servlet初始化");
	}
	
}
