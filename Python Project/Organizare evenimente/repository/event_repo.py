from domain.entities import Eveniment


class InMemoryRepositoryEvent:
    def __init__(self):
        self.__event_list = []

    def store(self, event):
        self.__event_list.append(event)

    def get_all_events(self):
        return self.__event_list

    def find_event(self, id):
        """
        Gaseste evenimentul cu un anumit ID.
        :param id: id-ul evenimentului
        :return: eveimentul cu id-ul respectiv
        """
        for event in self.__event_list:
            if Eveniment.getID(event) == id:
                return event

    def find_event_position(self, id):
        """
        Gaseste pozitia evenimentului cu un anumit ID.
        :param id: id-ul care se afla la pozitia pe care vrem sa o gasim
        :return: pozitia evenimentului
        """
        index = 0
        for event in self.__event_list:
            if Eveniment.getID(event) == id:
                return index
            index += 1

    def validatorID(self, id, comand):
        """
        Verifica daca un eveniment cu acest ID se gaseste deja in lista si returneaza eroarea in functie de caz.
        :param id: id-ul evenimentului
        :type id: int
        :param comand: comanda
        :type comand: string
        :return:
        :raises: un text daca ID -ul e in lista, si alt text daca nu e.
        """
        id_list = [event for event in self.__event_list if Eveniment.getID(event) == id]
        errors = []
        if id_list != [] and comand == 'add':
            errors.append('Exista deja un eveniment cu acest ID.')
        elif id_list == []:
            if comand == 'delete' or comand == 'update' or comand == 'else':
                errors.append('Nu exista eveniment cu acest ID in lista.')
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def size(self):
        return len(self.get_all_events())

    def delete_event(self, the_event):
        """
        Sterge un eveniment din lista.
        :param the_event: evenimentul care urmeaza sa fie sters.
        :type the_event: string
        :return: lista dupa stergerea evenimentului
        """

        index = 0
        for event in self.__event_list:
            if Eveniment.getID(the_event) == Eveniment.getID(event):
                self.__event_list.pop(index)
            index += 1
        return self.__event_list

    def update_event(self, event, event_update):
        """
        Modifica datele unui eveniment.
        :param event: evenimentul care trebuie modificat
        :param event_update: modificarile efectuate
        :return: lista de evenimente dupa modificari.
        """
        index = 0
        for event in self.__event_list:
            if Eveniment.getID(event) == Eveniment.getID(event_update):
                self.__event_list[index] = event_update
            index += 1
        return self.__event_list

    def delete_all(self):
        self.__event_list = []


def test_InMemoryRepositoryEvent_store():
    test_repo = InMemoryRepositoryEvent()

    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    test_repo.store(event1)
    test_repo.store(event2)

    assert (len(test_repo.get_all_events()) == 2)
    assert (test_repo.get_all_events()[0].getID() == 1)
    assert (test_repo.get_all_events()[1].getData() == '25/10/2021')
    assert (test_repo.get_all_events()[0].getTip() == 'Meeting')
    assert (test_repo.get_all_events()[1].getDescriere() == 'In piata Mihai Viteazu.')


def test_InMemoryRepositoryEvent_find_event():
    test_repo = InMemoryRepositoryEvent()

    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    test_repo.store(event1)
    test_repo.store(event2)

    event = test_repo.find_event(2)
    assert (event.getData() == '25/10/2021')
    assert (event.getTip() == 'Team Building')


def test_InMemoryRepositoryEvent_ValidatorID():
    test_repo = InMemoryRepositoryEvent()

    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    event3 = Eveniment(3, '26/11/2021', 'Concurs', 'La Cluj Arena, ora 10:00.')
    test_repo.store(event1)
    test_repo.store(event2)
    test_repo.store(event3)
    id = 2
    cmd = 'add'
    try:
        test_repo.validatorID(id, cmd)
        assert False
    except ValueError:
        assert True

    id = 3
    try:
        test_repo.validatorID(id, cmd)
        assert False
    except ValueError:
        assert True


def test_InMemoryRepositoryEvent_delete_event():
    test_repo = InMemoryRepositoryEvent()

    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    event3 = Eveniment(3, '26/11/2021', 'Concurs', 'La Cluj Arena, ora 10:00.')
    test_repo.store(event1)
    test_repo.store(event2)
    test_repo.store(event3)
    events_list = test_repo.delete_event(event1)

    assert (len(events_list) == 2)
    assert (test_repo.get_all_events()[0].getID() == 2)
    assert (test_repo.get_all_events()[1].getID() == 3)


def test_InMemoryRepositoryEvent_update_event():
    test_repo = InMemoryRepositoryEvent()

    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    event2 = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    event3 = Eveniment(3, '26/11/2021', 'Concurs', 'La Cluj Arena, ora 10:00.')
    test_repo.store(event1)
    test_repo.store(event2)
    test_repo.store(event3)
    event_update = Eveniment(1, '2/11/2021', 'Bal', 'La Castelul din Carei.')
    events_list = test_repo.update_event(event1, event_update)

    assert (len(events_list) == 3)
    assert (test_repo.get_all_events()[0].getID() == 1)
    assert (test_repo.get_all_events()[0].getTip() == 'Bal')
    assert (test_repo.get_all_events()[0].getData() == '2/11/2021')


