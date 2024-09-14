# otsIntProject


# Member & Activity Management System

This project is a simple member and activity management system for an organization. The system manages members, their subscriptions, various activities, and booking sessions for those activities. Below is an explanation of the relationships between the different entities (classes) in this system.

## Relationships Between Classes

### 1. Member ↔ Subscription
- **Relationship**: A **Member** can have multiple **Subscriptions**.
- **Explanation**: Each member can subscribe to different activity packages. For example, a member can have an 8-visit package for swimming and a 15-visit package for CrossFit.
- **Direction**: One-to-many. One member can have multiple subscriptions, but each subscription belongs to one member.

### 2. Subscription ↔ Activity
- **Relationship**: A **Subscription** is tied to a specific **Activity**.
- **Explanation**: A subscription is always linked to a specific activity (like swimming or CrossFit). For instance, a member's subscription might be for swimming with a package of 8 visits per month.
- **Direction**: Many-to-one. Multiple subscriptions can be linked to the same activity.

### 3. Activity ↔ Session
- **Relationship**: An **Activity** can have multiple **Sessions** (time slots).
- **Explanation**: Activities (like swimming or CrossFit) have sessions, which are specific day/time slots. For example, CrossFit may have sessions on Monday and Wednesday at different times.
- **Direction**: One-to-many. An activity can have multiple sessions, but each session belongs to a single activity.

### 4. Session ↔ Member (via Booking)
- **Relationship**: A **Session** can have multiple **Members**, and a **Member** can attend multiple **Sessions**.
- **Explanation**: Members can book different sessions, and sessions keep track of which members are attending. A member might book a session on Monday for swimming and another session on Wednesday for CrossFit. This is managed through the `Booking` class.
- **Direction**: Many-to-many (via the `Booking` class). A session can have many members, and a member can attend many sessions.

### 5. Member ↔ Booking
- **Relationship**: A **Member** can make multiple **Bookings** for different sessions.
- **Explanation**: A member can book multiple sessions throughout the month for various activities and time slots. Each booking is associated with a specific session.
- **Direction**: One-to-many. One member can make many bookings, but each booking is linked to a specific session.

## Example Workflow

1. A member subscribes to the **CrossFit** activity with a 15-visit package.
2. The **CrossFit** activity offers multiple **sessions**, such as on Monday and Wednesday.
3. The member books the **Monday CrossFit session** using one of their available visits.
4. The system tracks the member's booking, and the session keeps track of all booked members.

This structure allows for a flexible system where members can subscribe to various activities, select different sessions, and manage their bookings based on their package limits.
