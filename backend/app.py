from flask import Flask, jsonify
from repositories.events_repository import EventsRepository
from services.events_service import EventsService

def create_app():
    app = Flask(__name__)

    repo = EventsRepository()
    service = EventsService(repo)

    @app.route("/api/events")
    def get_events():
        return jsonify(service.list_events())

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
