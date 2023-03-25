from datetime import datetime

from domain.entities import Participant, Persoana, Eveniment
from repository.event_repo import InMemoryRepositoryEvent
from repository.participant_repo import InMemoryRepositoryParticipant
from repository.person_repo import InMemoryRepositoryPers


class ServiceParticipant:
    def __init__(self, repo_participant, repo_person, repo_event):
        self.__repo_participant = repo_participant
        self.__repo_person = repo_person
        self.__repo_event = repo_event

    def get_all_participants(self):
        return self.__repo_participant.get_all_participants()

    def generate_participants(self):
        """
        Generez cativa participanti.
        :return:
        """
        person = self.__repo_person.find_person(10)
        event = self.__repo_event.find_event(10)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(13)
        event = self.__repo_event.find_event(10)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(66)
        event = self.__repo_event.find_event(10)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(7)
        event = self.__repo_event.find_event(43)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(24)
        event = self.__repo_event.find_event(43)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(24)
        event = self.__repo_event.find_event(10)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(24)
        event = self.__repo_event.find_event(79)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(24)
        event = self.__repo_event.find_event(1)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(7)
        event = self.__repo_event.find_event(79)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(66)
        event = self.__repo_event.find_event(1)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(13)
        event = self.__repo_event.find_event(8)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(7)
        event = self.__repo_event.find_event(10)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(66)
        event = self.__repo_event.find_event(79)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

        person = self.__repo_person.find_person(13)
        event = self.__repo_event.find_event(79)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

    def create_participant(self, person_id, event_id):
        """
        Se creeaza un parricipant.
        :param id_person: id-ul persoanei
        :param id_event: id-ul evenimentului
        :return:
        :raises: Persoana cu acest ID nu se gaseste in lista
                 Evenimentul cu acest ID nu se gaseste in lista.
                 Numarul participantului este invalid.
        """
        self.__repo_person.validatorID(person_id, 'else')
        person = self.__repo_person.find_person(person_id,0)

        self.__repo_event.validatorID(event_id, 'else')
        event = self.__repo_event.find_event(event_id,0)

        self.__repo_participant.validator_participant(person, event)
        participant = Participant(person, event)
        self.__repo_participant.store_participant(participant)

    def delete_all(self):
        self.__repo_participant.get_all_participants = []

    def events_list_for_one_person(self, person_id):
        """
        Gaseste lista de evenimente la care participa o persoana.
        :param person_id: id-ul persoanei pentru care se genereaza lista
        :type person_id: int
        :return: lista de evenimente
        """
        self.__repo_person.validatorID(person_id, 'else')
        person = self.__repo_person.find_person(person_id, 0)

        events_list = self.__repo_participant.events_list_for_one_person(person)
        return events_list

    def cmp_description(self, x, y):
        if x > y:
            return 1
        else:
            return 0

    def shake_sort(self, list, key = lambda x:x, reverse=False, cmp=False):
        """
        Sortez o lista cu metoda shake sort.
        :param list: lista pe care urmeaza sa o sortez.(list)
        :return: lista sortata
        """
        swapped = True
        start = 0
        end = len(list) - 1

        if cmp == False:
            while swapped == True:
                swapped = False
                for index in range(start, end):
                    if key(list[index]) > key(list[index + 1]):
                        list[index], list[index + 1] = list[index + 1], list[index]
                        swapped = True

                if swapped == False:
                    break

                swapped = False
                end = end - 1
                for index in range(end - 1, start - 1, -1):
                    if key(list[index]) > key(list[index + 1]):
                        list[index], list[index + 1] = list[index + 1], list[index]
                        swapped = True
                start += 1

            if reverse == True:
                list.reverse()
        else:
            while swapped == True:
                swapped = False
                for index in range(start, end):
                    if cmp(key(list[index]), key(list[index + 1])):
                        list[index], list[index + 1] = list[index + 1], list[index]
                        swapped = True

                if swapped == False:
                    break

                swapped = False
                end = end - 1
                for index in range(end - 1, start - 1, -1):
                    if cmp(key(list[index]), key(list[index + 1])):
                        list[index], list[index + 1] = list[index + 1], list[index]
                        swapped = True
                start += 1

            if reverse == True:
                list.reverse()

        return list

    def events_list_for_one_person_organised_by_description(self, person_id):
        """
        Ordoneaza evenimentele in ordine alfabetica dupa descriere.
        :param person_id: id ul persoanei
        :type person_id: int
        :return: lista de evenimente sortate in ordine alfabetica dupa descriere.
        """
        events_list = self.events_list_for_one_person(person_id)
        descriptions_list = []
        for event in events_list:
            desc = event.getDescriere()
            descriptions_list.append(desc)

        # print(descriptions_list)

        # descriptions_list.sort()
        # list = self.shake_sort(descriptions_list, events_list, key = lambda x:x,  reverse=False, cmp=self.cmp_description)
        list = self.shake_sort(descriptions_list, key = lambda x:x,  reverse=False, cmp=self.cmp_description)

        # print(descriptions_list)

        organised_events_list = []
        for desc in descriptions_list:
            for event in events_list:
                if desc == event.getDescriere():
                    organised_events_list.append(event)

        return organised_events_list

    # def events_list_for_one_person_organised_by_date(self, person_id):
    #     """
    #     Ordoneaza evenimentele in ordine alfabetica dupa data.
    #     :param person_id: id ul persoanei
    #     :type person_id: int
    #     :return: lista de evenimente sortate dupa data.
    #     """
    #     events_list = self.events_list_for_one_person(person_id)
    #     dates = []
    #     for event in events_list:
    #         date = event.getData()
    #         dates.append(date)
    #
    #     dates.sort(key = lambda date: datetime.strptime(date, "%d/%m/%Y"))
    #
    #     sorted_list = []
    #     index = 0
    #     while index < len(dates):
    #         for event in events_list:
    #             if event.getData() == dates[index]:
    #                 sorted_list.append(event)
    #         index += 1
    #
    #     return sorted_list

    def cmp_dates(self, x, y):
        if x > y:
            return 1
        else:
            return 0

    def cmp_dates_new(self, x, y):
        if x.getData() > y.getData():
            return 1
        elif x.getData() == y.getData():
            if x.getDescriere() > y.getDescriere():
                return 1
            elif x.getDescriere() < y.getDescriere():
                return 0
        else:
            return 0

    # def cmp_dates_new(self, x, y, events_list):
    #     if x > y:
    #         return 1
    #     elif x == y:
    #         ok = 0
    #         for event in events_list:
    #             if event.getData() == x:
    #                 x = event.getDescriere()
    #                 ok = 1
    #             if ok == 1 and event.getData() == y:
    #                 y = event.getDescriere()
    #             if x > y:
    #                 return -1
    #             else:
    #                 return 0
    #     else:
    #         return 0
    def selection_sort(self, events_list, list, key=lambda x: x, reverse=False, cmp=False):
        """
        Sortez o lista cu selection sort
        :param list: lista care trebuie sortata(list)
        :return: lista sortata
        """

        if cmp == False:
            for index in range(len(list)):
                min = index
                for index2 in range(index + 1, len(list)):
                    if key(list[min]) > key(list[index2]):
                        min = index2
                list[index], list[min] = list[min], list[index]

            if reverse == True:
                list.reverse()
        else:
            for index in range(len(events_list)):
                min = index
                for index2 in range(index + 1, len(events_list)):
                    if cmp(events_list[min], events_list[index2]):
                        min = index2
                events_list[index], events_list[min] = events_list[min], events_list[index]

            list = []
            # id_list = []
            for el in events_list:
                # if el.getID() not in id_list:
                    # id_list.append(el.getID())
                list.append(el.getData())

            if reverse == True:
                list.reverse()

        return list

    # def selection_sort(self, list, key=lambda x: x, reverse=False, cmp=False):
    #     """
    #     Sortez o lista cu selection sort
    #     :param list: lista care trebuie sortata(list)
    #     :return: lista sortata
    #     """
    #
    #     if cmp == False:
    #         for index in range(len(list)):
    #             min = index
    #             for index2 in range(index + 1, len(list)):
    #                 if key(list[min]) > key(list[index2]):
    #                     min = index2
    #             list[index], list[min] = list[min], list[index]
    #
    #         if reverse == True:
    #             list.reverse()
    #     else:
    #         for index in range(len(list)):
    #             min = index
    #             for index2 in range(index + 1, len(list)):
    #                 if cmp(key(list[min]), key(list[index2])):
    #                     min = index2
    #             list[index], list[min] = list[min], list[index]
    #
    #         if reverse == True:
    #             list.reverse()
    #
    #     return list

    # def selection_sort(self,events_list, list, key=lambda x: x, reverse=False, cmp=False):
    #     """
    #     Sortez o lista cu selection sort
    #     :param list: lista care trebuie sortata(list)
    #     :return: lista sortata
    #     """
    #     # lista_evenimente = []
    #     # for i in range(len(events_list)):
    #     #     lista_evenimente.append(0)
    #     # index = 0
    #     # for event in events_list:
    #     #     lista_evenimente[index] = event
    #     #     index += 1
    #
    #     if cmp == False:
    #         for index in range(len(list)):
    #             min = index
    #             for index2 in range(index + 1, len(list)):
    #                 if key(list[min]) > key(list[index2]):
    #                     min = index2
    #             list[index], list[min] = list[min], list[index]
    #
    #         if reverse == True:
    #             list.reverse()
    #     else:
    #         list = events_list
    #         for index in range(len(list)):
    #             min = index
    #             for index2 in range(index + 1, len(list)):
    #                 if cmp(list[min], list[index2]):
    #                     min = index
    #             list[index], list[min] = list[min], list[index]
    #
    #         if reverse == True:
    #             list.reverse()
    #
    #     return list

    def events_list_for_one_person_organised_by_date(self, person_id):
        """
        Ordoneaza evenimentele in ordine alfabetica dupa data.
        :param person_id: id ul persoanei
        :type person_id: int
        :return: lista de evenimente sortate dupa data.
        """
        events_list = self.events_list_for_one_person(person_id)
        events_sorted_by_date = sorted(events_list, key=lambda x:x.getData_format())
        dates = []
        for event in events_sorted_by_date:
            date = event.getData()
            dates.append(date)
        print(dates)

        # print(dates)
        # dates.sort(key = lambda date: datetime.strptime(date, "%d/%m/%Y"))
        # dates = self.selection_sort(dates, key=lambda date: datetime.strptime(date, "%d/%m/%Y"), reverse=False,
        #                             cmp=self.cmp_dates)
        # dates = self.selection_sort(events_list, dates, key=lambda date: datetime.strptime(date, "%d/%m/%Y"), reverse=False,
        #                             cmp=self.cmp_dates_new)

        sorted_list = []
        index = 0
        id_list = []
        while index < len(dates):
            for event in events_list:
                if event.getData() == dates[index] and event.getID() not in id_list:
                    id_list.append(event.getID())
                    sorted_list.append(event)
            index += 1

        return sorted_list

    def participants_to_the_most_events(self):
        """
        Persoanele participante la cele mai multe evenimente.
        :return: lista de persoane
        """
        participants_list = []
        max = -1
        for participant in self.__repo_participant.get_all_participants():
            events_list = self.__repo_participant.events_list_for_one_person(participant.getPerson())
            if len(events_list) > max:
                participants_list.clear()
                participants_list.append(participant.getPerson())
                max = len(events_list)
            elif len(events_list) == max and participant.getPerson() not in participants_list:
                participants_list.append(participant.getPerson())

        return participants_list

    def participants_for_one_event(self, event_id):
        """
        Creeaza lista de persoane care participa la evenimentul cu id-ul dat.
        :param event_id: id-ul evenimentului
        :type event_id: int
        :return: lista cu persoane
        """
        self.__repo_event.validatorID(event_id, 'else')
        event = self.__repo_event.find_event(event_id)

        return self.__repo_participant.participants_for_one_event(event)

    def events_with_most_participants(self):
        """
        Gaseste primele 20% evenimente cu cei mai multi participanti.
        :return: lista cu evenimente
        """
        no_part = []
        for event in self.__repo_event.get_all_events():
            person_list = self.participants_for_one_event(event.getID())
            no_part.append(len(person_list))

        no_part.sort(reverse=True)
        total = self.__repo_event.size()
        # print(total)
        # print(no_part)

        if total > 5:
            nr_events = int(total / 5)
        lista_events = []

        if total <= 5:
            for event in self.__repo_event.get_all_events():
                person_list = self.participants_for_one_event(event.getID())
                if len(person_list) == no_part[0]:
                    lista_events.append(event)
        else:
            index = 0
            while index < nr_events:
                for event in self.__repo_event.get_all_events():
                    person_list = self.participants_for_one_event(event.getID())
                    if len(person_list) == no_part[index]:
                        lista_events.append(event)
                        index += 1
                        break

        return lista_events

    def days_with_most_participants(self):
        """
        Zilele in care participa cele mai multe persoane.
        :return: lista cu primele 3 zile
        """
        dates = []

        for participant in self.get_all_participants():
            date = participant.getEvent().getData()
            if date not in dates:
                dates.append(date)

        lengths = []
        for i in range(len(self.__repo_event.get_all_events())):
            lengths.append(0)
        index = 0
        while index < len(dates):
            lengths[index] = 0
            for participant in self.get_all_participants():
                if dates[index] == participant.getEvent().getData():
                    lengths[index] += 1
            index += 1

        copie = []
        for el in lengths:
            copie.append(el)
        copie.sort(reverse=True)

        if len(lengths) >= 3:
            lista_finala = []
            index = 0
            while index < 3:
                index2 = 0
                list = []
                while index2 < len(lengths):
                    if copie[index] == lengths[index2]:
                        list.append(dates[index2])
                        list.append(lengths[index2])
                        break
                    index2 += 1
                lista_finala.append(list)
                index += 1

            return lista_finala
        else:
            return None


