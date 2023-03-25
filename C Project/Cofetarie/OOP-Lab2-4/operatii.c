#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include "materie_prima.h"
#include "vector_dinamic.h"
#include "operatii.h"
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)

Materie_prima get_materie(Vector_dinamic* v, int poz)
{
	/*
	Determina materia de pe o anumita pozitie in vector
	v->Vector*, adresa vectorului la care ne referim
	poz->int, pozitia elentului care va fi determinat
	return->Materie, materia de pe respectiva pozitie
	*/
	return get(v, poz);
}

int get_total_materii(Vector_dinamic* v)
{
	/*
	Determina numarul total de materii din vector
	v->Vector_dinamic*, adresa vectorului la care ne referim
	return->int, numarul de materii din vector
	*/
	return get_size(v);
}

void adauga(Vector_dinamic* v, char* nume, char* producator, int cantitate)
{
	/*
	Functia adauga o materie prima la vectorul dinamic.
	v ->Vectorul_dinamic*, adresa vectorului la care ne referim
	nume - numele materiei care urmeaza sa fie adaugata
	producator - producatorul materiei care urmeaza sa fie adaugata
	cantitate - cantitatea materiei care urmeaza sa fie adaugata
	*/
	Materie_prima materie;
	materie = creeaza(nume, producator, cantitate);
	if (valideaza_materie(materie) == 0)

		printf("Date invalide!\n");
	else {
		int i = cautare_dupa_nume(v, nume);
		if (i == -1)
		{
			add(v, materie);
		}
		else {
			Materie_prima* lista = get_lista(v);
			modificare_cantitate(&(lista[i]), cantitate);
			distruge_materie(&materie);
			
		}
	}
}

int cautare_dupa_nume(Vector_dinamic* v, char* nume)
{
	/*
	Cauta un anumit nume intre elementele vectorului
	v->Vector_dinamic*, adresa vectorului la care ne referim
	nume->char, numele pe care il cautam
	return->int, pozitia elentului din vectorul v
	*/
	char nume2[20];
	for (int i = 0; i < get_length(v); i++)
	{
		strcpy(nume2, nume);
		if (strcmp(get_nume(get(v, i)), nume2) == 0)
			return i;
	}
	return -1;
}

void modifica_cantitate_materie(Vector_dinamic* v, char* nume, int cantitate)
{
	/*
	Modifica cantitatea unuei materii prima
	v->Vector_dinamic*, adresa vectorului la care ne referim
	nume->char, numele pe care il cautam
	cantitate->int, noua cantitate a produsului
	*/
	int poz = cautare_dupa_nume(v, nume);
	Materie_prima* materie = get_adresa(v, poz);
	modificare_cantitate(materie, cantitate);
}

void modifica_producator_materie(Vector_dinamic* v, char* nume, char* producator)
{
	/*
	Modifica producatorul unuei materii prime
	v->Vector_dinamic*, adresa vectorului la care ne referim
	nume->char, numele pe care il cautam
	producator->char, noul producator a produsului
	*/
	int poz = cautare_dupa_nume(v, nume);
	Materie_prima* materie = get_adresa(v, poz);
	modificare_producator(materie, producator);
}

void stergere(Vector_dinamic* v, char* nume)
{
	/*
	Functia sterge o materie, daca aceasta exista in vectorul dinamic.
	v - vectorul dinamic
	materie - materia care urmeaza sa fie stearsa
	*/
	int poz = cautare_dupa_nume(v, nume);
	Materie_prima m = dell(v, poz);
	free(get_nume(m));
	free(get_producator(m));
}

Vector_dinamic filtrare_dupa_cantitate(Vector_dinamic* v, int cantitate)
{
	/*
	Filtreaza materiile prime dupa o cantitate data.
	v -> Vector_dinamic*, adresa vectorului la care ne referim
	cantitate -> cantitatea in functie de care se face filtrarea
	return->vFiltrat-Vector_dinamic, vectorul care contine materiile filtrate
	*/
	Vector_dinamic vFiltrat = creeaza_vector_dinamic();
	for (int i = 0; i < get_length(v); i++)
	{
		Materie_prima m = get(v, i);
		
		if (get_cantitate(m) < cantitate)
		{
			Materie_prima copie = creeaza(get_nume(m), get_producator(m), get_cantitate(m));
			add(&vFiltrat, copie);
		}
	}
	return vFiltrat;
}

