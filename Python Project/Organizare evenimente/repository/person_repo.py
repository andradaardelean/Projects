from termcolor import colored

from domain.entities import Persoana


class InMemoryRepositoryPers:
    def __init__(self):
        self.__person_list = []

    def store(self, persoana):
        self.__person_list.append(persoana)

    def get_all_persons(self):
        return self.__person_list

    def find_person(self, id):
        """
        Gaseste persoana cu un anumit ID.
        :param id: id-ul persoanei
        :return: persoana cu id-ul respectiv
        """
        for person in self.__person_list:
            if Persoana.getIDpersoana(person) == id:
                return person
        return None

    def validatorID(self, id, comand):
        """
        Verifica daca o persoana cu acest ID se gaseste deja in lista si returneaza eroarea in functie de caz.
        :param id: id-ul persoanei
        :type id: int
        :param comand: comanda
        :type comand: string
        :return:
        :raises: un text daca ID -ul e in lista, si alt text daca nu e.
        """
        id_list = [person for person in self.__person_list if Persoana.getIDpersoana(person) == id]
        errors = []
        if id_list != [] and comand == 'add':
            errors.append('Exista deja persosna cu acest ID.')
        elif id_list == []:
            if comand == 'delete' or comand == 'update' or comand == 'else':
                errors.append('Nu exista persoana cu acest ID in lista.')
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def size(self):
        """
        Returneaza numarul de persoane din lista.
        :return:
        """
        return len(self.get_all_persons())

    def delete_person(self, person):
        """
        Sterge o persoana din lista.
        :param person: persoana
        :type person: list
        :return: lista de persoane dupa stergerea persoanei date
        """
        index = 0
        for pers in self.__person_list:
            if Persoana.getIDpersoana(person) == Persoana.getIDpersoana(pers):
                self.__person_list.pop(index)
            index += 1
        return self.__person_list

    def update_person(self, person, person_update):
        """
        Modifica persoana din lista.
        :param person: persoana
        :type person: string
        :param person_update: persoana cu care se modifica
        :type person_update: string
        :return: lista de persoane dupa modificarea unei pers
        """
        index = 0
        for pers in self.__person_list:
            if Persoana.getIDpersoana(person) == Persoana.getIDpersoana(pers):
                self.__person_list[index] = person_update
            index += 1
        return self.__person_list

    def delete_all(self):
        self.__person_list = []


def test_InMemoryRepositoryPers_store():
    test_repo = InMemoryRepositoryPers()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    test_repo.store(person1)
    test_repo.store(person2)

    assert (len(test_repo.get_all_persons()) == 2)
    assert (test_repo.get_all_persons()[0].getIDpersoana() == 1)
    assert (test_repo.get_all_persons()[1].getIDpersoana() == 2)
    assert (test_repo.get_all_persons()[0].getNume() == 'Ardelean Andrada')
    assert (test_repo.get_all_persons()[1].getNume() == 'Acas George')


def test_InMemoryRepositoryPers_find_person():
    test_repo = InMemoryRepositoryPers()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    test_repo.store(person1)
    test_repo.store(person2)
    id = 2
    person = test_repo.find_person(id)
    assert (person.getNume() == 'Acas George')
    assert (person.getAdresa() == 'Bd. Libertatii')


def test_InMemoryRepositoryPers_ValidatorID():
    test_repo = InMemoryRepositoryPers()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    person3 = Persoana(3, 'Toth Maria', 'Bd. Lucian Blaga')

    test_repo.store(person1)
    test_repo.store(person2)
    test_repo.store(person3)
    id = 2
    cmd = 'add'
    try:
        test_repo.validatorID(id, cmd)
        assert False
    except ValueError:
        assert True

    id = 3
    try:
        test_repo.validatorID(id, cmd)
        assert False
    except ValueError:
        assert True


def test_InMemoryRepositoryPers_delete_person():
    test_repo = InMemoryRepositoryPers()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    person3 = Persoana(3, 'Toth Maria', 'Bd. Lucian Blaga')
    test_repo.store(person1)
    test_repo.store(person2)
    test_repo.store(person3)

    person_list = test_repo.delete_person(person1)

    assert (len(person_list) == 2)
    assert (test_repo.get_all_persons()[0].getIDpersoana() == 2)
    assert (test_repo.get_all_persons()[1].getIDpersoana() == 3)


def test_InMemoryRepositoryPers_update_person():
    test_repo = InMemoryRepositoryPers()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    person3 = Persoana(3, 'Toth Maria', 'Bd. Lucian Blaga')
    test_repo.store(person1)
    test_repo.store(person2)
    test_repo.store(person3)
    person_update = Persoana(5, 'Tatar Alex', 'Bd. Vasile Lucaciu')
    person_list = test_repo.update_person(person1, person_update)

    assert (len(person_list) == 3)
    assert (test_repo.get_all_persons()[0].getIDpersoana() == 5)
    assert (test_repo.get_all_persons()[0].getNume() == 'Tatar Alex')
    assert (test_repo.get_all_persons()[0].getAdresa() == 'Bd. Vasile Lucaciu')


