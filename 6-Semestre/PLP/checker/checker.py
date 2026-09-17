from lark import Tree


def get_type(t):
    match t.data:
        case "t_int":
            return "int"

        case "t_float":
            return "float"

        case "t_bool":
            return "bool"

        case "t_string":
            return "string"

        case _:
            raise TypeError(f"Tipo desconhecido: {t.data}")


def check_types(t: Tree, escopo: dict):
    match t.data:

        # Programa

        case "start":
            for stmt in t.children:
                check_types(stmt, escopo)

        # Literais

        case "int_lit":
            return "int"

        case "float_lit":
            return "float"

        case "string_lit":
            return "string"

        case "true_lit" | "false_lit":
            return "bool"

        # Variável

        case "var":
            nome = str(t.children[0])

            if nome not in escopo:
                raise TypeError(
                    f"Variável '{nome}' não declarada"
                )

            return escopo[nome]

        # Declaração

        case "var_decl":
            nome = str(t.children[0])

            tipo_declarado = get_type(t.children[1])

            tipo_expressao = check_types(
                t.children[2],
                escopo
            )

            if tipo_declarado != tipo_expressao:
                raise TypeError(
                    f"Tipo esperado: '{tipo_declarado}', "
                    f"encontrado: '{tipo_expressao}'"
                )

            escopo[nome] = tipo_declarado

            return tipo_declarado

        # Atribuição

        case "assign":
            nome = str(t.children[0])

            if nome not in escopo:
                raise TypeError(
                    f"Variável '{nome}' não declarada"
                )

            tipo_variavel = escopo[nome]

            tipo_expressao = check_types(
                t.children[1],
                escopo
            )

            if tipo_variavel != tipo_expressao:
                raise TypeError(
                    f"Tipo esperado: '{tipo_variavel}', "
                    f"encontrado: '{tipo_expressao}'"
                )

            return tipo_variavel

        # Aritmética

        case "add":
            tipo_esquerda = check_types(
                t.children[0],
                escopo
            )

            tipo_direita = check_types(
                t.children[1],
                escopo
            )

            # int + int
            if (
                tipo_esquerda == "int"
                and tipo_direita == "int"
            ):
                return "int"

            # float + float
            if (
                tipo_esquerda == "float"
                and tipo_direita == "float"
            ):
                return "float"

            # int + float
            if (
                tipo_esquerda == "int"
                and tipo_direita == "float"
            ):
                return "float"

            # string + string
            if (
                tipo_esquerda == "string"
                and tipo_direita == "string"
            ):
                return "string"

            raise TypeError(
                f"Tipos incompatíveis para '+': "
                f"'{tipo_esquerda}' e '{tipo_direita}'"
            )

        case "sub" | "mul" | "div":
            tipo_esquerda = check_types(
                t.children[0],
                escopo
            )

            tipo_direita = check_types(
                t.children[1],
                escopo
            )

            # int op int
            if (
                tipo_esquerda == "int"
                and tipo_direita == "int"
            ):
                return "int"

            # float op float
            if (
                tipo_esquerda == "float"
                and tipo_direita == "float"
            ):
                return "float"

            # int op float
            if (
                tipo_esquerda == "int"
                and tipo_direita == "float"
            ):
                return "float"

            raise TypeError(
                f"Tipos incompatíveis para '{t.data}': "
                f"'{tipo_esquerda}' e '{tipo_direita}'"
            )

        # Comparação

        case "compare":
            tipo_esquerda = check_types(
                t.children[0],
                escopo
            )

            tipo_direita = check_types(
                t.children[1],
                escopo
            )

            # int == int, int < int, int > int
            if (
                tipo_esquerda == "int"
                and tipo_direita == "int"
            ):
                return "bool"

            # float == float, float < float, float > float
            if (
                tipo_esquerda == "float"
                and tipo_direita == "float"
            ):
                return "bool"

            # int < float, int > float, int == float
            if (
                tipo_esquerda == "int"
                and tipo_direita == "float"
            ):
                return "bool"

            raise TypeError(
                f"Tipos incompatíveis na comparação: "
                f"'{tipo_esquerda}' e '{tipo_direita}'"
            )

        # AND

        case "and_":
            tipo_esquerda = check_types(
                t.children[0],
                escopo
            )

            tipo_direita = check_types(
                t.children[1],
                escopo
            )

            if tipo_esquerda != "bool":
                raise TypeError(
                    f"Tipo esperado: 'bool', "
                    f"encontrado: '{tipo_esquerda}'"
                )

            if tipo_direita != "bool":
                raise TypeError(
                    f"Tipo esperado: 'bool', "
                    f"encontrado: '{tipo_direita}'"
                )

            return "bool"

        # OR

        case "or_":
            tipo_esquerda = check_types(
                t.children[0],
                escopo
            )

            tipo_direita = check_types(
                t.children[1],
                escopo
            )

            if tipo_esquerda != "bool":
                raise TypeError(
                    f"Tipo esperado: 'bool', "
                    f"encontrado: '{tipo_esquerda}'"
                )

            if tipo_direita != "bool":
                raise TypeError(
                    f"Tipo esperado: 'bool', "
                    f"encontrado: '{tipo_direita}'"
                )

            return "bool"

        # NOT

        case "not_":
            tipo = check_types(
                t.children[0],
                escopo
            )

            if tipo != "bool":
                raise TypeError(
                    f"Tipo esperado: 'bool', "
                    f"encontrado: '{tipo}'"
                )

            return "bool"

        # IF

        case "if_stmt":
            tipo_condicao = check_types(
                t.children[0],
                escopo
            )

            if tipo_condicao not in ("bool", "int", "float"):
                raise TypeError(
                    f"Tipo esperado: 'bool' ou 'int' ou 'float', "
                    f"encontrado: '{tipo_condicao}'"
                )

            check_types(
                t.children[1],
                escopo.copy()
            )

            if len(t.children) > 2:
                check_types(
                    t.children[2],
                    escopo.copy()
                )

        # WHILE

        case "while_stmt":
            tipo_condicao = check_types(
                t.children[0],
                escopo
            )

            if tipo_condicao != "bool":
                raise TypeError(
                    f"Tipo esperado: 'bool', "
                    f"encontrado: '{tipo_condicao}'"
                )

            check_types(
                t.children[1],
                escopo.copy()
            )

        # Bloco

        case "block":
            for stmt in t.children:
                check_types(stmt, escopo)

        # Print

        case "print_stmt":
            check_types(
                t.children[0],
                escopo
            )

        # Função

        case "func_decl":
            nome = str(t.children[0])

            indice = 1
            parametros = []

            if (
                isinstance(t.children[indice], Tree)
                and t.children[indice].data == "params"
            ):
                params = t.children[indice]

                for param in params.children:
                    param_nome = str(param.children[0])
                    param_tipo = get_type(param.children[1])

                    parametros.append(
                        (param_nome, param_tipo)
                    )

                indice += 1

            tipo_retorno = get_type(t.children[indice])
            indice += 1

            bloco = t.children[indice]

            if "__funcoes__" not in escopo:
                escopo["__funcoes__"] = {}

            escopo["__funcoes__"][nome] = {
                "params": parametros,
                "return": tipo_retorno
            }

            escopo_funcao = escopo.copy()

            for param_nome, param_tipo in parametros:
                escopo_funcao[param_nome] = param_tipo

            escopo_funcao["__return_type__"] = tipo_retorno

            check_types(
                bloco,
                escopo_funcao
            )

        # Return

        case "return_stmt":
            if "__return_type__" not in escopo:
                raise TypeError(
                    "Return usado fora de uma função"
                )

            tipo_esperado = escopo["__return_type__"]

            tipo_encontrado = check_types(
                t.children[0],
                escopo
            )

            if tipo_esperado != tipo_encontrado:
                raise TypeError(
                    f"Tipo esperado: '{tipo_esperado}', "
                    f"encontrado: '{tipo_encontrado}'"
                )

            return tipo_encontrado

        # Chamada de função

        case "call":
            nome = str(t.children[0])

            if "__funcoes__" not in escopo:
                raise TypeError(
                    f"Função '{nome}' não declarada"
                )

            funcoes = escopo["__funcoes__"]

            if nome not in funcoes:
                raise TypeError(
                    f"Função '{nome}' não declarada"
                )

            funcao = funcoes[nome]

            parametros = funcao["params"]

            argumentos = []

            if len(t.children) > 1:
                args = t.children[1]

                for argumento in args.children:
                    argumentos.append(
                        check_types(
                            argumento,
                            escopo
                        )
                    )

            if len(argumentos) != len(parametros):
                raise TypeError(
                    f"Quantidade de argumentos esperada: "
                    f"{len(parametros)}, "
                    f"encontrada: {len(argumentos)}"
                )

            for (_, tipo_parametro), tipo_argumento in zip(
                parametros,
                argumentos
            ):
                if tipo_parametro != tipo_argumento:
                    raise TypeError(
                        f"Tipo esperado: '{tipo_parametro}', "
                        f"encontrado: '{tipo_argumento}'"
                    )

            return funcao["return"]

        case _:
            raise NotImplementedError(t.data)