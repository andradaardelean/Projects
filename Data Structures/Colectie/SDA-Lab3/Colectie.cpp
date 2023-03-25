#include "Colectie.h"
#include "IteratorColectie.h"
#include <iostream>
#include <assert.h>

using namespace std;

Nod::Nod(TElem e, PNod urm) {
	/* Theta(1) */
	this->el = e;
	this->urm = urm;
	this->frecv = 1;
}

TElem Nod::element() {
	/* Theta(1) */
	return el;
}

PNod Nod::urmator() {
	/* Theta(1) */
	return urm;
}

TElem Nod::get_frecv() {
	/* Theta(1) */
	return frecv;
}

bool rel(TElem e1, TElem e2) {
	/* Theta(1) */
	return e1 <= e2;
}

Colectie::Colectie() {
	/* Theta(1) */
	prim = nullptr;
}

void Colectie::adauga(TElem e) {
	/* O(nrElem)*/
	if (cauta(e) == true) {  //daca se gaseste in lista ii crestem frecventa
		PNod curent;
		curent = prim;
		while (rel(e, curent->el) == false)
		{
			curent = curent->urm;
		}
		curent->frecv++;
	}
	else { // daca nu se gaseste in lista trebuie adaugat
		if (dim() == 0) { //daca lista e goala il punem la inceput.
			PNod n = new Nod(e, nullptr);
			prim = n;
		}
		else {
			PNod curent, anterior;
			curent = prim;
			anterior = prim;
			while (rel(e, curent->el) == false && curent->urm != nullptr) {// cat timp el nou e mai mare decat cel curent si nu am ajuns la capatul listei
				anterior = curent;
				curent = curent->urm;
			}
			if (rel(e, curent->el) == true) { // daca el nou e mai mic decat cel curent 
				PNod n = new Nod(e, nullptr);
				if (curent == prim) { // daca e pe prima poz il adaugam la inceput
					n->urm = prim;
					prim = n;
				}
				else { // daca e pe alta pozitie il adaugam intre doua elemente
					n->urm = curent;
					anterior->urm = n;
				}
			}
			else if (curent->urm == nullptr) { // daca am ajuns la capatul listei, il adaugam la final
				PNod n = new Nod(e, nullptr);
				curent->urm = n;
			}
		}
	}
}

bool Colectie::sterge(TElem e) {
	/* O(nrElem) */
	if (nrAparitii(e) > 0) { // daca elem e in lista
		IteratorColectie it = iterator();
		while (it.element() != e)
			it.urmator();
		if (nrAparitii(e) == 1) { // daca apare o singura data, trebuie sters 
			if (it.curent == prim) {
				prim = prim->urmator();
				delete it.curent;
			}
			else {
				IteratorColectie pred = iterator();
				while (pred.curent->urm->element() != e)
					pred.urmator();
				PNod sters = pred.curent->urm;
				pred.curent->urm = pred.curent->urm->urm;
				delete sters;
			}
		}
		else it.curent->frecv--; // daca apare de mai multe ori, doar scadem frecventa
		return true;
	}
	return false;
}


bool Colectie::cauta(TElem elem) const {
	/* O(nrElem) */
	if (prim == nullptr)
		return false;
	PNod curent = prim;
	while (curent != nullptr) { // cat timp u suntem la finalul listei
		if (curent->el == elem)
			return true;
		curent = curent->urm;
	}
	return false;
}

int Colectie::nrAparitii(TElem elem) const {
	/* O(nrElem) */
	if (cauta(elem) == false)
		return 0;

	PNod curent = prim;
	while (curent->urm != nullptr && curent->el != elem)
		curent = curent->urm;
	return curent->frecv;
}

int Colectie::dim() const {
	/* O(nrElem) */
	int dim = 0;
	/*PNod curent = prim;
	while (curent->urm != nullptr) {
		dim = dim + curent->frecv;
		curent = curent->urm;
	}*/
	IteratorColectie it = iterator();
	while (it.valid() == true)
	{
		dim = dim + it.curent->get_frecv();
		it.urmator();
	}
	return dim;
}

bool Colectie::vida() const {
	/* Theta(1) */
	if (prim == nullptr)
		return true;
	return false;
}


IteratorColectie Colectie::iterator() const {
	return  IteratorColectie(*this);
}


Colectie::~Colectie() {
	/* Theta(1) */
	while (prim != nullptr) {
		PNod n = prim;
		prim = prim->urm;
		delete n;
	}
}

int Colectie::eliminaAparitii(int nr, TElem e) {
	if (nr < 0) {
		throw "nr este negativ";
	}
	int nrAp = nrAparitii(e);
	if (nrAp < nr) {
		for (int i = 0; i < nrAp; i++)
			sterge(e);
		return nrAp;
	}
	return 0;
}



