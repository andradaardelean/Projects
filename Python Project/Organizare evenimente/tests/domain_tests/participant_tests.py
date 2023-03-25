import unittest

from domain.entities import Persoana, Participant, Eveniment


class TestCaseParticipantDomain(unittest.TestCase):
    def test_create_participant(self):
        person = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        event = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')

        participant = Participant(person, event)
        self.assertEqual(participant.getPerson(), person)
        self.assertEqual(participant.getEvent(), event)

    def test_equals_participant(self):
        person1 = Persoana(1, 'Ardelean Andrada', 'Bd. Independentei')
        event = Eveniment(1, '24/10/2021', 'Meeting', 'Intalnire in parcul central.')
        participant1 = Participant(person1, event)
        participant2 = Participant(person1, event)

        self.assertEqual(participant1, participant2)

        person2 = Persoana(5, 'Ardelean Andrada', 'Bd. Independentei')
        participant3 = Participant(person2, event)

        self.assertNotEqual(participant2, participant3)