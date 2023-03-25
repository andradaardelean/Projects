#include "Matrice.h"
#include <exception>
#include <string>

using namespace std;


Matrice::Matrice(int nrLinii, int nrColoane) 
{
	/*	Theta(nrLinii)	*/
	if (nrLinii <= 0 && nrColoane <= 0)
		throw exception();

	this->cap = 2;
	this->dim = 0;
	this->totalLinii = nrLinii;
	this->totalColoane = nrColoane;
	this->linie = new int[totalLinii + 1];
	this->coloana = new int[cap];
	this->valoare = new TElem[cap];
	for (int i = 0; i <= this->totalLinii; i++)
		this->linie[i] = 0;
}

Matrice::~Matrice()
{ 
	/*	 Theta(1)	*/
	delete[] this->linie;
	delete[] this->coloana;
	delete[] this->valoare;
}

int Matrice::nrLinii() const 
{
	/*	 Theta(1)	*/
	return this->totalLinii;
}


int Matrice::nrColoane() const 
{
	/*	 Theta(1)	*/
	return this->totalColoane;
}


TElem Matrice::element(int i, int j) const 
{
	/*	O(nrColoane) */
	TElem m = NULL_TELEMENT;
	if (i < 0 || i >= this->totalLinii || j < 0 || j >= this->totalColoane)
		throw exception();
	for(int k = this->linie[i];k< this->linie[i+1];k++)
		if (this->coloana[k] == j)
		{
			m = this->valoare[k];
			break;
		}
	return m;
}

void Matrice::capacity()
{
	/*	Theta(dim) */
	this->cap *= 2;
	int* ncoloana = new int[this->cap];
	TElem* nvaloare = new TElem[this->cap];
	for (int j = 0; j < this->dim; j++)
	{
		ncoloana[j] = this->coloana[j];
		nvaloare[j] = this->valoare[j];
	}
	delete[] this->coloana;
	this->coloana = ncoloana;
	delete[] this->valoare;
	this->valoare = nvaloare;
}

void Matrice::delete_capacity()
{
	/*	Theta(dim)	 */
	this->cap /= 2;
	int* ncoloana = new int[this->cap];
	TElem* nvaloare = new TElem[this->cap];
	for (int j = 0; j < this->dim; j++)
	{
		ncoloana[j] = this->coloana[j];
		nvaloare[j] = this->valoare[j];
	}
	delete[] this->coloana;
	this->coloana = ncoloana;
	delete[] this->valoare;
	this->valoare = nvaloare;
}

void Matrice::add_poz(int i, int j, TElem e)
{
	/*		O(nrColoane)	*/
	if (this->dim == this->cap)
		capacity();
	this->dim++;
	for (int k = this->dim - 1; k > this->linie[i + 1]; k--)
	{
		this->coloana[k] = this->coloana[k - 1];
		this->valoare[k] = this->valoare[k - 1];
	}
	this->coloana[this->linie[i + 1]] = j;
	this->valoare[this->linie[i + 1]] = e;
	for (int k = i + 1; k < this->totalLinii; k++)
		this->linie[k] = this->linie[k] + 1;
}

void Matrice::delete_poz(int i, int j)
{
	/*	O(nrLinii)	 */
	int poz = -1;
	for(int k = this->linie[i];k<this->linie[i+1];k++)
		if (this->coloana[k] == j)
		{
			poz = k;
			break;
		}
	if (poz != -1)
	{
		for (int k = i + 1; k < this->totalLinii; k++)
			this->linie[k] = this->linie[k] - 1;
		for (int k = poz; k < this->dim - 1; k++)
		{
			this->coloana[k] = this->coloana[k + 1];
			this->valoare[k] = this->valoare[k + 1];
		}
		this->dim--;
	}
}

void Matrice::modify_poz(int i, int j, TElem e)
{
	/*	O(nrColoane)  */
	for (int k = this->linie[i]; k < this->linie[i + 1]; k++)
	{
		if (this->coloana[k] == j)
		{
			this->valoare[k] = e;
			break;
		}
	}
}

TElem Matrice::modifica(int i, int j, TElem e) {
	/* O(nrLinii+nr_elem_nenule) */
	TElem M = NULL_TELEMENT;
	if (i < 0 || i >= this->totalLinii || j<0 || j>this->totalColoane)
		throw exception();

	for (int k = this->linie[i]; k < this->linie[i + 1]; k++)
	{
		if (this->coloana[k] == j)
			if (this->valoare[k] != NULL_TELEMENT && e == NULL_TELEMENT)
			{
				m = this->valoare[k];
				delete_poz(i, j);
				if (this->dim < this->cap / 2)
					delete_capacity();
				return m;
			}
			else if (this->valoare[k] != NULL_TELEMENT && e != NULL_TELEMENT)
			{
				m = this->valoare[k];
				modify_poz(i, j, e);
				return m;
			}
	}
	if (e != NULL_TELEMENT)
		add_poz(i, j, e);
	return m;
}


