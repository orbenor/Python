#! /usr/bin/python

import smtplib

# dates ------------------------------------------------------------------------------
from datetime import date, timedelta

current_date = date.today().isoformat()   
days_before = (date.today()-timedelta(days=30)).isoformat()
days_after = (date.today()+timedelta(days=30)).isoformat()  

print("\nCurrent Date: ",current_date)
print("30 days before current date: ",days_before)
print("30 days after current date : ",days_after)

current_date = date.today().isoformat()   
days_before = (date.today()-timedelta(days=30)).isoformat()
days_after = (date.today()+timedelta(days=30)).isoformat()  

print("\nCurrent Date: ",current_date)
print("30 days before current date: ",days_before)
print("30 days after current date : ",days_after)

format1 = date.today().strftime('%d-%m-%Y')
days_before = (date.today()-timedelta(days=30)).strftime('%Y-%m-%d')
days_after = (date.today()+timedelta(days=30)).strftime('%Y-%m-%d')

print (format1)
print ('----------------------------------')
print("\nCurrent Date: ",format1)
print("30 days before current date: ",days_before)
print("30 days after current date : ",days_after)
# dates ------------------------------------------------------------------------------

# ======================== pandas ==================================

import pandas as pd

# dictionary of lists
# d = {'Car': ['BMW', 'Lexus', 'Audi', 'Mercedes', 'Jaguar', 'Bentley'],'Date_of_Purchase': ['2021-07-10', '2021-08-12', '2021-06-17', '2021-03-16', '2021-02-19', '2021-08-22']
#   }
d = pd.read_excel('list.xlsx')
# creating dataframe from the above dictionary of lists
dataFrame = pd.DataFrame(d)
print ('DataFrame...\n',dataFrame)

# fetch car purchased between two dates
# 1st Date: 2021-07-30
# 2nd Date: 2021-08-25
resDF = dataFrame.loc[(dataFrame["Until"] >= days_before) & (dataFrame["Until"] <= days_after)]

# print filtered data frame
print('\nCars purchased between 2 dates: \n',resDF)
result = resDF.to_html()
#text = resDF.astype(str)
print (result)
#print(text)
# ======================== pandas ==================================

#text = resDF

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "benor.or@example.com"
you = "benor.or@example.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi! TEXT\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
#html = """\
#<html>
#  <head></head>
#  <body>
#    <p>Hi! HTML <br>
#       How are you?<br>
#       Here is the <a href="http://www.python.org">link</a> you wanted.
#    </p>
#  </body>
#</html>
#"""

# Record the MIME types of both parts - text/plain and text/html.

part1 = MIMEText(text, 'plain')
part2 = MIMEText(result, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.example.com')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
