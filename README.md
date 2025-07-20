# JARVIS - The Smart AI Assistant

## Project Overview
JARVIS is a smart AI assistant designed to respond to voice commands and assist with various tasks. This project demonstrates the integration of voice recognition and AI capabilities in a Python-based application.

---

## Project Structure
- Ensure all files are located in the `Smart_Assistant` directory.
- It is recommended to create a virtual environment for the project (optional but preferred).
- Create a `.env` file to store your API key. Copy the last line from the `.gitignore` file into the `.env` file and replace `REPLACE_WITH_YOUR_API_KEY` with your actual API key.

---

## Installation

1. **Set Up Environment**:
   - If using a virtual environment, create and activate it.

2. **Install Dependencies**:
   - Open a terminal, navigate to the project directory, and run:
     ```bash
     pip install -r requirements.txt
     ```

---

## Usage

1. **Run the Application**:
   - Execute the `app.py` file in the terminal:
     ```bash
     python app.py
     ```

2. **Interaction**:
   - Upon successful execution, you will hear the sound: *"This is Jarvis!"*.
   - The terminal will display: *"Under Your Command Sir"*.
   - Say **"Jarvis"** to activate the assistant. If activated, it will respond with *"Yes Boss"*. Otherwise, it will keep prompting for activation.

---

## Notes
- Ensure your microphone is properly configured for voice input.
- For any issues, check the dependencies and ensure the `.env` file is correctly set up.
