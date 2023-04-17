def a(d):
    d[4]='d'
    return d

x={
    1:'a',
    2:'b',
    3:'c'

}

y=a(x)
print(y)