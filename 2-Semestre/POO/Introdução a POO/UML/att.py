from datetime import *
from random import randint
class Blog:
    def __init__(self):
        self.postagem=[]
        self.usuarios=[]
    def adicionarPostagem(self,postagem):
        postagem.titulo=input("Digite o título: ")
        postagem.texto=input("Digite o texto: ")
        r=input("Deseja publicar a postagem? [S/N] ")
        if r[0] in 'Ss':
            self.publicarPostagem(postagem)
        else:
            print('Blz')
        self.postagem.append(postagem)
    def publicarPostagem(self,postagem):
        postagem.data_publicacao=datetime.now()
        
class Postagem():
    def __init__(self,titulo,texto):
        self.id=1111
        self.titulo=titulo
        self.texto=texto
        self.data_publicacao=None
class Usuario():
    def __init__(self,nome,login,senha):
        self.id=2222
        self.nome=nome
        self.login=login
        self.senha=senha

blog=Blog()
user=Usuario('Jose','jose@gmail.com','ashe22')
blog.usuarios.append(user)
user=Usuario('Rose','rose@gmail.com','camaroamarelo15')
blog.usuarios.append(user)
post=Postagem('Vida boa','aaaaaa')
blog.postagem.append(post)
post=Postagem('Vida ruim','bbbbbb')
blog.postagem.append(post)
blog.publicarPostagem(post)
while True:
    saida=int(input("Digite uma ação: "))
    match saida:
        case 0:
            break
        case 1:
            nome=input('Nome: ')
            login=input('Login: ')
            senha=input('Senha: ')
            user=Usuario(nome,login,senha)
            blog.usuarios.append(user)
        case 2:
            while True:
                saida=int(input("Digite uma ação: "))
                match saida:
                    case 0:
                        break
                    case 1:
                        post=Postagem('','')
                        blog.adicionarPostagem(post)
                    case 2:
                        r=0
                        print("Publicações não publicadas:")
                        for i,post in enumerate(blog.postagem):
                            if post.data_publicacao == None:
                                print(f'{r} | \033[31m{post.titulo}\033[m')
                                r+=1
                        k=int(input("Digite o post que deseja postar: "))
                        j=0
                        for i,post in enumerate(blog.postagem):
                            if post.data_publicacao == None:
                                j+=1
                                if j==r:
                                    blog.publicarPostagem(blog.postagem[i])
        case 3:
           for i,post in enumerate(blog.postagem):
                if post.data_publicacao == None:
                    print(f'{i} | \033[31m{post.titulo}\033[m')
                else:
                    print(f'{i} | \033[32m{post.titulo}\033[m')