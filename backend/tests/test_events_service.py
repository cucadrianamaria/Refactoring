from services.events_service import EventsService
from repositories.events_repository import EventsRepository

def test_service_sorts_events():
    repo = EventsRepository()
    service = EventsService(repo)
    events = service.list_events()
    assert events[0]["date"] <= events[1]["date"]
