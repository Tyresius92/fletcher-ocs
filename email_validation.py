import re
import dns.resolver
import socket
import smtplib
import time

f = open("employer_emails.csv", "r")
lines = f.readlines()
f.close()

output = open("checked_emails_new.csv", "w")
output.write(lines[0].replace('\n', '') + ",isValid\n")

host = socket.gethostname()
server = smtplib.SMTP()
server.set_debuglevel(0)

del lines[0]

i = 0

for line in lines:
    time.sleep(1)
    
    i += 1
    if i % 100 == 0:
        print(str(i) + " emails processed")
        print("most recent email: " + email)
    
    try: 
        broken = line.split(sep=',')
        email = broken[-1].replace('\n', '')

        match = re.match(r'^[-_A-Za-z0-9]+(\.[-_A-Za-z0-9]+)*@[-A-Za-z0-9]+(\.[-A-Za-z0-9]+)*(\.[A-Za-z]{2,4})$', email).group

        if match == None:
            print("bad syntax: " + email)
            output.write(line.replace('\n', '') + ",Invalid,Bad Syntax\n")
        else:
            domain = email.split("@", 1)[1]
            
            records = dns.resolver.query(domain, 'MX')
            mxRecord = records[0].exchange
            mxRecord = str(mxRecord)

            host = socket.gethostname()
            server = smtplib.SMTP()
            server.set_debuglevel(0)

            server.connect(mxRecord)
            server.helo(host)
            server.mail('tyrel.clayton@tufts.edu')
            code, message = server.rcpt(str(email))
            server.quit()
            
            if code == 250:
                print("valid: " + email)
                output.write(line.replace('\n', '') + ",Valid\n")
            else:
                print("invalid: " + email)
                output.write(line.replace('\n', '') + ",Invalid,mxRecord returned value " + str(code) + "\n")
    except Exception as error:
        print("error: " + email)
        print(str(error))
        output.write(line.replace('\n', '') + ",Error," + str(error) + "\n")
        continue

    

output.close()
