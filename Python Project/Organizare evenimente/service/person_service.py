import string
from random import *

from domain.entities import Persoana
from domain.validators import ValidatorPersoana
from repository.person_repo import *


class ServicePersoana:
    def __init__(self, repo_pers, validator_pers):
        """
        Initializeaza un obiect de tip ServicePersoana
        :param repo_pers:
        :type repo_pers: InMemoryRepository
        :param validator_pers:
        :type validator_pers: ValidatorPersoana
        """
        self.__repo_pers = repo_pers
        self.__validator_pers = validator_pers

    def generate_persons(self):
        """
        Generam cateva persoane.
        :return:
        :raises: ValueError daca serialul are date invalide
        """
        person = Persoana(24, 'Ardelean Andrada', 'Str. Lucian Blaga, nr.201')
        self.__validator_pers.validate(person)
        self.__repo_pers.store(person)

        person = Persoana(10, 'Stan David', 'Str. Vasile Lucaciu, nr.25')
        self.__validator_pers.validate(person)
        self.__repo_pers.store(person)

        person = Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115')
        self.__validator_pers.validate(person)
        self.__repo_pers.store(person)

        person = Persoana(13, 'Chifor Sandra', 'Bd. Closca, nr. 181')
        self.__validator_pers.validate(person)
        self.__repo_pers.store(person)

        person = Persoana(66, 'Serghie Alex', 'Str. Noroieni, nr.92')
        self.__validator_pers.validate(person)
        self.__repo_pers.store(person)

    def add_person(self, id, nume, adresa):
        """
        Adauga persoana la lista din repo.
        :param id: id-ul persoanei
        :param nume: numele persoanei
        :param adresa: adresa persoanei
        :return:
        :raises: ValueError daca serialul are date invalide
        """
        person = Persoana(id, nume, adresa)

        self.__validator_pers.validate(person)
        self.__repo_pers.store(person)

    def get_all_persons(self):
        return self.__repo_pers.get_all_persons()

    def validatorID(self, id, comand):
        """
        Verifica daca ID-ul introdus este unic sau mai apare undeva.
        :param id: id-ul persoanei
        :type id: int
        :param comand: comanda pentru care se verifica
        :type comand: string
        :return:
        :raises: Un text daca cmd e add si ID ul ii apartine deja unei persoane
                alt text daca cmd e delete sau update si ID-ul nu este in lista
        """
        self.__repo_pers.validatorID(id,comand)

    def find_person(self,value,poz):
        """
        Cauta persoana in lista dupa criteriile value si poz.
        :param value: valoarea care se cauta in lista
        :type value: string
        :param poz: tipul valorii value, 0 = id, 1 = nume, 2 = adresa
        :type poz: int
        :return: lista cu persoanele gasite
        """
        if poz == 0:
            self.__validator_pers.validate_IDpersoana(value)
            return [el for el in self.__repo_pers.get_all_persons() if el.getIDpersoana() == value]
        elif poz == 1:
            self.__validator_pers.validate_Nume(value)
            return [el for el in self.__repo_pers.get_all_persons() if el.getNume() == value]
        elif poz == 2:
            self.__validator_pers.validate_Adresa(value)
            return [el for el in self.__repo_pers.get_all_persons() if el.getAdresa() == value]

    def delete_person(self,id):
        """
        Sterge persoana din lista.
        :param id: id-ul persoanei
        :type id: int
        :return: lista de persoane dupa stergerea unei pers
        """
        self.__validator_pers.validate_IDpersoana(id)
        # person = self.__repo_pers.find_person(id)
        person = self.__repo_pers.find_person(id,0)

        new_person_list = self.__repo_pers.delete_person(person)
        return new_person_list

    def update_person(self, id, nume, adresa):
        """
        Modifica datele unei persoane.
        :param id: id-ul persoanei
        :type id: int
        :param nume: numele persoanei
        :type nume: string
        :param adresa: adresa persoanei
        :type adresa: string
        :return: lista dupa actualizarea persoanei.
        """

        self.__validator_pers.validate_IDpersoana(id)
        # person = self.__repo_pers.find_person(id)
        person = self.__repo_pers.find_person(id,0)

        # print(person.getIDpersoana(), person.getNume())
        person_update = Persoana(id,nume,adresa)
        new_person_list = self.__repo_pers.update_person(person, person_update)
        return new_person_list

    def random_string_person(self, length):
        """
        Genereaza un sir random de lungimea length.
        :param length: lungimea sirului
        :return: sirul
        """
        return ''.join(choice(string.ascii_lowercase) for i in range(length))

