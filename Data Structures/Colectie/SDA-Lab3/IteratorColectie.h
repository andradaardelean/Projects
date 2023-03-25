#pragma once
#include "Colectie.h"
#include <stack>

class Colectie;
class Nod;
typedef int TElem;

using std::stack;

class IteratorColectie
{
	friend class Colectie;
	friend class Nod;

private:
	//constructorul primeste o referinta catre Container
	//iteratorul va referi primul element din container
	IteratorColectie(const Colectie& c);

	//contine o referinta catre containerul pe care il itereaza
	const Colectie& col;
	/* aici e reprezentarea  spcifica a iteratorului*/

	PNod curent;
	//TElem frecv_curenta;

public:

	//reseteaza pozitia iteratorului la inceputul containerului
	void prim();

	//muta iteratorul in container
	// arunca exceptie daca iteratorul nu e valid
	void urmator();

	//verifica daca iteratorul e valid (indica un element al containerului)
	bool valid() const;

	//returneaza valoarea elementului din container referit de iterator
	//arunca exceptie daca iteratorul nu e valid
	TElem element() const;
};