Vector_dinamic filtrare_dupa_nume(Vector_dinamic* v, char* litera)
{
	/*
	Filtreaza materiile prime dupa o cantitate data.
	v -> Vector_dinamic*, adresa vectorului la care ne referim
	cantitate -> cantitatea in functie de care se face filtrarea
	return->vFiltrat-Vector_dinamic, vectorul care contine materiile filtrate
	*/
	Vector_dinamic vFiltrat = creeaza_vector_dinamic();
	for (int i = 0; i < get_length(v); i++)
	{
		Materie_prima m = get(v, i);
		if (get_nume(m)[0] == litera[0])
		{
			Materie_prima copie = creeaza(get_nume(m), get_producator(m), get_cantitate(m));
			add(&vFiltrat, copie);
		}
	}
	return vFiltrat;
}


Materie_prima compare(Materie_prima m1, Materie_prima m2)
{
	
	//Compara doua materii dupa cantitate si pe urma dupa nume.
	//m1 -> Materie_prima, o materie care se compara
	//m2 -> Materie_prima, o materie care se compara
	
	if (get_cantitate(m1) < get_cantitate(m2))
		return m1;
	else if (get_cantitate(m1) == get_cantitate(m2))
		if (strcmp(get_nume(m1), get_nume(m2)) < 0)
			return m1;
	return m2;
}


int cmpMaterie(Materie_prima m1, Materie_prima m2)
{
	if (get_cantitate(m1) < get_cantitate(m2))
		return 1;
	else if (get_cantitate(m1) == get_cantitate(m2))
		if (strcmp(get_nume(m1), get_nume(m2)) < 0)
			return 1;
	return 0;
}
void sortare(Vector_dinamic* v) {

	for(int i=0;i<get_length(v);++i)
		for (int j = i + 1; j < get_length(v); ++j)
		{
			Materie_prima mi = get(v, i), mj = get(v, j);
			if (cmpMaterie(mi, mj) == 0)
			{
				get_lista(v)[i] = mj;
				get_lista(v)[j] = mi;
			}
			}
}
//void sortare(Vector_dinamic* v)
//{
//	/*
//	Sorteaza materiile prime dupa cantitate, iar daca cantitatile sunt egale, dupa nume
//	v -> Vector_dinamic*, adresa vectorului la care ne referim
//	*/
//	Materie_prima m_min, m_j, m_i, aux;
//	int mi = 0;
//	for (int i = 0; i < get_length(v); i++)
//	{
//		m_min = get(v, i);
//		mi = i;
//		m_i = get(v, i);
//		for (int j = i + 1; j < get_length(v); j++)
//		{
//			m_j = get(v, j);
//			//if(cmp(m_j, m_min) > 0)
//			if (get_cantitate(m_j) < get_cantitate(m_min))
//			{
//				m_min = get(v, j);
//				mi = j;
//			}
//			else if (get_cantitate(m_j) == get_cantitate(m_min))
//			{
//				if (strcmp(get_nume(m_j), get_nume(m_min)) < 0)
//				{
//					m_min = get(v, j);
//					mi = j;
//				}
//			}
//		/*	{
//				mi = j;
//				m_min = m_j;
//			}*/
//			//m_c = compare(m_j, m_min);
//			//if (strcmp(get_nume(m_c), get_nume(m_min)) != 0)
//			
//		}
//		aux = m_i;
//		get_lista(v)[i] = m_min;
//		get_lista(v)[mi] = aux;
//	}
//}

Vector_dinamic sortareMaterii(Vector_dinamic* v)
{
	Vector_dinamic vSortat = creeaza_vector_dinamic();
	for (int i = 0; i < get_length(v); i++)
	{
		Materie_prima m = get(v, i);
		Materie_prima copie = creeaza(get_nume(m), get_producator(m), get_cantitate(m));
		add(&vSortat, copie);
	}
	sortare(&vSortat);
	return vSortat;
}

