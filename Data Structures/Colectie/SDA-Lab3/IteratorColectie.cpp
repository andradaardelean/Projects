#include "IteratorColectie.h"
#include "Colectie.h"


IteratorColectie::IteratorColectie(const Colectie& c) : col(c) {
	/* Theta(1) */
	curent = c.prim;
}

TElem IteratorColectie::element() const {
	/* Theta(1) */
	return curent->element();
}

bool IteratorColectie::valid() const {
	/* Theta(1) */
	if(curent == nullptr)
		return false;
	return true;
}

void IteratorColectie::urmator() {
	/* Theta(1) */
	curent = curent->urmator();
}

void IteratorColectie::prim() {
	/* Theta(1) */
	curent = col.prim;
}