def test_ServicePersoana_add_person():
    repo = InMemoryRepositoryPers()
    validator = ValidatorPersoana()
    test_srv = ServicePersoana(repo, validator)

    test_srv.add_person(1, 'Andrada', 'Str. Carei')
    assert (test_srv.get_all_persons()[0].getIDpersoana() == 1)
    assert (test_srv.get_all_persons()[0].getNume() == 'Andrada')
    assert (len(test_srv.get_all_persons()) == 1)

    try:
        test_srv.add_person(1, 'An', 'Str. Carei')
        assert False
    except ValueError:
        assert True

def test_ServicePersoana_get_all_persons():
    repo = InMemoryRepositoryPers()
    validator = ValidatorPersoana()
    test_srv = ServicePersoana(repo, validator)

    test_srv.add_person(1, 'Andrada', 'Str. Carei')
    test_srv.add_person(2, 'David', 'Str. Carei')
    assert (type(test_srv.get_all_persons()) == list)
    assert (len(test_srv.get_all_persons()) == 2)

def test_ServicePersoana_ValidatorID():
    repo = InMemoryRepositoryPers()
    validator = ValidatorPersoana()
    test_srv = ServicePersoana(repo, validator)
    test_srv.add_person(1, 'Andrada', 'Str. Carei')

    try:
        test_srv.validatorID(1,'add')
        assert False
    except ValueError:
        assert True

    try:
        test_srv.validatorID(2, 'delete')
        assert False
    except ValueError:
        assert True

    try:
        test_srv.validatorID(3, 'update')
        assert False
    except ValueError:
        assert True

def test_ServicePersoana_find_person():
    repo = InMemoryRepositoryPers()
    validator = ValidatorPersoana()
    test_srv = ServicePersoana(repo, validator)

    test_srv.add_person(1, 'Andrada', 'Str. Carei')
    test_srv.add_person(2, 'David', 'Str. Carei')
    test_srv.add_person(3, 'Andrada', 'Str. Carei')

    try:
        test_srv.find_person(-5,0)
        assert False
    except ValueError:
        assert True

    try:
        test_srv.find_person('A',1)
        assert False
    except ValueError:
        assert True

    pers_gasite = test_srv.find_person('Andrada', 1)
    assert(len(pers_gasite) == 2)
    assert (pers_gasite[0].getIDpersoana() == 1)
    assert (pers_gasite[1].getIDpersoana() == 3)

    pers_gasite = test_srv.find_person('Str. Carei',2)
    assert(len(pers_gasite) == 3)

def test_ServicePersoana_delete_person():
    repo = InMemoryRepositoryPers()
    validator = ValidatorPersoana()
    test_srv = ServicePersoana(repo, validator)
    test_srv.add_person(1, 'Andrada', 'Str. Carei')
    test_srv.add_person(2, 'David', 'Str. Carei')

    assert (len(test_srv.get_all_persons()) == 2)

    test_srv.delete_person(1)
    assert (len(test_srv.get_all_persons()) == 1)

    test_srv.delete_person(2)
    assert (len(test_srv.get_all_persons()) == 0)

def test_ServicePersoana_update_person():
    repo = InMemoryRepositoryPers()
    validator = ValidatorPersoana()
    test_srv = ServicePersoana(repo, validator)
    test_srv.add_person(1, 'Andrada', 'Str. Carei')
    test_srv.add_person(2, 'David', 'Str. Carei')

    test_srv.update_person(1,'Alexandra', 'str. Cernei')
    assert (test_srv.get_all_persons()[0].getNume() == 'Alexandra')
    assert (test_srv.get_all_persons()[0].getAdresa() == 'str. Cernei')

# test_ServicePersoana_add_person()
# test_ServicePersoana_get_all_persons()
# test_ServicePersoana_ValidatorID()
# test_ServicePersoana_find_person()
# test_ServicePersoana_delete_person()
# test_ServicePersoana_update_person()

