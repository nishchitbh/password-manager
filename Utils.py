def asc_to_txt(asc):  # Returns types of characters
    if asc >= 65 and asc <= 90:
        return 'U'
    elif asc >= 48 and asc <= 57:
        return 'N'
    elif asc >= 97 and asc <= 122:
        return 'L'
    else:
        return 'S'


def extractor(lines):  # Takes list of lines as input
    usernames = []
    passwords = []
    usrpwds = {}
    for i in lines:
        base = i.replace('\n', '').split(',')
        usr = base[0]
        pwd = base[-1].lstrip()
        usernames.append(usr)
        passwords.append(pwd)

    usrpwds |= {usernames[i]: passwords[i] for i in range(len(usernames))}
    return usrpwds


upper = [a for a in range(65, 91)]
lower = [a for a in range(97, 123)]
numbers = [a for a in range(48, 58)]
