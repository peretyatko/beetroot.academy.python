# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.
import random
CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController():

    def __init__(self):
        self.channel = ["BBC", "Discovery", "TV1000"]
        self.channel_now = 0

    def lucky_channel(self):
        self.channel_now = random.choice(self.channel)
        print(self.channel_now)

    def first_channel(self):
        self.channel_now = self.channel[0]
        print(self.channel_now)

    def last_channel(self):
        self.channel_now = self.channel[-1]
        print(self.channel_now)

    # def next_channel(self):

    def current_channel(self):
        return f'{self.channel[self.channel_now]}'


controller = TVController()

controller.lucky_channel()
controller.first_channel()
controller.last_channel()
# controller.turn_channel(1)
# controller.next_channel()
# controller.previous_channel()
controller.current_channel()
# controller.is_exist(4)
# controller.is_exist("BBC")
