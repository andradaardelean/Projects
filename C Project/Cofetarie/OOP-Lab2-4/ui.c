#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)

#include <stdio.h>
#include <string.h>
#include "vector_dinamic.h"
#include "ui.h"
#include "operatii.h"


void print_menu()
{
	printf("1 - Adauga materie prima.\n");
	printf("2 - Modificare materie prima.\n");
	printf("3 - Stergere materie prima.\n");
	printf("4 - Vizualizare materii prime care au cantitatea mai mica decat o cantitate data.\n");
	printf("5 - Vizualizare materii prime organizat dupa cantitatea disponibila.\n");
	printf("print - Afisare materii prime.\n");
	printf("exit - Iesire din program.\n");
}

void ui_adauga(Vector_dinamic* v)
{
	char nume[20], producator[20];
	int cantitate;

	printf("Introduceti numele materiei prime: ");
	scanf_s("%s", &nume, 20);

	printf("Introduceti numele producatorului: ");
	scanf_s("%s", &producator, 20);

	printf("Introduceti cantitatea materiei prime: ");
	scanf_s("%d", &cantitate);
	
	adauga(v, nume, producator, cantitate);
	printf("Materie prima adaugata cu succes!\n");
}

void ui_modifica(Vector_dinamic* v)
{
	char nume[20];

	printf("Introduceti numele materiei pe care doriti s-o modificati:");
	scanf_s("%s", &nume, 20);
	if (cautare_dupa_nume(v, nume) == -1)
		printf("Nu exista materie prima cu acest nume!\n");
	else {
		while (1)
		{
			printf("1 - Modifica producator.\n2 - Modifica cantitate.\n0 - Iesire.\n");
			char cmd[20];
			printf("Comanda dvs este:");
			scanf_s("%s", &cmd, 20);
			if (strcmp(cmd, "1") == 0)
			{
				char producator2[20];
				printf("Noul producator:");
				scanf_s("%s", &producator2, 20);
				modifica_producator_materie(v, nume, producator2);
				printf("Producator modificat cu succes!\n");
				break;
			}
			else if (strcmp(cmd, "2") == 0)
			{
				int cantitate;
				printf("Noua cantitate:");
				scanf_s("%d", &cantitate);
				modifica_cantitate_materie(v, nume, cantitate);
				printf("Cantitate modificata cu succes!\n");
				break;
			}
			else if (strcmp(cmd, "0"))
				break;
			else printf("Comanda gresita!\n");
		}
	}
}

void ui_sterge(Vector_dinamic* v)
{
	
	char nume[20];

	printf("Introduceti numele materiei prime: ");
	scanf_s("%s", &nume, 20);
	if (cautare_dupa_nume(v, nume) == -1)
		printf("Nu exista materie prima cu acest nume!\n");
	else 
	{
		stergere(v, nume);
		printf("Materia prima a fost stearsa cu succes!\n");
	}
}

void ui_filtrare(Vector_dinamic* v)
{
	int cmd = 0;
	char nume[20], producator[20];
	printf("Dupa ce criteriu doriti sa filtrati: \n1-dupa nume\n2-dupa cantitate\n");
	printf("Introduceti comanda:");
	scanf_s("%d", &cmd);
	if (cmd == 1)
	{
		char litera[20];
		printf("Introduceti litera dupa care doriti sa filtrati:");
		scanf_s("%s", &litera, 20);
		Vector_dinamic vFiltrat = filtrare_dupa_nume(v, litera);
		if (get_length(&vFiltrat) == 0)
			printf("Nu sunt materii care sa indeplineasca acest cristeriu!\n");
		else
		{
			for (int i = 0; i < get_length(&vFiltrat); i++)
			{
				Materie_prima m = get(&vFiltrat, i);
				strcpy(nume, get_nume(m));
				strcpy(producator, get_producator(m));
				int cantitate = get_cantitate(m);

				printf("Nume: %s\nProducator: %s\nCantitate %d\n", nume, producator, cantitate);
			}
			distruge(&vFiltrat);
		}
	}
	else if (cmd == 2)
	{
		int cant_filtr = 0;
		printf("Introduceti cantitatea dupa care doriti sa filtrati:");
		scanf_s("%d", &cant_filtr);
		Vector_dinamic vFiltrat = filtrare_dupa_cantitate(v, cant_filtr);
		if (get_length(&vFiltrat) == 0)
			printf("Nu sunt materii care sa indeplineasca acest cristeriu!\n");
		else
		{
			for (int i = 0; i < get_length(&vFiltrat); i++)
			{
				Materie_prima m = get(&vFiltrat, i);
				strcpy(nume, get_nume(m));
				strcpy(producator, get_producator(m));
				int cantitate = get_cantitate(m);

				printf("Nume: %s\nProducator: %s\nCantitate %d\n", nume, producator, cantitate);
			}
			distruge(&vFiltrat);
		}
	}
}

