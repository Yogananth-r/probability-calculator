import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents=[keys for keys,val in kwargs.items() for _ in range(val)]
  def draw(self,number):
    number=min(number,len(self.contents))
    removed=[self.contents.pop(random.randrange(len(self.contents))) for _ in range(number)]
    return (removed)
    
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M=0
  for _ in range(num_experiments):
    copied_hat=copy.deepcopy(hat)
    expected_balls_copy=copy.deepcopy(expected_balls)
    colors_given=copied_hat.draw(num_balls_drawn)

    for color in colors_given:
      if color in expected_balls_copy:
        expected_balls_copy[color]-=1


    if(all(x<=0 for x in expected_balls_copy.values())):
      M+=1
  probability=(M/num_experiments)
  return(probability)
        
    
  