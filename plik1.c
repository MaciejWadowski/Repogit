#include <stdio.h>ssssssssss
#include <conio.h>
#include <math.h>


void main(void)
{
int i,j,zakres,dokad;
int tablica[10000];
printf("Podaj gorny zakres, do ktorego chcesz odnalezc liczby pierwsze\n");
scanf("%d",&zakres);
dokad=floor(sqrt(zakres));
//inicjuj tablice
for (i=1; i<=zakres; i++) tablica[i]=1;
//algorytm - sito eratostenesa
for (i=2; i<=dokad; i++)
{

{
j = i+i;
while (j<=zakres)
{
tablica[j] = 0;
j += i;
}
}
}
//wypisz wynik
printf("Liczby pierwsze z zakresu od 1 do %d\n\n",zakres);
for (i=2; i<=zakres; i++) if (tablica[i]!=0) printf("%d, ",i);
getch();
}
