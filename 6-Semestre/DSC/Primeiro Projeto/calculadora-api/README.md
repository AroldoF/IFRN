🧮 API Calculadora Spring Boot

API REST desenvolvida em Spring Boot para realização de operações matemáticas básicas e análises numéricas via requisições HTTP.

---

## 🛠️ Tecnologias Utilizadas

* **Java 21** (ou 17)
* **Spring Boot 3**
* **Spring Web**
* **SpringDoc OpenAPI (Swagger UI)**

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/calculadora-api.git](https://github.com/SEU-USUARIO/calculadora-api.git)

    Acesse a pasta do projeto:
    Bash

    cd calculadora-api

    Execute a aplicação via Maven Wrapper:

        Linux/Mac: ./mvnw spring-boot:run

        Windows: .\mvnw.cmd spring-boot:run

    A aplicação estará rodando em: http://localhost:8080

📚 Documentação Interativa (Swagger)

Acesse a interface interativa do Swagger UI para testar as rotas diretamente no navegador:

    http://localhost:8080/swagger-ui.html

📌 Endpoints da API

Todas as rotas possuem o prefixo /calculadora.
1. Soma via @PathVariable

Soma dois números passados diretamente no caminho da URL.

    URL: GET /calculadora/somar/{numero1}/{numero2}

    Exemplo: GET /calculadora/somar/10/5

    Retorno: 15.0

2. Subtração via @RequestParam

Subtrai dois números informados através de parâmetros de busca (query parameters).

    URL: GET /calculadora/subtrair?numero1={valor}&numero2={valor}

    Exemplo: GET /calculadora/subtrair?numero1=20&numero2=8

    Retorno: 12.0

3. Cálculo Único

Realiza as operações de somar, subtrair, multiplicar e dividir. Aceita o parâmetro opcional casasDecimais (padrão: 2).

    URL: GET /calculadora/calcular/{operacao}?numero1={v1}&numero2={v2}&casasDecimais={opcional}

    Exemplo: GET /calculadora/calcular/dividir?numero1=10&numero2=3&casasDecimais=2

    Retorno Exemplo:
    Plaintext

    Operação: divisão
    Número 1: 10.0
    Número 2: 3.0
    Resultado: 3.33

    Tratamento de erro: Caso tente dividir por zero (numero2=0), o sistema retornará: Erro: não é possível dividir por zero..

4. Par ou Ímpar

Verifica se o número passado é PAR ou ÍMPAR.

    URL: GET /calculadora/par-ou-impar/{numero}

    Exemplo: GET /calculadora/par-ou-impar/7

    Retorno: ÍMPAR

5. Análise de Número

Informa diversos dados sobre o número (Par/Ímpar, Sinal, Dobro, Metade e Quadrado).

    URL: GET /calculadora/analisar/{numero}

    Exemplo: GET /calculadora/analisar/10

    Retorno Exemplo:
    Plaintext

    Número: 10.0
    Par ou ímpar: PAR
    Positivo, negativo ou zero: POSITIVO
    Dobro: 20.0
    Metade: 5.0
    Quadrado: 100.0

6. Desafio: Cálculo de Média

Recebe três notas por parâmetro e retorna a média com a situação do aluno (APROVADO, RECUPERAÇÃO ou REPROVADO).

    URL: GET /calculadora/media?nota1={n1}&nota2={n2}&nota3={n3}

    Exemplo: GET /calculadora/media?nota1=7&nota2=8&nota3=6

    Retorno Exemplo:
    Plaintext

    Média: 7.0
    Situação: APROVADO