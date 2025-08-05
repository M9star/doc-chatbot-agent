from langchain.tools import Tool

# Tool function to save appointment info
def save_appointment(user_info):
    with open("appointments.txt", "a") as f:
        f.write(f"{user_info['name']}, {user_info['phone']}, {user_info['email']}, {user_info['date']}\n")
    return "Appointment saved."

# LangChain Tool for booking appointments
book_appointment_tool = Tool(
    name="BookAppointment",
    func=save_appointment,
    description="Save user appointment info to a file."
)

# You can add more tools here as needed
