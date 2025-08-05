from .tools import book_appointment_tool
from .retriever import create_vector_store, load_documents, build_qa_chain

# Load documents and create vector store for QA
base_dir = __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
data_dir = __import__('os').path.join(base_dir, "data")
docs = load_documents(data_dir)
vectordb = create_vector_store(docs)
qa_chain, llm = build_qa_chain(vectordb)

# Simple chatbot loop: keyword-based routing
APPOINTMENT_KEYWORDS = ["book appointment", "call me", "schedule meeting", "contact me"]

def run_chatbot():
    print("Welcome to the Document QA & Appointment Chatbot!")
    chat_history = []
    while True:
        query = input(">> ").strip()
        if query.lower() == 'exit':
            break
        if any(kw in query.lower() for kw in APPOINTMENT_KEYWORDS):
            # Call appointment tool
            # Simulate user info collection (replace with your form logic if needed)
            name = input("Name: ").strip()
            phone = input("Phone Number: ").strip()
            email = input("Email: ").strip()
            date = input("Preferred Appointment Date (YYYY-MM-DD or natural language): ").strip()
            user_info = {"name": name, "phone": phone, "email": email, "date": date}
            result = book_appointment_tool.func(user_info)
            print("Bot:", result)
            continue
        # Otherwise, answer with QA chain
        result = qa_chain({"question": query, "chat_history": chat_history})
        print("Bot:", result['answer'])
        chat_history.append((query, result['answer']))

if __name__ == "__main__":
    run_chatbot()
