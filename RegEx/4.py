import re

file = open('kyrn.data', 'r',encoding='utf-8')
text = file.read()
"""
binpattern=r"\nБИН.*(?P<BIN>\b[0-9]+)"
ndspattern=r"\nНДС.*(?P<NDS>\b[0-9]+)"
bintext=re.search(binpattern,text).group("BIN")
ndstext=re.search(ndspattern,text).group("NDS")
"""
itemPatternText=r"(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemText=re.search(itemPatternText,text).group("total1")

print(itemText)
file.close()
