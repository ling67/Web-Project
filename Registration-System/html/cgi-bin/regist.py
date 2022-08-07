#!/usr/local/bin/python3

# Import modules for CGI handling
import cgi
import cgitb

cgitb.enable()

resHtml = '''
<HTML>
   <HEAD>
      <TITLE>Registration Form</TITLE>
   </HEAD>
   Registration Form
   <form action="/cgi-bin/process.py" method=GET>
      Name: <input type=text name=name value="" size=23>
      <br>
      Email: <input type=text name=email value="" size=23>
      <br>
      <input type=submit value=Submit name=B1>        
      <input type=reset value=Reset name=B2>
   </form>
   </BODY>
</HTML>
'''

print(resHtml)
