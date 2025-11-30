#include <stdio.h>

int hanoiTower[5][3] = {{1, 0, 0}, {2, 0, 0}, {3, 0, 0}, {4, 0, 0}, {5, 0, 0}};

void swap(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

int winCheck()
{
    int ant = 0;
    for (int i = 0; i < 5; i++)
    {
        if (hanoiTower[i][2] <= ant)
        {
            return 0;
        }
        ant = hanoiTower[i][2];
    }
    return 1;
}

void printHanoi()
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", hanoiTower[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int validate(int init, int destiny)
{
    return !(init == destiny || init < 1 || init > 3 || destiny < 1 || destiny > 3 || hanoiTower[4][init - 1] == 0);
}

int getTop(int column)
{
    for (int i = 0; i < 5; i++)
    {
        if (hanoiTower[i][column] != 0)
            return i;
    }
    return 5;
}

int swapHanoi(int init, int destiny)
{
    init--;
    destiny--;
    int idxTopInit = getTop(init);
    int idxTopDestiny = getTop(destiny);
    if (hanoiTower[idxTopDestiny][destiny] != 0 && hanoiTower[idxTopInit][init] > hanoiTower[idxTopDestiny][destiny])
    {
        return 0;
    }
    if (idxTopDestiny == 5)
    {
        swap(&hanoiTower[idxTopInit][init], &hanoiTower[4][destiny]);
        return 1;
    }
    swap(&hanoiTower[idxTopInit][init], &hanoiTower[idxTopDestiny - 1][destiny]);
    return 1;
}

int main()
{
    int init, destiny;

    while (1)
    {
        printHanoi();
        printf("escolha seu movimento [inicio | destino](1|2|3): ");
        scanf("%d%d", &init, &destiny);

        if (validate(init, destiny))
        {

            if (swapHanoi(init, destiny))
            {
                printf("ok!\n");
            }
            else
            {
                printf("movimento invalido\n");
            }
            if (winCheck())
            {
                printHanoi();
                printf("voce ganhou!\n\n");
                break;
            }
        }
    }

    return 0;
}
