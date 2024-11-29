#include <stdio.h>

int main() {
    int numero, soma = 0;

    // O loop acontece enquanto o número for diferente de zero
    while (1) {
        // Solicita um número inteiro
        printf("Digite um número inteiro maior que 0 ou 0 para encerrar: ");
        scanf("%d", &numero);

        // Verificação do número inserido, se for igual a 0, encerra o loop
        if (numero == 0) {
            break;  // Encerra o loop
        }

        // Adiciona o número à soma
        soma += numero;
    }

    // Exibe o resultado final da soma
    printf("A soma dos números inseridos é: %d\n", soma);

    return 0;
}
