#pragma once
#include "vector_dinamic.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#pragma warning(disable : 4996)
#define INIT_CAPACITY 100

Vector_dinamic creeaza_vector_dinamic()
{
	/*
	Functia creeaza vectorul dinamic v si ii aloca spatiu necesar.
	*/
	//Vector_dinamic* v = (Vector_dinamic*)malloc(sizeof(Vector_dinamic));
	//Vector_dinamic* v = (Vector_dinamic*)malloc(sizeof(Vector_dinamic));
	Vector_dinamic v;
	v.lista_materii = (Materie_prima*)malloc((INIT_CAPACITY) * sizeof(Materie_prima));
	v.capacity = INIT_CAPACITY;
	v.length = 0;
	
	return v;
}

Materie_prima* get_lista(Vector_dinamic* v)
{
	/*
	Determina adreasa elementelor din vectorul dinamic
	v - Vector*, vector a carei adresa a elementelor va fi determinata
	return -> Produs*, adresa respectiva
	*/
	return v->lista_materii;
}

int get_capacity(Vector_dinamic* v)
{
	/*
	Determina capacitatea maxima a vectorului dinamic (la momentul de fata)
	v - Vector*, vector a carei capacitate va fi determinata
	return -> int, capacitatea respectiva
	*/
	return v->capacity;
}

int get_length(Vector_dinamic* v)
{
	/*
	Determina dimensiunea vectorului dinamic (la momentul de fata)
	v - Vector*, vector a carei dimensiune va fi determinata
	return -> int, dimensiunea respectiva
	*/
	return v->length;
}

void distruge(Vector_dinamic* v)
{
	/*
	Elibereaza din memorie vectorul v
	v - Vector*, vector care va fi distrus
	*/
	for (int i = 0; i < get_length(v); i++)
	{
		Materie_prima m = get(v, i);
		distruge_materie(&m);
	}
	free(get_lista(v));
}

void modifica_capacitate(Vector_dinamic* v, int capacitate_noua)
{
	/*
	Modifica capacitatea vectorului dinamic
	v - Vector*, vector dinamic la care ne referim
	cp - int, noua capacitate a vectorului dinamic
	*/
	v->capacity = capacitate_noua;
}

void modifica_lungime(Vector_dinamic* v, int lungime_noua)
{
	/*
	Modifica dimensiunea vectorului
	v - Vector*, vector dinamic la care ne referim
	n - int, noua dimensiune a vectorului
	*/
	v->length = lungime_noua;
}

void modifica_lista(Vector_dinamic* v, Materie_prima* Lista_materii)
{
	/*
	Modifica adresa elementelor din vector
	v - Vector*, vector dinamic la care ne referim
	*/
	v->lista_materii = Lista_materii;
}

void redimensionare(Vector_dinamic* v)
{
	/*
	Aloca mai multa memorie pentru elementele din vector
	v - Vector*, vector dinamic la care ne referim
	*/
	int  new_cap = (v->capacity) * 2;
	Materie_prima* materii_list = (Materie_prima*)malloc(new_cap * sizeof(Materie_prima));
	
	for (int i = 0; i < get_size(v); i++)
	{
		materii_list[i] = get(v, i);
	}
	free(get_lista(v));
	modifica_capacitate(v, new_cap);
	modifica_lista(v, materii_list);
}

void add(Vector_dinamic* v, Materie_prima m)
{
	/*
	Adauga o noua materie in vector
	v - Vector*, vector dinamic la care ne referim
	pr - Materie, materia care va fi adaugata in vector
	*/
	if (get_size(v) == get_capacity(v))
		redimensionare(v);
	get_lista(v)[v->length] = m;
	modifica_lungime(v, get_size(v) + 1);
}

Materie_prima get(Vector_dinamic* v, int poz)
{
	/*
	Determina elementul de pe pozitia "poz" din vector
	v - Vector*, vector dinamic la care ne referim
	poz - int, indicele elementului a carei valoare va fi determinata
	return -> Materie, elementul cautat
	*/
	return get_lista(v)[poz];
}

Materie_prima* get_adresa(Vector_dinamic* v, int poz)
{
	/*
	Determina adresa elementului de pe pozitia "poz" din vector
	v - Vector*, vector dinamic la care ne referim
	poz - int, indicele elementului a carei adresa va fi determinata
	return -> Materie*, adresa elementului cautat
	*/
	Materie_prima* m = &(get_lista(v)[poz]);
	return m;
}

int get_size(Vector_dinamic* v) {
	return v->length;
}

Materie_prima dell(Vector_dinamic* v, int poz)
{
	/*
	Sterge un element din vector dupa o anumita pozitie
	v->Vector*, vector dinamic la care ne referim
	poz->int, indicele elementului care va fi sters din vector
	*/
	Materie_prima m1 = get(v, poz);
	for (int i = poz; i < get_size(v) - 1; i++)
	{
		Materie_prima* m = get_adresa(v, i);
		Materie_prima m2 = get(v, i + 1);
		*m = m2;
	}
	modifica_lungime(v, get_size(v) - 1);
	return m1;
	//free(&get_lista(v)[get_size(v)-1]);
}

