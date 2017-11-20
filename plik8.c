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

/*!Macierz przyleg³oœci, w indeksie (i,j) zawiera wartoœci:
0           dla i=j
nieskonczonosc      jeœli nie istnieje krawêdŸ (i,j)
K>0          waga krawêdzi (i,j)
*/
int     A[100][100];

/*!Wektor odleg³oœci od pierwszego wierzcho³ka do pozosta³ych,
Zostal wyliczony przez 
*/
int     D[100];

//!Liczba wierzcho³ków grafu
int n;

//!Stos, na którym odk³adane bêd¹ wierzcho³ki tworz¹ce drogê
stack <int, vector<int> > Stos;

//!Metoda wyznacza listê poprzednikow wierzcho³ka x
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

//Dodaj wierzcho³ek koñcowy na stos
Stos.push(x);
v=x;

//Konstruuj drogê a¿ dojdziesz do wierzcho³ka startowego
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
//!Wczytujemy liczbê wierzcho³ków grafu
fscanf(plik,"%d",&Graf.n);

//!Wczytujemy dane do macierzy przyleg³oœci
for (j=0;j<Graf.n;j++)
for (i=0;i<Graf.n;i++)
{
fscanf(plik,"%s",s);
if (strcmp(s,"*")!=0)
Graf.A[j][i]=atoi(s); else Graf.A[j][i]=nieskonczonosc;
}
//Wczytaj wektor odleg³osci, zosta³ on obliczony algorytmem Forda-Bellmana
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
