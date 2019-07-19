import pyperclip

def Is_Email(text):
    for i in text:
        if i == '@':
            return True
    return False

spisak = pyperclip.paste()
spisak = spisak.split()

novi_spisak = ""

for i in spisak:
    if Is_Email(i):
        novi_spisak += i + ", "

novi_spisak = novi_spisak[0:-2]
pyperclip.copy(novi_spisak)
input()