# test_InMemoryRepositoryEvent_store()
# test_InMemoryRepositoryEvent_find_event()
# test_InMemoryRepositoryEvent_ValidatorID()
# test_InMemoryRepositoryEvent_delete_event()
# test_InMemoryRepositoryEvent_update_event()


class FileRepositoryEvent:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        """
        Incarca din fisier.
        :return: lista de evenimente din fisier
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        lines = f.readlines()
        event_list = []


        # for line in lines:
        #     if len(line) > 3:
        #         id_event, data, tip, descriere = [token.strip() for token in line.split(';')]
        #         id_event = int(id_event)
        #
        #         event = Eveniment(id_event, data, tip, descriere)
        #         event_list.append(event)

        for i in range(0, len(lines) - 1, 4):
            new_line = lines[i:i + 4]
            id_event, data, tip, descriere = new_line
            id_event = id_event.replace('\n', '')
            id_event = int(id_event)
            data = data.replace('\n', '')
            tip = tip.replace('\n', '')
            descriere = descriere.replace('\n','')
            event = Eveniment(id_event, data, tip, descriere)
            event_list.append(event)


        f.close()
        return event_list

    def save_to_file(self, event_list):
        """
        Salveaza evenimente in fisier.
        :param event_list: lista de evenimente din fisier.
        :return:
        """
        with open(self.__filename, 'w') as f:
            for event in event_list:
                # event_string = str(event.getID()) + ';' + str(event.getData()) + ';' + str(
                #     event.getTip()) + ';' + str(event.getDescriere()) + '\n'
                event_string = str(event.getID()) + '\n' + str(event.getData()) + '\n' + str(
                    event.getTip()) + '\n' + str(event.getDescriere()) + '\n'
                f.write(event_string)

    # def find_event(self, id):
    #     """
    #     Cauta evenimentul in functie de id.
    #     :param id: id-ul evenimentului pe care il cauta.
    #     :return: evenimentul cautat
    #     """
    #     events_list = self.load_from_file()
    #     for event in events_list:
    #         if event.getID() == id:
    #             return event
    #     return None

    def find_event(self, id, index):
        """
        Cauta evenimentul in functie de id.
        :param id: id-ul evenimentului pe care il cauta.
        :return: evenimentul cautat
        """
        events_list = self.load_from_file()
        if index == len(events_list):
            return None
        elif events_list[index].getID() == id:
            return events_list[index]
        else:
            return self.find_event(id, index+1)

    def store(self, event):
        """
        Adauga un eveniment la lista din fisier.
        :param event: evenimentul pe care il adauga
        :return: - ; lista de evenimente se modifica
        """
        event_list = self.load_from_file()

        event_list.append(event)
        self.save_to_file(event_list)

    def validatorID(self, id, cmd):
        """
        Valideaza id ul unui eveniment
        :param id: id-ul evenimentului
        :param cmd: comanda in functie de care se genereaza eroarea.
        :return:
        :raises: ValueError daca id-ul se afla sau nu in lista in functie de caz
        """
        event_list = self.load_from_file()
        events_with_id = [event for event in event_list if event.getID() == id]
        errors = []
        if events_with_id != [] and cmd == 'add':
            errors.append("Evenimentul cu acest id a fost deja adaugat.")
        elif events_with_id == []:
            if cmd == 'delete' or cmd == 'update' or cmd == 'else':
                errors.append("Nu se gasesc evenimente cu acest id in lista.")

        if len(errors) != 0:
            erros_string = '\n'.join(errors)
            raise ValueError(erros_string)

    def get_all_events(self):
        """
        Returneaza lista cu toate evenimentele.
        :return:
        """
        return self.load_from_file()

    def size(self):
        """
        Redturneaza numarul de evenimente din lista.
        :return:
        """
        return len(self.load_from_file())

    def delete_event(self, event):
        """
        Sterge eveniment din lista din fisier.
        :param event: evenimentul care urmeaza sa fie sters.
        :return: list de evenimente dupa stergerea evenimentului
        """
        event_list = self.load_from_file()
        index = 0
        for ev in event_list:
            if Eveniment.getID(event) == Eveniment.getID(ev):
                event_list.pop(index)
            index += 1

        self.save_to_file(event_list)
        return self.load_from_file()

    def update_event(self, event, updated_event):
        """
        Modifica un eveniment din lista.
        :param event: evenimentul care trebuie modificat
        :param updated_event: evenimentul modificat
        :return: lista noua
        """
        event_list = self.load_from_file()
        index = 0
        for ev in event_list:
            if Eveniment.getID(event) == Eveniment.getID(ev):
                event_list[index] = updated_event
            index += 1

        self.save_to_file(event_list)
        return self.load_from_file()

    def delete_all(self):
        self.save_to_file([])
