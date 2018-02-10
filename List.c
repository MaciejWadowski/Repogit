/* Maciej Wadowski Temat Nr 4  A-2-b-S */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX 35
#define TRUE 1
#define FALSE 0
#define SAME 2


typedef struct tagListElement{
	struct tagListElement *next;
	char *word;
	int krotnosc;
}ListElement;

typedef struct tagList{
	int size;
	ListElement *head;
}List;

void init(List *list);
void add(List *list, char word[]);
void addPosition(List *list, char word[]);
void printList(List *list, int a);
void deleteFront(List *list);
void freeList(List *list);
int isSameString(char word1[],char word2[]);

int main(void)
{
	FILE *fp;
	List list[26];
	char line[MAX];
	char new_line[MAX];
	int listCharacter;
	int i, j;
	char *blank = "";
	if ((fp = fopen("tekst.txt","r")) == NULL)
	{
		printf("Nie moglem otworzyc pliku\n");
		exit(-1);
	}
	
	for ( i = 0; i<26; i++)
	{
		init(&list[i]);
	}
	
	while(fscanf(fp,"%s",line) != EOF)
	{
		i = 0;
		j = 0;
	
		if (line[i] >= 'A' && line[i] <='Z' )
			listCharacter = line[i] - 'A';
		else if (line[i] >= 'a' && line[i] <= 'z')
			listCharacter = line[i] - 'a';
		i++;
		while(line[i] != '\0')
		{
			if( line[i] >= 'A' && line [i] <='Z')
			{
				line[i] = line[i] + 32;
			 	new_line[j] = line[i];
				j++;
			}
			else if( line[i] >='a' && line[i] <='z')
			{
				new_line[j] = line[i];
				j++;
			}
			else if(line[i] == '-')
			{
				new_line[j] = line[i];
				j++;
			}
			i++;
		}
		new_line[j] = '\0'; 
		if (strlen(new_line) != 0)
			addPosition(&list[listCharacter],new_line);
		else if ( strlen(line) == 1)
			addPosition(&list[listCharacter],blank);
	}
	

	for ( i = 0; i<26; i++)	
		printList(&list[i],i);
	
	for ( i = 0; i<26; i++)
		freeList(&list[i]);

	return 0;
}

void init(List *list)
{
	list->head = 0;
	list->size = 0;
}

void add(List *list, char word[])
{
	ListElement *element = (ListElement*)malloc(sizeof(ListElement));
	element->word = (char*)malloc(sizeof(char)*(strlen(word)+1));
	element->next = list->head;
	strcpy(element->word,word);
	element->krotnosc = 1;
	list->head = element;
	list->size++;
}

void addPosition(List *list, char word [])
{
	int Flag = FALSE;
	ListElement *i, *p;
	int j;
	if (list->size == 0)
	{
		add(list,word);
		return;
	}
	else if(list->head->word[0] >= word[0])
		Flag = isSameString(list->head->word, word);
	if(Flag == TRUE)
		add(list,word);
	else
	{
		for (i = list->head, j = 1; j < list->size; i = i->next, j++)
		{
			if (i->next->word[0] >= word[0])
				Flag = isSameString(i->next->word, word);

			if (Flag == TRUE)
			{
				ListElement *element = (ListElement*)malloc(sizeof(ListElement));
				element->word = (char*)malloc(sizeof(char)*(strlen(word)+1));
				strcpy(element->word, word);
				element->krotnosc = 1;
				p = i->next;
				i->next = element;
				element->next = p;
				list->size++;
				break;
			}
			else if(Flag == SAME)
			{
				i->next->krotnosc++;
				break;
			}
					
		}
	}

	if (Flag == FALSE)
	{
		ListElement *element = (ListElement*)malloc(sizeof(ListElement));
		element->word = (char*)malloc(sizeof(char)*(strlen(word)+1));
		strcpy(element->word, word);
		element->krotnosc = 1;
		i->next = element;
		list->size++;
	}
}

int isSameString(char word1[],char  word2[])
{
	int i = 0;

	while (word1[i]!= '\0' && word2[i] != '\0')
	{
		if (word1[i] > word2[i])
			return TRUE;
		else if (word2[i] > word1[i])
			return FALSE;
		i++;
	}

	int length1 = strlen(word1);
	int length2 = strlen(word2);
	if (length1 < length2)
		return FALSE;
	else if(length1 > length2)
		return TRUE;
	else if(length1 == length2)
		return SAME;
}

void printList(List *list, int a)
{
	a = a + 'a';
	ListElement *i;
	int k = list->size;
	int j;
	for(i = list->head, j = 0 ; j < k ; i = i->next, j++)
		printf("%c%s  %d\n",a,i->word, i->krotnosc);

}	

void freeList(List *list)
{
	while(list->size != 0)
		deleteFront(list);
}

void deleteFront(List *list)
{
	ListElement *toDelete;
	if (list->size == 0)
	{
		return;
	}
	toDelete = list->head;
	list->head = list->head->next;
	free(toDelete);
	list->size--;
}

