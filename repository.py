class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.movie_num = 0
        self.users = {}
        self.user_num = 0
        self.tickets = {}
        self.ticket_num = 0

    def add_movie(self, movie_name):
        self.movie_num += 1
        self.movies[self.movie_num] = movie_name
        return self.movie_num

    def show_all_movies(self):
        return self.movies

    def add_user(self, user_name):
        self.user_num += 1
        self.users[self.user_num] = user_name
        return self.user_num

    def buy_ticket(self, user_id, movie_id):
        if user_id in self.users and movie_id in self.movies:
            self.ticket_num += 1
            self.tickets[self.ticket_num] = (user_id, movie_id)
            return self.ticket_num
        else:
            return None

    def cancel_ticket(self, ticket_id):
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            return True
        else:
            return False
