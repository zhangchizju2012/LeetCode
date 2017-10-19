<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>
<%@ taglib prefix="java1234" uri="/WEB-INF/java1234.tld" %> <!-- 前缀这个可以随意写，跟下面11行对应就可以了 -->
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	List people = new ArrayList();
	people.add("rich2");
	people.add("sutton2");
	people.add("osmar2");
	pageContext.setAttribute("people", people);
%>
<java1234:iterate2 items="people" var="p">
	<h2>${p }</h2>
</java1234:iterate2>
</body>
</html>