<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	//每一个输出都是有缓冲的
	int totalBuffer = out.getBufferSize();//获取总共缓冲区的大小
	int available = out.getRemaining();//获取未使用的缓冲区大小
	int used = totalBuffer - available;//使用了的
	out.println("总共缓冲区大小："+totalBuffer);
	out.println("总共未使用缓冲区大小："+available);
	out.println("使用缓冲区大小："+used);
%>
</body>
</html>