class Agent:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
      printStr = "My name is " + self.last_name + ", " + self.first_name + " " +self.last_name
      return printStr

