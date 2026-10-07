#a = input()
#name = input("Zadejte svoje jméno: ")
#print(name)

#N = int(input("Zadej nějaké celé číslo: "))
#print(10*N)

#name = input('Zadejte jmeno: ')
#print('Letošního programovacího bootcampu se účastní ' +  name)

#a = float(input('Zadejte rozmer ctverce: '))
#v = a * 4
#s = a ** 2
#print(f'Obvod je {v}')
#print(f'Obsah je {s}')

#a = float(input('Zadejte stranu a: '))
#b = float(input('Zadejte stranu b: '))
#v = 2 * (a + b)
#s = a * b
#print('Obvod je: ' + str(v))
#print(f'Obsah je {s}')

#import math
#r = float(input('zadejte polomer kruhu: '))
#s = r*r*math.pi # v zadani je p = 3.14 ale takhle presnejsi
#v = 2*r*math.pi
#print(f'Obsah je {s}' )
#print(f'Obvod je {v}' )

#import math
#r = float(input('zadejte polomer koule: '))
#s = (r**2)*math.pi*4
#v = (4/3)*(r**3)*math.pi
#print(f'Povrch je {s}' )
#print(f'Objem je {v}' )

#a = float(input('Zadejte cislo: '))
#b = float(input('Zadejte druhe cislo: '))
#ab = a + b
#ba = a - b
#abc = a * b
#print(f'Soucet je {ab}')
#print(f'Rozdil je {ba}')
#print(f'Soucin je {abc}') #jde to udelat i taktok print('a+b= ', a+b) a nemusim psat s ab = a+b a pak print

#a = int(input('Zadejte cislo: '))
#b = int(input('Zadejte druhe cislo: '))
#print('Prvni cislo:' ,a + b - a)
#print('Druhe cislo:' ,b + a - b) #podtimto je druhy pristup k tomu tohle reseni jde u cislech protoze pouzivame - a + ale u slov to nepujde proto pouzijeme druhou metodu

#a = int(input('Zadejte cislo: '))
#b = int(input('Zadejte druhe cislo: '))
#c = a
#a = b
#b = c
#print("a = ", a)
#print("b = ", b)

#a = int(input("Zadejte cele cislo: "))
#x = 0
#if a > 5:
 #   print("Podminka je splnena.")
  #  print("Zadane cislo je vetsi nez 5.")
   # x = 1
#print("Konec programu, x je:")
#print(x)

#a = int(input("Zadejte cislo: "))
#x = 0
#if a > 5:
#    print("Podminka je splnena.")
#    print("Zadane cislo je vetsi nez 5.")
#    x = 1
#else:
#    print("Podminka neni splnena.")
#    print("Zadane cislo neni vetsi nez 5.")
#    x = -1
#print("Konec programu, x je:")
#print(x)

#a = int(input("Zadejte cislo: "))
#x = 0
#if a > 5:
#    print("Prvni podminka je splnena.")
#    print("Zadane cislo je vetsi nez 5.")
#    x = 1
#elif a < 5:
#    print("Druha podminka je splnena.")
#    print("Zadane cislo je mensi nez 5.")
#    x = -1
#else:
#    print("Zadna podminka neni splnena.")
#    print("Zadane cislo je 5.")
#    x = 0
#print("Konec programu, x je:")
#print(x)

#a = int(input('Napis prvni cislo: '))
#b = int(input('Napis druhe cislo: '))
#if a == b:
#    print('Stejna hodnota')
#else:
#    print('Jina hodnota')

#a = int(input('Napis zaklad: '))
#b = int(input('Napis exponent: '))
#print(a**b)

#a = int(input('Napis prvni cislo: '))
#b = int(input('Napis druhe cislo: '))
#if a > b:
#    print(a)
#elif a < b:
#    print(b)
#else:
#    print('Zadana cisla jsou stejna.')

#a = float(input('Napis cislo: '))
#if a < 20 and a > 10:
#    print('je v intervalu')
#elif a == 20:
#    print('je vyssi interval')
#elif a == 10:
#    print('je mensi interval')
#else:
#    print('Mimo interval')

#a = int(input('Napis cislo: '))
#if a%2 == 0:
#    print('sude')
#else:
#    print('liche')

#a = int(input('Prvni strana: '))
#b = int(input('Druha strana: '))
#c = int(input('Treti strana: '))
#s = (a+b+c)/2
#S = (s*(s-a)*(s-b)*(s-c))**(1/2)
#print(f'Obsah trojuhelniku: {S}')

#import math
#d = float(input('Prumer sudu: '))
#v = float(input('Vyska sudu: '))
#V = ((math.pi * (d/2)**2 * v)*1000)
#print(f'Objem sudu v litrech je: {V}')
#l = float(input('Mnozstvi vody: '))
#a = V - l
#if a > 0:
#    print('Vejde se')
#    print(f'Voda je ve vysce: {v * (l/V)} metru')
#elif a < 0:
#    print('Nevejde se')
#else:
#    print('Plno')

#import math
#a = float(input('Prvni strana: '))
#b = float(input('Druha strana: '))
#c = float(input('Treti strana: '))
#if a <= 0 or b <= 0 or c <= 0:
#    print('Kladne hodnoty vlozte')
#elif (a+b>c) and (a+c>b) and (b+c>a):
#    print('Lze sestavit')
#    if (a**2)+(b**2)==(c**2) or (a**2)==(b**2)+(c**2) or (a**2)+(c**2)==(b**2):
#        print('Pravouhly')
#    elif (a**2)+(b**2)<(c**2) or (a**2)>(b**2)+(c**2) or (a**2)+(c**2)<(b**2):
#        print('Tupouhly')
#    else:
#        print('Ostrouhly')
#else:
#    print('Nelze sestavit')

#import math
#a = float(input('Prvni cislo: '))
#b = float(input('Druhe cislo: '))
#c = float(input('Treti cislo: '))
#d = b**2 - 4*a*c
#if d < 0:
#    print('Nema reseni')
#elif d == 0:
#    print(-b / 2 * a)
#else:
#   print((-b + math.sqrt(d)) / 2 * a)
#   print((-b - math.sqrt(d)) / 2 * a)

#import math
#x1 = float(input('Prvni souradnice x: '))
#y1 = float(input('Druha souradnice y: '))
#x2 = float(input('Prvni souradnice x: '))
#y2 = float(input('Druha souradnice y: '))
#if((x2-x1) == 0):
#    print('Lezi v nekonecnu')
#else:
#    c = (y2 - y1) / (x2 - x1)  
#    d = math.degrees(math.atan(c))
#    print(d)

# x1 = int(input('Prvni souradnice x: '))
# y1 = int(input('Druha souradnice y: '))
# x2 = int(input('Prvni souradnice x: '))
# y2 = int(input('Druha souradnice y: '))
# x3 = int(input('Prvni souradnice x: '))
# y3 = int(input('Druha souradnice y: '))
# x4 = x2 - x1
# y4 = y2 - y1
# a = -x4
# b = y4
# c = -a*x1 - b*y1
# if(a*x3 + b*y3 + c == 0):
#    print('Lezi na primce')
# else:
#    print('Nelezi na primce')