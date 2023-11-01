a = 229485948752935839659869863969683386
b = 121847864857736598135698536598356895

c = a + b

print(type(a))
print(f'a={a}')
print(f'b={b}')
#print(type(c))
print(f'c={c}')

af = 2294859487529358396598.69863969683386
bf = 12184786485.7736598135698536598356895

cf = af + bf

print(type(af))
print(f'af={af}')
print(f'bf={bf}')
#print(type(cf))
print(f'cf={cf}')

g = 1e+2
print(g)
cfi=int(cf*1e+20)
print(f'cfi={cfi}')
h=1.8e+308
print(f'h={h}')

afs = '22948594875.2935839659869863969683386'
bfs = '12184786485.7736598135698536598356895'
print(type(afs))
cfs=afs+bfs
print(f'cfs={cfs}')

cfs=float(afs)+float(bfs)
print(type(cfs))
print(f'cfs={cfs}')

j=int(6853.3214)
print(j)
k=round(54333.7890)
print(k)

ab = 0b1001
print(ab)

ax = 0xa
print(ax)
ax1= 0x10
print(ax1)
ax2= 0x1f
print(ax2)

s = 'abcdefgh'
print(s)
print(ord('a'))
print(ord('A'))
print('avsavsab\nafaggw\\ra\\negwg2wghq')
s1 = print('avsavsab\tafaggw\ta\\tegwg2wghq')
print(s1)
print(s1[2])
print(s1[2:])
print(s1[:5])
print(s1[-5:])
print('--------------',end='')
print('aagae')
s2 = 'avsavsab\tagfaggw\ta\ttnegwg2wghq'
s2a = s2.split('\t')
print(s2a)
print(s2a[1])

p = True
q = False

if p and q:
    print('p and q True')
else:
    print('p and q False')

    if p or q:
        print('p or q True')
    else:
        print('p or q False')