#pragma once

typedef struct
{
	char nume[20], producator[20];
	int cantitate;
}Materie_prima;

typedef struct
{
	Materie_prima* lista_materii;
	int length;
	int capacity;
}Vector_dinamic;

Vector_dinamic* v;
