class Game:

    all = []


    def __init__(self, title):
        self._title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def set_title(self, title):
        if (type(title) == str) and (len(title) > 0):
            self._title = title
        else:
            raise Exception
    

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        unique_players = []

        for result in self.results():
            if result.player not in unique_players:
                unique_players.append(result.player)
        
        return unique_players

    def average_score(self, player):
        a = Game.results(self)
        total = 0
        for i in a:
            total += i.score
        return (total/len(a))

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if type(username) == str and (2 <= len(username) <= 16):
            self._username = username
        else:
            raise Exception
    
    username = property(get_username, set_username)

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        unique_games = []

        for result in self.results():
            if result.game not in unique_games:
                unique_games.append(result.game)

        return unique_games


    def played_game(self, game):
        for a in self.results():
            if game == a.game:
                return True
            else:
                pass
        return False



    def num_times_played(self, game):
        counter = 0
        for a in self.results():
            if game == a.game:
                counter+=1
        return counter

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score

        Result.all.append(self)

    def get_player(self):
        return self._player

    def set_player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception
        
    player = property(get_player, set_player)
    
    def get_game(self):
        return self._game

    def set_game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception
        
    game = property(get_game, set_game)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if (type(score) == int) and (1 <= score <= 5000):
            if self._score == score:
                self._score = score
        