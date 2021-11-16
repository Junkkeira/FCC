'''
Victor Junqueira Colombaro
42123712
Turma 01N11
Profa. Fabiana A. Silvestre Matheus

5) Elabore um programa que calcule e apresente a soma dos inteiros existentes entre dois valores
lidos. Considere que o segundo número lido deve ser maior que o primeiro número lido.
'''
#Variáveis
som=0
x=0

#Input
a=int(input('insira um valor para A:'))
b=int(input('Insira um valor maior que A para B:'))

#Resolução das Respostas de acordo com as Condições
#Output
if b>a:
    for i in range(a+1,b,1):
        som=som+i
    print(som)
else:
    print('O segundo valor deve ser obrigatoriamente maior que o primeiro')
    a = int(input('insira um valor para A:'))
    b = int(input('Insira um valor maior que A para B:'))
    for i in range(a+1,b,1):
        som=som+i
    print(som)