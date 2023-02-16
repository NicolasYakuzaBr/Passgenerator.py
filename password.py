#------------------------------------------------------------------| Simple python code to generate random passwords----------------|Written in Brazilian Portuguese------|
import random                                                      

print('Gerador de senhas em Python')

print(input('Pressione: ENTER (↵), para gerar a sua senha :)'))

letra_min = 'abcdefghijklmnopqrstuvwxyz'
letra_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numero = '0123456789'
simbolo = '.+-[]*~_@#:?'

usar = letra_min + letra_mai + numero + simbolo
taman_senha = 10

password = "".join(random.sample(usar, taman_senha))
print('Senha gerada com sucesso!')
print('Sua senha é: ', password)
#-------------------------------------------------------------------| I do not recommend it for use, only for studies----------------|I accept any criticism or opinion that makes me progress :)---|

#--------------| Thanks for reading and using <3
