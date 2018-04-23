import cgi
form = cgi.FieldStorage()
text =  form.getvalue('tweet')

print(text);
