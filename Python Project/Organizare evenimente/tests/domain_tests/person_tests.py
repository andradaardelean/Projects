import unittest

from domain.entities import Persoana
from domain.validators import ValidatorPersoana


class TestCasePersonDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = ValidatorPersoana()

    def test_create_person(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')

        self.assertEqual(person1.getIDpersoana(), 1)
        self.assertEqual(person1.getNume(), 'Ardelean Andrada')
        self.assertEqual(person1.getAdresa(), 'Bd. Independentei')

    def test_equals_person(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')

        self.assertEqual(person1, person2)

    def test_ValidatorPersoana(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        self.__validator.validate(person1)

        person2 = Persoana(2, '', 'Bd. Lucian Blaga')
        person3 = Persoana(-2, 'Andrada', '')

        self.assertRaises(ValueError, self.__validator.validate, person2)
        self.assertRaises(ValueError, self.__validator.validate, person3)

    def test_ValidatorPersoana_IDpersoana(self):
        person1 = Persoana(-5, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(20000, 'Ardelean Andrada', 'Bd. Independentei')


        self.assertRaises(ValueError, self.__validator.validate, person1)
        self.assertRaises(ValueError, self.__validator.validate, person2)


    def test_ValidatorPersoana_Nume(self):
        person1 = Persoana(5, 'Ar', 'Bd. Independentei')
        person2 = Persoana(5, '', 'Bd. Independentei')

        self.assertRaises(ValueError, self.__validator.validate, person1)
        self.assertRaises(ValueError, self.__validator.validate, person2)

    def test_ValidatorPersoana_Adresa(self):
        person1 = Persoana(5, 'Ardelean Andrada', 'Bd')
        person2 = Persoana(5, 'Ardelean Andrada', '')

        self.assertRaises(ValueError, self.__validator.validate, person1)
        self.assertRaises(ValueError, self.__validator.validate, person2)
