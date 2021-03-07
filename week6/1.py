a=int(input())
b=int(input())
c=int(input())
def two( x, y ):
    if x > y:
        return x
    return y
def three( x, y, z ):
    return two( x, two( y, z ) )
print(three(a,b,c))