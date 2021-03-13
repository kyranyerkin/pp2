import re
import csv
file= open("kyrn.data","r",encoding='utf-8')
text=file.read()

binpattern=r"\nБИН.*(?P<BIN>\b[0-9]+)"
ndspattern=r"\nНДС.*(?P<NDS>\b[0-9]+)"

bintext=re.search(binpattern,text).group("BIN")
ndspattern=re.search(ndspattern,text).group("NDS")

itemPatternText=r"\n{1}Стоимость\n{1}(?P<total2>.*)"
itenPattern=re.compile(itemPatternText)
items=[["БИН","НДС","Наименование товара","Колөво","Цена за единиц"]]
#for m in re.finditer(itemPattern,text):
