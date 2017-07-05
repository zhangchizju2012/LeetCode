<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%-- <%@ page import="com.java1234.model.Student" %> --%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	request.setCharacterEncoding("utf-8");
%>
<jsp:useBean id="student" scope="page" class="com.java1234.model.Student"/>
<jsp:setProperty property="name" name="student"/>
<jsp:setProperty property="age" name="student" value="10"/>
<!-- 此处的property是实例化对象的property，如果实例化对象的property名称和发送过来的表单的名称不匹配，就要 -->
<!-- 用到param了，详情请看6A视频最末端，param是表单的名称 -->
<h1>姓名：<%=student.getName() %></h1>
<h1>年龄：<%=student.getAge() %></h1>
</body>
</html>