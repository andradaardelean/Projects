#pragma once

typedef int TElem;

#define NULL_TELEMENT 0

class Matrice {

private:
	/* aici e reprezentarea */
	int* linie;
	int* coloana;
	TElem* valoare;

	int m, n, dim, cap;
	int totalLinii, totalColoane;

	void capacity();
	void delete_capacity();

	void add_poz(int i, int j, TElem m);
	void delete_poz(int i, int j);
	void modify_poz(int i, int j, TElem m);
	

public:

	//constructor
	//se arunca exceptie daca nrLinii<=0 sau nrColoane<=0
	Matrice(int nrLinii, int nrColoane);


	//destructor
	~Matrice();

	//returnare element de pe o linie si o coloana
	//se arunca exceptie daca (i,j) nu e pozitie valida in Matrice
	//indicii se considera incepand de la 0
	TElem element(int i, int j) const;


	// returnare numar linii
	int nrLinii() const;

	// returnare numar coloane
	int nrColoane() const;


	// modificare element de pe o linie si o coloana si returnarea vechii valori
	// se arunca exceptie daca (i,j) nu e o pozitie valida in Matrice
	TElem modifica(int i, int j, TElem);

};







