class EventsService:
    def __init__(self, repository):
        self.repo = repository

    def list_events(self):
        events = self.repo.get_all()
        # aici poți adăuga sortări, filtre, validări
        return sorted(events, key=lambda e: e["date"])
