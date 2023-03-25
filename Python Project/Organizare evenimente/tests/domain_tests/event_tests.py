import unittest

from domain.entities import Eveniment
from domain.validators import ValidatorEveniment


class TestCaseEventDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = ValidatorEveniment()

    def test_create_event(self):
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')

        self.assertEqual(event1.getID(), 1)
        self.assertEqual(event1.getData(), '24/10/2021')
        self.assertEqual(event1.getTip(), 'Meeting')
        self.assertEqual(event1.getDescriere(), 'Intalnire in parcul central.')

    def test_equals_person(self):
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')

        self.assertEqual(event1, event2)

    def test_ValidatorEveniment(self):
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__validator.validate(event1)

        event2 = Eveniment(21233, '40/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event3 = Eveniment(2, '40/10/2021', 'Me', '')

        self.assertRaises(ValueError, self.__validator.validate, event2)
        self.assertRaises(ValueError, self.__validator.validate, event3)

    def test_ValidatorEveniment_ID(self):
        event1 = Eveniment(-5, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')

        self.assertRaises(ValueError, self.__validator.validate, event1)

    def test_ValidatorEveniment_Tip(self):
        event1 = Eveniment(5, '24/10/2021', 'M', 'Intalnire in parcul central.')

        self.assertRaises(ValueError, self.__validator.validate, event1)

    def test_ValidatorEveniment_Descriere(self):
        event1 = Eveniment(5, '24/10/2021', 'Meeting', '.')

        self.assertRaises(ValueError, self.__validator.validate, event1)

