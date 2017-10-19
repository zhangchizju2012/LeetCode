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
	pageContext.setAttribute("info1","page范围的值");
	request.setAttribute("info2","request范围的值");
	session.setAttribute("info3","session范围的值");
	application.setAttribute("info4","application范围的值");
%> 
<h1>${info1 }</h1> <!-- EL表达式，避免了不停地get，太麻烦了，可以直接通过名字拿出来, 寻找值的顺序:page->request->session->application -->
<h1>${info2 }</h1>
<h1>${info3 }</h1>
<h1>${info4 }</h1>
</body>

</html>