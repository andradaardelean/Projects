import datetime
import random

from termcolor import colored

from domain.entities import Persoana, Eveniment

from random import *
import string


class Console:
    def __init__(self, srv_pers, srv_event, srv_participant):
        self.__srv_pers = srv_pers
        self.__srv_event = srv_event
        self.__srv_participant = srv_participant

    def __add_person(self):
        try:
            id = int(input(colored('ID-ul persoanei:', 'grey')))
            self.__srv_pers.validatorID(id,'add')
            nume = input(colored("Numele persoanei: ", 'grey'))
            adresa = input(colored("Adresa persoanei: ", 'grey'))
            try:
                self.__srv_pers.add_person(id, nume, adresa)
                print(colored('Persoana a fost adaugata cu succes!', 'cyan'))
            except ValueError as ve:
                print(colored(str(ve), 'red'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __generate_person(self):
        try:
            nr = int(input(colored('Introduceti numarul:', 'grey')))
            for i in range(nr):
                id = randint(0, 1000)
                self.__srv_pers.validatorID(id,'add')
                nume = self.__srv_pers.random_string_person(randint(3,30))
                adresa = self.__srv_pers.random_string_person(randint(3,30))
                try:
                    self.__srv_pers.add_person(id, nume, adresa)
                    print(colored('Persoana a fost adaugata cu succes!', 'cyan'))
                except ValueError as ve:
                    print(colored(str(ve), 'red'))
        except ValueError:
            print(colored('Trebuie sa introduceti un numar!','red'))

    def __print_all_persons(self):
        person_list = self.__srv_pers.get_all_persons()
        if len(person_list) == 0:
            print(colored("Nu exista persoane in lista!", 'red'))
        else:
            print(colored("Lista de persoane este:", 'magenta'))
            for person in person_list:
                print('Id:', colored(Persoana.getIDpersoana(person), 'cyan'), ' - Nume:',
                      colored(Persoana.getNume(person), 'cyan'), ' - Adresa:',
                      colored(Persoana.getAdresa(person), 'cyan'))

    def __delete_person(self):
        person_list = self.__srv_pers.get_all_persons()
        if len(person_list) == 0:
            print(colored("Nu exista persoane in lista!", 'red'))
        else:
            try:
                id = int(input(colored('ID-ul persoanei:', 'grey')))
                self.__srv_pers.validatorID(id,'delete')
                try:
                    self.__srv_pers.delete_person(id)
                    print(colored("Persoana stearsa cu succes!", 'cyan'))
                except ValueError:
                    print(colored('ID-ul este invalid!', 'red'))
            except ValueError as ve:
                print(colored(str(ve), 'red'))

    def __update_person(self):
        try:
            id = int(input(colored('ID-ul persoanei:', 'grey')))
            self.__srv_pers.validatorID(id,'update')
            nume = input(colored("Numele persoanei: ", 'grey'))
            adresa = input(colored("Adresa persoanei: ", 'grey'))
            try:
                self.__srv_pers.update_person(id, nume, adresa)
                print(colored('Datele persoanei au fost modificate cu succes!', 'cyan'))
            except ValueError as ve:
                print(colored(str(ve), 'red'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __find_person(self):
        print(colored('Pentru a cauta in functie de ID, introduceti 0.','magenta'))
        print(colored('Pentru a cauta in functie de nume, introduceti 1.','magenta'))
        print(colored('Pentru a cauta in functie de adresa, introduceti 2.','magenta'))
        try:
            poz = int(input(colored('Introduceti numarul:','grey')))
            if poz == 0:
                try:
                    value = int(input(colored('Introduceti valoarea:','grey')))
                except ValueError:
                    print(colored('Trebuie sa se introduca un numar', 'red'))
            elif poz == 1 or poz == 2:
                value = input(colored('Introduceti valoarea:', 'grey'))
            else:
                print(colored('Pozitie invalida!','red'))
        except ValueError:
            print(colored('Trebuie sa se introduca un numar', 'red'))

        if poz == 0 or poz == 1 or poz == 2:
            person_list = self.__srv_pers.find_person(value, poz)
            if len(person_list) == 0:
                if poz == 0:
                    print(colored('Nu se gasesc persoane cu acest ID in lista!', 'red'))
                elif poz == 1:
                    print(colored('Nu se gasesc persoane cu acest nume in lista!', 'red'))
                elif poz == 2:
                    print(colored('Nu se gasesc persoane cu aceasta adresa in lista!', 'red'))
            else:
                print(colored('Persoanele cautate sunt:', 'magenta'))
                for person in person_list:
                    print('Id:', colored(Persoana.getIDpersoana(person), 'cyan'), ' - Nume:',
                          colored(Persoana.getNume(person), 'cyan'), ' - Adresa:',
                          colored(Persoana.getAdresa(person), 'cyan'))

    def __print_all_participants(self):
        participants = self.__srv_participant.get_all_participants()
        if len(participants) == 0:
            print(colored('Nu sunt persoane inscrise la evenimente!','red'))
        else:
            print(colored('Lista cu persoanele inscrise este:','magenta'))
            for participant in participants:
                print('Persoana cu id-ul:',colored(participant.getPerson().getIDpersoana(),'cyan'), 'si cu numele:',
                      colored(participant.getPerson().getNume(),'cyan'), 'este inscrisa la evenimentul cu id-ul:',
                      colored(participant.getEvent().getID(),'cyan'), 'si de tip:',
                      colored(participant.getEvent().getTip(),'cyan'))

    def __sign_up_person(self):
        try:
            person_id = int(input(colored('Introduceti ID-ul persoanei:', 'grey')))
            event_id = int(input(colored('Introduceti ID-ul evenimentului:', 'grey')))
            self.__srv_participant.create_participant(person_id, event_id)
            print(colored('Persoana a fost inscrisa cu succes!', 'cyan'))
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __events_list_for_one_person_organised_by_description(self):
        person_id = int(input(colored('Introduceti ID-ul persoanei:','grey')))
        try:
            events_list = self.__srv_participant.events_list_for_one_person_organised_by_description(person_id)
            if len(events_list) != 0:
                print(colored('Lista cu evenimentele la care participa persoana cu id-ul','magenta'),
                      colored(person_id,'cyan'), colored('ordonata aflabetic dupa descriere este:','magenta'))
                for event in events_list:
                    print('Id:', colored(Eveniment.getID(event), 'cyan'), ' - Data:',
                          colored(Eveniment.getData(event), 'cyan'), ' - Tip:',
                          colored(Eveniment.getTip(event), 'cyan'), ' - Descriere:',
                          colored(Eveniment.getDescriere(event), 'cyan'))
            else:
                print(colored("Persoana cu acest ID nu este inscrisa la niciun eveniment",'red'))
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __events_list_for_one_person_organised_by_date(self):
        person_id = int(input(colored('Introduceti ID-ul persoanei:', 'grey')))
        try:
            events_list = self.__srv_participant.events_list_for_one_person_organised_by_date(person_id)
            if len(events_list) != 0:
                print(colored('Lista cu evenimentele la care participa persoana cu id-ul', 'magenta'),
                      colored(person_id, 'cyan'), colored('ordonata dupa data este:', 'magenta'))
                for event in events_list:
                    print('Id:', colored(Eveniment.getID(event), 'cyan'), ' - Data:',
                          colored(Eveniment.getData(event), 'cyan'), ' - Tip:',
                          colored(Eveniment.getTip(event), 'cyan'), ' - Descriere:',
                          colored(Eveniment.getDescriere(event), 'cyan'))
            else:
                print(colored("Persoana cu acest ID nu este inscrisa la niciun eveniment", 'red'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __participants_to_the_most_events(self):
        try:
            persons_list = self.__srv_participant.participants_to_the_most_events()
            if len(persons_list) != 0:
                print(colored('Lista cu persoanele care participa la cele mai multe evenimente este:','magenta'))
                for person in persons_list:
                    print('Id:', colored(Persoana.getIDpersoana(person), 'cyan'), ' - Nume:',
                          colored(Persoana.getNume(person), 'cyan'), ' -Adresa:',
                          colored(Persoana.getAdresa(person), 'cyan'))
            else:
                print(colored("Nu sunt peroane participante la evenimente!",'red'))
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __events_with_most_participants(self):
        try:
            events_list = self.__srv_participant.events_with_most_participants()
            if len(events_list) != 0:
                print(colored('Primele 20% evenimente cu cei mai multi participanti:','magenta'))
                for event in events_list:
                    print('Evenimentul cu descrierea: ', colored(event.getDescriere(),'cyan'), 'are', colored(
                        len(self.__srv_participant.participants_for_one_event(event.getID())),'cyan'), 'participanti.')
            else:
                print(colored("Nu sunt persoane participante la evenimente!",'red'))
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __days_with_most_participants(self):
        try:
            lista_date = self.__srv_participant.days_with_most_participants()
            print(colored('Primele 3 zile cu cei mai multi participanti sunt.','magenta'))
            if len(lista_date) == 3:
                for el in lista_date:
                    print('In data de', colored(el[0],'cyan'),'participa la evenimete',colored(el[1],'cyan'),'persoane.')
            else:
                print(colored("Nu sunt persoane participante la evenimente!",'red'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __find_event(self):
        print(colored('Pentru a cauta in functie de ID, introduceti 0.', 'magenta'))
        print(colored('Pentru a cauta in functie de data, introduceti 1.', 'magenta'))
        print(colored('Pentru a cauta in functie de tip, introduceti 2.', 'magenta'))
        print(colored('Pentru a cauta in functie de descriere, introduceti 3.', 'magenta'))
        try:
            poz = int(input(colored('Introduceti numarul:','grey')))
            if poz == 0:
                try:
                    value = int(input(colored('Introduceti ID-ul:','grey')))
                except ValueError:
                    print(colored('Trebuie sa se introduca un numar', 'red'))
            elif poz == 1:
                try:
                    zi = int(input(colored('Ziua evenimentului:', 'grey')))
                    luna = int(input(colored('Luna evenimentului:', 'grey')))
                    an = int(input(colored('Anul evenimentului:', 'grey')))
                    value = datetime.date(an, luna, zi)
                except ValueError:
                    print(colored('Data introdusa este invalida!', 'red'))
            elif poz == 2:
                value = input(colored('Introduceti tipul:', 'grey'))
            elif poz == 3:
                value = input(colored('Introduceti descrierea:', 'grey'))
            else:
                print(colored('Pozitie invalida!','red'))
        except ValueError:
            print(colored('Trebuie sa se introduca un numar', 'red'))

        if poz == 0 or poz == 1 or poz == 2 or poz == 3:
            events_list = self.__srv_event.find_event(value, poz)
            if len(events_list) == 0:
                if poz == 0:
                    print(colored('Nu se gasesc evenimente cu acest ID in lista!', 'red'))
                elif poz == 1:
                    print(colored('Nu se gasesc evenimente cu aceasta data in lista!', 'red'))
                elif poz == 2:
                    print(colored('Nu se gasesc evenimente cu acest tip in lista!', 'red'))
                elif poz == 3:
                    print(colored('Nu se gasesc evenimente cu aceasta descriere in lista!', 'red'))
            else:
                print(colored('Evenimentele cautate sunt:', 'magenta'))
                for event in events_list:
                    print('Id:', colored(Eveniment.getID(event), 'cyan'), ' - Data:',
                          colored(Eveniment.getData(event), 'cyan'), ' - Tip:',
                          colored(Eveniment.getTip(event), 'cyan'), ' - Descriere:',
                          colored(Eveniment.getDescriere(event), 'cyan'))

    def __add_event(self):

        try:
            id = int(input(colored('ID-ul evenimentului:', 'grey')))
            self.__srv_event.validatorID(id,'add')
            # try:
                # zi = int(input(colored('Ziua evenimentului:', 'grey')))
                # luna = int(input(colored('Luna evenimentului:', 'grey')))
                # an = int(input(colored('Anul evenimentului:', 'grey')))
            #     data = datetime.strptime(input("Data evenimentului"), '%d/%m/%Y')
            # except ValueError:
            #     print(colored('Trebuie sa se introduca numere', 'red'))
            try:
                data = input(colored("Data evenimentului:",'grey'))
                datetime.datetime.strptime(data, '%d/%m/%Y').date()
                # ora = input("ora:")
                # ora = datetime.datetime.strptime(ora, '%H:%M').time()
                # print(ora)
                tip = input(colored('Tipul evenimentului:', 'grey'))
                descriere = input(colored('Descrierea evenimentului:', 'grey'))
                try:
                    self.__srv_event.add_event(id, data, tip, descriere)
                    print(colored('Evenimentul a fost adaugata cu succes!', 'cyan'))
                except ValueError as ve:
                    print(colored(str(ve), 'red'))
            except ValueError:
                print(colored('Data introdusa este invalida','red'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __print_all_events(self):
        events_list = self.__srv_event.print_all_events()

        if len(events_list) == 0:
            print(colored("Nu exista evenimente in lista!", 'red'))
        else:
            print(colored("Lista de evenimente este:", 'magenta'))
            for event in events_list:
                print('Id:', colored(Eveniment.getID(event), 'cyan'), ' - Data:',
                      colored(Eveniment.getData(event), 'cyan'), ' - Tip:',
                      colored(Eveniment.getTip(event), 'cyan'),' - Descriere:',
                      colored(Eveniment.getDescriere(event), 'cyan'))

    def __delete_event(self):
        try:
            id = int(input(colored('ID-ul evenimentului:','grey')))
        except ValueError:
            print(colored('ID-ul este invalid!', 'red'))
        events_list = self.__srv_event.get_all_events()
        if len(events_list) == 0:
            print(colored("Nu exista evenimente in lista!", 'red'))
        else:
            try:
                self.__srv_event.validatorID(id,'delete')
                try:
                    self.__srv_event.delete_event(id)
                    print(colored("Eveniment sters cu succes!", 'cyan'))
                except ValueError:
                    print(colored('ID-ul este invalid!', 'red'))
            except ValueError as ve:
                print(colored(str(ve), 'red'))

    def __update_event(self):
        try:
            id = int(input(colored('ID-ul evenimentului:', 'grey')))
            self.__srv_event.validatorID(id,'update')
            try:
                zi = int(input(colored('Ziua evenimentului:', 'grey')))
                luna = int(input(colored('Luna evenimentului:', 'grey')))
                an = int(input(colored('Anul evenimentului:', 'grey')))
            except ValueError:
                print(colored('Trebuie sa se introduca numere', 'red'))
            try:
                data = datetime.date(an, luna, zi)
                tip = input(colored('Tipul evenimentului:', 'grey'))
                descriere = input(colored('Descrierea evenimentului:', 'grey'))
                try:
                    self.__srv_event.update_event(id, data, tip, descriere)
                    print(colored('Datele evenimentului au fost modificate cu succes!', 'cyan'))
                except ValueError as ve:
                     print(colored(str(ve), 'red'))
            except ValueError:
                print(colored('Data introdusa este invalida','red'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def run(self):
        # self.__srv_pers.generate_persons()
        # self.__srv_event.generate_events()
        # self.__srv_participant.generate_participants()
        while True:
            print(colored("Comenzi disponibile: add, delete, list, update, find, generate, sign up, reports, exit", 'magenta'))
            print(colored("Clasele sunt: person, event", 'magenta'))
            comanda = input(colored('Comanda este: ', 'grey'))
            comenzi = comanda.split(' ')

            if len(comenzi) == 2:
                cmd = comenzi[0]
                cls = comenzi[1]
                if cls == 'person':
                    if cmd == 'add':
                        self.__add_person()
                    elif cmd == 'list':
                        self.__print_all_persons()
                    elif cmd == 'delete':
                        self.__delete_person()
                    elif cmd == 'update':
                        self.__update_person()
                    elif cmd == 'find':
                        self.__find_person()
                    elif cmd == 'generate':
                        self.__generate_person()
                    elif cmd == 'exit':
                        return
                    else:
                        print(colored("Comanda invalida!", 'red'))
                elif cls == 'event':
                    if cmd == 'add':
                        self.__add_event()
                    elif cmd == 'list':
                        self.__print_all_events()
                    elif cmd == 'delete':
                        self.__delete_event()
                    elif cmd == 'update':
                        self.__update_event()
                    elif cmd == 'find':
                        self.__find_event()
                    elif cmd == 'exit':
                        return
                    else:
                        print(colored("Comanda invalida!", 'red'))
                else:
                    print(colored("Comanda invalida!", 'red'))
            elif len(comenzi) == 3:
                if comenzi[0] == 'sign' and comenzi[1] == 'up' and comenzi[2] == 'person':
                    self.__sign_up_person()
                elif comenzi[0] == 'list' and comenzi[1] == 'all' and comenzi[2] == 'participants':
                    self.__print_all_participants()
                else:
                    print(colored("Comanda invalida!", 'red'))
            elif comenzi[0] == 'reports':
                print(colored('1 - Lista de evenimente la care participa o persoana ordonat alfabetic dupa descriere.',
                              'magenta'))
                print(colored('2 - Lista de evenimente la care participa o persoana ordonat alfabetic dupa data.',
                              'magenta'))
                print(colored('3 - Persoanele participante la cele mai multe evenimente.',
                              'magenta'))
                print(colored('4 - Primele 20% evenimente cu cei mai multi participanti(descriere, nr participanti).',
                              'magenta'))
                print(colored('5 - Afișați zilele in care numarul de participanți e cel mai mare(data,numar_persoane).',
                              'magenta'))
                option = input(colored('Introduceti optiunea:','grey'))
                if option == '1':
                    self.__events_list_for_one_person_organised_by_description()
                elif option == '2':
                    self.__events_list_for_one_person_organised_by_date()
                elif option == '3':
                    self.__participants_to_the_most_events()
                elif option == '4':
                    self.__events_with_most_participants()
                elif option == '5':
                    self.__days_with_most_participants()
                elif option == 'exit':
                    return
                else:
                    print(colored('Comanda invalida!','red'))
            elif comenzi[0] == 'exit':
                return
            else:
                print(colored("Comanda invalida!", 'red'))
