with open( 'input.txt' ) as fin :
    text = fin.read()
print(len(set(text.split())))

