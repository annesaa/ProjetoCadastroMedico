arq = open('Administrador.txt', 'a')
login_adm =input ("Administrador, Digite seu usuario\n")
arq.write('{}\n'.format(login_adm))
senha_adm =input ("Administrador, Digite sua senha\n")
arq.write('{}\n'.format(senha_adm))
print('Login realizado com sucesso!\n')

arq.close() #O arquivo é fechado do modo de adição para ser aberto
            #depois no modo de leitura