/*
void sortare(Vector_dinamic* v)
{
	
	Sorteaza materiile prime dupa cantitate, iar daca cantitatile sunt egale, dupa nume
	v -> Vector_dinamic*, adresa vectorului la care ne referim
	
	Materie_prima m_min, m_j, m_i, aux;
	int mi = 0;
	for (int i = 0; i < get_length(v); i++)
	{
		m_min = get(v,i);
		mi = i;
		for (int j = i+1; j < get_length(v); j++)
		{
			m_j = get(v, j);
			if (get_cantitate(m_j) < get_cantitate(m_min))
			{
				m_min = get(v, j);
				mi = j;
			}
			else if (get_cantitate(m_j) == get_cantitate(m_min))
			{
				if (strcmp(get_nume(m_j), get_nume(m_min)) < 0)
				{
					m_min = get(v, j);
					mi = j;
				}
			}
		}
		m_i = get(v, i);
		aux = m_i;
		get_lista(v)[i] = m_min;
		get_lista(v)[mi] = aux;
	}
}
*/

//Teste

void test_sortare_dupa_cantitate()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1 = creeaza("lapte", "Hola", 250);
	adauga(&v, get_nume(m1), get_producator(m1), get_cantitate(m1));

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	adauga(&v, get_nume(m2), get_producator(m2), get_cantitate(m2));

	Materie_prima m3 = creeaza("cafea", "Jacobs", 143);
	adauga(&v, get_nume(m3), get_producator(m3), get_cantitate(m3));

	Materie_prima m4 = creeaza("apa", "Dorna", 100);
	adauga(&v, get_nume(m4), get_producator(m4), get_cantitate(m4));

	Vector_dinamic lista_sorata = sortareMaterii(&v);
	distruge_materie(&m1);
	distruge_materie(&m2);
	distruge_materie(&m3);
	distruge_materie(&m4);

	m1 = get(&lista_sorata, 0);
	assert(get_cantitate(m1) == 100);

	m2 = get(&lista_sorata, 1);
	assert(get_cantitate(m2) == 100);

	m3 = get(&lista_sorata, 2);
	assert(get_cantitate(m3) == 143);

	m4 = get(&lista_sorata, 3);
	assert(get_cantitate(m4) == 250);

	Materie_prima m5 = get(&lista_sorata, 0);
	assert(strcmp(get_nume(m5), "cascaval"));

	Materie_prima m6 = get(&lista_sorata, 1);
	assert(strcmp(get_nume(m6),"apa"));
	
	distruge(&v);
	distruge(&lista_sorata);
}

void test_filtrare_dupa_cantitate()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	adauga(&v, get_nume(m1), get_producator(m1), get_cantitate(m1));
	
	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	adauga(&v, get_nume(m2), get_producator(m2), get_cantitate(m2));

	Materie_prima m3 = creeaza("cafea", "Jacobs", 143);
	adauga(&v, get_nume(m3), get_producator(m3), get_cantitate(m3));

	Vector_dinamic vFiltrat1 = filtrare_dupa_cantitate(&v, 100);
	assert(get_length(&vFiltrat1) == 1);
	distruge(&vFiltrat1);


	Vector_dinamic vFiltrat2 = filtrare_dupa_cantitate(&v, 150);
	assert(get_length(&vFiltrat2) == 3);
	distruge(&vFiltrat2);

	Vector_dinamic vFiltrat3 = filtrare_dupa_cantitate(&v, 101);
	assert(get_length(&vFiltrat3) == 2);
	Materie_prima m = get(&vFiltrat3, 0);
	assert(strcmp(get_nume(m), "lapte") == 0);
	assert(get_cantitate(m) == 25);
	distruge(&vFiltrat3);
	
	distruge_materie(&m1);
	distruge_materie(&m2);
	distruge_materie(&m3);
	distruge(&v);
}

void test_filtrare_dupa_nume()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	adauga(&v, get_nume(m1), get_producator(m1), get_cantitate(m1));

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	adauga(&v, get_nume(m2), get_producator(m2), get_cantitate(m2));

	Materie_prima m3 = creeaza("cafea", "Jacobs", 143);
	adauga(&v, get_nume(m3), get_producator(m3), get_cantitate(m3));

	Vector_dinamic vFiltrat1 = filtrare_dupa_nume(&v, "c");
	assert(get_length(&vFiltrat1) == 2);
	Materie_prima m = get(&vFiltrat1, 0);
	assert(strcmp(get_nume(m), "cascaval") == 0);
	m = get(&vFiltrat1, 1);
	assert(strcmp(get_nume(m), "cafea") == 0);
	distruge(&vFiltrat1);

	distruge_materie(&m1);
	distruge_materie(&m2);
	distruge_materie(&m3);
	distruge(&v);
}

