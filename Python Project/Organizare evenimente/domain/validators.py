import datetime

from domain.entities import Persoana, Eveniment


class ValidatorPersoana:
    def validate(self, persoana):
        errors = []
        if persoana.getIDpersoana() < 0 or persoana.getIDpersoana() > 1000:
            errors.append('ID-ul este invalid!')
        if len(persoana.getNume()) < 3:
            errors.append('Numele este invalid!')
        if len(persoana.getAdresa()) < 3:
            errors.append('Adresa este invalida!')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def validate_IDpersoana(self, id):
        if id < 0 or id > 1000:
            raise ValueError("ID-ul este invalid!")

    def validate_Nume(self, nume):
        if len(nume) < 3:
            raise ValueError('Numele este invalid!')

    def validate_Adresa(self, adresa):
        if len(adresa) < 3:
            raise ValueError('Adresa este invalida!')


class ValidatorEveniment:
    def validate(self, eveniment):
        errors = []
        if eveniment.getID() < 0 or eveniment.getID() > 1000:
            errors.append('ID-ul este invalid!')
        if len(eveniment.getTip()) < 2:
            errors.append('Tipul evenimentului este invalid!')
        if len(eveniment.getDescriere()) < 3:
            errors.append('Descrierea este prea scurta!')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def validate_ID(self, id):
        if id < 0 or id > 1000:
            raise ValueError("ID-ul este invalid!")

    def validate_Data(self,data):
        format = "%d/%m/%Y"
        if bool(datetime.datetime.strptime(data, format)) == False:
            raise ValueError("Data introdusa este invalida!")

    def validate_Tip(self,tip):
        if len(tip) < 2:
            raise ValueError('Tipul evenimentului este invalid!')

    def validate_Descriere(self,descriere):
        if len(descriere) < 2:
            raise ValueError('Descrierea evenimentului este invalida!')

def test_ValidatorPersoana():
    test_validator = ValidatorPersoana()
    person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
    test_validator.validate(person1)
    person2 = Persoana(2, '', 'Bd. Lucian Blaga')

    try:
        test_validator.validate(person2)
        assert False
    except ValueError:
        assert True

    person3 = Persoana(-5, 'Stan David', 'Bd. Lucian Blaga')
    try:
        test_validator.validate(person3)
        assert False
    except ValueError:
        assert True

    person4 = Persoana(2, 'Stan David', '')
    try:
        test_validator.validate(person4)
        assert False
    except ValueError:
        assert True

def test_ValidatorEveniment():
    test_validator = ValidatorEveniment()
    event1 = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    test_validator.validate(event1)
    event2 = Eveniment(21233, '40/10/2021', 'Meeting', 'Intalnire in parcul central.')

    try:
        test_validator.validate(event2)
        assert False
    except ValueError:
        assert True

    event3 = Eveniment(1, '24/10/2021', '','Intalnire in parcul central.')
    try:
        test_validator.validate(event3)
        assert False
    except ValueError:
        assert True

    event4 = Eveniment(1, '24/10/2021', 'Meeting','In')
    try:
        test_validator.validate(event4)
        assert False
    except ValueError:
        assert True

def test_ValidatorPersoana_IDpersoana():
    person1 = Persoana(-5, 'Ardelean Andrada', 'Bd. Independentei')
    test_validator = ValidatorPersoana()
    try:
        test_validator.validate_IDpersoana(person1.getIDpersoana())
        assert False
    except ValueError:
        assert True

def test_ValidatorPersoana_Nume():
    person1 = Persoana(5, 'Ar', 'Bd. Independentei')
    test_validator = ValidatorPersoana()
    try:
        test_validator.validate_Nume(person1.getNume())
        assert False
    except ValueError:
        assert True

def test_ValidatorPersoana_Adresa():
    person1 = Persoana(5, 'Ardelean Andrada', 'Bd')
    test_validator = ValidatorPersoana()
    try:
        test_validator.validate_Adresa(person1.getAdresa())
        assert False
    except ValueError:
        assert True

def test_ValidatorEveniment_ID():
    event1 = Eveniment(-5, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
    test_validator = ValidatorEveniment()
    try:
        test_validator.validate_ID(event1.getID())
        assert False
    except ValueError:
        assert True

def test_ValidatorEveniment_Data():
    event1 = Eveniment(5, '44/104/2021', 'Meeting', 'Intalnire in parcul central.')
    test_validator = ValidatorEveniment()
    try:
        test_validator.validate_Data(event1.getData())
        assert False
    except ValueError:
        assert True

def test_ValidatorEveniment_Tip():
    event1 = Eveniment(5, '24/10/2021', 'M', 'Intalnire in parcul central.')
    test_validator = ValidatorEveniment()
    try:
        test_validator.validate_Tip(event1.getTip())
        assert False
    except ValueError:
        assert True

def test_ValidatorEveniment_Descriere():
    event1 = Eveniment(5, '24/10/2021', 'Meeting', '.')
    test_validator = ValidatorEveniment()
    try:
        test_validator.validate_Descriere(event1.getDescriere())
        assert False
    except ValueError:
        assert True

# test_ValidatorPersoana()
# test_ValidatorEveniment()
# test_ValidatorPersoana_IDpersoana()
# test_ValidatorPersoana_Nume()
# test_ValidatorPersoana_Adresa()
# test_ValidatorEveniment_ID()
# test_ValidatorEveniment_Data()
# test_ValidatorEveniment_Tip()
# test_ValidatorEveniment_Descriere()
