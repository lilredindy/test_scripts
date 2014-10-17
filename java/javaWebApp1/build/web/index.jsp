<%-- 
    Document   : index
    Created on : Feb 3, 2013, 1:12:06 PM
    Author     : shriamin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<%@ page import="javaWebApp1Pkg.JavaVersionDisplayApplet" %>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <script>
            document.write("javascript champ");
        </script>
<jsp:plugin type="applet" code="JavaVersionDisplayApplet.class"
  width="400" height="400">
  <jsp:fallback>
   <p>Unable to load applet</p>
   </jsp:fallback>
</jsp:plugin>

        <%
  //JavaVersionDisplayApplet myJavaVersionDisplayApplet = new JavaVersionDisplayApplet();
  
%>
    </body>
</html>
