import random
import numpy as np

class Bot:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.data = None

    def process_data(self, data):
        """Process incoming data according to the bot's strategy."""
        if self.strategy == 'average':
            self.data = np.mean(data)
        elif self.strategy == 'sum':
            self.data = np.sum(data)
        elif self.strategy == 'max':
            self.data = np.max(data)
        elif self.strategy == 'min':
            self.data = np.min(data)
        else:
            self.data = data
    
    def interact(self, other_bot, mode):
        """Interact with another bot based on the specified mode."""
        if mode == 'cooperative':
            self.data = (self.data + other_bot.data) / 2
        elif mode == 'competitive':
            self.data = max(self.data, other_bot.data)
    
    def get_output(self):
        """Return the bot's output data."""
        return self.data


class ComputationalDataReactor:
    def __init__(self, bots, interaction_mode='cooperative'):
        self.bots = bots
        self.interaction_mode = interaction_mode
        self.data_feed = []

    def feed_data(self, data):
        """Feed data into the reactor."""
        self.data_feed.append(data)

    def run(self):
        """Run the reactor to process data and simulate interactions."""
        for data in self.data_feed:
            for bot in self.bots:
                bot.process_data(data)
            
            for i in range(len(self.bots)):
                for j in range(i + 1, len(self.bots)):
                    self.bots[i].interact(self.bots[j], self.interaction_mode)
    
    def get_results(self):
        """Collect the outputs from all bots."""
        return {bot.name: bot.get_output() for bot in self.bots}


# Example Usage
if __name__ == "__main__":
    # Define bots with different strategies
    bot1 = Bot(name="Bot1", strategy="average")
    bot2 = Bot(name="Bot2", strategy="sum")
    bot3 = Bot(name="Bot3", strategy="max")
    
    # Create a reactor with the bots
    reactor = ComputationalDataReactor(bots=[bot1, bot2, bot3], interaction_mode='cooperative')
    
    # Feed data into the reactor
    reactor.feed_data([1, 2, 3, 4, 5])
    reactor.feed_data([10, 20, 30, 40, 50])
    
    # Run the reactor
    reactor.run()
    
    # Get and print results
    results = reactor.get_results()
    print(results)
