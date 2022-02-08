op =str (input (" Selecione M para Medico, P para paciente, G para gestor de consultas, ADM para administrador \n") )

if op=="M" or op=="P" or op=="G" or op=="ADM":
        
    op=="ADM"
    arq = open('Administrador.txt') #Arquivo aberto
    login_adm = input ("Entre com seu usuario de administrador\n") 
    senha_adm =input ("Administrador, Digite sua senha\n")
    Administrador = arq.readlines()
    if login_adm +"\n" in Administrador:
        if senha_adm +"\n" in Administrador:
            print('Bem vindo, {}!'.format(login_adm))
        else:
            print('Você deve ter digitado seu nome de usuario ou senha incorreta, por favor verifique.')
    arq.close()#O arquivo é fechado do modo de adição para ser aberto
            #depois no modo de leitura
    opcao =str (input (" Se deseja cadastrar medico digite med, se deseja cadastrar paciente digite pac, se deseja cadastrar gestor digite gest \n") )

    if opcao=="med":
        arq = open('medicos.txt', 'a')#Arquivo aberto
        novo_medico =input ("Deseja cadastrar novo Medico? ")
        while  novo_medico == "sim":#laço para saber se o usuario adm quer
                            #cadastrar mais medicos
    
            nome_medico = input('Digite o nome do médico: ')
            arq.write('{}\n'.format(nome_medico))

            senha_medico = input('Digite a senha do médico: ')
            arq.write('{}\n'.format(senha_medico))
    
            crm_medico = input('Digite o CRM do médico: ')
            arq.write('{}\n'.format(crm_medico))

            esp_medico = input('Digite a especialidade do médico: ')
            arq.write('{}\n'.format(esp_medico))

            novo_medico =input ("Deseja cadastrar novo Medico? ")

            print('Cadastro realizado com sucesso!\n')

        arq.close() #O arquivo é fechado do modo de adição para ser aberto
            #depois no modo de leitura

        if opcao=="pac":
                arq = open('Pacientes.txt', 'a')#Arquivo aberto
                novo_pac =input ("Deseja cadastrar novo Paciente? ")
                while  novo_pac == "sim":#laço para saber se o usuario adm quer
                            #cadastrar mais pacientes
    
                    nome_pac = input('Digite o nome do paciente: ')
                    arq.write('{}\n'.format(nome_pac))

                    senha_pac = input('Digite a senha do paciente: ')
                    arq.write('{}\n'.format(senha_pac))

                    cpf_pac = input('Digite o CPF do paciente: ')
                    arq.write('{}\n'.format(cpf_pac))

                    novo_pac =input ("Deseja cadastrar novo paciente? ")
                 
                print('Cadastro realizado com sucesso!\n')

                arq.close() #O arquivo é fechado do modo de adição para ser aberto
                #depois no modo de leitura

        if opcao=="gest":
            arq = open('Gestores.txt', 'a')#Arquivo aberto
            novo_gest =input ("Deseja cadastrar novo Gestor? ")
            while  novo_gest == "sim":#laço para saber se o usuario adm quer
                            #cadastrar mais Gestores
    
                nome_gest = input('Digite o nome do Gestor: ')
                arq.write('{}\n'.format(nome_gest))

                senha_gest = input('Digite a senha do Gestor: ')
                arq.write('{}\n'.format(senha_gest))

                cpf_gest = input('Digite o CPF do Gestor: ')
                arq.write('{}\n'.format(cpf_gest))

                novo_gest =input ("Deseja cadastrar novo Gestor? ")

            print('Cadastro realizado com sucesso!\n')
    
            arq.close() #O arquivo é fechado do modo de adição para ser aberto
            #depois no modo de leitura
    else:
        print('Opção inválida!\n')

else:
    print('Você digitou uma opção incorreta.')



    
