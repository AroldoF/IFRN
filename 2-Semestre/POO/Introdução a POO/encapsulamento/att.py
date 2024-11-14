from random import randint
from os import system

class Livro:
    def __init__(self,titulo,autor,ano_de_publicacao,isbn):
        self.titulo=titulo
        self.autor=autor
        self.ano_de_publicacao=ano_de_publicacao
        self.__isbn=isbn
        self.__disponivel=True
    def get_isbn(self):
        return self.__isbn
    def set_isbn(self,novo_isbn):
        if novo_isbn.len()==13:
            self.__isbn=novo_isbn
        else:
            print("O ISBN e inválido!")
    def get_disponivel(self):
        return self.__disponivel
    def emprestar(self):
        if self.__disponivel==True: 
            self.__disponivel=False
        else:
            print("O livro esta Indisponivel para Emprestimo")
    def devolver(self):
        if self.__disponivel==False:
            self.__disponivel=True
        else:
            print("Você não pegou o livro emprestado!")
    def exibir_informacoes(self):
        print("Informações sobre o livro:")
        print(f"O nome {self.titulo}!")
        print(f"O autor é {self.autor}!")
        print(f"O ano de publicação é {self.ano_de_publicacao}!")
        if self.__disponivel == True:
            print(f"Livro Disponivel")
        else:
            print("livro Indisponivel")
        print()

class Autor:
    def __init__(self,nome,data_nacimento,nacionalidade):
        self.nome=nome
        self.__data_nacimento=data_nacimento
        self.nacionalidade=nacionalidade
    def get_data_nascimento(self):
        return self.__data_nacimento
    def set_data_nascimento(self, nova_data):
        self.__data_nacimento=nova_data
    def exibir_informacoes(self):
        print("Informações sobre o autor:")
        print(f"O nome {self.nome}!")
        print(f"O ano de nacimento é {self.__data_nacimento}!")
        print(f"A sua nacionalidade é {self.nacionalidade}!\n")

class Usuario:
    def __init__(self,nome,endereco,telefone,id_usuario):
        self.nome=nome
        self.endereco=endereco
        self.telefone=telefone
        self.__id_usuario=id_usuario
        self.__livros_emprestados=list()
    def get_id_usuario(self):
        return self.__id_usuario 
    def get_livros_emprestados(self):
        for j,i in enumerate(self.__livros_emprestados):
            print(f'{j} | {i.titulo}')
    def emprestar_livro(self, livro):
        if livro.get_disponivel():
            self.__livros_emprestados.append(livro)  
        livro.emprestar()

    def devolver_livro(self, livro):
        livro.devolver()
        self.__livros_emprestados.remove(livro)

    def exibir_informacoes(self): 
        print("Informações sobre o Usuário:")
        print(f"O nome {self.nome}!")
        print(f"O endereço é {self.endereco}!")
        print(f"O telefone é {self.telefone}!")
        print(f"A lista de livros de {self.nome}:")
        for i in self.__livros_emprestados:
            print(f"    {i.titulo}")
        print()
Biblioteca=list()
autores=list()
usuarios=list()
us=Usuario('robert','rua flavio andrade','84 99999-9999','22245')
usuarios.append(us)
ar=Autor('guidan','12/08/2005','Brasileiro')
autores.append(ar)
livro1=Livro('Percy Jackson','JK','2004','125125135412')
Biblioteca.append(livro1)
while True:
    print("Digite 0 para finalizar o código")
    print("Digite 1 para adicionar um livro")
    print("Digite 2 para adicionar um autor")
    print("Digite 3 para criar um usuário")
    print("Digite 4 para acessar os menus")
    saida=int(input("Sua Ação: "))
    system('cls')
    match saida:
        case 0:
           break
        case 1:
            titulo=input('Digite o titulo: ')
            autor=input("Digite o autor: ")
            ano_de_publicacao=int(input("Digite o ano de publicação: "))
            isbn=randint(0,100)
            livro=Livro(titulo,autor,ano_de_publicacao,isbn)
            Biblioteca.append(livro)
        case 2:
            nome=input("Digite o nome: ")
            data_nacimento=input("Digite a data de nascimento: ")
            nacionalidade=input("Digite a nacionalidade: ")
            autor=Autor(nome,data_nacimento,nacionalidade)
            autores.append(autor)
        case 3:
            nome=input("Digite o nome: ")
            endereco=input("Digite endereço: ")
            telefone=input("Digite o telefone: ")
            id_usuario=randint(0,100)
            usuario=Usuario(nome,endereco,telefone,id_usuario)
            usuarios.append(usuario)
        case 4:
            system('cls')
            while True:
                print("Digite 0 para voltar\nDigite 1 para menu de Usuário:\nDigite 2 para menu do autor")
                print('Digite 3 para o menu de livros')
                esc=int(input("Digite sua escolha: "))
                match esc:
                    case 0:
                        break
                    case 1:
                        for j,i in enumerate(usuarios):
                            print(f'{j} | {i.nome}')
                        esc=int(input("Digite sua escolha de usuário: "))
                        system('cls')
                        while True:
                            print('Digite 0 para voltar\nDigite 1 Emprestar\nDigite 2 Devolver\nDigite 3 Informações')
                            s=int(input("Sua Ação: "))
                            system('cls')
                            match s:
                                case 0:
                                    break
                                case 1:
                                    for j,i in enumerate(Biblioteca):
                                        if not i.get_disponivel():
                                            print(f'{j} | {i.titulo} | Indisponivel!')
                                        else:
                                            print(f'{j} | {i.titulo}')
                                    r=int(input("Digite o nome do livro: "))
                                    usuarios[esc].emprestar_livro(Biblioteca[r])
                                case 2:
                                    usuarios[esc].get_livros_emprestados()
                                    r=int(input("Digite o nome do livro: "))
                                    usuarios[esc].devolver_livro(Biblioteca[r])
                                case 3:
                                    usuarios[esc].exibir_informacoes()   
                    case 2:
                        for j,i in enumerate(autores):
                            print(f'{j} | {i.nome}')
                        esc=int(input("Digite sua escolha de autor: "))
                        system('cls')
                        while True:
                            print("Digite 0 para voltar\nDigite 1 para ver informações")
                            s=int(input("Sua Ação: "))
                            system('cls')
                            match s:
                                case 0:
                                    break 
                                case 1:
                                    autores[esc].exibir_informacoes()
                    case 3:
                        for j,i in enumerate(Biblioteca):
                            print(f'{j} | {i.titulo}')
                        esc=int(input("Digite sua escolha de livro: "))
                        system('cls')
                        while True:
                            print("Digite 0 para voltar\nDigite 1 para ver informações")
                            s=int(input("Sua Ação: "))
                            system('cls')
                            match s:
                                case 0:
                                    break 
                                case 1:
                                    Biblioteca[esc].exibir_informacoes()
            system('cls')
        case _:
            print("Erro\n") 
