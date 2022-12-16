a = open('Users-Pwds.txt', 'r').readlines()
usernames = []
passwords = []
usrpwds = {}
for i in a:
    base = i.replace('\n', '').split(',')
    usr = base[0]
    pwd = base[-1].lstrip()
    usernames.append(usr)
    passwords.append(pwd)

usrpwds |= {usernames[i]: passwords[i] for i in range(len(usernames))}
print(usrpwds)
for i in usrpwds:
    print(i)