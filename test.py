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

a = float(input('Napis cislo: '))
if a < 20 and a > 10:
    print('je v intervalu')
elif a == 20:
    print('je vyssi interval')
elif a == 10:
    print('je mensi interval')
else:
    print('Mimo interval')