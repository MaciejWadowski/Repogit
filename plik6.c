#include<iostream>
using namespace std;

void sort(int *tab, int rozmiar)
{
int abc=rozmiar-1;
int temp;
bool zamiana;
while (true) // petla nieskonczona - wyjscie breakem
{
zamiana=false;
for (int i=0;i<abc;i++) // sprawdzamy tablice od poczatku
{
if (tab[i]>tab[i+1]) // jezeli poprzedni element jest wiekszy to zamien
{
zamiana=true; // sygnalizujemy zmiane
temp=tab[i];
tab[i]=tab[i+1];
tab[i+1]=temp;
}
}
if (!zamiana)
break;
}
}
int main()
{
int rozmiar;
cin>>rozmiar; // wczytaj rozmiar tablicy
int *tab=new int[rozmiar]; // utwórz dynamicznie tablicê

for (int i=0;i<rozmiar;i++) // wczytaj liczby do tablicy
cin>>tab[i];

sort (tab,rozmiar); // posortuj tablicê

for (int i=0;i<rozmiar;i++) // wyswietl tablice
cout<<tab[i]<<" ";

return 0; // zakoncz
}
