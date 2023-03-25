#include "IteratorMultime.h"
#include "Multime.h"


IteratorMultime::IteratorMultime(const Multime& m) : mult(m) {
	/* O(h) */
	if (mult.dim() == 0) {
		this->curent = nullptr;
		return;
	}
	this->curent = mult.rad;
	while (this->curent->stanga() != nullptr) {	// initializez curentul cu cel mai din stanga nod
		this->stack.push(this->curent);
		this->curent = this->curent->stanga();
	}
}

TElem IteratorMultime::element() const {
	/*  */
	if (!valid())
		throw exception();
	return this->curent->element();
}

bool IteratorMultime::valid() const {
	/*  */
	return this->curent != nullptr;
}

void IteratorMultime::urmator() {
	/* de adaugat */
	if (!this->valid())
		throw exception();
	if (this->curent->dreapta() != nullptr) {
		this->curent = this->curent->dreapta();
		while (this->curent->stanga() != nullptr) {
			this->stack.push(this->curent);
			this->curent = this->curent->stanga();
		}
	}
	else if (!stack.empty()) {
		this->curent = this->stack.top();
		this->stack.pop();
	}
	else
		this->curent = nullptr;
}

void IteratorMultime::prim() {
	/* de adaugat */
	if (mult.dim() == 0) {
		this->curent = nullptr;
		return;
	}
	while (!this->stack.empty())
		this->stack.pop();
	this->curent = mult.rad;
	while (this->curent->stanga() != nullptr) {
		this->stack.push(this->curent);
		this->curent = this->curent->stanga();
	}
}

