#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#include <stack>
#include <vector>


#define nieskonczonosc 1000

using namespace std;


class   cGraf{

public:

/*!Macierz przyległości, w indeksie (i,j) zawiera wartości:
0           dla i=j
nieskonczonosc      jeśli nie istnieje krawędź (i,j)
K>0          waga krawędzi (i,j)
*/
int     A[100][100];

/*!Wektor odległości od pierwszego wierzchołka do pozostałych,
Zostal wyliczony przez 
*/
int     D[100];

//!Liczba wierzchołków grafu
int n;

//!Stos, na którym odkładane będą wierzchołki tworzące drogę
stack <int, vector<int> > Stos;

//!Metoda wyznacza listę poprzednikow wierzchołka x
vector<int> Poprzedniki(int x){
vector<int> wynik;

for (int i=0;i<n;i++)
if ((A[i][x]!=nieskonczonosc)&&(A[i][x]!=0))
wynik.push_back(i);

return(wynik);
}


//Metoda konstruuje droge miedzy wierzcholkiem 1 i x o dlugosci D[x]
void KonstruujDroge(int x){
int u,v,i;
//!Lista poprzedników
vector<int>           poprzedniki;

//Dodaj wierzchołek końcowy na stos
Stos.push(x);
v=x;

//Konstruuj drogę aż dojdziesz do wierzchołka startowego
while (v!=0){
poprzedniki=Poprzedniki(v);

for (i=0;i<poprzedniki.size();i++)
if (D[v]==D[poprzedniki[i]]+A[poprzedniki[i]][v])
u=poprzedniki[i];

Stos.push(u);
v=u;
}

/*Wypisujac wierzcholki dodaj 1, bo numerujemy je od jeden
a w macierzy od 0 */

printf("Droga od wierzcholka 1 do %d: ",x+1);
while (Stos.empty()!=true){
printf("%d ",Stos.top()+1);
Stos.pop();
}
printf("\n");
return;
}

};


void main(void)
{
FILE                *plik;
char                s[5];
int                 i,j;
cGraf               Graf;

//--------------------------------------------

if ((plik=fopen("graf.txt","r"))==NULL)
printf("Brak pliku graf.txt!\n"); else
{
//!Wczytujemy liczbę wierzchołków grafu
fscanf(plik,"%d",&Graf.n);

//!Wczytujemy dane do macierzy przyległości
for (j=0;j<Graf.n;j++)
for (i=0;i<Graf.n;i++)
{
fscanf(plik,"%s",s);
if (strcmp(s,"*")!=0)
Graf.A[j][i]=atoi(s); else Graf.A[j][i]=nieskonczonosc;
}
//Wczytaj wektor odległosci, został on obliczony algorytmem Forda-Bellmana
for (i=0;i<Graf.n;i++){
fscanf(plik,"%s",s);
Graf.D[i]=atoi(s);
}

fclose(plik);

//Wyznacz drogi od wierzcholka 1 do pozostalych (w macierzy numerujemy je od 0)
for (i=1;i<Graf.n;i++)
Graf.KonstruujDroge(i);
}

printf("\nDowolny klawisz...\n");
getch();
return;
}
