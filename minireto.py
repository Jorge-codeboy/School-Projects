def ui():
    decimal = 0
    posicion = 1
    potencia = 3
    booleanos = []

    while True:
        boolean = True
        if potencia < 0:
            break
        inputt = int(input((str(posicion) + "° bit mas significativo: ")))
        if inputt == 0:
            boolean = False
        booleanos.append(boolean)
        decimal = decimal + (inputt * (2**potencia))
        potencia = potencia - 1
        posicion = posicion + 1
    return decimal, booleanos

print ("---Inserte número en binario---")
decimal, booleanos = ui()
print ("El número decimal que corresponde al número binario insertado es:", decimal)
#print(booleanos)

s = 0
a = booleanos[3]
b = booleanos[2]
c = booleanos[1]
d = booleanos[0]

# strHor = Astr = Gstr = Dstr
# strDoble = (Fstr and Bstr) or (Estr and Cstr)
# strIzq = Fstr or Estr
# strDer = Bstr or Cstr

strHor = "******"
strDoble = '''*    *
*    *
*    *
*    *'''
strIzq = '''*
*
*
*'''
strDer = '''     *
     *
     *
     *'''
#A = D + B + A'C' + AC
if d or b or (not a and not c) or (a and c):
    print(strHor)

#F = D + A'B' + A'C + B'C
Fbool = d or (not a and not b) or (not a and c) or (not b and c)
#B = C' + A'B' + AB
Bbool = (not c) or (not a and not b) or (a and b)
if Fbool and Bbool:
    print(strDoble)
else:
    if Fbool:
      print(strIzq)
    else:
      print(strDer)
        
#G = D + A'C + BC' + B'C
if (d) or (not a and c) or (b and not c) or (not b and c):
  print(strHor)

#E = A'B + A'C'
Ebool = (not a and b) or (not a and not c)

#C = C + A + B'
Cbool = (c) or (a) or (not b)
if Ebool and Cbool:
  print(strDoble)
else:
    if Ebool:
      print(strIzq)
    else:
      print(strDer)

#D = D + A'B + A'C' + BC' + AB'C
if d or (not a and b) or (not a and not c) or (b and not c) or (a and not b and c):
  print(strHor)
print("---------------")
print("Coded by CodeJ")
