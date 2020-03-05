#metodo da soma entre dois numeros inteiros

#multiplique 3 numeros um deles é opcional
#na hora de testar, fazer com dois numeros e depois com 3

#metodo que some duas strings e retorne a string concatenada


def soma(n1,n2)-> int:
    return n1+n2

def mult(n1,n2,n3=1)-> int:
   n1=n1
   n2=n2
   n3=n3
   return n1*n2*n3

def soma_str(str1,str2)->str:
    str1=str1
    str2=str2
    return str1 + str2

#numero1=int(input('n1: '))
#numero2=int(input('n2: '))


#res = soma(numero1,numero2)
#print(res)

#produto=mult(numero1, numero2)
print(mult(2,4,2))

print(soma_str('deixa ', 'o like'))





