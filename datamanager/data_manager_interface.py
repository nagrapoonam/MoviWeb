from abc import ABC, abstractmethod


class DataManagerInterface(ABC):
    """ Interface for DataManager classes. """



    @abstractmethod
    def list_all_users(self):
        """ List all users in the database. """
        pass

    @abstractmethod
    def list_user_movies(self, user_id):
        """ List all movies for a specific user. """
        pass

    @abstractmethod
    def add_user(self, user):
        """ Add a new user to the database. """
        pass

    @abstractmethod
    def add_movie(self, movie):
        """ Add a new movie to the database. """
        pass

    @abstractmethod
    def update_movie(self, movie):
        """ Update the details of a specific movie in the database. """
        pass

    @abstractmethod
    def delete_movie(self, movie_id):
        """ Delete a specific movie from the database. """
        pass
