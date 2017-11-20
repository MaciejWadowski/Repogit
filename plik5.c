#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
void selectionsort(int tablica[10], int ile_liczb)
{
int min,i,j,temp;
for (i=0;i<ile_liczb-1;i++)
{
min=i;
for (j=i+1;j<ile_liczb;j++)
if (tablica[j]<tablica[min]) min=j;
temp=tablica[min];
tablica[min]=tablica[i];
tablica[i]=temp;
}
printf("\nTablica po posortowaniu:");
for(i=0; i<ile_liczb; i++) printf("\n%i",tablica[i]);
}
void main(void)
{
int ile_liczb,i,liczba;
int tablica[10];

printf("Ile liczb chesz posortowac (do 10) ? ");
scanf("%i",&ile_liczb);
for(i=0; i<ile_liczb; i++)
{
printf("Wprowadz liczbe #%i: ",i+1);
scanf("%i",&liczba);
tablica[i]=liczba;
}
clrscr();
printf("Tablica przed posortowaniem:");
for(i=0; i<ile_liczb; i++) printf("\n%i",tablica[i]);
selectionsort(tablica,ile_liczb);
printf("\nDowolny klawisz.");
getch();
}
