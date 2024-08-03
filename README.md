# Cinema Ticket System

## Project Structure

- `main.py`: FastAPI application setup and endpoints.
- `repository.py`: CinemaTicketSystem` class where main logic with methods are implemented.
- `schemas.py`: Pydantic models for requests.
- `test.py`: Tests for FastAPI endpoints using `pytest`.
- `requirements.txt`: List of dependencies.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NurbolatSatybaldy/nfactorial_task.git
   cd nfactorial_task
   ```

2. Create virtual environment (Optional but highly recommended): 
   ```bash
   python -m venv cinema
   source cinema/bin/activate  # On Windows use `cinema\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running App
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  to test with Swagger.

3. If you want to use ready tests
   ```bash
   pytest -v test.py
   ```
