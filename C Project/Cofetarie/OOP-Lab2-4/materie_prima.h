#pragma once

typedef struct
{
	char* nume;
	char* producator;
	int cantitate;
}Materie_prima;

Materie_prima creeaza(char* nume, char* producator, int cantitate);

void distruge_materie(Materie_prima* m);
char* get_nume(Materie_prima m);
char* get_producator(Materie_prima m);
int get_cantitate(Materie_prima m);
void modificare_cantitate(Materie_prima* m , int cantitate_noua);
void modificare_producator(Materie_prima* m, char* producator_nou);
int valideaza_materie(Materie_prima m);


void test_creeaza();
void test_modificare_cantitate();
void test_modificare_producator();
void test_get_nume();
void test_get_producator();
void test_get_cantitate();
void test_valideaza_materie();




