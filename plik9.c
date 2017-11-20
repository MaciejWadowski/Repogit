#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#define nieskonczonosc 100000

#define MIN(a,b) (a<b)?a:b

void main(void)
{
FILE *plik;
int     n; //liczba wierzcholkow
int     A[100][100];
int     D[100];
char    s[5];
int     i,j,k;
int N;


if ((plik=fopen("graf.txt","r"))==NULL)
printf("Brak pliku graf.txt!\n"); else
{
fscanf(plik,"%i",&n);
printf("Liczba wierzcholkow: %i\n",n);
for (j=0;j<n;j++)
for (i=0;i<n;i++)
{
fscanf(plik,"%s",s);
if (strcmp(s,"*")!=0)
A[j][i]=atoi(s); else A[j][i]=nieskonczonosc;
}
fclose(plik);

for (i=0;i<n;i++) D[i]=A[0][i];


for (k=1;k<=n-2;k++)
{
for (i=1;i<n;i++)
for (j=0;j<n;j++)
{
if (D[j]+A[j][i]>nieskonczonosc)
N=nieskonczonosc; else
N=D[j]+A[j][i];
D[i]=MIN(D[i],N);
}
}
k=nieskonczonosc;
for (i=0;i<n;i++)
if (D[i]<k)
printf("D(%i)=%i\n",i+1,D[i]);
else
printf("D(%i)=%s\n",i+1,"*");
}
}
