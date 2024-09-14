class Booking:
    def __init__(self, member, session):
        self.member = member
        self.session = session

    def book(self):
        # Check if member has remaining visits
        subscription = self.get_subscription_for_activity(self.session.activity)
        if subscription and subscription.remaining_visits > 0:
            self.session.book_member(self.member)
            subscription.use_visit()  # Deduct a visit
        else:
            print("No remaining visits for this activity.")

    def get_subscription_for_activity(self, activity):
        for subscription in self.member.subscriptions:
            if subscription.activity == activity:
                return subscription
        return None