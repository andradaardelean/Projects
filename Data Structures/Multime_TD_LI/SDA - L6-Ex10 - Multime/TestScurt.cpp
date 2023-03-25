#include "TestScurt.h"
#include <assert.h>
#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>

void testAll() { //apelam fiecare functie sa vedem daca exista
	Multime m;
	assert(m.vida() == true);
	assert(m.dim() == 0); //adaug niste elemente
	assert(m.adauga(5) == true);
	assert(m.adauga(1) == true);
	assert(m.adauga(10) == true);
	assert(m.adauga(7) == true);
	assert(m.adauga(1) == false);
	assert(m.adauga(10) == false);
	assert(m.adauga(-3) == true);
	assert(m.dim() == 5);
	assert(m.cauta(10) == true);
	assert(m.cauta(16) == false);
	assert(m.sterge(1) == true);
	assert(m.sterge(6) == false);
	assert(m.dim() == 4);

	//assert(m.cauta(-1) == false);


	IteratorMultime im = m.iterator();
	im.prim();
	int s = 0;
	while (im.valid()) {
		TElem e = im.element();
		s += e;
		im.urmator();
	}
	//std::cout << s;
	assert(s == 19);

}

void testIt() {
	Multime m1;
	IteratorMultime im1 = m1.iterator();

	m1.adauga(1);
	m1.adauga(4);

	assert(im1.element() == 4);
	im1.anterior();
	assert(im1.element() == 1);
}
