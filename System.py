# Define the data structures
events = {
    "Concert A": {
        "seats": [1, 2, 3, 4, 5],  # Available seats
        "price": 50  # Price per ticket
    },
    "Movie B": {
        "seats": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "price": 15
    }
}

# List to keep track of orders
orders = []

# Function to place an order
def place_order(event_name, seat_number, customer_name):
    if event_name in events:
        event = events[event_name]
        if seat_number in event["seats"]:
            # Remove the seat from available seats
            event["seats"].remove(seat_number)
            # Create an order
            order = {
                "event": event_name,
                "seat": seat_number,
                "customer": customer_name,
                "price": event["price"]
            }
            # Add the order to the list of orders
            orders.append(order)
            return f"Order placed successfully for {customer_name} at {event_name}, Seat {seat_number}"
        else:
            return "Seat not available"
    else:
        return "Event not found"

# Add some sample data
place_order("Concert A", 1, "Alice")
place_order("Movie B", 2, "Bob")

# Display current state of events and orders
print("Events:", events)
print("Orders:", orders)