int equal(Materie_prima m1, Materie_prima m2)
{
	/*
	verifica daca doua materii sunt egale
	m1->Materie, prima materie
	m2->Materie, a doua materie
	return->int, 1 daca cele doua sunt egale, si 0 daca nu sunt egale
	*/
	if (strcmp(get_nume(m1), get_nume(m2)) == 0)
		return 1;
	else return 0;
}


//Teste

void test_equal()
{
	Materie_prima m1, m2, m3;
	m1 = creeaza("lapte", "Hola", 25);
	m2 = creeaza("lapte", "Hola", 25);
	assert(equal(m1, m2) == 1);

	m3 = creeaza("lapt", "Hoa", 20);
	assert(equal(m1, m3) == 0);
	distruge_materie(&m1);
	distruge_materie(&m2);
	distruge_materie(&m3);
}

void test_creeaza_vector()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	assert(get_capacity(&v) == INIT_CAPACITY);
	assert(get_size(&v) == 0);
	distruge(&v);
}

void test_distruge()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	assert(get_capacity(&v) == INIT_CAPACITY);
	assert(get_size(&v) == 0);
	distruge(&v);
}

void test_redimensionare()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	assert(get_capacity(&v) == INIT_CAPACITY);
	assert(get_size(&v) == 0);
	Materie_prima m;
	for (int i = 0; i <= 100; ++i)
	{
		m = creeaza("BASIC", "BASIC", 25);
		add(&v, m);
	}
	//printf("%d", get_size(&v));
	assert(get_capacity(&v) == 2 * INIT_CAPACITY);
	distruge(&v);
}

void test_get()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	assert(get_capacity(&v) == INIT_CAPACITY);
	assert(get_size(&v) == 0);

	Materie_prima m1,m2;
	m1 = creeaza("lapte", "Hola", 25);
	add(&v, m1);
	m2 = get(&v, 0);
	assert(strcmp(get_nume(m1), get_nume(m2))==0);
	assert(get_size(&v) == 1);

	m1 = creeaza("lapte", "Hola", 25);
	add(&v, m1);
	m2 = get(&v, 0);
	assert(strcmp(get_nume(m1), get_nume(m2))==0);
	assert(get_size(&v) == 2);

	m1 = creeaza("lapte", "Hola", 25);
	add(&v, m1);
	m2 = get(&v, 0);
	assert(strcmp(get_nume(m1), get_nume(m2))==0);
	assert(get_size(&v) == 3);
	distruge(&v);
}

void test_get_capacity()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1;
	char nume[4];
	//Materie_prima m;
	for (int i = 0; i < 100; ++i)
	{
		itoa(i, nume, 10);
		m1 = creeaza(nume, "Hola", 25);
		add(&v, m1);
	}
	assert(get_capacity(&v) == 100);
	m1 = creeaza("doi", "Hola", 25);
	add(&v, m1);
	assert(get_capacity(&v) == 200);
	//distruge_materie(&m1);
	distruge(&v);
}

void test_get_length()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1;
	for (int i = 0; i < 100; i++)
	{
		m1 = creeaza("lapte", "Hola", 25);
		add(&v, m1);
	}
	assert(get_length(&v) == 100);
	//distruge_materie(&m1);
	distruge(&v);
}

void test_modifica_capacitate()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	
	modifica_capacitate(&v, 20);
	assert(get_capacity(&v) == 20);

	modifica_capacitate(&v, 50);
	assert(get_capacity(&v) == 50);

	modifica_capacitate(&v, 100);
	assert(get_capacity(&v) == 100);
	distruge(&v);
}

void test_modifica_lungime()
{
	Vector_dinamic v = creeaza_vector_dinamic();

	modifica_lungime(&v, 20);
	assert(get_length(&v) == 20);

	modifica_lungime(&v, 15);
	assert(get_length(&v) == 15);

	modifica_lungime(&v, 30);
	assert(get_length(&v) == 30);

	modifica_lungime(&v, 0);
	distruge(&v);
}

void test_modifica_lista()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Vector_dinamic v2 = creeaza_vector_dinamic();
	free(get_lista(&v));
	modifica_lista(&v, get_lista(&v2));
	assert(get_lista(&v) == get_lista(&v2));
	distruge(&v2);
}

void test_delete()
{
	Vector_dinamic v = creeaza_vector_dinamic();
	Materie_prima m1 = creeaza("lapte", "Hola", 25);
	add(&v, m1);
	assert(get_length(&v) == 1);
	dell(&v, 0);
	assert(get_length(&v) == 0);
	distruge_materie(&m1);
	distruge(&v);
}
