import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#cemail="demo"
def SM(name,email,opfilepath,yrstr):

  #print(name)
  #global cemail
  #cemail=cemail+str(email)
  
  result = yrstr.split('-')

  d1=result[1]
  d2=result[2]
  
  if email is not None:
   
   gpath=opfilepath+"/"+name+".xlsx"
   gname=name+".xlsx"
  
   print("---------------------")
    #print(gpath)
    # Email configuration
   sender_email = "swarajchbiswas11@gmail.com"
   app_password = "qcmwhqxxxxxxxxxx"
   recipient_email = email
   subject = "Bill of"+d1+" "+d2


# Creating the MIME object
   msg = MIMEMultipart()
   msg['From'] = sender_email
   msg['To'] = recipient_email
   msg['Subject'] = subject

# Attaching the .doc file
   docx_file_path = gpath
   with open(docx_file_path, 'rb') as file:
    attachment = MIMEApplication(file.read(), _subtype=".xlsx")
    attachment.add_header('Content-Disposition', 'attachment', filename=gname)
    msg.attach(attachment)

   body = "Dear Sir/Madam,Please find attached the bill of "+d1+" "+d2
   msg.attach(MIMEText(body, 'plain'))

# Connecting to the SMTP server and sending the email
   try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)  #  App Password
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully.")
   except Exception as e:
    print(f"Error: {e}")
    
    
    
    
    
   else:
    print("The string is None")
    
    



