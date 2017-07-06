package com.java1234.tag;

import java.io.IOException;
import java.util.Iterator;
import java.util.List;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.tagext.SimpleTagSupport;
import javax.servlet.jsp.tagext.TagSupport;

public class IterateSimpleTag extends SimpleTagSupport{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private String var;
	private String items;

	public String getVar() {
		return var;
	}
	public void setVar(String var) {
		this.var = var;
	}
	public String getItems() {
		return items;
	}
	public void setItems(String items) {
		this.items = items;
	}

	@Override
	public void doTag() throws JspException, IOException {
		Object value = this.getJspContext().getAttribute(items); //this.getJspContext()是获取pageContext的方式
		if(value!=null && value instanceof List){
			Iterator iter=((List)value).iterator();
			while(iter.hasNext()){
				this.getJspContext().setAttribute(var, iter.next());
				this.getJspBody().invoke(null); //相应页面，可以直接相应页面，直接来个循环 不断相应页面 一下全部输出
			}
		}
	}
	

	
}
