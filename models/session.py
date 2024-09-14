class Session:
    def __init__(self, day, start_time, end_time, activity):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.activity = activity
        self.booked_members = []  # List of members booked in this session

        activity.add_session(self)  # Link session to activity

    def book_member(self, member):
        if len(self.booked_members) < self.activity.max_participants:
            self.booked_members.append(member)
            print(f"Member {member.full_name} booked for session on {self.day}.")
        else:
            print(f"Session on {self.day} is full! No more bookings allowed.")

    def cancel_booking(self, member):
        if member in self.booked_members:
            self.booked_members.remove(member)

    def __str__(self):
        return f"Session: {self.day} {self.start_time}-{self.end_time}, Participants: {len(self.booked_members)}/{self.activity.max_participants}"
