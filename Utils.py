def asc_to_txt(asc): # Returns types of characters
    if asc >= 65 and asc <= 90:
        return 'U'
    elif asc >= 48 and asc <= 57:
        return 'N'
    elif asc >= 97 and asc <= 122:
        return 'L'
    else:
        return 'S'

def extractor(lines):  # Takes list of lines as input
    pw = []
    for i in lines:
        pwd = i.replace('\n', '').split(',')[-1].lstrip()
        pw.append(pwd)
    return pw
