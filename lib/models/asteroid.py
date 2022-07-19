# * Goal is to create a local 'copy' of the apod response to display to the user
class Asteroid:
  def __init__(self, apod_json):
    for key in apod_json:
      # print("\nKEY: ", end=key)
      # print("\nVAL: ", end=apod_json[key])
      # copyright, date, explanation,hdurl, media_type, service_version, title, url
      self.__setattr__(key, apod_json[key])

  def display_asteroid(self):
    print(f'Title:\t\t{self.title}')
    print(f'Date:\t\t{self.date}')
    print(f'Image:\t\t{self.hdurl}')
    print(f'Explanation:\n')
    print(f'\t{self.explanation}')
    # print("Explanation:\t", end=self.explanation)
    # self.create_explanation_text()

  def create_explanation_text(self):
    print("Explanation:")
    split_array = self.explanation.split("  ")
    for x in split_array:
      print(x, end=" ")
