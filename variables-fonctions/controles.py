# if elif else
x = 2
if x > 0 :
    print(x, 'positif')
elif x == 0 :
    print(x, 'nul')
else :
    print(x, 'negatif')

y = 2
if (x>0) & (y>=x) :
    print(x, y, 'positif')
    
    
# boucle for de 3 à 10 par pas de 2
for i in range(3, 10, 2) : 
    print(i)

# boucle for de 10 à -10 par pas de -2
for i in range(10, -10, -2) : 
    print(i)
    
# boucle while
x = 6
while x<10 :
    print(x)
    x += 1
    
# print la suite de fibonacci jusqu'à la valeur de n
def fibonacci(n):
    a = 0
    b = 1
    while a < n:
        print(a)
        a, b = b, a+b
        
fibonacci(1000)