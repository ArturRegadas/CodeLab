#include <stdio.h>
#include <string.h>



typedef struct {
    char nome[50];
    char endereco[100];
    int idade;
    char telefone[10];
} Pessoa;

void cadastrar(Pessoa agenda[]) {
    for (int i = 0; i < 5; i++) {
        printf("Cadastro %d:\n", i + 1);
        printf("Nome: ");
        scanf(" %s", agenda[i].nome);
        printf("Endereco: ");
        scanf(" %s", agenda[i].endereco);
        printf("Idade: ");
        scanf("%d", &agenda[i].idade);
        printf("Telefone: ");
        scanf(" %s", agenda[i].telefone);
    }
}

void pesquisarPorIdade(Pessoa agenda[]) {
    int idade;
    printf("Digite a idade para pesquisa: ");
    scanf("%d", &idade);
    for (int i = 0; i < 5; i++) {
        if (agenda[i].idade == idade) {
            printf("Nome: %s, Endereco: %s, Telefone: %s\n", agenda[i].nome, agenda[i].endereco, agenda[i].telefone);
        }
    }
}

void ordenarPorNome(Pessoa agenda[]) {
    Pessoa temp;
    for (int i = 0; i < 5 - 1; i++) {
        for (int j = i + 1; j < 5; j++) {
            if (strcmp(agenda[i].nome, agenda[j].nome) > 0) {
                temp = agenda[i];
                agenda[i] = agenda[j];
                agenda[j] = temp;
            }
        }
    }
    printf("Agenda ordenada por nome:\n");
    for (int i = 0; i < 5; i++) {
        printf("Nome: %s, Endereco: %s, Idade: %d, Telefone: %s\n", agenda[i].nome, agenda[i].endereco, agenda[i].idade, agenda[i].telefone);
    }
}

void alterarRegistro(Pessoa agenda[]) {
    char nome[50];
    printf("Digite o nome da pessoa para alterar o registro: ");
    scanf(" %s", nome);
    for (int i = 0; i < 5; i++) {
        if (strcmp(agenda[i].nome, nome) == 0) {
            printf("Novo Nome: ");
            scanf(" %s", agenda[i].nome);
            printf("Novo Endereco: ");
            scanf(" %s", agenda[i].endereco);
            printf("Nova Idade: ");
            scanf("%d", &agenda[i].idade);
            printf("Novo Telefone: ");
            scanf(" %s", agenda[i].telefone);
            return;
        }
    }
    printf("error.\n");
}

int main() {
    Pessoa agenda[5];
    int opcao;

    do {
        printf("Menu da Agenda:\n");
        printf("1- Cadastro\n");
        printf("2- Pesquisa de registro por idade\n");
        printf("3- Classificacao alfabetica\n");
        printf("4- Alteracao de registro digitado com erro\n");
        printf("5- Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                cadastrar(agenda);
                break;
            case 2:
                pesquisarPorIdade(agenda);
                break;
            case 3:
                ordenarPorNome(agenda);
                break;
            case 4:
                alterarRegistro(agenda);
                break;
            case 5:
                printf("Saindo...\n");
                break;
            default:
                printf("Opcao invalida.\n");
        }
    } while (opcao != 5);

    return 0;
}