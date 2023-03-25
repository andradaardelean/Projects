import unittest

from domain.entities import Persoana
from domain.validators import ValidatorPersoana
from repository.person_repo import InMemoryRepositoryPers
from service.person_service import ServicePersoana


class TestCasePersonService(unittest.TestCase):
    def setUp(self):
        repo = InMemoryRepositoryPers()
        validator = ValidatorPersoana()
        self.__srv = ServicePersoana(repo, validator)

    def test_add_person(self):
        self.__srv.add_person(1, 'Andrada', 'Str. Carei')
        self.assertTrue (self.__srv.get_all_persons()[0].getIDpersoana() == 1)
        self.assertTrue (self.__srv.get_all_persons()[0].getNume() == 'Andrada')
        self.assertTrue (len(self.__srv.get_all_persons()) == 1)

        with self.assertRaises(ValueError):
            self.__srv.add_person(1, 'An', 'Str. Carei')

    def test_get_all_persons(self):
        self.__srv.add_person(1, 'Andrada', 'Str. Carei')
        self.__srv.add_person(2, 'David', 'Str. Carei')
        self.assertTrue (type(self.__srv.get_all_persons()) == list)
        self.assertTrue (len(self.__srv.get_all_persons()) == 2)

    def test_ValidatorID(self):
        self.__srv.add_person(1, 'Andrada', 'Str. Carei')

        with self.assertRaises(ValueError):
            self.__srv.validatorID(1,'add')

        with self.assertRaises(ValueError):
            self.__srv.validatorID(2, 'delete')

        with self.assertRaises(ValueError):
            self.__srv.validatorID(3, 'update')

    def test_find_person(self):
        self.__srv.add_person(1, 'Andrada', 'Str. Carei')
        self.__srv.add_person(2, 'David', 'Str. Carei')
        self.__srv.add_person(3, 'Andrada', 'Str. Carei')

        pers_gasite = self.__srv.find_person('Andrada', 1)
        self.assertTrue (len(pers_gasite) == 2)
        self.assertTrue (pers_gasite[0].getIDpersoana() == 1)
        self.assertTrue (pers_gasite[1].getIDpersoana() == 3)

        pers_gasite = self.__srv.find_person('Str. Carei', 2)
        self.assertTrue (len(pers_gasite) == 3)

    def test_delete_person(self):
        self.__srv.add_person(1, 'Andrada', 'Str. Carei')
        self.__srv.add_person(2, 'David', 'Str. Carei')

        self.assertTrue (len(self.__srv.get_all_persons()) == 2)

        self.__srv.delete_person(1)
        self.assertTrue (len(self.__srv.get_all_persons()) == 1)

        self.__srv.delete_person(2)
        self.assertTrue (len(self.__srv.get_all_persons()) == 0)

    def test_update_person(self):
        self.__srv.add_person(1, 'Andrada', 'Str. Carei')
        self.__srv.add_person(2, 'David', 'Str. Carei')

        self.__srv.update_person(1, 'Alexandra', 'str. Cernei')
        self.assertTrue (self.__srv.get_all_persons()[0].getNume() == 'Alexandra')
        self.assertTrue (self.__srv.get_all_persons()[0].getAdresa() == 'str. Cernei')




