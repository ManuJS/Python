print ("-----Calculadora Python-----")


num1 = float(input("informe um numero: "))
num2 = float(input ("informe outro numero "))
print ("escolha uma operação")
print ("1 - soma")
print ("2 - subtração")
print ("3 - multiplicação")
print ("4 - divisão")


funcao = int(input("escolha uma das opções de calculo: "))

if funcao == 1:
	soma = num1 + num2
	print (soma)
elif funcao == 2:
	sub = num1 - num2
	print (sub)
elif funcao ==3:
	mult = num1 * num2
	print (mult)
elif funcao == 4:
	divis = num1 / num2
	print (divis)

else:
	print ("opção invalida")

