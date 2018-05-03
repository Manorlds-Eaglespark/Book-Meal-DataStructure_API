
class User:
   
   #Constructor for the User object, for initialization
   def __init__(self, name, email):
      self.id = random.randint(1001)
      self.name = name
      self.email = email
      self.admin_status = "false"
      self.time_created = time.time()