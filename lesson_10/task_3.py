#  Task 3
#  TV controller
#  Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#  first_channel() - turns on the first channel from the list.
#  last_channel() - turns on the last channel from the list.
#  turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
#  next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
#  previous_channel() - turns on the previous channel.
#  If the current channel is the first one, turns on the last channel.
#  current_channel() - returns the name of the current channel.
#  is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
#  if the channel N or 'name' exists in the list, or "No" - in the other case.
#  The default channel turned on before all commands is №1.
#  Your task is to create the TVController class and methods described above.

class TVController:
    def __init__(self, channels):
        self.channels = self.if_list_channels_empty(channels)
        self.current_channel = self.channels[0]

    def if_list_channels_empty(self, channels):
        """checking if list of channels is empty"""
        if len(channels) == 0:
            raise ValueError('Your list of channels is empty')
        else:
            return channels

    def first_channel(self):
        """turns on the first channel from the list"""
        self.if_list_channels_empty(self.channels)
        self.current_channel = self.channels[0]
        print(self.channels[0])

    def last_channel(self):
        """turns on the last channel from the list"""
        self.if_list_channels_empty(self.channels)
        self.current_channel = self.channels[-1]
        print(self.channels[-1])

    def turn_channel(self, n):
        """ turns on the N channel"""
        self.if_list_channels_empty(self.channels)
        self.current_channel = self.channels[n-1]
        print(self.channels[n-1])

    def next_channel(self):
        """turns on the next channel"""
        self.if_list_channels_empty(self.channels)
        if self.current_channel == self.channels[-1]:
            self.current_channel = self.channels[0]
            print(self.current_channel)
        else:
            n = self.channels.index(self.current_channel)
            self.current_channel = self.channels[n+1]
            print(self.current_channel)

    def previous_channel(self):
        """turns on the previous channel"""
        self.if_list_channels_empty(self.channels)
        if self.current_channel == self.channels[0]:
            self.current_channel = self.channels[-1]
            print(self.current_channel)
        else:
            n = self.channels.index(self.current_channel)
            self.current_channel = self.channels[n - 1]
            print(self.current_channel)

    def cur_channel(self):
        """returns the name of the current channel"""
        self.if_list_channels_empty(self.channels)
        print(self.current_channel)

    def is_exist(self, channel):
        """checking if the channel is in the list_channels"""
        self.if_list_channels_empty(self.channels)
        try:
            if channel in self.channels or self.channels[channel] in self.channels:
                print('Yes')
            else:
                print('No')
        except IndexError:
            print('No')


CHANNELS = ["BBC", "Discovery", "TV1000"]
#  CHANNELS = []
controller = TVController(CHANNELS)
controller.first_channel()                     # == "BBC"
controller.last_channel()                      # == "TV1000"
controller.turn_channel(1)                     # == "BBC"
controller.next_channel()                      # == "Discovery"
controller.previous_channel()                  # == "BBC"
controller.cur_channel()                       # == "BBC"
controller.is_exist(4)                         # == "No"
controller.is_exist("BBC")                     # == "Yes"


# def main():
#     try:
#         channels = ["BBC", "Discovery", "TV1000"]
#         #channels = []
#         controller = TVController(channels)
#         controller.first_channel()                     # == "BBC"
#         controller.last_channel()                      # == "TV1000"
#         controller.turn_channel(1)                     # == "BBC"
#         controller.next_channel()                      # == "Discovery"
#         controller.previous_channel()                  # == "BBC"
#         controller.cur_channel()                       # == "BBC"
#         controller.is_exist(4)                         # == "No"
#         controller.is_exist("BBC")                     # == "Yes"
#     except Exception:
#         print('You must check settings TVController')
# main()
