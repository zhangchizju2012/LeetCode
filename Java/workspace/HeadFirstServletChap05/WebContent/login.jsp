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
<form action="login" method="post"> 
<!-- 注意这里是login哦，没有.jsp，与web.xml中的 -->
<!-- <url-pattern>/login</url-pattern>对应 （自己写的）跳转了以后url会变-->
<table>
	<tr>
		<td>用户名：</td>
		<td><input type="text" name="userName" value="${userName }"/></td>
	</tr>
	<tr>
		<td>密码：</td>
		<td><input type="password" name="password" value="${password }"/></td>
	</tr>
	<tr>
		<td colspan="2"><input type="submit" value="提交"/></td>
		<!-- colspan用来合并单元格 -->
		<td><font color="red">${error }</font></td>
	</tr>
</table>
</form>
</body>
</html>