i = 15 
j = 22
print(""" Ce va afișa programul?
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
""")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print("""Ce va afișa programul?
print((2 ** 4), (2 * 4.), (2 * 4))
""")
print((2 ** 4), (2 * 4.), (2 * 4))

print("""
Ce va afișa programul?
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
 """)
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print("""
Ce va afișa programul?
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
 """)
print((2 % -4), (2 % 4), (2 ** 3 ** 2))


c = (3 ** 2 + 4 ** 2) ** 0.5

print(c)

print(""" 
Ce determină linia de program de mai jos?
c = (a ** 2 + b ** 2) ** 0.5
""")
def miletokm(a):
    return a*1.6
def kmtomile(a):
    return a/1.6

print(""" 
Ce va afișa programul?
var = 2 
var = 3 
print(var)
""")
var = 2 
var = 3 
print(var)


print("""
Ce va afișa programul?
a = '1' 
b = "1" 
print(a + b)
 """)
x =2
rel= 3*x**2-2*x**2+3*x-1;

print(""" """)
a = '1' 
b = "1" 
print(a + b)

print(""" 
a = 6
b = 3
a /= 2 * b
print(a)
""")
a = 6
b = 3
a /= 2 * b
print(a)


print("""
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
 """)
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

print("""
#cod care afișează poziția Like-ului median""")
test = "iiiLikePythonLikeILikeIcecream"
print(test.index('Like'))
print(test.rindex('Like'))


nr = 25
sir=str(bin(nr))
print(sir)
print(len(sir))
bitNumber = 3
rezultat = nr^(1<<bitNumber)
print(rezultat)
p=4
print('1' in str(bin(nr))[-p-1])
print(bool((nr>>p)&1))