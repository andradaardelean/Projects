#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>


using namespace std;

//o posibila relatie
bool rel(TElem e1, TElem e2) {
	if (e1 < e2) {
		return true;
	}
	else {
		return false;
	}
}

Nod::Nod(TElem e, PNod st, PNod dr) {
	this->e = e;
	this->st = st;
	this->dr = dr;
}

TElem Nod::element() {
	return this->e;
}

PNod Nod::stanga() {
	return this->st;
}

PNod Nod::dreapta() {
	return this->dr;
}

Multime::Multime() {
	rad = nullptr;
	//h = 0;
	dimensiune = 0;
}

//PNod Multime::minim(PNod p) {
//	while (p->st != nullptr) {
//		p = p->st;
//	}
//	return p;
//}

//adaugarea recursiva a unui element
PNod Multime::adauga_rec(PNod p, TElem e) {
	if (p == nullptr) {
		p = new Nod(e, nullptr, nullptr);
	}
	else {
		if (rel(e, p->e)) //se adauga in stanga
			p->st = adauga_rec(p->st, e);
		else //se adauga in dreapta
			p->dr = adauga_rec(p->dr, e);
	}
	return p;
}

void Multime::distrug_rec(PNod p) {
	if (p != nullptr) {
		distrug_rec(p->stanga());
		distrug_rec(p->dreapta());
		delete p;
	}
}

bool Multime::adauga(TElem elem) {
	/* */
	if(cauta(elem))
		return false;
	rad = adauga_rec(rad, elem);
	this->dimensiune++;
	return true;
}

//PNod Multime::sterge_rec(PNod p, TElem e) {
//	PNod temp;
//	PNod nodNou;
//
//	if (p == nullptr)
//		return nullptr;
//	else {
//		if (rel(e, p->e)) {
//			p->st = sterge_rec(p->st, e);
//			return p;
//		}
//		else {
//			if (p->st != nullptr && p->dr != nullptr) { // nodul are si subarbore stang si drept
//				temp = minim(p->dr);
//				p->e = temp->e;		// mutam cheia minima in p
//				p->dr = sterge_rec(p->dr, p->e);
//				return p;
//			}
//			else {
//				temp = p;
//				if (p->st == nullptr) // nu exista subarbore stang
//					nodNou = p->dr;
//				else //nu exista subarbore drept
//					nodNou = p->st;
//			}
//			delete temp;
//			return nodNou;
//		}
//	}
//}

bool Multime::sterge(TElem elem) {
	/* O(h) */
	if (!cauta(elem))
		return false;
	this->dimensiune--;
	PNod curent = this->rad;
	if (curent->e == elem) { //sterge radacina 
		PNod stanga = this->rad->st;	//stanga sunt nodurile din stanga radacinii
		this->rad = this->rad->dr;		//radacina devine nodul din dreapta
		delete curent;	
		if (this->dimensiune == 0)	//am avut doar radacina si am sters o
			return true;
		curent = this->rad;	
		while (curent->st != nullptr) {	//punem nodurile din stanga in stanga jos de la noua radacina
			curent = curent->st;
		}
		curent->st = stanga;
		return true;
	}
	else { // sterge alt nod
		PNod prev = curent;
		while (curent->e != elem) {		//cautam elementul care urmeaza sa fie sters si salvam in prev anteriorul lui
			prev = curent;	
			if (rel(elem, curent->e))
				curent = curent->st;
			else
				curent = curent->dr;
		}
		PNod stanga = curent->st;	//stanga nodului care urmeaza sa fie sters
		PNod dreapta = curent->dr;	// dreapta nodului care urmeaza sa fie sters
		if (stanga == nullptr && dreapta == nullptr) { // daca nodul e frunza
			if (prev->st != nullptr) {	// daca frunza e in stanga anteriorului se face nullptr
				if (curent->e == prev->st->e)
				prev->st = nullptr;
			}
			else // sau daca e in dreapta se face nullptr
				prev->dr = nullptr;
			delete curent;
			return true;
		}
		delete curent;
		if (dreapta == nullptr) {
			prev->st = stanga;
			return true;
		}
		while (dreapta->st != nullptr) {
			dreapta = dreapta->st;
		}
		prev->st = dreapta;		// daca nodul are fii si in stanga i in dreapta cei din dreapta se leaga mai intai de predecesorul nodului, iar pe urma cei din stanga
		dreapta->st = stanga;
		return true;
	}
}


bool Multime::cauta(TElem elem) const {
	/* O(h) */
	if (this->dimensiune == 0)
		return false;
	PNod p = this->rad;
	while (p != nullptr && p->e != elem) {
		if (rel(elem, p->e))
			p = p->st;
		else p = p->dr;
		/*if (p == nullptr)
			break;
		if (p->dr == nullptr && p->st == nullptr)
			break;*/
	}
	if (p == nullptr)
		return false;
	if (p->e == elem)
		return true;
	return false;

}


int Multime::dim() const {
	/* Theta(1) */
	return this->dimensiune;
}



bool Multime::vida() const {
	/* Theta(1) */
	if(this->dimensiune == 0)
		return true;
	return false;
}

IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}


Multime::~Multime() {
	distrug_rec(rad);
}



int Multime::diferenta(const Multime& b) {
	int nr = 0;
	//int size = b.dim();
	TElem e;
	IteratorMultime im = b.iterator();
	im.prim();
	
	while (im.valid()) {
		e = im.element();
		//cout << e <<" ";
		if (cauta(e) == true) {
			nr++;
			sterge(e);
		}
		im.urmator();
	}
	return nr;
}


