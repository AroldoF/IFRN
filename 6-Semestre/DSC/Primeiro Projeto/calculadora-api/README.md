# 🧮 API Calculadora Spring Boot

API REST desenvolvida com Spring Boot para realizar operações matemáticas básicas e análises numéricas por meio de requisições HTTP.

---

## 🛠️ Tecnologias Utilizadas

* **Java 21** (ou Java 17)
* **Spring Boot 3**
* **Spring Web**
* **SpringDoc OpenAPI (Swagger UI)**

---

## 🚀 Como Baixar e Rodar o Projeto

### 1. Baixe o projeto pelo GitHub

Acesse o repositório no GitHub e faça o download do projeto:

1. Clique no botão **Code**
2. Selecione **Download ZIP**
3. Extraia o arquivo baixado
4. Acesse a pasta `calculadora-api`

### 2. Acesse a pasta do projeto

Abra um terminal dentro da pasta:

```bash
cd calculadora-api
```

### 3. Execute a aplicação

#### Linux / macOS

```bash
./mvnw spring-boot:run
```

#### Windows

```bash
.\mvnw.cmd spring-boot:run
```

A aplicação estará disponível em:

```text
http://localhost:8080
```


---

## 📚 Documentação Interativa

A API possui documentação interativa utilizando Swagger UI.

Acesse:

```text
http://localhost:8080/swagger-ui.html
```

---

# 📌 Endpoints da API

Todas as rotas possuem o prefixo:

```text
/calculadora
```

---

## 1. ➕ Soma via `@PathVariable`

Soma dois números passados diretamente no caminho da URL.

### URL

```text
GET /calculadora/somar/{numero1}/{numero2}
```

### Exemplo

```text
GET /calculadora/somar/10/5
```

### Retorno

```text
15.0
```

---

## 2. ➖ Subtração via `@RequestParam`

Subtrai dois números informados através de parâmetros de consulta.

### URL

```text
GET /calculadora/subtrair?numero1={valor}&numero2={valor}
```

### Exemplo

```text
GET /calculadora/subtrair?numero1=20&numero2=8
```

### Retorno

```text
12.0
```

---

## 3. 🧮 Cálculo Único

Realiza operações de:

* Soma
* Subtração
* Multiplicação
* Divisão

Aceita o parâmetro opcional `casasDecimais`, cujo valor padrão é `2`.

### URL

```text
GET /calculadora/calcular/{operacao}?numero1={v1}&numero2={v2}&casasDecimais={opcional}
```

### Operações disponíveis

```text
somar
subtrair
multiplicar
dividir
```

### Exemplo

```text
GET /calculadora/calcular/dividir?numero1=10&numero2=3&casasDecimais=2
```

### Retorno

```text
Operação: divisão
Número 1: 10.0
Número 2: 3.0
Resultado: 3.33
```

### Tratamento de erro

Caso seja realizada uma divisão por zero:

```text
GET /calculadora/calcular/dividir?numero1=10&numero2=0
```

O sistema retornará:

```text
Erro: não é possível dividir por zero.
```

---

## 4. 🔢 Par ou Ímpar

Verifica se o número informado é **PAR** ou **ÍMPAR**.

### URL

```text
GET /calculadora/par-ou-impar/{numero}
```

### Exemplo

```text
GET /calculadora/par-ou-impar/7
```

### Retorno

```text
ÍMPAR
```

---

## 5. 📊 Análise de Número

Realiza uma análise do número informado, retornando:

* Par ou ímpar
* Positivo, negativo ou zero
* Dobro
* Metade
* Quadrado

### URL

```text
GET /calculadora/analisar/{numero}
```

### Exemplo

```text
GET /calculadora/analisar/10
```

### Retorno

```text
Número: 10.0
Par ou ímpar: PAR
Positivo, negativo ou zero: POSITIVO
Dobro: 20.0
Metade: 5.0
Quadrado: 100.0
```

---

## 6. 🎓 Desafio: Cálculo de Média

Recebe três notas através de parâmetros e calcula a média do aluno.

A situação é definida da seguinte forma:

| Média                | Situação    |
| -------------------- | ----------- |
| Maior ou igual a 7.0 | APROVADO    |
| Entre 4.0 e 6.9      | RECUPERAÇÃO |
| Menor que 4.0        | REPROVADO   |

### URL

```text
GET /calculadora/media?nota1={n1}&nota2={n2}&nota3={n3}
```

### Exemplo

```text
GET /calculadora/media?nota1=7&nota2=8&nota3=6
```

### Retorno

```text
Média: 7.0
Situação: APROVADO
```

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
