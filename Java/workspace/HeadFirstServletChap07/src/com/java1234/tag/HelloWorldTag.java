package com.java1234.tag;

import java.io.IOException;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.tagext.TagSupport;

public class HelloWorldTag extends TagSupport{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	@Override
	public int doStartTag() throws JspException {
		// 标签开始的时候执行后台代码, 标签处理类
		JspWriter out = this.pageContext.getOut();
		try {
			out.println("自定义标签！");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return TagSupport.SKIP_BODY; //直接结束标签
	}
	
}
