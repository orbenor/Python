import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# https://stackoverflow.com/questions/41286569/get-total-of-pandas-column
df = pd.read_csv ('data.csv')
# X,MyColumn,Y,Z
# A,84,13.0,69.0
# B,76,77.0,127.0
# C,28,69.0,16.0
# D,28,28.0,31.0
# E,19,20.0,85.0
# F,84,193.0,70.0

print(df)
#a = df.loc['Total'] = pd.Series(df['MyColumn'].sum(), index = ['MyColumn'])
#print (a)
#b = df.loc['Total'] = pd.Series(df['Y'].sum(), index = ['Y'])
#print (b)
df = df.loc[df['MyColumn'] >= 78]
html = df.append(pd.DataFrame(df.MyColumn.sum(), index = ["Total"], columns=["MyColumn"]))
print (html)
html = html.to_html()
print (html)
html = html.replace("NaN", "")
print (html)

# select numeric columns and calculate the sums
#sums = df.select_dtypes(pd.np.number).sum().rename('total')

me = "benor.or@example.co.il"
you = "benor.or@example.co.il"

# you = "igal.turgeman@example.co.il"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Link'
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "yes" #select_age)
# "( my_df.loc[my_df['Age'] < 22].sum().Age )"
#text = "Hi! TEXT\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html + "Sent from benoradmin /root/scripts/excel/2.py\n", 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.example.co.il')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
