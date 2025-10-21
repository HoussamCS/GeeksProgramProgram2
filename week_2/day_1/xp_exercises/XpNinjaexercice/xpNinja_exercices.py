# Exercice : Call history
print("EXERCICE 5: Call History")

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []  # stores call logs
        self.messages = []      # stores message dictionaries

    # Method to make a call
    def call(self, other_phone):
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)

    # Show call history
    def show_call_history(self):
        print(f"Call history for {self.phone_number}:")
        if not self.call_history:
            print("No calls yet.")
        for record in self.call_history:
            print(record)

    # Send a message
    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: '{content}'")


    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number}:")
        outgoing = [msg for msg in self.messages if msg["from"] == self.phone_number]
        if not outgoing:
            print("No outgoing messages.")
        for msg in outgoing:
            print(f"To {msg['to']}: {msg['content']}")


    def show_incoming_messages(self):
        print(f"Incoming messages to {self.phone_number}:")
        incoming = [msg for msg in self.messages if msg["to"] == self.phone_number]
        if not incoming:
            print("No incoming messages.")
        for msg in incoming:
            print(f"From {msg['from']}: {msg['content']}")

    # Show messages from a specific phone number
    def show_messages_from(self, sender_phone):
        print(f"Messages to {self.phone_number} from {sender_phone.phone_number}:")
        specific = [msg for msg in self.messages if msg["to"] == self.phone_number and msg["from"] == sender_phone.phone_number]
        if not specific:
            print("No messages from this number.")
        for msg in specific:
            print(msg["content"])


# --- Example Test ---

# Create phone objects
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")

# Make calls
phone1.call(phone2)
phone2.call(phone1)

# Show call history
phone1.show_call_history()
phone2.show_call_history()

# Send messages
phone1.send_message(phone2, "Hello, how are you?")
phone2.send_message(phone1, "I'm fine, thanks!")

# Show messages
phone1.show_outgoing_messages()
phone2.show_incoming_messages()

# Show messages from a specific number
phone1.show_messages_from(phone2)
