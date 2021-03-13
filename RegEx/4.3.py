import re
import csv
l=open("khan.data","r",encoding="utf-8")
text=l.read()
namepattern=r"\nname.*(?P<NAME>\b[0-9]+)"
univerpattern=r"\nuniversity.*(?P<univer>.*"
x=re.search(namepattern,text).group("NAME")
