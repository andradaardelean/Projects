from domain.entities import Eveniment
from domain.validators import ValidatorEveniment
from repository.event_repo import InMemoryRepositoryEvent


class ServiceEveniment:
    def __init__(self, repo_event, validator_event):
        """
        Initializeaza un obiect de top ServiceEveniment
        :param repo:
        :type repo: InMemoryRepository
        :param validator:
        :type validator: ValidatorEveniment
        """
        self.__repo_event = repo_event
        self.__validator_event = validator_event

    def get_all_events(self):
        return self.__repo_event.get_all_events()

    def generate_events(self):
        """
        Genereaza cateva evenimente
        :return:
        """
        event = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)

        event = Eveniment(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)

        event = Eveniment(8, '2/12/2021', 'Prezentare de arta', 'La muzeu, ora 17:30.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)

        event = Eveniment(10, '30/10/2021', 'Balul bobocilor', 'La casa de cultura.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)

        event = Eveniment(43, '17/9/2021', 'Concert', 'In centrul vechi. Ora 20:00.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)

        event = Eveniment(4, '22/11/2021', 'Street Music Festival', 'La centru vechi, ora 19:00.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)

        event = Eveniment(14, '12/12/2021', 'Revelion', 'Cabana in Somesul Rece.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)

        event = Eveniment(17, '9/7/2021', 'Festival', 'Pe plaja.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)

        event = Eveniment(79, '19/11/2021', 'Premiera film', 'La cinema-ul din Iulius Mall, ora 18:00.')
        self.__validator_event.validate(event)
        self.__repo_event.store(event)


    def add_event(self, id, data, tip, descriere):
        """
        Adauga eveniment la lista.
        :param id: id-ul evenimentului
        :type id: int
        :param data: data evenimentului
        :type data: string
        :param tip: tipul evenimentului
        :type tip: string
        :param descriere: descrierea evenimentului
        :type descriere: string
        :return:
        """
        event = Eveniment(id, data, tip, descriere)

        self.__validator_event.validate(event)
        self.__repo_event.store(event)

    def print_all_events(self):
        """
        Afiseaza toate evenimentele din lista.
        :return: lista de evenimente
        """
        return self.__repo_event.get_all_events()

    def validatorID(self,id,comand):
        """
        Verifica daca ID-ul introdus este unic sau mai apare undeva.
        :param id: id-ul evenimentului
        :type id: int
        :param comand: comanda pentru care se verifica
        :type comand: string
        :return:
        :raises: Un text daca cmd e add si ID ul ii apartine deja unui eveniment
                alt text daca cmd e delete sau update si ID-ul nu este in lista
        """
        self.__repo_event.validatorID(id,comand)

    def find_event(self,value,poz):
        """
        Cauta persoana in lista dupa criteriile value si poz.
        :param value: valoarea care se cauta in lista
        :type value: string
        :param poz: tipul valorii value, 0 = id, 1 = data, 2 = tipul, 3 = descrierea
        :type poz: int
        :return: lista cu persoanele gasite
        """
        if poz == 0:
            self.__validator_event.validate_ID(value)
            return [el for el in self.__repo_event.get_all_events() if el.getID() == value]
        if poz == 1:
            return [el for el in self.__repo_event.get_all_events() if el.getData() == value]
        elif poz == 2:
            self.__validator_event.validate_Tip(value)
            return [el for el in self.__repo_event.get_all_events() if el.getTip() == value]
        elif poz == 3:
            self.__validator_event.validate_Descriere(value)
            return [el for el in self.__repo_event.get_all_events() if el.getDescriere() == value]

        return self.__repo_event.find_event_by_value(value, poz)

    def find_event_position(self,id):
        """
        Gaseste pozitia evenimentului cu un anumit ID.
        :param id: id-ul evenimentului
        :type id: int
        :return: pozitia evenimentului
        """
        return self.__repo_event.find_event_position(id)

    def delete_event(self, id):
        """
        Sterge un eveniment din lista.
        :param id: id-ul evenimenntului
        :type id: int
        :return: lista dupa stergerea evenimentului cu id-ul respectiv
        """
        self.__validator_event.validate_ID(id)
        # event = self.__repo_event.find_event(id)
        event = self.__repo_event.find_event(id,0)

        new_event_list = self.__repo_event.delete_event(event)

        return new_event_list

    def update_event(self, id, data, tip, descriere):
        """
        Creeaza noul eveniment si il inlocuieste pe cel vechi cu cel nou.
        :param id: id-ul evenimentului
        :type id: int
        :param data: data evenimentului
        :type data: string
        :param tip: tipul evenimentului
        :type tip: string
        :param descriere: descrierea evenimentului
        :type deescriere: string
        :return: lista dupa modificare
        """

        self.__validator_event.validate_ID(id)
        # event = self.__repo_event.find_event(id)
        event = self.__repo_event.find_event(id,0)

        event_update = Eveniment(id,data,tip,descriere)
        new_events_list = self.__repo_event.update_event(event, event_update)
        return new_events_list



def test_ServiceEveniment_add_event():
    repo = InMemoryRepositoryEvent()
    validator = ValidatorEveniment()
    test_srv = ServiceEveniment(repo, validator)


    test_srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    assert (test_srv.get_all_events()[0].getID() == 1)
    assert (test_srv.get_all_events()[0].getData() == '24/10/2021')
    assert (test_srv.get_all_events()[0].getTip() == 'Meeting')
    assert (test_srv.get_all_events()[0].getDescriere() == 'Intalnire in parcul central.')

    assert (len(test_srv.get_all_events()) == 1)

    try:
        test_srv.add_event(-5, '35/10/2021', 'Te', 'In piata Mihai Viteazu.')
        assert False
    except ValueError:
        assert True

def test_ServiceEveniment_get_all_events():
    repo = InMemoryRepositoryEvent()
    validator = ValidatorEveniment()
    test_srv = ServiceEveniment(repo, validator)

    test_srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    test_srv.add_event(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    assert (type(test_srv.get_all_events()) == list)
    assert (len(test_srv.get_all_events()) == 2)

def test_ServiceEveniment_ValidatorID():
    repo = InMemoryRepositoryEvent()
    validator = ValidatorEveniment()
    test_srv = ServiceEveniment(repo, validator)
    test_srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')

    try:
        test_srv.validatorID(1,'add')
        assert False
    except ValueError:
        assert True

    try:
        test_srv.validatorID(2, 'delete')
        assert False
    except ValueError:
        assert True

    try:
        test_srv.validatorID(3, 'update')
        assert False
    except ValueError:
        assert True

def test_ServiceEveniment_find_event():
    repo = InMemoryRepositoryEvent()
    validator = ValidatorEveniment()
    test_srv = ServiceEveniment(repo, validator)
    test_srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    test_srv.add_event(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')
    test_srv.add_event(3, '24/10/2021', 'Meeting', 'Intalnire in centru.')

    try:
        test_srv.find_event(-5,0)
        assert False
    except ValueError:
        assert True

    try:
        test_srv.find_event('A', 2)
        assert False
    except ValueError:
        assert True

    event_gasite = test_srv.find_event('24/10/2021',1)
    assert (len(event_gasite) == 2)
    assert (event_gasite[0].getTip() == 'Meeting')
    assert (event_gasite[1].getData() == '24/10/2021')
    assert (event_gasite[0].getDescriere() == 'Intalnire in parcul central.')

    event_gasite = test_srv.find_event('Team Building', 2)
    assert (len(event_gasite) == 1)
    assert (event_gasite[0].getTip() == 'Team Building')
    assert (event_gasite[0].getData() == '25/10/2021')

def test_ServiceEveniment_delete_event():
    repo = InMemoryRepositoryEvent()
    validator = ValidatorEveniment()
    test_srv = ServiceEveniment(repo, validator)
    test_srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    test_srv.add_event(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')

    assert (len(test_srv.get_all_events()) == 2)

    test_srv.delete_event(1)
    assert (len(test_srv.get_all_events()) == 1)

    test_srv.delete_event(2)
    assert (len(test_srv.get_all_events()) == 0)

def test_ServiceEveniment_update_event():
    repo = InMemoryRepositoryEvent()
    validator = ValidatorEveniment()
    test_srv = ServiceEveniment(repo, validator)
    test_srv.add_event(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    test_srv.add_event(2, '25/10/2021', 'Team Building', 'In piata Mihai Viteazu.')

    test_srv.update_event(2, '27/11/2021', 'Bal mascat', 'La casa de cultura.')
    assert (test_srv.get_all_events()[1].getData() == '27/11/2021')
    assert (test_srv.get_all_events()[1].getTip() == 'Bal mascat')
    assert (test_srv.get_all_events()[1].getDescriere() == 'La casa de cultura.')


# test_ServiceEveniment_add_event()
# test_ServiceEveniment_get_all_events()
# test_ServiceEveniment_ValidatorID()
# test_ServiceEveniment_find_event()
# test_ServiceEveniment_delete_event()
# test_ServiceEveniment_update_event()
