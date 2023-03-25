#include "IteratorMultime.h"

#include <exception>

using namespace std;


IteratorMultime::IteratorMultime(const Multime& m) : multime(m) {
	curent = 0;
	ant = 0;

	deplasare();
	
}

void IteratorMultime::deplasare() {
	// O(m)
	while ((curent < multime.m) && multime.e[curent] == INIT)
		curent++;
}


void IteratorMultime::prim() {
	// O(m)
	curent = 0;
	ant = curent;
	deplasare();
}


void IteratorMultime::urmator() {
	// O(m)
	if (!valid())
		throw(exception());
	ant = curent;
	curent++;
	deplasare();
}


TElem IteratorMultime::element() const {
	// Theta(1)
	if (!valid())
		throw(exception());
	return multime.e[curent];
}

bool IteratorMultime::valid() const {
	// Theta(1)
	if (curent < multime.m)
		return true;
	return false;
}

void IteratorMultime::anterior() {
	// Theta(1)
	if (!valid())
		throw(exception());
	curent = ant;
}

