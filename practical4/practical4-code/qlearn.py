# Imports.
import numpy as np
import numpy.random as npr

from SwingyMonkey import SwingyMonkey


class Learner(object):
    def __init__(self):
        self.last_state  = None
        self.last_action = None
        self.last_reward = None
        self.gravity = 0
        self.findGravity = 1
        self.alpha = 0.5
        self.gamma = 0.5
        self.box = 56
        # Monkey bottom -> Tree dist -> Monkey bottom - tree bottom -> Gravity -> Action
        self.Q = [[[[[0 for _ in xrange(2)]
            for _ in xrange(2)]
            for _ in xrange(800 / self.box)] 
            for _ in xrange(600 / self.box)] 
            for _ in xrange(400 / self.box)]

    def reset(self):
        self.last_state  = None
        self.last_action = None
        self.last_reward = None
        self.gravity = 0
        self.findGravity = 1

    def action_callback(self, state):
        '''
        Implement this function to learn things and take actions.
        Return 0 if you don't want to jump and 1 if you do.
        '''

        # You might do some learning here based on the current state and the last state.

        # print state
        print self.last_reward
        print ""

        curr = self.Q[state["monkey"]["bot"] / self.box][state["tree"]["dist"] / self.box][(state["monkey"]["bot"] - state["tree"]["bot"] + 400) / self.box][self.gravity]
        # If previous action exists, update Q on it
        if self.last_state != None:
            prev = self.Q[self.last_state["monkey"]["bot"] / self.box][self.last_state["tree"]["dist"] / self.box][(self.last_state["monkey"]["bot"] - self.last_state["tree"]["bot"] + 400) / self.box][self.gravity]
            prev[self.last_action] = prev[self.last_action] + self.alpha * (self.last_reward + self.gamma * curr[self.findBestAction(curr)] - prev[self.last_action])
        elif self.findGravity == 1:
            self.gravity = 0 if (state["monkey"]["vel"] == -1) else 1
            self.findGravity = 0

        # You'll need to select and action and return it.
        # Return 0 to swing and 1 to jump.

        new_action = self.findBestAction(curr)
        new_state  = state

        self.last_action = new_action
        self.last_state  = new_state

        return self.last_action

    def reward_callback(self, reward):
        '''This gets called so you can see what reward you get.'''

        self.last_reward = reward

    def findBestAction(self, curr):
        return curr.index(max(curr))



def run_games(learner, hist, iters = 100, t_len = 100):
    '''
    Driver function to simulate learning by having the agent play a sequence of games.
    '''
    
    for ii in range(iters):
        # Make a new monkey object.
        swing = SwingyMonkey(sound=False,                  # Don't play sounds.
                             text="Epoch %d" % (ii),       # Display the epoch on screen.
                             tick_length = t_len,          # Make game ticks super fast.
                             action_callback=learner.action_callback,
                             reward_callback=learner.reward_callback)

        # Loop until you hit something.
        while swing.game_loop():
            pass
        
        # Save score history.
        hist.append(swing.score)

        # Reset the state of the learner.
        learner.reset()
        
    return


if __name__ == '__main__':

    # Select agent.
    agent = Learner()

    # Empty list to save history.
    hist = []

    # Run games. 
    run_games(agent, hist, 100, 10)

    # Save history. 
    print hist
    np.save('qlearnhist',np.array(hist))


