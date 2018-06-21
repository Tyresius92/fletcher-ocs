from validate_email import validate_email

f = open("employer_emails.csv", "r")

lines = f.readlines()

f.close()

output = open("checked_emails.csv", "w")
output.write(lines[0].replace('\n', '') + ", isValid\n")

del lines[0]

i = 0

for line in lines:
    broken = line.split(sep=',')
    email = broken[-1].replace('\n', '')

    i += 1
    if i % 100 == 0:
        print(str(i) + " emails processed")
        print("most recent email: " + email)

    is_valid = validate_email(email, verify=True)

    if is_valid:
        output.write(line.replace('\n', '') + ", Valid\n")
    else:
        output.write(line.replace('\n', '') + ", Invalid\n")

output.close()
