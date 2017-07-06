package com.java1234.tag;

import java.io.IOException;
import java.util.Iterator;
import java.util.List;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.JspWriter;
import javax.servlet.jsp.tagext.TagSupport;

public class IterateTag extends TagSupport{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private String var;
	private String items;
	private Iterator iter;
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
	public Iterator getIter() {
		return iter;
	}
	public void setIter(Iterator iter) {
		this.iter = iter;
	}
	@Override
	public int doAfterBody() throws JspException {
		// 标签体执行完了之后的操作，本文件第57行，就是去执行标签体，执行完那个之后来执行这个
		if(iter.hasNext()){
			this.pageContext.setAttribute(var, iter.next());
			return TagSupport.EVAL_BODY_AGAIN; // 再执行一次标签体，还是第20行<h2>${p }</h2>
		}else{
			return TagSupport.SKIP_BODY; // 退出标签体执行
		}
	}
	@Override
	public int doStartTag() throws JspException {
		// 标签体执开始时的操作
		Object value=this.pageContext.getAttribute(items);
		if(value!=null && value instanceof List){
			this.iter=((List)value).iterator();
			if(iter.hasNext()){
				this.pageContext.setAttribute(var, iter.next());
				return TagSupport.EVAL_BODY_INCLUDE; // 执行标签体，对应于iterateTag里的第20行<h2>${p }</h2>
			}else{
				return TagSupport.SKIP_BODY; // 退出标签体执行
			}
		}else{
			return TagSupport.SKIP_BODY; // 退出标签体执行
		}
	}
	

	
}
