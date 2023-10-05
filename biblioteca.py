def somar(num1, num2):
    resp=num1+num2
    print(resp)

def somar(num1, num2, num3):
    resp=num1+num2+num3
    print(resp)
def subtrair(num1, num2):
    resp=num1-num2
    print(resp)

def multiplicar(num1, num2):
    resp=num1*num2
    print(resp)

def dividir(num1, num2):
    resp=num1/num2
    print(resp)

def abaixo(num):
    for x in range(1, num+1):
        print(x*str(x))

def totalvogais(texto):
    contador=0
    for x in texto:
        if x in "aeiouAEIOU":
            contador+=1
    print(f"o total de vogais é: {contador}")

def estoque(produto, quantidade, valor):
    vtotal= quantidade*valor
    return


