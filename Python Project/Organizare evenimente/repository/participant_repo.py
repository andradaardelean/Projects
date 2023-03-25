import datetime

from domain.entities import Persoana, Eveniment, Participant


class InMemoryRepositoryParticipant:
    def __init__(self):
        self.__participants = []

    def get_all_participants(self):
        return self.__participants

    def store_participant(self, participant):
        """
        Inscrie o persoana la un eveniment.
        :param pers_id: id-ul persoanei care va fi inscrisa.
        :type pers_id: int
        :param event_id: id-ul evenimentului la care se inscrie persoana.
        :type event_id: int
        :return:
        :raises: ValueError daca participantul nu se gaseste in lista
        """
        p = self.find_participant(participant)
        # if p is None:
        #     raise ValueError('Participantul nu se gaseste in lista.')
        self.__participants.append(participant)

    def delete_all_participants(self):
        """
        Sterge toti participantii din lista.
        :return:
        """
        self.__participants = []

    def find_participant(self, p):
        """
        Gaseste un participant in lista dupa numarul de participant.
        :param nr_p: numarul de participant.
        :type nr_p: int
        :return:
        """
        for participant in self.__participants:
            if p == participant:
                return participant
        return None

    def validator_participant(self, person, event):
        """
        Verifica daca un participant exista deja sau nu.
        :param person: o persoana
        :param event: un eveniment
        :return:
        :raises: ValueError daca persoana este deja inregistrata
        """
        participant = Participant(person, event)
        if participant in self.__participants:
            raise ValueError("Persoana a fost deja inscrisa la evenimentul acesta.")

    def events_list_for_one_person(self, person):
        """
        Gaseste lista de evenimente la care participa o persoana.
        :param person: o persoana
        :return: lista de evenimente
        """
        participant_list = [participant for participant in self.__participants if participant.getPerson() == person]
        events_list = []
        for participant in participant_list:
            events_list.append(participant.getEvent())

        return events_list

    def participants_for_one_event(self, event):
        """
        Gaseste lista cu persoanele care participa la un eveniment.
        :param event: eveniment
        :return: lista cu persoane
        """
        events_list = [participant for participant in self.__participants if participant.getEvent() == event]
        persons_list = []
        for participant in events_list:
            persons_list.append(participant.getPerson())

        return persons_list


def test_InMemoryRepositoryParticipants_store():
    test_repo = InMemoryRepositoryParticipant()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    participant1 = Participant(person1, event1)
    participant2 = Participant(person2, event2)
    test_repo.store_participant(participant1)
    test_repo.store_participant(participant2)

    assert (len(test_repo.get_all_participants()) == 2)
    assert (test_repo.get_all_participants()[0].getPerson().getNume() == 'Ardelean Andrada')
    assert (test_repo.get_all_participants()[1].getEvent().getTip() == 'Team Building')

def test_InMemoryRepositoryParticipant_find_participant():
    test_repo = InMemoryRepositoryParticipant()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    participant1 = Participant(person1, event1)
    participant2 = Participant(person2, event2)
    test_repo.store_participant(participant1)
    test_repo.store_participant(participant2)

    participant = test_repo.find_participant(participant1)
    assert (participant.getPerson().getNume() == 'Ardelean Andrada')
    assert (participant.getEvent().getTip() == 'Meeting')

    participant = test_repo.find_participant(participant2)
    assert (participant.getPerson().getAdresa() == 'Bd. Libertatii')
    assert (participant.getEvent().getData() == '25/10/2021')

