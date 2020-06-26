class Baller:
    all_players = []
    
    def __init__(self, name, has_ball = False):
        self.name = name
        self.has_ball = has_ball
        Baller.all_players.append(self)
        
    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            return True
        else:
            return False
        
class BallHog(Baller):
    def pass_ball(self, other_player):
        return False

class TeamBaller(Baller):
    """
    >>> cheerballer = TeamBaller('Thomas', has_ball=True)
    >>> cheerballer.pass_ball(surya)
    Yay!
    True
    >>> cheerballer.pass_ball(surya)
    I don't have the ball
    False
    """
    def pass_ball(self, other_player):
        if self.has_ball:
            self.has_ball = False
            other_player.has_ball = True
            print('Yay!')
            return True
        else:
            print('I don\'t have the ball')
            return False
            
def has_seven(k):
    if k < 10:
        return k == 7
    else:
        return has_seven(k // 10) or has_seven(k % 10)
            
class PingPongTracker:
    def __init__(self):
        self.current = 0
        self.index = 1
        self.add = True
    def next(self):
        self.current += 1 if self.add else -1
        if self.index % 7 == 0 or has_seven(self.index):
            self.add = not self.add
        self.index += 1
        return self.current

tracker1 = PingPongTracker()
tracker2 = PingPongTracker()
tracker1.next() # 1
tracker1.next() # 2
tracker2.next() # 1