def test_ServiceParticipant_create_participant():
    test_repo_pers = InMemoryRepositoryPers()
    test_repo_event = InMemoryRepositoryEvent()
    test_repo_part = InMemoryRepositoryParticipant()

    test_srv = ServiceParticipant(test_repo_part, test_repo_pers, test_repo_event)

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    test_repo_pers.store(person1)
    test_repo_pers.store(person2)
    test_repo_event.store(event1)
    test_repo_event.store(event2)

    test_srv.create_participant(1, 2)

    assert (test_srv.get_all_participants()[0].getPerson() == test_repo_pers.find_person(1))
    assert (test_srv.get_all_participants()[0].getEvent() == test_repo_event.find_event(2))

    try:
        test_srv.create_participant(1, 2)
        assert False
    except ValueError:
        assert True

    try:
        test_srv.create_participant(6, 2)
        assert False
    except ValueError:
        assert True

    try:
        test_srv.create_participant(24, 2)
        assert False
    except ValueError:
        assert True

    try:
        test_srv.create_participant(-5, 2)
        assert False
    except ValueError:
        assert True


def test_ServiceParticipant_events_list_for_one_person():
    test_repo_pers = InMemoryRepositoryPers()
    test_repo_event = InMemoryRepositoryEvent()
    test_repo_part = InMemoryRepositoryParticipant()

    test_srv = ServiceParticipant(test_repo_part, test_repo_pers, test_repo_event)

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    test_repo_pers.store(person1)
    test_repo_pers.store(person2)
    test_repo_event.store(event1)
    test_repo_event.store(event2)

    test_srv.create_participant(1, 1)
    test_srv.create_participant(1, 2)
    test_srv.create_participant(2, 1)

    events_list = test_srv.events_list_for_one_person(1)
    assert (len(events_list) == 2)
    assert (events_list[0].getID() == 1)
    assert (events_list[1].getData() == '25/10/2021')

    events_list = test_srv.events_list_for_one_person((2))
    assert (len(events_list) == 1)
    assert (events_list[0].getTip() == 'Meeting')


