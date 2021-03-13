import re

file = open('kyrn.data', 'r',encoding='utf-8')
text = file.read()

itemPatternText=r"(?P<total1>,*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern=re.compile(itemPatternText)
for m in re.finditer(itemPattern,text):
    print(m.group("total1"))

file.close()