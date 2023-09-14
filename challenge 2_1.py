class player:
  def play(self):
      print("The player is playing cricket.")

#defing the berived class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")

#defing the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create objects of Batssman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()