def test_ServiceParticipant_events_list_for_one_person_organised_by_description():
    test_repo_pers = InMemoryRepositoryPers()
    test_repo_event = InMemoryRepositoryEvent()
    test_repo_part = InMemoryRepositoryParticipant()

    test_srv = ServiceParticipant(test_repo_part, test_repo_pers, test_repo_event)

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'Parcul Central')
    event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
    event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
    test_repo_pers.store(person1)
    test_repo_event.store(event1)
    test_repo_event.store(event2)
    test_repo_event.store(event3)
    test_repo_event.store(event4)

    test_srv.create_participant(1, 1)
    test_srv.create_participant(1, 2)
    test_srv.create_participant(1, 3)
    test_srv.create_participant(1, 4)

    events_list = test_srv.events_list_for_one_person_organised_by_description(1)
    assert (len(events_list) == 4)
    assert (events_list[0].getID() == 4)
    assert (events_list[1].getData() == '24/10/2021')
    assert (events_list[2].getTip() == 'Festivitate de deschidere')
    assert (events_list[3].getDescriere() == 'Parcul Central')


def test_ServiceParticipant_events_list_for_one_person_organised_by_date():
    test_repo_pers = InMemoryRepositoryPers()
    test_repo_event = InMemoryRepositoryEvent()
    test_repo_part = InMemoryRepositoryParticipant()

    test_srv = ServiceParticipant(test_repo_part, test_repo_pers, test_repo_event)

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'Parcul Central')
    event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
    event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
    test_repo_pers.store(person1)
    test_repo_event.store(event1)
    test_repo_event.store(event2)
    test_repo_event.store(event3)
    test_repo_event.store(event4)

    test_srv.create_participant(1, 1)
    test_srv.create_participant(1, 2)
    test_srv.create_participant(1, 3)
    test_srv.create_participant(1, 4)

    events_list = test_srv.events_list_for_one_person_organised_by_date(1)
    assert (len(events_list) == 4)
    assert (events_list[0].getID() == 3)
    assert (events_list[1].getData() == '24/10/2021')
    assert (events_list[0].getTip() == 'Festivitate de deschidere')
    assert (events_list[2].getDescriere() == 'Parcul Central')


