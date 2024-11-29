#include <stdio.h>

int main() {
    int num1, num2, num3;
    
    // Solicitar três números inteiros
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);
    printf("Digite o segundo número: ");
    scanf("%d", &num2);
    printf("Digite o terceiro número: ");
    scanf("%d", &num3);

    // 1. Calcular soma, subtração, multiplicação e divisão
    int soma = num1 + num2 + num3;
    int subtracao = num1 - num2 - num3;
    int multiplicacao = num1 * num2 * num3;
    float divisao = (float)num1 / num2 / num3;

    printf("\nResultados das operações:\n");
    printf("Soma: %d\n", soma);
    printf("Subtração: %d\n", subtracao);
    printf("Multiplicação: %d\n", multiplicacao);
    printf("Divisão: %.2f\n", divisao);

    // 2. Verificar condições
    if (num1 > num2) {
        printf("\nO primeiro número (%d) é maior que o segundo (%d).\n", num1, num2);
    } else {
        printf("\nO primeiro número (%d) não é maior que o segundo (%d).\n", num1, num2);
    }

    if (num2 < num3) {
        printf("O segundo número (%d) é menor que o terceiro (%d).\n", num2, num3);
    } else {
        printf("O segundo número (%d) não é menor que o terceiro (%d).\n", num2, num3);
    }

    // 3. Verificar condições
    if (num1 > 0 && num2 % 2 == 0) {
        printf("\nO primeiro número é positivo e o segundo número é par.\n");
    } else {
        printf("\nCondição lógica não atendida: ou o primeiro número não é positivo, ou o segundo número não é par.\n");
    }

    return 0;
}
