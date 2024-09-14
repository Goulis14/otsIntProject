# models/subscription.py
class Subscription:
    def __init__(self, package_type, activity, member):
        self.package_type = package_type  # 8 visits or 15 visits
        self.activity = activity  # The activity the subscription is for
        self.member = member  # The member who has the subscription
        self.remaining_visits = package_type  # Start with full package visits
        member.add_subscription(self)  # Link subscription to member

    def use_visit(self):
        if self.remaining_visits > 0:
            self.remaining_visits -= 1
        else:
            print("No visits remaining!")

    def __str__(self):
        return f"Subscription for {self.activity.name}, Remaining visits: {self.remaining_visits}"