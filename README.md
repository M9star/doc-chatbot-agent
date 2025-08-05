# Document Chatbot Agent

## Overview
This project is a conversational AI agent that can answer user queries from any documents (PDF, TXT) in the `data/` folder and book appointments via a conversational form. It uses LangChain, Hugging Face models (specifically `google/flan-t5-base` for document QA), and custom validation logic.

## Features
- **Document QA:** Ask questions about the contents of any PDF or TXT file in the `data/` folder.
- **Conversational Appointment Booking:** Collects and validates user info (name, phone, email, date) when booking an appointment.
- **Tool Integration:** Uses LangChain tools for booking and saving appointments.
- **Input Validation:** Validates email, phone number, and date formats.

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   - Using requirements.txt:
     ```bash
     pip install -r requirements.txt
     ```
   - Or manually:
     ```bash
     pip install langchain sentence-transformers transformers dateparser
     ```
3. **Add your documents:**
   - Place PDF and TXT files in the `data/` folder (e.g., `Resume.pdf`, `sample.txt`).

## Running the Chatbot
```bash
python -m app.chatbot
```
or
```bash
python app/chatbot.py
```

## Usage
- **Ask questions about your documents:**
  - Example: `What is the candidate's experience?`
  - Example: `List the candidate's skills.`
- **Book an appointment:**
  - Type: `book appointment`, `call me`, `schedule meeting`, or `contact me`
  - The chatbot will prompt for your name, phone, email, and preferred date.
  - Appointments are saved in `appointments.txt`.

## Example Prompts
- What programming languages does the candidate know?
- Summarize Resume.pdf
- What is the candidate's educational background?
- Book appointment

## Notes
- All documents in the `data/` folder are processed together. The chatbot answers using information from all files.
- For document-specific queries, mention the filename in your question.
- The project uses only free, local models (no API keys required).

## Future Improvements
- Migrate to LangGraph for advanced agent workflows.
- Add support for document upload via UI.
- Improve answer formatting and context targeting.

---
Feel free to contribute or customize for your needs!