def test_InMemoryRepositoryParticipant_validator_participant():
    test_repo = InMemoryRepositoryParticipant()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    participant1 = Participant(person1, event1)
    participant2 = Participant(person2, event2)
    test_repo.store_participant(participant1)
    test_repo.store_participant(participant2)

    person3 = Persoana(3, 'Acas George', 'Bd. Libertatii')
    event3 = Eveniment(4, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    test_repo.validator_participant(person3, event3)

    try:
        test_repo.validator_participant(person1, event1)
        assert False
    except ValueError:
        assert True

    try:
        test_repo.validator_participant(person2, event2)
        assert False
    except ValueError:
        assert True


def test_InMemoryRepositoryParticipants_events_list_for_one_person():
    test_repo = InMemoryRepositoryParticipant()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    participant1 = Participant(person1, event1)
    participant2 = Participant(person2, event2)
    participant3 = Participant(person1, event2)

    test_repo.store_participant(participant1)
    test_repo.store_participant(participant2)
    test_repo.store_participant(participant3)

    events_list = test_repo.events_list_for_one_person(person1)
    assert (len(events_list) == 2)
    assert (events_list[0].getTip() == 'Meeting')
    assert (events_list[1].getDescriere() == 'In piata Mihai Viteazu.')

    events_list = test_repo.events_list_for_one_person(person2)
    assert (len(events_list) == 1)
    assert (events_list[0].getData() == '25/10/2021')

def test_InMemoryRepositoryParticipants_participants_for_one_event():
    test_repo = InMemoryRepositoryParticipant()

    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(2, 'Acas George', 'Bd. Libertatii')
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    participant1 = Participant(person1, event1)
    participant2 = Participant(person2, event2)
    participant3 = Participant(person1, event2)

    test_repo.store_participant(participant1)
    test_repo.store_participant(participant2)
    test_repo.store_participant(participant3)

    person_list = test_repo.participants_for_one_event(event1)
    assert (len(person_list) == 1)
    assert (person_list[0].getNume() == 'Ardelean Andrada')

    person_list = test_repo.participants_for_one_event(event2)
    assert (len(person_list) == 2)
    assert (person_list[0].getIDpersoana() == 2)
    assert (person_list[0].getNume() == 'Acas George')
    assert (person_list[1].getAdresa() == 'Bd. Independentei')

# test_InMemoryRepositoryParticipants_store()
# test_InMemoryRepositoryParticipant_find_participant()
# test_InMemoryRepositoryParticipant_validator_participant()
# test_InMemoryRepositoryParticipants_events_list_for_one_person()
# test_InMemoryRepositoryParticipants_participants_for_one_event()


class FileRepositoryParticipant(InMemoryRepositoryParticipant):
    def __init__(self, filename):
        InMemoryRepositoryParticipant.__init__(self)
        self.__filename = filename
        self.load_from_file()

    def load_from_file(self):
        """
        Incarca datele din fisier.
        :return: lista de participantii din fisier
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        lines = f.readlines()

        # for line in lines:
        #     if len(line) > 1:
        #         person, event = [token.strip() for token in line.split(';')]
        #         id_person, nume, adresa = [token.strip() for token in person.split(' - ')]
        #         id_event, data, tip, descriere = [token.strip() for token in event.split(' - ')]
        #         id_person = int(id_person)
        #         id_event = int(id_event)
        #
        #         pers = Persoana(id_person, nume, adresa)
        #         ev = Eveniment(id_event, data, tip, descriere)
        #         participant = Participant(pers, ev)
        #         InMemoryRepositoryParticipant.store_participant(self, participant)

        for i in range(0, len(lines)-1, 2):
            new_line = lines[i:i+2]
            person, event = new_line
            person = person.replace('\n','')
            event = event.replace('\n','')

            id_person, nume, adresa = [token.strip() for token in person.split(' - ')]
            id_event, data, tip, descriere = [token.strip() for token in event.split(' - ')]
            id_person = int(id_person)
            id_event = int(id_event)

            pers = Persoana(id_person, nume, adresa)
            ev = Eveniment(id_event, data, tip, descriere)
            participant = Participant(pers, ev)
            InMemoryRepositoryParticipant.store_participant(self, participant)

        f.close()

    def save_to_file(self):
        """
        Salveaza evenimente in fisier.
        :param event_list: lista de evenimente din fisier.
        :return:
        """
        participants = InMemoryRepositoryParticipant.get_all_participants(self)
        with open(self.__filename, 'w') as f:
            for participant in participants:
                # participant_string = str(participant.getPerson().getIDpersoana()) + ' - ' + str(
                #     participant.getPerson().getNume()) + ' - ' + str(participant.getPerson().getAdresa()) + ';' + str(
                #     participant.getEvent().getID()) + ' - ' + str(participant.getEvent().getData()) + ' - ' + str(
                #     participant.getEvent().getTip()) + ' - ' + str(participant.getEvent().getDescriere()) + '\n'
                participant_string = str(participant.getPerson().getIDpersoana()) + ' - ' + str(
                    participant.getPerson().getNume()) + ' - ' + str(participant.getPerson().getAdresa()) + '\n' + str(
                    participant.getEvent().getID()) + ' - ' + str(participant.getEvent().getData()) + ' - ' + str(
                    participant.getEvent().getTip()) + ' - ' + str(participant.getEvent().getDescriere()) + '\n'
                f.write(participant_string)

    def get_all_participants(self):
        """
        Returneaza o lista cu toti participantii.
        :return: lista cu participantii
        :rtype: list of Participants objects
        """
        return InMemoryRepositoryParticipant.get_all_participants(self)

    def find_participant(self, p):
        """
        Cauta participant in lista
        :param r: participant-ul cautat
        :type r: Participant
        :return: participantul-ul cautat daca exista in lista, None altfel
        :rtype: Participant
        """
        return InMemoryRepositoryParticipant.find_participant(self, p)

    def store_participant(self, participant):
        """
        Inscrie o persoana la un eveniment.
        :param pers_id: id-ul persoanei care va fi inscrisa.
        :type pers_id: int
        :param event_id: id-ul evenimentului la care se inscrie persoana.
        :type event_id: int
        :return:
        :raises: ValueError daca participantul nu se gaseste in lista
        """
        InMemoryRepositoryParticipant.store_participant(self, participant)
        self.save_to_file()

    def delete_all_participants(self):
        """
        Sterge toti participantii din lista.
        :return:
        """
        InMemoryRepositoryParticipant.delete_all_participants(self)
        self.save_to_file()

    def validator_participant(self, person, event):
        """
        Verifica daca un participant exista deja sau nu.
        :param person: o persoana
        :param event: un eveniment
        :return:
        :raises: ValueError daca persoana este deja inregistrata
        """
        participant = Participant(person, event)
        participants = InMemoryRepositoryParticipant.get_all_participants(self)
        if participant in participants:
            raise ValueError("Persoana a fost deja inscrisa la evenimentul acesta.")

    def events_list_for_one_person(self, person):
        """
        Gaseste lista de evenimente la care participa o persoana.
        :param person: o persoana
        :return: lista de evenimente
        """
        return InMemoryRepositoryParticipant.events_list_for_one_person(self, person)

    def participants_for_one_event(self, event):
        """
        Gaseste lista cu persoanele care participa la un eveniment.
        :param event: eveniment
        :return: lista cu persoane
        """
        return InMemoryRepositoryParticipant.participants_for_one_event(self, event)
