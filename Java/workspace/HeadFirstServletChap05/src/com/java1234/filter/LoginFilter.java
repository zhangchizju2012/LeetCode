package com.java1234.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

public class LoginFilter implements Filter{

	@Override
	public void destroy() {

	}

	@Override
	public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)
			throws IOException, ServletException {
		//注意这里的是ServletRequest而不是HttpServletRequest，需要进行类型转换
		HttpServletRequest request=(HttpServletRequest)servletRequest;
		HttpSession session=request.getSession();
		//Object o=request.getAttribute("resultUser");
		Object o=session.getAttribute("resultUser");
		String path=request.getServletPath();
		// 因为前面LoginServlet里是session.setAttribute("currentUser", resultUser);
		// 所以就算登录成功，sess
		if(o==null&&path.indexOf("login")<0){
			request.getRequestDispatcher("login.jsp").forward(servletRequest, servletResponse);
		}else{
			filterChain.doFilter(servletRequest, servletResponse);
			//这里是继续执行的意思（就是忽略这个过滤器，之前该怎么跑怎么跑），整体跑一边，可以把整个servlet的要注意的点都复习一遍
		}
	}

	@Override
	public void init(FilterConfig arg0) throws ServletException {

	}

}
