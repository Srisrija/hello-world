#!/usr/bin/env python
import smtplib
import subprocess
import os
import sys

def report_via_email():
 msg = MIMEText(“Server running out of disk space”)
 msg[“Subject”] = “Low disk space warning”
 msg[“From”] = “admin@example.com”
 msg[“To”] = “test@gmail.com”
 with smtplib.SMTP(“smtp.gmail.com”, 587) as server:
 server.ehlo()
 server.starttls()
 server.login(“gmail_user”,”gmail_password)
 server.sendmail(“admin@example.com”,”test@gmail.com”,msg.as_string())
def check_once():
 df = subprocess.Popen([“df”,”-h”], stdout=subprocess.PIPE)
 for line in df.stdout:
 splitline = line.decode().split()
 if splitline[5] == partition:
 if int(splitline[4][:-1]) > threshold:
 report_via_email()
check_once()
