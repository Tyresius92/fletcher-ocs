import smtplib
import email_config

smtpObj = smtplib.SMTP('exchange.tufts.edu', 587)

smtpObj.ehlo()
smtpObj.starttls()

smtpObj.login(email_config.user, email_config.password)

smtpObj.sendmail(email_config.me, email_config.target, email_config.msg)

smtpObj.quit()
