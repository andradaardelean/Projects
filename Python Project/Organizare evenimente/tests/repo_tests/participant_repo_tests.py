import unittest

from domain.entities import Persoana, Eveniment, Participant
from repository.participant_repo import InMemoryRepositoryParticipant, FileRepositoryParticipant


class TestCaseParticipantRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InMemoryRepositoryParticipant()

    def test_store(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)

        self.assertEqual(len(self.__repo.get_all_participants()), 2)
        self.assertEqual(self.__repo.get_all_participants()[0].getPerson().getNume(), 'Ardelean Andrada')
        self.assertEqual(self.__repo.get_all_participants()[1].getEvent().getTip(), 'Team Building')

    def test_find_participant(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)

        participant = self.__repo.find_participant(participant1)
        self.assertTrue(participant.getPerson().getNume() == 'Ardelean Andrada')
        self.assertTrue(participant.getEvent().getTip() == 'Meeting')

        participant = self.__repo.find_participant(participant2)
        self.assertTrue(participant.getPerson().getAdresa() == 'Bd. Libertatii')
        self.assertTrue(participant.getEvent().getData() == '25/10/2021')

    def test_ValidatorParticipant(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)

        person3 = Persoana(3, 'Acas George', 'Bd. Libertatii')
        event3 = Eveniment(4, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__repo.validator_participant(person3, event3)

        with self.assertRaises(ValueError):
            self.__repo.validator_participant(person1, event1)

        with self.assertRaises(ValueError):
            self.__repo.validator_participant(person2, event2)

    def test_events_list_for_one_person(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        participant3 = Participant(person1, event2)

        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)
        self.__repo.store_participant(participant3)

        events_list = self.__repo.events_list_for_one_person(person1)
        self.assertTrue(len(events_list) == 2)
        self.assertTrue(events_list[0].getTip() == 'Meeting')
        self.assertTrue(events_list[1].getDescriere() == 'In piata Mihai Viteazu.')

        events_list = self.__repo.events_list_for_one_person(person2)
        self.assertTrue(len(events_list) == 1)
        self.assertTrue(events_list[0].getData() == '25/10/2021')


    def test_participants_for_one_event(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        participant3 = Participant(person1, event2)

        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)
        self.__repo.store_participant(participant3)

        person_list = self.__repo.participants_for_one_event(event1)
        self.assertTrue (len(person_list) == 1)
        self.assertTrue (person_list[0].getNume() == 'Ardelean Andrada')

        person_list = self.__repo.participants_for_one_event(event2)
        self.assertTrue (len(person_list) == 2)
        self.assertTrue (person_list[0].getIDpersoana() == 2)
        self.assertTrue (person_list[0].getNume() == 'Acas George')
        self.assertTrue (person_list[1].getAdresa() == 'Bd. Independentei')

    def tearDown(self) -> None:
        self.__repo.delete_all_participants()

class TestCaseParticipantRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = FileRepositoryParticipant('test_participant_repo.txt')

    def test_store(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)

        self.assertEqual(len(self.__repo.get_all_participants()), 2)
        self.assertEqual(self.__repo.get_all_participants()[0].getPerson().getNume(), 'Ardelean Andrada')
        self.assertEqual(self.__repo.get_all_participants()[1].getEvent().getTip(), 'Team Building')

    def test_find_participant(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)

        participant = self.__repo.find_participant(participant1)
        self.assertTrue(participant.getPerson().getNume() == 'Ardelean Andrada')
        self.assertTrue(participant.getEvent().getTip() == 'Meeting')

        participant = self.__repo.find_participant(participant2)
        self.assertTrue(participant.getPerson().getAdresa() == 'Bd. Libertatii')
        self.assertTrue(participant.getEvent().getData() == '25/10/2021')

    def test_ValidatorParticipant(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)

        person3 = Persoana(3, 'Acas George', 'Bd. Libertatii')
        event3 = Eveniment(4, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__repo.validator_participant(person3, event3)

        with self.assertRaises(ValueError):
            self.__repo.validator_participant(person1, event1)

        with self.assertRaises(ValueError):
            self.__repo.validator_participant(person2, event2)

    def test_events_list_for_one_person(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        participant3 = Participant(person1, event2)

        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)
        self.__repo.store_participant(participant3)

        events_list = self.__repo.events_list_for_one_person(person1)
        self.assertTrue(len(events_list) == 2)
        self.assertTrue(events_list[0].getTip() == 'Meeting')
        self.assertTrue(events_list[1].getDescriere() == 'In piata Mihai Viteazu.')

        events_list = self.__repo.events_list_for_one_person(person2)
        self.assertTrue(len(events_list) == 1)
        self.assertTrue(events_list[0].getData() == '25/10/2021')


    def test_participants_for_one_event(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        participant1 = Participant(person1, event1)
        participant2 = Participant(person2, event2)
        participant3 = Participant(person1, event2)

        self.__repo.store_participant(participant1)
        self.__repo.store_participant(participant2)
        self.__repo.store_participant(participant3)

        person_list = self.__repo.participants_for_one_event(event1)
        self.assertTrue (len(person_list) == 1)
        self.assertTrue (person_list[0].getNume() == 'Ardelean Andrada')

        person_list = self.__repo.participants_for_one_event(event2)
        self.assertTrue (len(person_list) == 2)
        self.assertTrue (person_list[0].getIDpersoana() == 2)
        self.assertTrue (person_list[0].getNume() == 'Acas George')
        self.assertTrue (person_list[1].getAdresa() == 'Bd. Independentei')

    def tearDown(self) -> None:
        self.__repo.delete_all_participants()