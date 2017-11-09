#include <stdio.h>
#include <conio.h>

int  flag, graficzny;
int  n,i,j,smin,s;
int  c[100];

int main()
{

printf("Podaj liczbe wierzcholkow grafu\n");
scanf("%d",&n);
for (i=0; i<n; i++)
{
printf("Podaj stopien wierzcholka %d\n",i+1);
scanf("%d",&c[i]);
}
//algorytm testowania czy podany ci¹g stopni wierzcholkow jest graficzny
graficzny=1;
//sprawdz czy suma ci¹gu jest liczb¹ parzyst¹
s=0;
for (i=0; i<n; i++) s+=c[i];
if ((s%2)!=0)
graficzny=0;
else
//posortuj ci¹g nierosn¹co je¿eli suma jest liczb¹ parzyst¹
{
flag=1;
while (flag==1)
{
flag=0;
for (i=0; i<n-1; i++)
if (c[i]<c[i+1])
{
s=c[i];
c[i]=c[i+1];
c[i+1]=s;
flag=1;
}
}
}
//sprawdz czy spelniona jest nierownosc P. Erdos, T. Gallai (1960)
j=0;
while ((graficzny==1) && (j<n-1))
{
s=0;
for (i=0; i<=j; i++) s+=c[i];
smin=0;
for (i=0; i<n; i++)
if ((j+1)<c[i]) smin=smin+(j+1);
else smin+=c[i];
if (s>(j*(j+1)+smin)) graficzny=0;
else j++;
}
//podaj u¿ytkownikowi wynik
if (graficzny==1) printf("Podany ci¹g jest graficzny\n");
else printf("Podany ci¹g nie jest graficzny\n");
getch();
}
