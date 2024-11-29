#include <stdio.h>

int main() {
    // Declaração de um vetor para armazenar 5 valores inteiros
    int vendas[5];
    int soma = 0;
    
    // Solicita os valores das vendas
    printf("Digite as vendas realizadas em 5 dias:\n");
    for (int i = 0; i < 5; i++) {
        printf("Dia %d: ", i + 1);
        scanf("%d", &vendas[i]);
        soma += vendas[i]; // Soma os valores inseridos no vetor
    }
    
    // Exibe os valores e a soma total
    printf("\nVendas por dia:\n");
    for (int i = 0; i < 5; i++) {
        printf("Dia %d: %d vendas\n", i + 1, vendas[i]);
    }
    
    printf("\nSoma total de vendas: %d\n", soma);
    
    return 0;
}