def test_ServiceParticipant_participants_to_the_most_events():
    test_repo_pers = InMemoryRepositoryPers()
    test_repo_event = InMemoryRepositoryEvent()
    test_repo_part = InMemoryRepositoryParticipant()

    test_srv = ServiceParticipant(test_repo_part, test_repo_pers, test_repo_event)

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
    event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
    test_repo_pers.store(person1)
    test_repo_pers.store(person2)
    test_repo_event.store(event1)
    test_repo_event.store(event2)
    test_repo_event.store(event3)
    test_repo_event.store(event4)

    test_srv.create_participant(1, 1)
    test_srv.create_participant(1, 2)
    test_srv.create_participant(2, 1)

    part_list = test_srv.participants_to_the_most_events()
    assert (len(part_list) == 1)
    assert (part_list[0].getIDpersoana() == 1)
    assert (part_list[0].getNume() == 'Ardelean Andrada')

    test_srv.create_participant(2, 2)
    part_list = test_srv.participants_to_the_most_events()
    assert (len(part_list) == 2)
    assert (part_list[0].getIDpersoana() == 1)
    assert (part_list[1].getIDpersoana() == 2)
    assert (part_list[1].getAdresa() == 'Bd. Libertatii')


def test_ServiceParticipant_events_with_most_participants():
    test_repo_pers = InMemoryRepositoryPers()
    test_repo_event = InMemoryRepositoryEvent()
    test_repo_part = InMemoryRepositoryParticipant()

    test_srv = ServiceParticipant(test_repo_part, test_repo_pers, test_repo_event)

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
    event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
    test_repo_pers.store(person1)
    test_repo_pers.store(person2)
    test_repo_event.store(event1)
    test_repo_event.store(event2)
    test_repo_event.store(event3)
    test_repo_event.store(event4)

    test_srv.create_participant(1, 1)
    test_srv.create_participant(1, 2)
    test_srv.create_participant(2, 1)

    event_list = test_srv.events_with_most_participants()

    assert (len(event_list) == 1)
    assert (event_list[0].getDescriere() == 'Intalnire in parcul central.')
    assert (event_list[0].getID() == 1)


