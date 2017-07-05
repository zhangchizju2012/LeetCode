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
<!-- form是用来收集数据的 -->
<!-- action作用：on submit, send the form-data to a file named /javabean03-3.jsp  -->
<!-- method定义了发送表单数据的方法，get:appends form data into the URL in name/value pairs -->
<!-- post: appends form data inside the body of the HTTP request. not shown in URL -->
<form action="javabean03_2.jsp" method="post">
<table>
	<tr>
		<td>姓名：</td>
		<td><input type="text" name="name"/></td>
	</tr>
	<tr>
		<td>年龄：</td>
		<td><input type="text" name="age"/></td>
	</tr>
	<tr>
		<td colspan="2"><input type="submit" value="提交"/></td>
		<!-- colspan用来合并单元格 -->
	</tr>
</table>
</form>
</body>
</html>