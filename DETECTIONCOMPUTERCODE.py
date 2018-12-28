import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromaddr = "adhi.thirumala@gmail.com"
toaddr = "adhi.thirumala@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Your camera has detected a bird."

body = "placeholder for file"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "adhitya2006")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
