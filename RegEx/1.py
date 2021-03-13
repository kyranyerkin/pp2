import re
file=open("kyrn.data","r",encoding='utf-8')
text=file.read()
pattern=r"\nБИН.*(?P<BIN>\b[0-9]+).*\nНДС.*(?P<NDS>\b[0-9]+)"
x=re.compile(pattern)
print(x)
print(x.finditer(text))
for m in x.finditer(text):
    print(m.group("BIN"))
    print(m.group("NDS"))