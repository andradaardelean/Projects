from domain.validators import ValidatorPersoana, ValidatorEveniment
from repository.event_repo import InMemoryRepositoryEvent, FileRepositoryEvent
from repository.person_repo import InMemoryRepositoryPers, FileRepositoryPers
from repository.participant_repo import InMemoryRepositoryParticipant, FileRepositoryParticipant
from service.event_service import ServiceEveniment
from service.participant_service import ServiceParticipant
from service.person_service import ServicePersoana
from ui.console import Console

repo_pers = FileRepositoryPers('data/persons_new.txt')
repo_event = FileRepositoryEvent('data/events_new.txt')
# repo_event = InMemoryRepositoryEvent()
repo_participant = InMemoryRepositoryParticipant()
file_repo_participant = FileRepositoryParticipant('data/participants_new.txt')

val_pers = ValidatorPersoana()
val_event = ValidatorEveniment()

srv_pers = ServicePersoana(repo_pers,val_pers)
srv_event = ServiceEveniment(repo_event, val_event)
srv_participant = ServiceParticipant(file_repo_participant, repo_pers, repo_event)

ui = Console(srv_pers, srv_event, srv_participant)
ui.run()

