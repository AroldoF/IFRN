### 1 - Processo, PID e processo-pai (PPID)

#### a) Qual é o PID do sleep e qual é o PPID (o processo que o criou)?

#### b) Rode também `echo $$`. O que esse número tem a ver com o PPID acima?

### 2 - A chamada fork() cria um novo processo 

#### a) A mensagem apareceu quantas vezes? Por quê, se o programa tem um só printf em cada ramo?

#### b) Qual valor o fork() devolveu ao pai e qual devolveu ao filho? (dica: o teste f == 0 ) 

### 3 - Estados de um processo

#### a) Qual o estado inicial do sleep e o que essa letra significa? 

#### b) Para que estado ele vai após o -STOP ? E depois do -CONT ?

### 4 - As regiões de memória de um processo

#### a) Escreva a faixa de endereços da linha marcada como [heap] e da linha [stack] . 

#### b) A linha do binário com permissão r-xp guarda o quê: dados, pilha ou código? Justifique pela permissão.

### 5 - Onde mora cada variável 

#### Associe cada item à sua região (escreva ao lado): DADOS, STACK (pilha) ou HEAP. 
- [ ] a variável global x 
- [ ] a variável local y 
- [ ] o ponteiro p em si  
- [ ] o valor 50 apontado por *p 

**Explique em uma frase por que p e *p ficam em regiões diferentes:**