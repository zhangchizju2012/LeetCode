<%@page import="java.net.CookieStore"%>
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

<script type="text/javascript">
	function resetValue(){
		document.getElementById("userName").value = "";
		document.getElementById("pwd").value = "";
	}
</script>

<%
	String userName = null;
	String pwd = null;
	Cookie[] cookie = request.getCookies(); //浏览器的cookie，不是request带来的
	for(int i=0; cookie!=null && i<cookie.length;i++){
		if(cookie[i].getName().equals("userNameAndPwd")){
			userName=cookie[i].getValue().split("-")[0];
			pwd=cookie[i].getValue().split("-")[1];
		}
	}
	if(userName==null){
		userName = "";
	}
	if(pwd==null){
		pwd = "";
	}
%>
<!-- on submit, send the form-data to a file named /userLogin.jsp  -->
<form action="userLogin.jsp" method="get">
	<table>
		<tr>
			<td>用户名：</td>
			<td><input type="text" id="userName" name="userName" value="<%=userName%>"/></td>
		</tr>
		<tr>
			<td>密码：</td>
			<td><input type="password" id="pwd" name="pwd" value="<%=pwd%>"/></td>
		</tr>
		<tr>
			<td>记住密码：</td>
			<td><input type="checkbox" id="remember" name="remember" value="remember-me"/></td>
		</tr>
		<tr>
			<td><input type="submit" value="登录"/></td>
			<td><input type="button" value="重置" onclick="resetValue()"/></td>
		</tr>
	</table>
</form>
</body>
</html>