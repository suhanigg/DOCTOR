import hashlib
import datetime

# Block class: represents each block in the chain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # appointment info
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_data.encode()).hexdigest()

# Blockchain class: manages the chain of blocks
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_new_block(self, data):
        last_block = self.get_latest_block()
        new_index = last_block.index + 1
        new_timestamp = str(datetime.datetime.now())
        new_block = Block(new_index, new_timestamp, data, last_block.hash)
        self.chain.append(new_block)

    def display_chain(self):
        print("\n========== Blockchain ===========\n")
        for block in self.chain:
            print("Block Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Appointment Info:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Current Hash:", block.hash)
            print("--------------------------------\n")

# Main program for student interaction
def main():
    my_appointments = Blockchain()

    print("Welcome to the Doctor Appointment Booking System (Blockchain-Based)\n")

    while True:
        print("1. Add New Appointment")
        print("2. View All Appointments")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            # Get appointment details from the user
            patient = input("Enter patient name: ")
            doctor = input("Enter doctor name: ")
            time = input("Enter appointment time (e.g. 2025-05-10 14:00): ")
            appointment_data = {
                "patient": patient,
                "doctor": doctor,
                "time": time
            }
            my_appointments.add_new_block(appointment_data)
            print("Appointment added successfully!\n")

        elif choice == "2":
            my_appointments.display_chain()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice, please try again.\n")

# Run the program
main()
