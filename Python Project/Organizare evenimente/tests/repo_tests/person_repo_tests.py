import unittest

from domain.entities import Persoana
from repository.person_repo import InMemoryRepositoryPers, FileRepositoryPers


class TestCasePersonRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InMemoryRepositoryPers()

        person1 = Persoana(24, 'Ardelean Andrada', 'Str. Lucian Blaga, nr.201')
        person2 = Persoana(10, 'Stan David', 'Str. Vasile Lucaciu, nr.25')
        person3 = Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115')
        person4 = Persoana(13, 'Chifor Sandra', 'Bd. Closca, nr. 181')
        person5 = Persoana(66, 'Serghie Alex', 'Str. Noroieni, nr.92')

        self.__repo.store(person1)
        self.__repo.store(person2)
        self.__repo.store(person3)
        self.__repo.store(person4)
        self.__repo.store(person5)

    def test_store(self):
        initial_size = self.__repo.size()
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        self.__repo.store(person1)
        self.assertEqual(self.__repo.size(), initial_size + 1)

        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        self.__repo.store(person2)
        self.assertEqual(self.__repo.size(), initial_size + 2)

        pers_list = self.__repo.get_all_persons()
        self.assertEqual(pers_list[initial_size].getIDpersoana(), 1)
        self.assertEqual(pers_list[initial_size + 1].getIDpersoana(), 2)

    def test_find(self):
        person = self.__repo.find_person(7)

        self.assertEqual(person.getNume(), 'Ripan George')
        self.assertEqual(person.getAdresa(), 'Str. Crizantemelor, nr.115')

        person = self.__repo.find_person(100)
        self.assertIs(person, None)

    def test_ValidatorID(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        person3 = Persoana(3, 'Toth Maria', 'Bd. Lucian Blaga')

        self.__repo.store(person1)
        self.__repo.store(person2)
        self.__repo.store(person3)

        with self.assertRaises(ValueError):
            self.__repo.validatorID(1,'add')

        with self.assertRaises(ValueError):
            self.__repo.validatorID(3,'add')

    def test_size(self):
        initial_size = self.__repo.size()
        person1 = Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115')
        person2 = Persoana(66, 'Serghie Alex', 'Str. Noroieni, nr.92')
        self.__repo.delete_person(person1)
        self.__repo.delete_person(person2)

        self.assertEqual(self.__repo.size(), initial_size - 2)

        self.__repo.store(person1)
        self.assertEqual(self.__repo.size(), initial_size - 1)
        self.__repo.update_person(person1, person2)
        self.assertEqual(self.__repo.size(), initial_size - 1)

    def test_delete_person(self):
        initial_size = self.__repo.size()
        person = self.__repo.find_person(7)
        person_list = self.__repo.delete_person(person)

        self.assertTrue(len(person_list) == initial_size - 1)

        person2 = Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115')
        self.__repo.store(person2)

        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        self.__repo.store(person1)

        person = self.__repo.find_person(1)
        person_list = self.__repo.delete_person(person)
        self.assertEqual(len(person_list), initial_size)

    def test_update_person(self):
        initial_size = self.__repo.size()
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        self.__repo.store(person1)
        self.__repo.store(person2)

        person_update = Persoana(5, 'Tatar Alex', 'Bd. Vasile Lucaciu')
        person_list = self.__repo.update_person(person1, person_update)

        self.assertEqual(self.__repo.size(), initial_size + 2)
        self.assertTrue(person_list[initial_size].getIDpersoana() == 5)
        self.assertTrue(person_list[initial_size].getNume() == 'Tatar Alex')
        self.assertTrue(person_list[initial_size].getAdresa() == 'Bd. Vasile Lucaciu')

    def tearDown(self) -> None:
        self.__repo.delete_all()

class TestCasePersonRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = FileRepositoryPers('test_pers_repo.txt')
        self.__repo.delete_all()
        self.populate_list()

    def populate_list(self):
        person1 = Persoana(24, 'Ardelean Andrada', 'Str. Lucian Blaga, nr.201')
        person2 = Persoana(10, 'Stan David', 'Str. Vasile Lucaciu, nr.25')
        person3 = Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115')
        person4 = Persoana(13, 'Chifor Sandra', 'Bd. Closca, nr. 181')
        person5 = Persoana(66, 'Serghie Alex', 'Str. Noroieni, nr.92')

        self.__repo.store(person1)
        self.__repo.store(person2)
        self.__repo.store(person3)
        self.__repo.store(person4)
        self.__repo.store(person5)

    def test_find(self):
        p = self.__repo.find_person(24)
        self.assertTrue(p.getNume() == 'Ardelean Andrada')
        self.assertTrue(p.getAdresa() == 'Str. Lucian Blaga, nr.201')

        p1 = self.__repo.find_person(100)
        self.assertIs(p1, None)

    def test_store(self):
        #Black Box
        initial_size = self.__repo.size()
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        self.__repo.store(person1)
        self.assertEqual(self.__repo.size(), initial_size + 1)

        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        self.__repo.store(person2)
        self.assertEqual(self.__repo.size(), initial_size + 2)

        pers_list = self.__repo.get_all_persons()
        self.assertEqual(pers_list[initial_size].getIDpersoana(), 1)
        self.assertEqual(pers_list[initial_size + 1].getIDpersoana(), 2)

    def test_ValidatorID(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        person3 = Persoana(3, 'Toth Maria', 'Bd. Lucian Blaga')

        self.__repo.store(person1)
        self.__repo.store(person2)
        self.__repo.store(person3)

        with self.assertRaises(ValueError):
            self.__repo.validatorID(1, 'add')

        with self.assertRaises(ValueError):
            self.__repo.validatorID(3, 'add')

    def test_get_all_persons(self):
        #White Box
        initial_size = self.__repo.size()
        crt_persons = self.__repo.get_all_persons()
        self.assertIsInstance(crt_persons, list)

        self.assertEqual(len(crt_persons), initial_size)

        person1 = self.__repo.find_person(7)
        self.__repo.delete_person(person1)
        person2 = self.__repo.find_person(66)
        self.__repo.delete_person(person2)

        crt_persons = self.__repo.get_all_persons()
        self.assertEqual(len(crt_persons), initial_size - 2)

        self.__repo.store(Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115'))
        self.assertEqual(self.__repo.size(), initial_size - 1)

        self.__repo.store(Persoana(66, 'Serghie Alex', 'Str. Noroieni, nr.92'))
        self.assertEqual(self.__repo.size(), initial_size)

    def test_size(self):
        initial_size = self.__repo.size()
        self.__repo.delete_person(Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115'))
        self.__repo.delete_person(Persoana(66, 'Serghie Alex', 'Str. Noroieni, nr.92'))

        self.assertEqual(self.__repo.size(), initial_size - 2)

        self.__repo.store(Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115'))
        self.assertEqual(self.__repo.size(), initial_size - 1)
        self.__repo.update_person(Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115'),
                                  Persoana(66, 'Serghie Alex', 'Str. Noroieni, nr.92'))
        self.assertEqual(self.__repo.size(), initial_size - 1)

    def test_delete_person(self):
        initial_size = self.__repo.size()
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        self.__repo.store(person1)
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        self.__repo.store(person2)
        self.__repo.delete_person(person1)
        person_list = self.__repo.delete_person(person1)

        self.assertTrue(len(person_list) == initial_size + 1)

        person_list = self.__repo.delete_person(person2)
        self.assertTrue(len(person_list) == initial_size)

        pers = self.__repo.find_person(1)
        self.assertIs(pers, None)

        pers = self.__repo.find_person(2)
        self.assertIs(pers, None)

    def test_update(self):
        initial_size = self.__repo.size()
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        self.__repo.store(person1)
        self.__repo.store(person2)

        person_update = Persoana(5, 'Tatar Alex', 'Bd. Vasile Lucaciu')
        person_list = self.__repo.update_person(person1, person_update)

        self.assertEqual(self.__repo.size(), initial_size + 2)
        self.assertTrue(person_list[initial_size].getIDpersoana() == 5)
        self.assertTrue(person_list[initial_size].getNume() == 'Tatar Alex')
        self.assertTrue(person_list[initial_size].getAdresa() == 'Bd. Vasile Lucaciu')

    def tearDown(self) -> None:
        self.__repo.delete_all()