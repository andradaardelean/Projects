#pragma once
#include "materie_prima.h"
#include <string.h>
#include <stdlib.h>
#include <assert.h>

Materie_prima creeaza(char* nume, char* producator, int cantitate)
{
	/*
	Creeaza un obiect de tip materie prima.
	pre: True
	post: obiectul creat
	nume - numele materiei prime
	producator - producatorul materiei prime
	cantitate - cantitatea materiei
	return: materia creata
	rtype: Materie_prima
	*/
	Materie_prima materie;
	int nrCaractere = (int)strlen(nume) + 1;
	materie.nume = malloc(nrCaractere * sizeof(char));
	strcpy_s(materie.nume, nrCaractere, nume);

	nrCaractere = (int)strlen(producator) + 1;
	materie.producator = malloc(nrCaractere * sizeof(char));
	strcpy_s(materie.producator, nrCaractere,producator);
	
	materie.cantitate = cantitate;

	return materie;
}

void distruge_materie(Materie_prima* m)
{
	//free(get_nume(m));
	//free(get_producator(m));
	//m.nume = NULL;
	free(m->nume);
	free(m->producator);
	m->nume = NULL;
	m->producator = NULL;
	m->cantitate = -1;
}

char* get_nume(Materie_prima materie)
{
	/*
	Determina numele unei anumite materii
	m->Materia, materia careia i se determina numele
	return->nume, numele respectiv
	*/
	return materie.nume;
}

char* get_producator(Materie_prima materie)
{
	/*
	Determina producatorul unei anumite materii
	m->Materia, materia careia i se determina numele
	return->producator, producator respectiv
	*/
	return materie.producator;
}
int get_cantitate(Materie_prima materie)
{
	/*
	Determina cantitatea unei anumite materii
	m->Materia, materia careia i se determina numele
	return->cantitate, cantitatea respectiva
	*/
	return materie.cantitate;
}

void modificare_cantitate(Materie_prima* materie, int cantitate_noua)
{
	/*
	Modifica cantitatea unei materii
	m->Materia, materia careia i se determina numele
	return-> -
	*/
	materie->cantitate = cantitate_noua;
}

void modificare_producator(Materie_prima* materie, char* producator_nou)
{
	/*
	Modifica producatorul unei materii
	m->Materia, materia careia i se determina numele
	return-> -
	*/
	int nrCaractere = (int)strlen(producator_nou) + 1;
	strcpy_s(materie->producator,nrCaractere, producator_nou);
}

int valideaza_materie(Materie_prima m)
{
	/*
	Functia verficia daca datele unei materii prime sunt valide.
	nume - numele materiei
	producator - producatorul materiei
	cantitate - cantitatea materiei
	*/
	if (strlen(get_nume(m)) > 10 || strlen(get_nume(m)) < 1 || !strcmp(get_nume(m), ""))
		return 0;
	if (strlen(get_producator(m)) > 20 || !strcmp(get_producator(m), ""))
		return 0;
	if (get_cantitate(m) < 0 || get_cantitate(m) > 5000)
		return 0;
	return 1;
}

// Teste

void test_creeaza()
{
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	assert(get_cantitate(m1) == 25);
	assert(strcmp(get_nume(m1), "lapte") == 0);
	assert(strcmp(get_producator(m1), "Hola") == 0);
	distruge_materie(&m1);

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	assert(get_cantitate(m2) == 100);
	assert(strcmp(get_nume(m2), "cascaval") == 0);
	assert(strcmp(get_producator(m2), "Hochland") == 0);
	distruge_materie(&m2);
}

void test_modificare_cantitate()
{
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	modificare_cantitate(&m1, 100);
	assert(get_cantitate(m1) == 100);
	distruge_materie(&m1);

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	modificare_cantitate(&m2, 50);
	assert(get_cantitate(m2) == 50);
	distruge_materie(&m2);

	Materie_prima m3 = creeaza("cafea", "Jacobs", 143);
	modificare_cantitate(&m3, 150);
	assert(get_cantitate(m3) == 150);
	distruge_materie(&m3);
}

void test_modificare_producator()
{
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	modificare_producator(&m1, "Zuzu");
	assert(strcmp(get_producator(m1),"Zuzu")==0);
	distruge_materie(&m1);

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	modificare_producator(&m2, "Lidl");
	assert(strcmp(get_producator(m2), "Lidl") == 0);
	distruge_materie(&m2);

	//Materie_prima m3 = creeaza("cafea", "Jacobs", 143);
	//modificare_producator(&m3, "Lavazza");
	//assert(strcmp(get_producator(m3), "Lavazza") == 0);
	//distruge_materie(m3);

}

void test_get_nume()
{
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	assert(strcmp(get_nume(m1), "lapte") == 0);
	distruge_materie(&m1);

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	assert(strcmp(get_nume(m2), "cascaval") == 0);
	distruge_materie(&m2);
}

void test_get_producator()
{
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	assert(strcmp(get_producator(m1), "Hola") == 0);
	distruge_materie(&m1);

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	assert(strcmp(get_producator(m2), "Hochland") == 0);
	distruge_materie(&m2);
}

void test_get_cantitate()
{
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	assert(get_cantitate(m1) == 25);
	distruge_materie(&m1);

	Materie_prima m2 = creeaza("cascaval", "Hochland", 100);
	assert(get_cantitate(m2) == 100);
	distruge_materie(&m2);
}

void test_valideaza_materie()
{
	
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	assert(valideaza_materie(m1) == 1);
	distruge_materie(&m1);

	Materie_prima m2 = creeaza("c", "Hochland", 100);
	assert(valideaza_materie(m2) == 1);
	distruge_materie(&m2);

	Materie_prima m3 = creeaza("c", "Hochland", -2);
	assert(valideaza_materie(m3) == 0);
	distruge_materie(&m3);
	
	Materie_prima m4 = creeaza("carne", "", 100);
	assert(valideaza_materie(m4) == 0);
	distruge_materie(&m4);

	Materie_prima m5 = creeaza("", "zuzu", 100);
	assert(valideaza_materie(m5) == 0);
	distruge_materie(&m5);
}
