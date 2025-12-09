class EventsRepository:
    def __init__(self):
        # poți începe cu in-memory storage
        self._events = [
            {"id": 1, "title": "Hackathon 2025", "date": "2025-11-15"},
            {"id": 2, "title": "AI Workshop", "date": "2025-12-01"},
        ]

    def get_all(self):
        return list(self._events)

    def add_event(self, event):
        self._events.append(event)

    def find_by_id(self, event_id):
        return next((e for e in self._events if e["id"] == event_id), None)

