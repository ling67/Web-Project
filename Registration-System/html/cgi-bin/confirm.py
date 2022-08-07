#!/usr/local/bin/python3

import mysql.connector

# Import modules for CGI handling
import cgi
import cgitb
from send import sendEmailToUser

cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

resultHtml1 = '''
<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >
   <TR VALIGN=TOP>
      <TD>
         <pre>
Registration Successful
     Thanks
</pre>
      </TD>
   </TR>
</TABLE>
'''

resultHtml2 = '''
<HTML>
   <TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >
      <TR VALIGN=TOP>
         <TD>
            <pre>
So, The Information Is Incorrect.

       <a href="/cgi-bin/regist.py">Please Registration Again</a>

       <a href="/regist.html">Back To Top</a>
</pre>
         </TD>
      </TR>
   </TABLE>
</HTML>
'''

"""
create table user_tb(
user_id int not null auto_increment,
user_name varchar(100) not null,
user_email varchar(40) not null,
submission_date date,
primary key (user_id)
)
"""

form = cgi.FieldStorage()

# Step 6.1: Read Name and E-mail address sent from the client.
name = form.getvalue('name')
email = form.getvalue('email')

# Open database connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    database="cs531",
    user="root",
    password="12345678",
    auth_plugin='mysql_native_password')


# Get data from fields
if form.getvalue('confirm') == 'yes':
    
    # prepare a cursor object using cursor() method
    cursor = conn.cursor()
    sql1 = "insert into user(user_name, email) VALUES (%s, %s)"
    val = (name, email)
    cursor.execute(sql1, val)

    # Step 6.3: Read the client's E-mail address from the database.
    # Step 6.4: Send a SMS to the client. The message content is
    sql2 = "select * from user where user_name = '%s'" % (name)
    cursor.execute(sql2)
    results = cursor.fetchall()
    for row in results:
        sendEmailToUser(row[2], "Thank you")
    conn.close()

    print(resultHtml1)

else:  # form.getvalue('confirm') == 'no'
    print(resultHtml2)



