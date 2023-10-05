from biblioteca import *
novamente="S"
while novamente=="S":
    print("=======================================")
    print("para somar dois números digite(1)")
    print("para subbtrair dois números digite(2)")
    print("para multiplicar dois números digite(3)")
    print("para dividir dois números digite(4)")
    print("=======================================")
    resposta=(input("resposta: "))
    while resposta!="1" and resposta!="2" and resposta!="3" and resposta!="4":
        resposta=(input("dado inválido, digite novamente:"))
    else:

        num1 = int(input("digite o primeiro algarismo: "))
        num2 = int(input("digite o segundo algarismo: "))
        print("=======================================")

        if resposta == "1":
            somar(num1, num2)
        elif resposta == "2":
            subtrair(num1, num2)
        elif resposta == "3":
            multiplicar(num1, num2)
        elif resposta == "4":
            dividir(num1, num2)
        else:
            print("invalido")
        novamente = input("deseja fazer novamente? S/N ")
else:
    print("tchau")










