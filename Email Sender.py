## This program is used to send E-mails from your account to one or,
## multiple accounts using the smtplib library in python.

import smtplib    ## used for sending emails using the Simple Mail Transfer Protocol (SMTP).

to = input("Enter The Email of recipent:\n")

content = input("Enter the content for E-mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)                     ## creates an SMTP (Simple Mail Transfer Protocol) object for the Gmail SMTP server on port 587.
    server.ehlo()                                                    ## sends an EHLO (Extended HELO) command to the SMTP server to identify the client and initiate the SMTP session.
    server.starttls()                                                ## starts a TLS (Transport Layer Security) encryption for the SMTP connection.
    server.login('SenderEmailAddress@gmail.com', '#######Password')  ## Login to Gmail Account
    server.sendmail('RecipentEmailAddress@gmail.com', to, content)   ## Recipent Information
    server.close()                                                   ## Closing the Server.

sendEmail(to, content)

## In Order For this to Work, We have to have Enabled Less Secure Apps on our G-MAil Account.



