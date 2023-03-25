#pragma once
#include "vector_dinamic.h"


void adauga(Vector_dinamic* v, char* nume, char* producator, int cantitate);
Materie_prima get_materie(Vector_dinamic* v, int poz);
int get_total_materii(Vector_dinamic* v);
int cautare_dupa_nume(Vector_dinamic* v, char* nume);
void modifica_cantitate_materie(Vector_dinamic* v, char* nume, int cantitate);
void modifica_producator_materie(Vector_dinamic* v, char* nume, char* producator);
void stergere(Vector_dinamic* v, char* nume);
Vector_dinamic filtrare_dupa_cantitate(Vector_dinamic* v, int cantitate);
Vector_dinamic filtrare_dupa_nume(Vector_dinamic* v, char* litera);
Materie_prima compare(Materie_prima m1, Materie_prima m2);

int cmpMaterie(Materie_prima m1, Materie_prima m2);
Vector_dinamic sortareMaterii(Vector_dinamic* v);

typedef int (Compare)(Materie_prima m1, Materie_prima m2);
void sortare(Vector_dinamic* v);


void test_adauga();
void test_get_materie();
void test_get_total_materii();
void test_cautare_dupa_nume();
void test_modifica_cantitate_materie();
void test_producator_materie();
void test_sterge();
void test_filtrare_dupa_cantitate();
void test_sortare_dupa_cantitate();
void test_filtrare_dupa_nume();

