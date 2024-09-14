# main.py
from models.member import Member
from models.subscription import Subscription
from models.activity import Activity
from models.session import Session
from models.booking import Booking


def main():
    # User inputs for the member details
    full_name = input("Enter full name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    age = int(input("Enter age: "))

    # Create a new member using user inputs
    member1 = Member(full_name, email, phone, age)

    # Predefined activities (these could be dynamic too, but here we define them)
    swimming = Activity("Swimming Pool", max_participants=6)
    crossfit = Activity("CrossFit", max_participants=6)

    # Ask user for subscription type and activity
    print("\nAvailable activities: 1. Swimming Pool, 2. CrossFit")
    activity_choice = int(input("Choose activity (1 for Swimming, 2 for CrossFit): "))

    if activity_choice == 1:
        selected_activity = swimming
    elif activity_choice == 2:
        selected_activity = crossfit
    else:
        print("Invalid activity choice!")
        return

    package_type = int(input("Choose subscription package (8 visits or 15 visits): "))
    if package_type not in [8, 15]:
        print("Invalid package type!")
        return

    # Create a subscription based on the user's choice
    subscription = Subscription(package_type=package_type, activity=selected_activity, member=member1)

    # Ask user to choose a session for booking
    print("\nCreating sessions for selected activity:")
    session1 = Session("Monday", "09:00", "11:00", selected_activity)
    session2 = Session("Wednesday", "16:00", "18:00", selected_activity)

    print(f"Available sessions for {selected_activity.name}:")
    print("1. Monday 09:00-11:00")
    print("2. Wednesday 16:00-18:00")

    session_choice = int(input("Choose session (1 or 2): "))
    if session_choice == 1:
        selected_session = session1
    elif session_choice == 2:
        selected_session = session2
    else:
        print("Invalid session choice!")
        return

    # Book the session for the member
    booking = Booking(member1, selected_session)
    booking.book()

    # Print out the result
    print("\nBooking Complete!")
    print(member1)
    print(subscription)
    print(selected_session)


if __name__ == "__main__":
    main()
