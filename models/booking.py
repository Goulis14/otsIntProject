# models/booking.py
class Booking:
    def __init__(self, member, session):
        self.member = member
        self.session = session

    def book(self):
        # Ensure the session is not full and the member has visits left
        if len(self.session.booked_members) < self.session.activity.max_participants:
            self.session.book_member(self.member)
        else:
            print("Session is full or no visits left!")
