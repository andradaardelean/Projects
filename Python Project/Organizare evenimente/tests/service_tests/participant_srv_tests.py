import unittest
from datetime import datetime

from domain.entities import Persoana, Eveniment
from repository.event_repo import InMemoryRepositoryEvent
from repository.participant_repo import InMemoryRepositoryParticipant
from repository.person_repo import InMemoryRepositoryPers
from service.participant_service import ServiceParticipant


class TestCaseParticipantService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo_event = InMemoryRepositoryEvent()
        self.__repo_pers = InMemoryRepositoryPers()
        self.__repo_part = InMemoryRepositoryParticipant()
        self.__srv = ServiceParticipant(self.__repo_part, self.__repo_pers, self.__repo_event)
        # self.populate_list()

    def populate_list(self):
        person1 = Persoana(24, 'Ardelean Andrada', 'Str. Lucian Blaga, nr.201')
        person2 = Persoana(10, 'Stan David', 'Str. Vasile Lucaciu, nr.25')
        person3 = Persoana(7, 'Ripan George', 'Str. Crizantemelor, nr.115')
        person4 = Persoana(13, 'Chifor Sandra', 'Bd. Closca, nr. 181')
        person5 = Persoana(66, 'Serghie Alex', 'Str. Noroieni, nr.92')

        self.__repo_pers.store(person1)
        self.__repo_pers.store(person2)
        self.__repo_pers.store(person3)
        self.__repo_pers.store(person4)
        self.__repo_pers.store(person5)

        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        event3 = Eveniment(8, '2/12/2021', 'Prezentare de arta', 'La muzeu, ora 17:30.')
        event4 = Eveniment(10, '30/10/2021', 'Balul bobocilor', 'La casa de cultura.')
        event5 = Eveniment(43, '17/9/2021', 'Concert', 'In centrul vechi. Ora 20:00.')
        event6 = Eveniment(4, '22/11/2021', 'Street Music Festival', 'La centru vechi, ora 19:00.')
        event7 = Eveniment(14, '12/12/2021', 'Revelion', 'Cabana in Somesul Rece.')
        event8 = Eveniment(17, '9/7/2021', 'Festival', 'Pe plaja.')
        event9 = Eveniment(79, '19/11/2021', 'Premiera film', 'La cinema-ul din Iulius Mall, ora 18:00.')

        self.__repo_event.store(event1)
        self.__repo_event.store(event2)
        self.__repo_event.store(event3)
        self.__repo_event.store(event4)
        self.__repo_event.store(event5)
        self.__repo_event.store(event6)
        self.__repo_event.store(event7)
        self.__repo_event.store(event8)
        self.__repo_event.store(event9)

    def test_ServiceParticipant_create_participant(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo_pers.store(person1)
        self.__repo_pers.store(person2)
        self.__repo_event.store(event1)
        self.__repo_event.store(event2)

        self.__srv.create_participant(1, 2)

        self.assertTrue(self.__srv.get_all_participants()[0].getPerson() == self.__repo_pers.find_person(1))
        self.assertTrue(self.__srv.get_all_participants()[0].getEvent() == self.__repo_event.find_event(2))

        try:
            self.__srv.create_participant(1, 2)
            assert False
        except ValueError:
            assert True

        try:
            self.__srv.create_participant(6, 2)
            assert False
        except ValueError:
            assert True

    def test_events_list_for_one_person(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__repo_pers.store(person1)
        self.__repo_pers.store(person2)
        self.__repo_event.store(event1)
        self.__repo_event.store(event2)

        self.__srv.create_participant(1, 1)
        self.__srv.create_participant(1, 2)
        self.__srv.create_participant(2, 1)

        events_list = self.__srv.events_list_for_one_person(1)
        self.assertTrue(len(events_list) == 2)
        self.assertTrue(events_list[0].getID() == 1)
        self.assertTrue(events_list[1].getData() == '25/10/2021')

        events_list = self.__srv.events_list_for_one_person((2))
        self.assertTrue(len(events_list) == 1)
        self.assertTrue(events_list[0].getTip() == 'Meeting')

    def test_events_list_for_one_person_organised_by_description(self):
        self.__srv.delete_all()
        person1 = Persoana(11, 'Ardelean Andrada', 'Bd. Independentei')
        event1 = Eveniment(50, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(51, '25/10/2021', 'Team Building', 'Parcul Central')
        event3 = Eveniment(52, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
        event4 = Eveniment(53, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
        self.__repo_pers.store(person1)
        self.__repo_event.store(event1)
        self.__repo_event.store(event2)
        self.__repo_event.store(event3)
        self.__repo_event.store(event4)

        self.__srv.create_participant(11, 50)
        self.__srv.create_participant(11, 51)
        self.__srv.create_participant(11, 52)
        self.__srv.create_participant(11, 53)

        events_list = self.__srv.events_list_for_one_person_organised_by_description(11)
        self.assertTrue(len(events_list) == 4)
        self.assertTrue(events_list[0].getID() == 53)
        self.assertTrue(events_list[1].getData() == '24/10/2021')
        print(events_list[2].getTip(), events_list[3].getDescriere())
        self.assertTrue(events_list[2].getTip() == 'Festivitate de deschidere')
        self.assertTrue(events_list[3].getDescriere() == 'Parcul Central')

    def test_events_list_for_one_person_organised_by_date(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'Parcul Central')
        event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
        event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
        self.__repo_pers.store(person1)
        self.__repo_event.store(event1)
        self.__repo_event.store(event2)
        self.__repo_event.store(event3)
        self.__repo_event.store(event4)

        self.__srv.create_participant(1, 1)
        self.__srv.create_participant(1, 2)
        self.__srv.create_participant(1, 3)
        self.__srv.create_participant(1, 4)

        events_list = self.__srv.events_list_for_one_person_organised_by_date(1)
        self.assertTrue(len(events_list) == 4)
        self.assertTrue(events_list[0].getID() == 3)
        self.assertTrue(events_list[1].getData() == '24/10/2021')
        self.assertTrue(events_list[0].getTip() == 'Festivitate de deschidere')
        self.assertTrue(events_list[2].getDescriere() == 'Parcul Central')

    def test_participants_to_the_most_events(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
        event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
        self.__repo_pers.store(person1)
        self.__repo_pers.store(person2)
        self.__repo_event.store(event1)
        self.__repo_event.store(event2)
        self.__repo_event.store(event3)
        self.__repo_event.store(event4)

        self.__srv.create_participant(1, 1)
        self.__srv.create_participant(1, 2)
        self.__srv.create_participant(2, 1)

        part_list = self.__srv.participants_to_the_most_events()
        self.assertTrue(len(part_list) == 1)
        self.assertTrue(part_list[0].getIDpersoana() == 1)
        self.assertTrue(part_list[0].getNume() == 'Ardelean Andrada')

        self.__srv.create_participant(2, 2)
        part_list = self.__srv.participants_to_the_most_events()
        self.assertTrue(len(part_list) == 2)
        self.assertTrue(part_list[0].getIDpersoana() == 1)
        self.assertTrue(part_list[1].getIDpersoana() == 2)
        self.assertTrue(part_list[1].getAdresa() == 'Bd. Libertatii')

    def test_events_with_most_participants(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
        event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
        self.__repo_pers.store(person1)
        self.__repo_pers.store(person2)
        self.__repo_event.store(event1)
        self.__repo_event.store(event2)
        self.__repo_event.store(event3)
        self.__repo_event.store(event4)

        self.__srv.create_participant(1, 1)
        self.__srv.create_participant(1, 2)
        self.__srv.create_participant(2, 1)

        event_list = self.__srv.events_with_most_participants()

        self.assertTrue(len(event_list) == 1)
        self.assertTrue(event_list[0].getDescriere() == 'Intalnire in parcul central.')
        self.assertTrue(event_list[0].getID() == 1)

    def test_ServiceParticipant_days_with_most_participants(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        person2 = Persoana(2, 'Ardelean David', 'Bd. Independentei')
        person3 = Persoana(3, 'Ardelean Andrada', 'Bd. Independentei')
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '25/10/2021', 'Team Building', 'Parcul Central')
        event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
        event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
        self.__repo_pers.store(person1)
        self.__repo_pers.store(person2)
        self.__repo_pers.store(person3)
        self.__repo_event.store(event1)
        self.__repo_event.store(event2)
        self.__repo_event.store(event3)
        self.__repo_event.store(event4)

        self.__srv.create_participant(1, 1)
        self.__srv.create_participant(1, 2)
        self.__srv.create_participant(1, 3)
        self.__srv.create_participant(1, 4)
        self.__srv.create_participant(2, 4)
        self.__srv.create_participant(3, 4)
        self.__srv.create_participant(2, 3)
        self.__srv.create_participant(2, 2)

        days_list = self.__srv.days_with_most_participants()
        self.assertTrue(len(days_list) == 3)
        self.assertTrue(days_list[0][0] == '28/11/2021')
        self.assertTrue(days_list[0][1] == 3)
        self.assertTrue(days_list[2][0] == '25/10/2021')
        self.assertTrue(days_list[2][1] == 2)

    def test_ServiceParticipant_selection_sort(self):
        list = ["24/10/2021", "25/9/2021", "12/11/2021", "16/9/2021", "17/12/2021"]

        list_org = ["16/9/2021", "25/9/2021", "24/10/2021", "12/11/2021", "17/12/2021"]
        organised_list = self.__srv.selection_sort(list, key=lambda list: datetime.strptime(list, "%d/%m/%Y"),
                                                   reverse=False, cmp=self.__srv.cmp_dates)
        self.assertEqual(list_org, organised_list)

        list_org_rev = ["17/12/2021","12/11/2021", "24/10/2021", "25/9/2021", "16/9/2021"]
        organised_list = self.__srv.selection_sort(list, key=lambda list: datetime.strptime(list, "%d/%m/%Y"),
                                                   reverse=True, cmp=self.__srv.cmp_dates)
        self.assertTrue(list_org_rev == organised_list)

        organised_list = self.__srv.selection_sort(list, key=lambda list: datetime.strptime(list, "%d/%m/%Y"),
                                                   reverse=False, cmp=False)
        self.assertTrue(list_org == organised_list)

    def test_ServiceParticipant_shake_sort(self):
        list = ['arc', 'casa', 'foc', 'concert', 'arici', 'concurs']

        list_org = ['arc', 'arici', 'casa', 'concert','concurs', 'foc']
        organised_list = self.__srv.shake_sort(list, key = lambda x:x,  reverse=False, cmp=self.__srv.cmp_description)
        self.assertEqual(list_org, organised_list)

        list_org_rev = ['foc', 'concurs', 'concert', 'casa', 'arici', 'arc']
        organised_list = self.__srv.shake_sort(list, key = lambda x:x,  reverse=True, cmp=self.__srv.cmp_description)
        self.assertEqual(list_org_rev, organised_list)

        list_org = ['arc', 'arici', 'casa', 'concert', 'concurs', 'foc']
        organised_list = self.__srv.shake_sort(list, key=lambda x: x, reverse=False, cmp=False)
        self.assertEqual(list_org, organised_list)

    def test_ServiceParticipant_cmp_dates_new(self):
        event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        event2 = Eveniment(2, '24/10/2021', 'Team Building', 'Parcul Central')
        event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
        event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')

        self.assertEqual(self.__srv.cmp_dates_new(event1, event2), 0)
        self.assertEqual(self.__srv.cmp_dates_new(event1, event3), 1)
        self.assertTrue(self.__srv.cmp_dates_new(event3, event4) == 0)

