#!/usr/local/bin/python3

# Import modules for CGI handling
import cgi
import cgitb
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('name')
email = form.getvalue('email')

resultHtml = '''
<HTML>
   Registration Form
   <table datasrc="#xmlRegData" border=2>
      <tr>
         <td> Name:</td>
         <td><span datafld="name">%s</span></td>
      </tr>
      <tr>
         <td>E-mail:</td>
         <td><span datafld="email">%s</td>
      </tr>
   </table>
   Is this information correct ?
   <form method=GET action=/cgi-bin/confirm.py>
      <input type="hidden" id='name' name='name' value='%s'>   
      <input type="hidden" id='email' name='email' value='%s'>   
      <input type=radio name='confirm' value='yes'> YES   
      <input type=radio name='confirm' value='no' checked> NO 
      <input type=submit value=Submit>     
      <input type=reset value=Reset>
   </form>
</HTML>
'''

print(resultHtml % (name, email, name, email))
