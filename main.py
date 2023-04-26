'''

Create a system that takes a task and how often it should be repeated(numDays)

Create a method that marks when the user "does" the task:
    Marks down the date and keeps track of it

Create a method that tells the user all tasks to complete.
    Lists every task, the date frequency, and how long it's been since last completion

Create a method that lists all tasks whose deadlines are due within x days.
    x depends on user input

Create a method that adds a task.
  Struct?
    TaskName
    DateFrequency
    CompletionDateTimes

Create a method that removes a task.

'''

#Necessary for tracking the current date, time
from datetime import datetime
import pytz  #Necessary for checking time zone

#Tracking the datetime based on LA time zone since that's the one I'm in
#TODO: Ask the user for their time zone
myTZ = pytz.timezone("America/Los_Angeles")

#TASKS:
#  Params:
#    name --> task's name
#    dateFrequency --> how often the task reoccurs(days)
#    priority --> the lower the number, the higher priority
#    completions --> dictionary containing datetimes of previous completions as the keys, and possible messages as values.
#  Methods:
#    init --> initializes stuff, has to be here
#    complete --> marks the task as complete: Adds an entry to the completions dictionary, then print the result
class Task:
  def __init__(self,name="N/A",dateFrequency=1,priority=3,completions={}):
    self.name = name
    self.dateFrequency = dateFrequency
    self.priority = priority
    self.completions = completions
    
  def complete(self,message):
    today = datetime.now(myTZ)
    today = today.strftime("%B %d, %Y %H:%M:%S")
    self.completions[today] = message
    print("Current time:", today, ",", myTZ, "timezone.")
    print("Task complete:", self.name)
    print("Note:", message)

#TESTING:
Task1 = Task("Wash the Bedsheets", 14, 4)
Task1.complete("I washed itt yay")

print(Task1.completions)

#EVERYTHING WORKS!!