void ui_sortare(Vector_dinamic* v)
{
	char nume[20], producator[20];
	Vector_dinamic lista_sortata = sortareMaterii(v);
	printf("Cum doriti sa sortati: \n1-crescator \n2-descrescator \n");
	int cmd = 0;
	printf("Introduceti comanda:");
	scanf_s("%d", &cmd);
	if (cmd == 1)
	{
		for (int i = 0; i < get_length(&lista_sortata); i++)
		{
			Materie_prima m = get(&lista_sortata, i);
			strcpy(nume, get_nume(m));
			strcpy(producator, get_producator(m));
			int cantitate = get_cantitate(m);

			printf("Nume: %s\nProducator: %s\nCantitate %d\n", nume, producator, cantitate);
			distruge(&lista_sortata);
		}
	}
	else if (cmd == 2)
	{
		for (int i = get_length(&lista_sortata) - 1; i >= 0; i--)
		{
			Materie_prima m = get(&lista_sortata, i);
			strcpy(nume, get_nume(m));
			strcpy(producator, get_producator(m));
			int cantitate = get_cantitate(m);

			printf("Nume: %s\nProducator: %s\nCantitate %d\n", nume, producator, cantitate);
			distruge(&lista_sortata);
		}
	}
	else printf("Comanda indisponibila!");
}

void afisare(Vector_dinamic* v)
{
	char nume[20], producator[20];
	for (int i = 0; i < get_size(v); i++)
	{
		Materie_prima m = get(v, i);
		strcpy(nume, get_nume(m));
		strcpy(producator, get_producator(m));
		int cantitate = get_cantitate(m);
		
		printf("Nume: %s\nProducator: %s\nCantitate %d\n", nume, producator, cantitate);
	}
}

void testare()
{
	
	/*Se testeaza toate functionalitatile.
	*/
	
	test_creeaza();
	test_modificare_cantitate();
	test_modificare_producator();
	test_get_nume();
	test_get_producator();
	test_get_cantitate();
	test_valideaza_materie();
	test_producator_materie();
	
	
	test_creeaza_vector();
	test_distruge();
	test_redimensionare();
	test_get();

	test_get_capacity();
	test_get_length();
	
	test_modifica_lungime();
	test_modifica_lista();
	test_modifica_capacitate();
	test_modifica_cantitate_materie();
	test_equal();
	test_delete();

	test_sterge();
	/*Memory leaks*/
	test_adauga();
	test_get_total_materii();
	test_cautare_dupa_nume();
	/**/
	
	test_get_materie();
	test_filtrare_dupa_cantitate();
	test_filtrare_dupa_nume();
	test_sortare_dupa_cantitate();
	
	printf("Toate testele au trecut!\n");	
}

void run()
{
	char cmd[20] = "";
	testare();
	Vector_dinamic v = creeaza_vector_dinamic();
	int ok = 1;
	print_menu();
	while (ok == 1)
	{
		printf("Introduceti comanda: ");
		scanf_s("%s", &cmd, 20);
		if (!strcmp(cmd, "1"))
			ui_adauga(&v);
		else if (!strcmp(cmd, "2"))
			ui_modifica(&v);
		else if (!strcmp(cmd, "3"))
			ui_sterge(&v);
		else if (!strcmp(cmd, "4"))
			ui_filtrare(&v);
		else if (!strcmp(cmd, "5"))
			ui_sortare(&v);
		else if (!strcmp(cmd, "print"))
			afisare(&v);
		else if (!strcmp(cmd, "exit"))
			ok = 0;
		else printf("Comanda invalida!\n");
	}
	distruge(&v);
}