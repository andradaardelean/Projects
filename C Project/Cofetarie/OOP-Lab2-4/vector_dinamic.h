#pragma once
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#include "materie_prima.h"


typedef struct
{
	Materie_prima* lista_materii;
	int length;
	int capacity;
}Vector_dinamic;

Materie_prima* get_lista(Vector_dinamic* v);
int get_capacity(Vector_dinamic* v);
int get_length(Vector_dinamic* v);
void modifica_capacitate(Vector_dinamic* v, int c);
void modifica_lungime(Vector_dinamic* v, int l);

Vector_dinamic creeaza_vector_dinamic();
void distruge(Vector_dinamic* v);
//void adauga(Vector_dinamic* v, Materie_prima m);
void redimensionare(Vector_dinamic* v);
Materie_prima get(Vector_dinamic* v, int poz);

Materie_prima* get_adresa(Vector_dinamic* v, int poz);
int get_size(Vector_dinamic* v);
void add(Vector_dinamic* v, Materie_prima m);
Materie_prima dell(Vector_dinamic* v, int poz);


void test_creeaza_vector();
void test_distruge();
void test_redimensionare();
void test_get();
void test_get_capacity();
void test_get_length();
void test_modifica_capacitate();
void test_modifica_lungime();
void test_modifica_lista();
void test_delete();
void test_equal();