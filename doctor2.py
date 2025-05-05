import streamlit as st
import hashlib
import datetime

# Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_data.encode()).hexdigest()

# Blockchain class
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
        for block in self.chain:
            with st.expander(f"Block {block.index}"):
                st.write("🕒 Timestamp:", block.timestamp)
                st.write("📄 Appointment Info:", block.data)
                st.write("🔗 Previous Hash:", block.previous_hash)
                st.write("🔒 Current Hash:", block.hash)

# Initialize blockchain in session state
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

st.title("🩺 Doctor Appointment Booking System (Blockchain-based)")

# Input form
with st.form("appointment_form"):
    st.subheader("📅 Book a New Appointment")
    patient = st.text_input("Patient Name")

    # Doctor selection from predefined list
    doctor_list = ["Dr. Joshi", "Dr. Kumar", "Dr. Patel", "Dr. Jagde", "Dr. Kulkari", "Dr. Gaikwad"]
    doctor = st.selectbox("Choose Doctor", doctor_list)

    time = st.text_input("Appointment Time (e.g. 2025-05-10 14:00)")
    submitted = st.form_submit_button("Add Appointment")

    if submitted:
        if patient and doctor and time:
            appointment_data = {
                "patient": patient,
                "doctor": doctor,
                "time": time
            }
            st.session_state.blockchain.add_new_block(appointment_data)
            st.success("✅ Appointment added successfully!")
        else:
            st.warning("Please fill in all fields!")

# Display blockchain
st.subheader("📜 All Appointments on Blockchain")
st.session_state.blockchain.display_chain()
