#include <stdio.h>

// Calcular o salário bruto
float calcular_salario_bruto(float valor_hora, int horas_trabalhadas) {
    return valor_hora * horas_trabalhadas;
}

// Calcular o desconto de 9%
float calcular_desconto(float salario_bruto) {
    return salario_bruto * 0.09; // 9% de desconto
}

// Calcular o salário líquido
float calcular_salario_liquido(float salario_bruto, float desconto) {
    return salario_bruto - desconto;
}

int main() {
    float valor_hora, salario_bruto, desconto, salario_liquido;
    int horas_trabalhadas;

    // Solicita o valor da hora de trabalho e a quantidade de horas trabalhadas
    printf("Digite o valor da hora de trabalho: R$ ");
    scanf("%f", &valor_hora);

    printf("Digite a quantidade de horas trabalhadas no mês: ");
    scanf("%d", &horas_trabalhadas);

    // Calcula o salário bruto
    salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas);

    // Calcula o desconto de 9%
    desconto = calcular_desconto(salario_bruto);

    // Calcula o salário líquido
    salario_liquido = calcular_salario_liquido(salario_bruto, desconto);

    // Exibe os resultados
    printf("\nSalário Bruto: R$ %.2f\n", salario_bruto);
    printf("Desconto (9%%): R$ %.2f\n", desconto);
    printf("Salário Líquido: R$ %.2f\n", salario_liquido);

    return 0;
}
