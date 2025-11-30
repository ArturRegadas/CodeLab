print('sequencia de fibonacci')

p =int(input('escreva a quantidade de termos que quer mostrar '))

x = 0
q=1
z=1
w=0
print(0, end=' ')
p1=p % 2

if p1 == 1:
    p=p//2
    po=p+1
    while x != p :
        x=x+1
        w=w+q
        print(q, end=' ')
        if x!=  p or x == p:
            print(w, end=' ')
        q = w+q


if p1 == 0:
    x = 0
    p=p/2
    while x != p :
        x = x + 1
        w = w + q
        print(q, end=' ')
        if x != p :
            print(w, end=' ')
        q = w + q
