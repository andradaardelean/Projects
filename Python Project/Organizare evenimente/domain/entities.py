import datetime


class Persoana:
    def __init__(self, IDpersoana, nume, adresa):
        self.__IDpersoana = IDpersoana
        self.__nume = nume
        self.__adresa = adresa

    def getIDpersoana(self):
        return self.__IDpersoana

    def getNume(self):
        return self.__nume

    def getAdresa(self):
        return self.__adresa

    def setIDpersoana(self, value):
        self.__IDpersoana = value

    def setNume(self, value):
        self.__nume = value

    def setAdresa(self, value):
        self.__adresa = value

    def __str__(self):
        return "ID persoana: " + str(self.__IDpersoana) + "; Nume: " + self.__nume + "; Adresa: " + self.__adresa

    def __eq__(self, other):
        """
        Verifica egalitatea intre doua persoane.
        :param other:
        :type other: persoana
        :return: True daca persoanele sunt egale si False daca nu sunt egale
        """
        if self.__IDpersoana == other.getIDpersoana() and self.__nume == other.getNume() and self.__adresa == other.getAdresa():
            return True
        return False


class Eveniment:
    def __init__(self, ID, data, tip, descriere):
        self.__ID = ID
        self.__data = data
        self.__tip = tip
        self.__descriere = descriere
        ID: int
        data: datetime
        tip: str
        descriere: str

    def getID(self):
        return self.__ID

    def getData(self):
        return self.__data

    def getTip(self):
        return self.__tip

    def getDescriere(self):
        return self.__descriere

    def getData_format(self):
        return datetime.datetime.strptime(self.__data, "%d/%m/%Y")

    def setID(self, value):
        self.__ID = value

    def setData(self, value):
        self.__data = value

    def setTip(self, value):
        self.__tip = value

    def setDescriere(self, value):
        self.__descriere = value

    # def __str__(self):
    #     return "ID : " + str(self.__ID) + "; Data: " + str(
    #         self.data) + "; Tip: " + self.__tip + "; Descriere: " + self.__descriere

    # def __str__(self):
    #     return f"Id: {self.__ID},"\
    #            f"{self.__data.strftime('%d/%m/%Y')},"\
    #            f"{self.__tip},"\
    #            f"{self.__descriere}"

    def __str__(self):
        return "ID : " + str(self.__ID) + "; Data: " + self.__data.strftime(
            '%d/%m/%Y') + "; Tip: " + self.__tip + "; Descriere: " + self.__descriere

    def __eq__(self, other):
        """
        Verifica egalitatea intre doua evenimente.
        :param other:
        :type other: eveniment
        :return: True daca eveniimentele sunt egale si False daca nu sunt egale
        """
        if self.__ID == other.getID() and self.__data == other.getData() and self.__tip == other.getTip():
            return True
        return False


class Participant:
    def __init__(self, person, event):
        self.__person = person
        self.__event = event

    def getPerson(self):
        return self.__person

    def getEvent(self):
        return self.__event

    def setPerson(self, value):
        self.__person = value

    def setEvent(self, value):
        self.__event = value

    def __eq__(self, other):
        if self.__person == other.__person and self.__event == other.__event:
            return True
        return False

    def __str__(self):
        return 'Persoana: [' + str(self.__person.getIDpersoana()) + '; ' + str(
            self.__person.getNume()) + ']' + 'Eveniment: [' + str(self.__event.getID()) + '; ' + str(
            self.__event.getTip()) + ']'


def test_create_person():
    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')

    assert (person1.getIDpersoana() == 1)
    assert (person1.getNume() == 'Ardelean Andrada')
    assert (person1.getAdresa() == 'Bd. Independentei')


def test_create_event():
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')

    assert (event1.getID() == 1)
    assert (event1.getData() == '24/10/2021')
    assert (event1.getTip() == 'Meeting')
    assert (event1.getDescriere() == 'Intalnire in parcul central.')


def test_create_participant():
    person = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    event = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')

    participant = Participant(person, event)
    assert (participant.getPerson() == person)
    assert (participant.getEvent() == event)


def test_equals_participant():
    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    event = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    participant1 = Participant(person1, event)
    participant2 = Participant(person1, event)

    assert (participant1 == participant2)

    person2 = Persoana(5, 'Ardelean Andrada', 'Bd. Independentei')
    participant3 = Participant(person2, event)

    assert (participant2 != participant3)


def test_equals_person():
    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    person2 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')

    assert (person1 == person2)

# test_create_person()
# test_create_event()
# test_equals_person()
# test_create_participant()
# test_equals_participant()