void test_producator_materie()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1;

	m1 = creeaza("lapte", "Hola", 25);
	add(&v, m1);
	modifica_producator_materie(&v, "lapte", "Zuzu");
	assert(strcmp(get_producator(get(&v, 0)), "Zuzu") == 0);
	distruge(&v);
}

void test_adauga()
{
	Vector_dinamic v = creeaza_vector_dinamic();

	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	adauga(&v, get_nume(m1), get_producator(m1), get_cantitate(m1));
	assert(get_total_materii(&v) == 1);

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	adauga(&v, get_nume(m2), get_producator(m2), get_cantitate(m2));
	assert(get_total_materii(&v) == 2);

	Materie_prima m3 = creeaza("cafea", "Jacobs", 143);
	adauga(&v, get_nume(m3), get_producator(m3), get_cantitate(m3));
	assert(get_total_materii(&v) == 3);
	distruge_materie(&m1);
	distruge_materie(&m2);
	distruge_materie(&m3);
	distruge(&v);
}

void test_get_materie()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1, m2;

	m1 = creeaza("lapte", "Hola", 25);
	adauga(&v, get_nume(m1), get_producator(m1), get_cantitate(m1));
	m2 = get_materie(&v, 0);
	assert(strcmp(get_nume(m1), get_nume(m2)) == 0);
	assert(strcmp(get_producator(m1), get_producator(m2)) == 0);
	assert(get_cantitate(m1) == get_cantitate(m2));
	
	distruge_materie(&m1);
	distruge(&v);
}

void test_get_total_materii()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1;
	char nume[4];
	for (int i = 0; i <= 90; i++)
	{
		itoa(i,nume,10);
		m1 = creeaza(nume, "Hola", 25);
		adauga(&v, get_nume(m1), get_producator(m1), get_cantitate(m1));
		distruge_materie(&m1);
	}
	m1 = creeaza("1", "Hola", 25);
	adauga(&v, get_nume(m1), get_producator(m1), get_cantitate(m1));
	assert(get_total_materii(&v) == 91);
	distruge_materie(&m1);
	distruge(&v);
}

void test_cautare_dupa_nume()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1, m2, m3;


	m1 = creeaza("lapte", "Hola", 25);
	adauga(&v, get_nume(m1), get_producator(m1), get_cantitate(m1));
	assert(cautare_dupa_nume(&v, get_nume(m1)) == 0);

	m2 = creeaza("cascaval", "Hochland", 100);
	adauga(&v, get_nume(m2), get_producator(m2), get_cantitate(m2));
	assert(cautare_dupa_nume(&v, get_nume(m2)) == 1);

	m3 = creeaza("cafea", "Jacobs", 143);
	adauga(&v, get_nume(m3), get_producator(m3), get_cantitate(m3));
	assert(cautare_dupa_nume(&v, get_nume(m3)) == 2);

	distruge_materie(&m1);
	distruge_materie(&m2);
	distruge_materie(&m3);
	distruge(&v);
}

void test_modifica_cantitate_materie()
{
	/*
	Vector_dinamic* v = creeaza_vector_dinamic();
	*/
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1, m2, m3;

	m1 = creeaza("lapte", "Hola", 25);
	add(&v, m1);
	modifica_cantitate_materie(&v, "lapte", 20);
	assert(get_cantitate(get(&v, 0)) == 20);

	m2 = creeaza("cascaval", "Hochland", 100);
	add(&v, m2);
	modifica_cantitate_materie(&v, "cascaval", 30);
	assert(get_cantitate(get(&v, 1)) == 30);

	m3 = creeaza("cafea", "Jacobs", 143);
	add(&v, m3);
	modifica_cantitate_materie(&v, "cafea", 30);
	assert(get_cantitate(get(&v, 2)) == 30);
	distruge(&v);
}

void test_sterge()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	add(&v, m1);
	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	add(&v, m2);
	Materie_prima m3 = creeaza("cafea", "Jacobs", 143);
	add(&v, m3);
	assert(get_size(&v) == 3);

	stergere(&v, "lapte");
	assert(get_size(&v) == 2);

	stergere(&v, "cascaval");
	assert(get_size(&v) == 1);

	stergere(&v, "cafea");
	assert(get_size(&v) == 0);
	distruge(&v);
}