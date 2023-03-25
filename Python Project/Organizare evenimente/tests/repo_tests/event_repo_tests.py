import unittest

from domain.entities import Eveniment
from repository.event_repo import InMemoryRepositoryEvent, FileRepositoryEvent


class TestCaseEventRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InMemoryRepositoryEvent()
        self.add_predifined_events()

    def add_predifined_events(self):
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        event3 = Eveniment(8, '2/12/2021', 'Prezentare de arta', 'La muzeu, ora 17:30.')
        event4 = Eveniment(10, '30/10/2021', 'Balul bobocilor', 'La casa de cultura.')
        event5 = Eveniment(43, '17/9/2021', 'Concert', 'In centrul vechi. Ora 20:00.')
        event6 = Eveniment(4, '22/11/2021', 'Street Music Festival', 'La centru vechi, ora 19:00.')
        event7 = Eveniment(14, '12/12/2021', 'Revelion', 'Cabana in Somesul Rece.')
        event8 = Eveniment(17, '9/7/2021', 'Festival', 'Pe plaja.')
        event9 = Eveniment(79, '19/11/2021', 'Premiera film', 'La cinema-ul din Iulius Mall, ora 18:00.')

        self.__repo.store(event1)
        self.__repo.store(event2)
        self.__repo.store(event3)
        self.__repo.store(event4)
        self.__repo.store(event5)
        self.__repo.store(event6)
        self.__repo.store(event7)
        self.__repo.store(event8)
        self.__repo.store(event9)

    def test_store(self):
        initial_size = self.__repo.size()
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__repo.store(event1)
        self.assertEqual(self.__repo.size(), initial_size + 1)

        event2 = Eveniment(5, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo.store(event2)
        self.assertEqual(self.__repo.size(), initial_size + 2)

        pers_list = self.__repo.get_all_events()
        self.assertEqual(pers_list[initial_size].getID(), 1)
        self.assertEqual(pers_list[initial_size + 1].getID(), 5)


    def test_find(self):
        person = self.__repo.find_event(1)

        self.assertEqual(person.getData(), '24/10/2021')
        self.assertEqual(person.getTip(), 'Meeting')

        person = self.__repo.find_event(100)
        self.assertIs(person, None)

    def test_ValidatorID(self):
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        event3 = Eveniment(3, '26/11/2021', 'Concurs', 'La Cluj Arena, ora 10:00.')
        self.__repo.store(event1)
        self.__repo.store(event2)
        self.__repo.store(event3)

        with self.assertRaises(ValueError):
            self.__repo.validatorID(2,'add')

        with self.assertRaises(ValueError):
            self.__repo.validatorID(3, 'add')

    def test_size(self):
        initial_size = self.__repo.size()
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo.delete_event(event1)
        self.__repo.delete_event(event2)

        self.assertEqual(self.__repo.size(), initial_size - 2)

        self.__repo.store(event1)
        self.assertEqual(self.__repo.size(), initial_size - 1)
        self.__repo.update_event(event1, event2)
        self.assertEqual(self.__repo.size(), initial_size - 1)

    def test_delete_event(self):
        initial_size = self.__repo.size()
        event = self.__repo.find_event(1)
        event_list = self.__repo.delete_event(event)

        self.assertTrue(len(event_list) == initial_size - 1)

        event1 = Eveniment(3, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__repo.store(event1)

        event2 = Eveniment(5, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo.store(event2)

        event = self.__repo.find_event(3)
        event_list = self.__repo.delete_event(event)
        self.assertEqual(len(event_list), initial_size)

    def test_update_event(self):
        initial_size = self.__repo.size()
        event1 = Eveniment(3, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(5, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo.store(event1)
        self.__repo.store(event2)

        event_update = Eveniment(5, '2/11/2021', 'Bal', 'La Castelul din Carei.')
        person_list = self.__repo.update_event(event1, event_update)

        self.assertEqual(self.__repo.size(), initial_size + 2)
        self.assertTrue(person_list[initial_size+1].getID() == 5)
        self.assertTrue(person_list[initial_size+1].getData() == '2/11/2021')
        self.assertTrue(person_list[initial_size+1].getTip() == 'Bal')

    def tearDown(self) -> None:
        self.__repo.delete_all()

class TestCaseEventRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = FileRepositoryEvent('test_event_repo.txt')
        self.__repo.delete_all()
        self.populate_list()

    def populate_list(self):
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        event3 = Eveniment(8, '2/12/2021', 'Prezentare de arta', 'La muzeu, ora 17:30.')
        event4 = Eveniment(10, '30/10/2021', 'Balul bobocilor', 'La casa de cultura.')
        event5 = Eveniment(43, '17/9/2021', 'Concert', 'In centrul vechi. Ora 20:00.')
        event6 = Eveniment(4, '22/11/2021', 'Street Music Festival', 'La centru vechi, ora 19:00.')
        event7 = Eveniment(14, '12/12/2021', 'Revelion', 'Cabana in Somesul Rece.')
        event8 = Eveniment(17, '9/7/2021', 'Festival', 'Pe plaja.')
        event9 = Eveniment(79, '19/11/2021', 'Premiera film', 'La cinema-ul din Iulius Mall, ora 18:00.')

        self.__repo.store(event1)
        self.__repo.store(event2)
        self.__repo.store(event3)
        self.__repo.store(event4)
        self.__repo.store(event5)
        self.__repo.store(event6)
        self.__repo.store(event7)
        self.__repo.store(event8)
        self.__repo.store(event9)

    def test_find(self):
        e = self.__repo.find_event(1)
        self.assertTrue(e.getData() == '24/10/2021')
        self.assertTrue(e.getTip() == 'Meeting')

        e1 = self.__repo.find_event(100)
        self.assertIs(e1, None)

    def test_store(self):
        initial_size = self.__repo.size()
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__repo.store(event1)
        self.assertEqual(self.__repo.size(), initial_size + 1)

        event2 = Eveniment(5, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo.store(event2)
        self.assertEqual(self.__repo.size(), initial_size + 2)

        pers_list = self.__repo.get_all_events()
        self.assertEqual(pers_list[initial_size].getID(), 1)
        self.assertEqual(pers_list[initial_size + 1].getID(), 5)

    def test_ValidatorID(self):
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        event3 = Eveniment(3, '26/11/2021', 'Concurs', 'La Cluj Arena, ora 10:00.')
        self.__repo.store(event1)
        self.__repo.store(event2)
        self.__repo.store(event3)

        with self.assertRaises(ValueError):
            self.__repo.validatorID(2,'add')

        with self.assertRaises(ValueError):
            self.__repo.validatorID(3, 'add')

    def test_size(self):
        initial_size = self.__repo.size()
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo.delete_event(event1)
        self.__repo.delete_event(event2)

        self.assertEqual(self.__repo.size(), initial_size - 2)

        self.__repo.store(event1)
        self.assertEqual(self.__repo.size(), initial_size - 1)
        self.__repo.update_event(event1, event2)
        self.assertEqual(self.__repo.size(), initial_size - 1)

    def test_get_all_events(self):
        initial_size = self.__repo.size()
        crt_events = self.__repo.get_all_events()
        self.assertIsInstance(crt_events, list)

        self.assertEqual(len(crt_events), initial_size)

        event1 = self.__repo.find_event(1)
        self.__repo.delete_event(event1)
        event2 = self.__repo.find_event(2)
        self.__repo.delete_event(event2)

        crt_persons = self.__repo.get_all_events()
        self.assertEqual(len(crt_persons), initial_size - 2)

        self.__repo.store(Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.'))
        self.assertEqual(self.__repo.size(), initial_size - 1)

        self.__repo.store(Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.'))
        self.assertEqual(self.__repo.size(), initial_size)

    def test_delete_event(self):
        initial_size = self.__repo.size()
        event = self.__repo.find_event(1)
        event_list = self.__repo.delete_event(event)

        self.assertTrue(len(event_list) == initial_size - 1)

        event1 = Eveniment(3, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__repo.store(event1)

        event2 = Eveniment(5, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo.store(event2)

        event = self.__repo.find_event(3)
        event_list = self.__repo.delete_event(event)
        self.assertEqual(len(event_list), initial_size)

    def test_update_event(self):
        initial_size = self.__repo.size()
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo.store(event1)
        self.__repo.store(event2)

        event_update = Eveniment(1, '2/11/2021', 'Bal', 'La Castelul din Carei.')
        event_list = self.__repo.update_event(event1, event_update)

        self.assertEqual(self.__repo.size(), initial_size + 2)
        self.assertTrue(event_list[initial_size].getID() == 1)
        self.assertTrue(event_list[initial_size].getData() == '2/11/2021')
        self.assertTrue(event_list[initial_size].getTip() == 'Bal')

    def tearDown(self) -> None:
        self.__repo.delete_all()