# test_InMemoryRepositoryPers_store()
# test_InMemoryRepositoryPers_find_person()
# test_InMemoryRepositoryPers_delete_person()
# test_InMemoryRepositoryPers_update_person()
# test_InMemoryRepositoryPers_ValidatorID()


class FileRepositoryPers:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        """
        Incarca datele din fisier.
        :return: lista de persoane din fisier
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        lines = f.readlines()
        person_list = []

        # for line in lines:
        #     if len(line) > 2:
        #         id_person, nume, adresa = [token.strip() for token in line.split(';')]
        #         id_person = int(id_person)
        #
        #         person = Persoana(id_person, nume, adresa)
        #         person_list.append(person)

        for i in range(0, len(lines)-1, 3):
            new_line = lines[i:i+3]
            id_person, nume, adresa = new_line
            id_person = id_person.replace('\n','')
            id_person = int(id_person)
            nume = nume.replace('\n','')
            adresa = adresa.replace('\n','')
            person = Persoana(id_person, nume, adresa)
            person_list.append(person)

        # for person in person_list:
        #     print(person.getIDpersoana(), person.getNume(), person.getAdresa())

        f.close()
        return person_list

    def save_to_file(self, person_list):
        """
        Salveaza persoanele in fisier.
        :param person_list: lista de persoane din fisier
        :return:
        """
        with open(self.__filename, 'w') as f:
            for person in person_list:
                # person_string = str(person.getIDpersoana()) + ';' + str(person.getNume()) + ';' + str(
                #     person.getAdresa()) + '\n'
                person_string = str(person.getIDpersoana()) + '\n' + str(person.getNume()) + '\n' + str(person.getAdresa()) + '\n'
                f.write(person_string)

    # def find_person(self, id):
    #     """
    #     Cauta persoana in functie de id.
    #     :param id: id-ul persoanei
    #     :return: persoana cautata
    #     """
    #     person_list = self.load_from_file()
    #     for person in person_list:
    #         if person.getIDpersoana() == id:
    #             # print(person)
    #             return person
    #     return None

    def find_person(self, id, index):
        """
        Cauta persoana in functie de id.
        :param id: id-ul persoanei
        :return: persoana cautata
        """
        person_list = self.load_from_file()
        n = len(person_list)
        if person_list[index].getIDpersoana() == id:
            return person_list[index]
        elif index == n:
            return None
        else:
            return self.find_person(id, index+1)

    # Caz favorabil: - persoana cautata se afla pe prima pozitie
    #     T(n) = 1
    #
    # Caz defavorabil: - persoana cautata se afla pe ultima pozitie
    #     T(n) = n-1
    #
    # Caz mediu: - persoana se afla pe una dintre pozitiile dintre 1 si n
    #     T(id, index+1) = 1 + T(id, index+2)
    #     T(id, index+3) = 1 + T(id, index+4)
    #     ...
    #     T(id, index+n-1) = 1 + T(n) = 1 + 0
    #    -> T(n) = n-1-1 = n-2
    #
    # Overall complexity = O(n)


    def store(self, person):
        """
        Adauga o persoana in fisierul care contine lista de persoane.
        :param person: persoana care urmeaza sa fie adaugata
        :return: - ; lista de persoane se modifica
        """
        person_list = self.load_from_file()
        if person in person_list:
            raise ValueError("Persoana exista deja in lista")

        person_list.append(person)
        self.save_to_file(person_list)

    def validatorID(self, id, cmd):
        """
        Valideaza id-ul unei persoane.
        :param id: id-ul. persoanei
        :return:
        :raises: ValueError daca id-ul se afla in lista sau nu.
        """
        person_list = self.load_from_file()
        pers_with_id = [person for person in person_list if person.getIDpersoana() == id]
        errors = []

        if pers_with_id != [] and cmd == 'add':
            errors.append("Persoana cu acest ID se gaseste deja in lista")
        elif pers_with_id == []:
            if cmd == 'delete' or cmd == 'update' or cmd == 'else':
                errors.append("Nu se gaseste persoana cu acest ID in lista.")

        if len(errors) != 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def get_all_persons(self):
        """
        Returneaza lista cu persoanele din fisier.
        :return:
        """
        return self.load_from_file()

    def size(self):
        """
        Returneaza numarul de persoane din lista.
        :return:
        """
        return len(self.load_from_file())

    def delete_person(self, person):
        """
        Sterge persoana din lista.
        :param person:
        :return:
        """
        person_list = self.load_from_file()
        index = 0
        for pers in person_list:
            if Persoana.getIDpersoana(pers) == Persoana.getIDpersoana(person):
                person_list.pop(index)
            index += 1

        self.save_to_file(person_list)
        return self.load_from_file()

    def update_person(self, person, updated_person):
        """
        Modifica persoana din lista.
        :param person: persoana care trebuie modificata
        :param updated_person: persoana cu care trebuie modificata
        :return: lista modificata
        """
        person_list = self.load_from_file()
        index = 0
        for pers in person_list:
            if Persoana.getIDpersoana(person) == Persoana.getIDpersoana(pers):
                person_list[index] = updated_person
            index += 1

        self.save_to_file(person_list)
        return self.load_from_file()

    def delete_all(self):
        self.save_to_file([])
