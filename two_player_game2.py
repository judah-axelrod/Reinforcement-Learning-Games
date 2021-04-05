import numpy as np



class two_player_game2():
    max_d = 3
    max_B = 10

    def __init__(self, ph=0.55, pl=0.45, ch=1, R=1000, a=2, p=0.2):
        ###Parameters that can be changed while initializing###
        self.ph = ph
        self.pl = pl
        self.ch = ch
        self.R = R
        self.a = a
        self.p = p
        #Other attributes to track (d, B define state of the environment)
        self.d = 0
        self.B = self.max_B
        self.reward = 0.0
        self.is_terminal=False

    def step(self, action):
        '''Take the specified action and return the next state, reward, and
           whether the game is finished'''
        ###Determine whether or not player wins depending on action taken##
        if action == 1:
            win = np.random.binomial(1, self.pl)
        elif action == 0:
            win = np.random.binomial(1, self.ph)
            self.B -= self.ch #Decrement player energy
            if self.B < 0: #Reset to 0 if out of energy
                self.B = 0
        else:
            assert False, "Actions should be in the range of (0,2)"
        #Add win to winning player's tally
        if win:
            self.d +=1
        else:
            self.d -=1
        #Add back 'a' energy with probability 'p'
        if np.random.binomial(1, self.p):
            self.B += self.a
        if self.B > self.max_B: #Cap energy at B
            self.B = self.max_B
        #Determine if player has won d rounds more than opponent
        if self.d == self.max_d:
            self.is_terminal = True
            self.reward += self.R
        elif self.d == -self.max_d:
            self.is_terminal = True
        #Transition to next state
        return [self.d, self.B], self.reward, self.is_terminal

    def reset(self):
        '''Return environment to its initial state'''
        self.reward = 0
        self.d = 0
        self.B = self.max_B
        self.is_terminal = False
        return [self.d, self.B]

    def get_ch(self):
        '''Getter method for cost of high effort'''
        return self.ch
