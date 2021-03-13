import re
import csv

file = open('kyrn.data', 'r',encoding='utf-8')
text = file.read()

binpattern=r"\nБИН.*(?P<BIN>\b[0-9]+)"
ndspattern=r"\nНДС.*(?P<NDS>\b[0-9]+)"
bintext=re.search(binpattern,text).group("BIN")
ndstext=re.search(ndspattern,text).group("NDS")

itemPatternText=r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern=re.compile(itemPatternText)
items=[["БИН","НДС","Наименование товара","Кол-во","Цена за единиц"]]
for m in re.finditer(itemPattern,text):
    items.append([bintext,ndstext,m.group("name").strip(),m.group("count").strip(),m.group("price").strip()])
with open('file.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(items)
file.close()