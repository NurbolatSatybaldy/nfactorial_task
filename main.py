from fastapi import FastAPI, HTTPException
from schemas import Movie, User, Ticket
from repository import CinemaTicketSystem

app = FastAPI()
cinema_system = CinemaTicketSystem()


@app.post("/movies/")
def add_movie(movie: Movie):
    movie_id = cinema_system.add_movie(movie.name)
    return {"movie_id": movie_id}


@app.get("/movies/")
def show_all_movies():
    movies = cinema_system.show_all_movies()
    return {"movies": movies}


@app.post("/users/")
def add_user(user: User):
    user_id = cinema_system.add_user(user.name)
    return {"user_id": user_id}


@app.post("/tickets/")
def buy_ticket(ticket: Ticket):
    ticket_id = cinema_system.buy_ticket(ticket.user_id, ticket.movie_id)
    if ticket_id is not None:
        return {"ticket_id": ticket_id}
    else:
        raise HTTPException(status_code=400, detail="User or movie not found")


@app.delete("/tickets/{ticket_id}")
def cancel_ticket(ticket_id: int):
    success = cinema_system.cancel_ticket(ticket_id)
    if success:
        return {"message": "Ticket successfully canceled"}
    else:
        raise HTTPException(status_code=404, detail="Ticket not found")


# Reset sys for tests
@app.post("/reset/")
def reset_system():
    global cinema_system
    cinema_system = CinemaTicketSystem()
    return {"message": "System reset"}
