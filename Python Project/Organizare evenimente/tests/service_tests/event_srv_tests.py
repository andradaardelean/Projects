import unittest

from domain.validators import ValidatorEveniment
from repository.event_repo import InMemoryRepositoryEvent
from service.event_service import ServiceEveniment


class TestCaseEventService(unittest.TestCase):
    def setUp(self) -> None:
        repo = InMemoryRepositoryEvent()
        val = ValidatorEveniment()
        self.__srv = ServiceEveniment(repo, val)

    def test_add_event(self):
        self.__srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.assertTrue(self.__srv.get_all_events()[0].getID() == 1)
        self.assertTrue(self.__srv.get_all_events()[0].getData() == '24/10/2021')
        self.assertTrue(self.__srv.get_all_events()[0].getTip() == 'Meeting')
        self.assertTrue(self.__srv.get_all_events()[0].getDescriere() == 'Intalnire in parcul central.')

        self.assertTrue(len(self.__srv.get_all_events()) == 1)

    def test_get_all_events(self):
        self.__srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__srv.add_event(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.assertTrue(type(self.__srv.get_all_events()) == list)
        self.assertTrue(len(self.__srv.get_all_events()) == 2)

    def test_ValidatorID(self):
        self.__srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')

        with self.assertRaises(ValueError):
            self.__srv.validatorID(1,'add')

        with self.assertRaises(ValueError):
            self.__srv.validatorID(2,'delete')

        with self.assertRaises(ValueError):
            self.__srv.validatorID(3,'update')

    def test_find_event(self):
        self.__srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__srv.add_event(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__srv.add_event(3, '24/10/2021', 'Meeting', 'Intalnire in centru.')

        event_gasite = self.__srv.find_event('24/10/2021',1)
        self.assertTrue (len(event_gasite) == 2)
        self.assertTrue (event_gasite[0].getTip() == 'Meeting')
        self.assertTrue (event_gasite[1].getData() == '24/10/2021')
        self.assertTrue (event_gasite[0].getDescriere() == 'Intalnire in parcul central.')

        event_gasite = self.__srv.find_event('Team Building', 2)
        self.assertTrue (len(event_gasite) == 1)
        self.assertTrue (event_gasite[0].getTip() == 'Team Building')
        self.assertTrue (event_gasite[0].getData() == '25/10/2021')


    def test_delete_event(self):
        self.__srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__srv.add_event(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')

        self.assertTrue (len(self.__srv.get_all_events()) == 2)

        self.__srv.delete_event(1)
        self.assertTrue (len(self.__srv.get_all_events()) == 1)

        self.__srv.delete_event(2)
        self.assertTrue (len(self.__srv.get_all_events()) == 0)

    def test_update_event(self):
        self.__srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__srv.add_event(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')

        self.__srv.update_event(2, '27/11/2021', 'Bal mascat', 'La casa de cultura.')
        self.assertTrue (self.__srv.get_all_events()[1].getData() == '27/11/2021')
        self.assertTrue (self.__srv.get_all_events()[1].getTip() == 'Bal mascat')
        self.assertTrue (self.__srv.get_all_events()[1].getDescriere() == 'La casa de cultura.')















