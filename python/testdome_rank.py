from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        print (self.standings)
        s = sorted(self.standings.items(), key=lambda x: x[1]['games_played']) #secondary key
        s2 = sorted(s, key=lambda x: x[1]['score'], reverse=True) #primary key
        print (s2)
        #print (sorted(self.standings.items(), key=lambda x: (x[1]['score'],x[1]['games_played']),reverse=True))
        return s2[rank-1][0]
         
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))