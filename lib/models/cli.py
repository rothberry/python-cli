from secrets import choice
from api import API
from asteroid import Asteroid

class CLI:
  def __init__(self):

    pass

  def start(self):
    print("Welcome to the Nasa API CLI!\n\n")
    name = input("What's your name?\n")
    yesno = self.choice(['y', 'n'], 'would you like to see an asteroid?')
    if (yesno == 'y'):
      # make the apod req
      apod_api = API("apod")
      print(apod_api.full_base_url())
      apod_res = apod_api.get_request()
      ast = Asteroid(apod_res)
      ast.display_asteroid()
    elif (yesno == 'n'):
      print("hi")
    
    breakpoint()

  def choice(options, prompt):
    while True:
        output = input(prompt)    # Use raw_input(prompt) for Python 2.x
        if output in options:
            return output
        else:
            print("Bad option. Options: " + ", ".join(options))
