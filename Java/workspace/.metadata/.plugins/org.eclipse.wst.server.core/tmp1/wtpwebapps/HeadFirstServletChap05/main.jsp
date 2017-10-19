<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="com.java1234.model.User" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	User user = null;/* 这里是为了配合request的试验 */
	user = (User)request.getAttribute("resultUser");
	if(user!=null){
		System.out.print(user.getUserName());
	}
%>
主页！当前登录用户：${resultUser.userName } &nbsp;&nbsp;<a href="logout">注销</a>
<!-- 这个logout在xml里进行配置 -->
</body>
</html>