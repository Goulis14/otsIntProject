# models/activity.py
class Activity:
    def __init__(self, name, max_participants):
        self.name = name
        self.max_participants = max_participants
        self.sessions = []  # List of available sessions for this activity

    def add_session(self, session):
        self.sessions.append(session)

    def __str__(self):
        return f"Activity: {self.name}, Max participants: {self.max_participants}"
