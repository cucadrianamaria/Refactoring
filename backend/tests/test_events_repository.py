from repositories.events_repository import EventsRepository

def test_repository_returns_list():
    repo = EventsRepository()
    result = repo.get_all()
    assert isinstance(result, list)


