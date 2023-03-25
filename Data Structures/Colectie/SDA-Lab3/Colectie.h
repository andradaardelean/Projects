#pragma once
//#include "IteratorColectie.h"

typedef int TElem;

typedef bool(*Relatie)(TElem, TElem);

//in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class IteratorColectie;

class Nod;

typedef Nod* PNod;

class Nod
{
public:
	friend class Colectie;

	//constructor

	Nod(TElem e, PNod urm);

	TElem element();
	// void set_elem(TElem elem_nou);

	PNod urmator();

	TElem get_frecv();
	//void set_frecv(TElem frecv_noua);

private:
	TElem el;
	TElem frecv;
	PNod urm;
};

class Colectie {

	friend class IteratorColectie;

private:
	
	PNod prim;
	PNod ultim;
	int len;

public:
	//constructorul implicit
	Colectie();

	int eliminaAparitii(int nr, TElem e);

	//adauga un element in colectie
	void adauga(TElem e);

	//sterge o aparitie a unui element din colectie
	//returneaza adevarat daca s-a putut sterge
	bool sterge(TElem e);

	//verifica daca un element se afla in colectie
	bool cauta(TElem elem) const;

	//returneaza numar de aparitii ale unui element in colectie
	int nrAparitii(TElem elem) const;


	//intoarce numarul de elemente din colectie;
	int dim() const;

	//verifica daca colectia e vida;
	bool vida() const;

	//returneaza un iterator pe colectie
	IteratorColectie iterator() const;

	// destructorul colectiei
	~Colectie();


};