def test_ServiceParticipant_days_with_most_participants():
    test_repo_pers = InMemoryRepositoryPers()
    test_repo_event = InMemoryRepositoryEvent()
    test_repo_part = InMemoryRepositoryParticipant()

    test_srv = ServiceParticipant(test_repo_part, test_repo_pers, test_repo_event)

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Ardelean David', 'Bd. Independentei')
    person3 = Persoana(3, 'Ardelean Andrada', 'Bd. Independentei')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'Parcul Central')
    event3 = Eveniment(3, '21/10/2021', 'Festivitate de deschidere', 'La ora 18:00')
    event4 = Eveniment(4, '28/11/2021', 'Bal', 'In piata Mihai Viteazu.')
    test_repo_pers.store(person1)
    test_repo_pers.store(person2)
    test_repo_pers.store(person3)
    test_repo_event.store(event1)
    test_repo_event.store(event2)
    test_repo_event.store(event3)
    test_repo_event.store(event4)

    test_srv.create_participant(1, 1)
    test_srv.create_participant(1, 2)
    test_srv.create_participant(1, 3)
    test_srv.create_participant(1, 4)
    test_srv.create_participant(2, 4)
    test_srv.create_participant(3, 4)
    test_srv.create_participant(2, 3)
    test_srv.create_participant(2, 2)

    days_list = test_srv.days_with_most_participants()
    assert (len(days_list) == 3)
    assert (days_list[0][0] == '28/11/2021')
    assert (days_list[0][1] == 3)
    assert (days_list[2][0] == '25/10/2021')
    assert (days_list[2][1] == 2)

# test_ServiceParticipant_create_participant()
# test_ServiceParticipant_events_list_for_one_person()
# test_ServiceParticipant_events_list_for_one_person_organised_by_description()
# test_ServiceParticipant_events_list_for_one_person_organised_by_date()
# test_ServiceParticipant_participants_to_the_most_events()
# test_ServiceParticipant_events_with_most_participants()
# test_ServiceParticipant_days_with_most_participants()
