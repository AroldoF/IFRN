package br.edu.ifrn.calculadora_api;

import org.springframework.web.bind.annotation.*;
import java.util.Locale;

@RestController
@RequestMapping("/calculadora")
public class CalculadoraController {

    // 1. Endpoint de soma com @PathVariable
    @GetMapping("/somar/{numero1}/{numero2}")
    public double somarPath(@PathVariable double numero1, @PathVariable double numero2) {
        return numero1 + numero2;
    }

    // 2. Endpoint de subtração com @RequestParam
    @GetMapping("/subtrair")
    public double subtrairQuery(@RequestParam double numero1, @RequestParam double numero2) {
        return numero1 - numero2;
    }

    // 3. Endpoint único de cálculo com parâmetro opcional
    @GetMapping("/calcular/{operacao}")
    public String calcular(
            @PathVariable String operacao,
            @RequestParam double numero1,
            @RequestParam double numero2,
            @RequestParam(defaultValue = "2") int casasDecimais) {

        if (operacao.equalsIgnoreCase("dividir") && numero2 == 0) {
            return "Erro: não é possível dividir por zero.";
        }

        double resultado;
        String nomeOperacao;
        switch (operacao.toLowerCase()) {
            case "somar": 
                resultado = numero1 + numero2; 
                nomeOperacao = "soma";
                break;
            case "subtrair": 
                resultado = numero1 - numero2; 
                nomeOperacao = "subtração";
                break;
            case "multiplicar": 
                resultado = numero1 * numero2; 
                nomeOperacao = "multiplicação";
                break;
            case "dividir": 
                resultado = numero1 / numero2; 
                nomeOperacao = "divisão";
                break;
            default: 
                return "Erro: Operação inválida.";
        }

        String formato = "%." + casasDecimais + "f";
        String resultadoFormatado = String.format(Locale.US, formato, resultado);

        return String.format(
            "Operação: %s%nNúmero 1: %s%nNúmero 2: %s%nResultado: %s",
            operacao, numero1, numero2, resultadoFormatado
        );
    }

    // 4. Par ou ímpar
    @GetMapping("/par-ou-impar/{numero}")
    public String parOuImpar(@PathVariable int numero) {
        return ((int) numero % 2 == 0) ? "PAR" : "ÍMPAR";
    }

    // 5. Análise de número
    @GetMapping("/analisar/{numero}")
    public String analisar(@PathVariable double numero) {
        String parImpar = (numero % 2 == 0) ? "PAR" : "ÍMPAR";
        String sinal = (numero > 0) ? "POSITIVO" : (numero < 0) ? "NEGATIVO" : "ZERO";

        return String.format(
            "Número: %s%nPar ou ímpar: %s%nPositivo, negativo ou zero: %s%nDobro: %s%nMetade: %s%nQuadrado: %s",
            numero, parImpar, sinal, (numero * 2), (numero / 2), (numero * numero)
        );
    }

    // Desafio adicional: cálculo de média
    @GetMapping("/media")
    public String calcularMedia(
            @RequestParam double nota1,
            @RequestParam double nota2,
            @RequestParam double nota3) {

        double media = (nota1 + nota2 + nota3) / 3.0;
        String situacao;

        if (media >= 7.0) {
            situacao = "APROVADO";
        } else if (media >= 4.0) {
            situacao = "RECUPERAÇÃO";
        } else {
            situacao = "REPROVADO";
        }

        return String.format("Média: %.1f%nSituação: %s", media, situacao);
    }
}