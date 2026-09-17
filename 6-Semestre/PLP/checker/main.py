from lark import Lark

from checker import check_types


grammar = r"""
start: stmt+

stmt: "var" NAME ":" type "=" expr ";" -> var_decl
    | NAME "=" expr ";" -> assign
    | "if" "(" expr ")" block ("else" block)? -> if_stmt
    | "while" "(" expr ")" block -> while_stmt
    | "func" NAME "(" [params] ")" "->" type block -> func_decl
    | "return" expr ";" -> return_stmt
    | "print" expr ";" -> print_stmt

block: "{" stmt+ "}"

params: param ("," param)*
param: NAME ":" type

type: "int" -> t_int
    | "float" -> t_float
    | "bool" -> t_bool
    | "string" -> t_string

?expr: expr "or" expr1 -> or_
      | expr1

?expr1: expr1 "and" expr2 -> and_
       | expr2

?expr2: "not" expr2 -> not_
       | expr3

?expr3: expr3 ("=="|"<"|">") expr4 -> compare
       | expr4

?expr4: expr4 "+" expr5 -> add
      | expr4 "-" expr5 -> sub
      | expr5

?expr5: expr5 "*" atom -> mul
      | expr5 "/" atom -> div
      | atom

?atom: FLOAT -> float_lit
     | NUMBER -> int_lit
     | STRING -> string_lit
     | "true" -> true_lit
     | "false" -> false_lit
     | NAME "(" [args] ")" -> call
     | NAME -> var
     | "(" expr ")"

args: expr ("," expr)*

NAME: /[a-zA-Z_][a-zA-Z0-9_]*/

%import common.NUMBER
%import common.FLOAT
%import common.ESCAPED_STRING -> STRING
%import common.WS

%ignore WS
"""


parser = Lark(
    grammar,
    parser="lalr"
)


def testar(nome, codigo):
    print(nome)

    try:
        # 1. Parser
        arvore = parser.parse(codigo)

        print("Parser: OK")

        # 2. Checker
        escopo = {
            "__funcoes__": {}
        }

        check_types(arvore, escopo)

        print("Checker: ACEITOU")

    except Exception as e:
        print("Checker: REJEITOU")
        print(f"Erro: {e}")

    print()


# (a)

codigo_a = """
var ligado: int = 1;

if (ligado) {
    print "ligado";
}
"""


# (b)

codigo_b = """
var y: int = "dez";
"""


# (c)

codigo_c = """
func dobro(n: int) -> int {
    return n + n;
}

print dobro(3.5);
"""


# (d)

codigo_d = """
func eco(n: int) -> int {
    return eco(n);
}
"""


testar("(a) Condição do if", codigo_a)
testar("(b) Tipo da variável", codigo_b)
testar("(c) Tipo do argumento", codigo_c)
testar("(d) Função recursiva", codigo_d)