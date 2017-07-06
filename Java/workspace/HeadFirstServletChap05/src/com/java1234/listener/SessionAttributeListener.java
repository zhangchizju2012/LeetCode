package com.java1234.listener;

import javax.servlet.http.HttpSessionAttributeListener;
import javax.servlet.http.HttpSessionBindingEvent;

public class SessionAttributeListener implements HttpSessionAttributeListener{

	@Override
	public void attributeAdded(HttpSessionBindingEvent httpSessionBindingEvent) {
		// TODO Auto-generated method stub
		System.out.println("添加的属性名："+httpSessionBindingEvent.getName()+",属性值："+httpSessionBindingEvent.getValue());
	}

	@Override
	public void attributeRemoved(HttpSessionBindingEvent httpSessionBindingEvent) {
		// TODO Auto-generated method stub
		System.out.println("删除的属性名："+httpSessionBindingEvent.getName()+",属性值："+httpSessionBindingEvent.getValue());
	}

	@Override
	public void attributeReplaced(HttpSessionBindingEvent httpSessionBindingEvent) {
		// TODO Auto-generated method stub
		System.out.println("修改的属性名："+httpSessionBindingEvent.getName()+",属性值："+httpSessionBindingEvent.getValue());
	}
	

}
