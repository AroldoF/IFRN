class Date:
    def __init__(self, data_str):
        # Exemplo de formato esperado: "dd/mm/aaaa"
        dia, mes, ano = map(int, data_str.split("/"))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"


class Pessoa:
    def __init__(self, nome, sexo, data_nasc):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nasc = Date(data_nasc)

    def __str__(self):
        return f"{self.__nome}, {self.__sexo}, {self.__data_nasc}"


class Aluno(Pessoa):
    def __init__(self, nome, sexo, data_nasc, matric):
        super().__init__(nome, sexo, data_nasc)
        self.__matric = matric

    def __str__(self):
        return f"Aluno: {super().__str__()}, Matrícula: {self.__matric}"


class Contrato:
    def __init__(self, inicio, fim, salario):
        self.__inicio = Date(inicio)
        self.__fim = Date(fim)
        self.__salario = salario

    def __str__(self):
        return (
            f"Contrato: {self.__inicio} a {self.__fim}, Salário: {self.__salario:.2f}"
        )


class Ator(Pessoa):
    def __init__(self, nome, sexo, data_nasc, contrato):
        super().__init__(nome, sexo, data_nasc)
        self.__contrato = contrato

    def __str__(self):
        return f"Ator: {super().__str__()}, {self.__contrato}"


class Personagem(Ator):
    def __init__(self, nome, sexo, data_nasc, contrato, caracterizacao, novela):
        super().__init__(nome, sexo, data_nasc, contrato)
        self.__caracterizacao = caracterizacao
        self.__novela = novela

    def __str__(self):
        return (
            f"Personagem: {super().__str__()}, Caracterização: {self.__caracterizacao}, "
            f"Novela: {self.__novela}"
        )


contrato = Contrato("1/1/2023", "31/12/2023", 50000)
ator = Ator("João", "Masculino", "15/05/1985", contrato)
personagem = Personagem(
    "Maria", "Feminino", "22/07/1990", contrato, "Vampira", "Vampiros do Além"
)

print(contrato, "\n")
print(ator, "\n")
print(personagem, "\n")
