import numpy as np

class two_player_game1:

    max_d=3 #Stop the game when one player has won 3 games more than her opponent

    def __init__(self, ph=0.55, pl=0.45, ch=50, cl=10, R=1000):
        self.ph = ph #Probability of winning if player invests high effort
        self.pl = pl #Probability of winning if player invests low effort
        self.ch = ch #Cost of investing high effort
        self.cl = cl #Cost of investing low effort
        self.R = R #Reward for winning (i.e. reaching state d=3)
        self.d = 0 #Used to track states of the environment
        self.reward = 0.0
        self.is_terminal=False

    def step(self, action):
        '''Take the specified action and return the next state, reward, and
           whether the game is finished'''
        #Determine whether or not player wins depending on action taken
        if action == 0:
            win = np.random.binomial(1, self.ph)
            self.reward = -self.ch
        elif action == 1:
            win = np.random.binomial(1, self.pl)
            self.reward = -self.cl
        else:
            assert False, "Actions should be in the range of (0,2)"
        #Add win to winning player's tally
        if win:
            self.d +=1
        else:
            self.d -=1
        #Determine if player has won d rounds more than opponent
        if self.d == self.max_d:
            self.is_terminal = True
            self.reward += self.R
        elif self.d == -self.max_d:
            self.is_terminal = True
        #Transition to next state
        return self.d, self.reward, self.is_terminal

    def reset(self):
        '''Return environment to its initial state'''
        self.reward = 0
        self.d = 0
        self.is_terminal = False
        return self.d
