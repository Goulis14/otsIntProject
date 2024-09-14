# models/member.py
class Member:
    def __init__(self, full_name, email, phone, age):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.age = age
        self.subscriptions = []  # A member can have multiple subscriptions

    def add_subscription(self, subscription):
        self.subscriptions.append(subscription)

    def __str__(self):
        return f"Member: {self.full_name}, Email: {self.email}"