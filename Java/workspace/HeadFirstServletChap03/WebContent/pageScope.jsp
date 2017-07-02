<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	//设置两个page范围的数据key->value
	pageContext.setAttribute("name", "张弛");
	pageContext.setAttribute("age", 23);
%>
<%
	//取值
	String name = (String)pageContext.getAttribute("name");
	int age = (Integer)pageContext.getAttribute("age");
%>
<p>姓名：<%=name %></p>
<p>年龄：<%=age %></p>
</body>
</html>