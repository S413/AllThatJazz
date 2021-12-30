import HSCp as harsea
from objectiveFun import ObjectiveFun

from random import random, randint, choice

class StandardHarmonySearch():
    def __init__(self, HSettings, iters):
       self.cost = objectiveFun()
       self.HSettings = HSettings()
       self.fitness = None
       self.iters = iters
       self.best = None
       self.memory = HSettings.retrieveMem()
       
    def Jam(self):
        for es in range(self.iters):
            self.Improvise()
            self.Update_HM()

        print("Best lick found: {},{}\n".format(self.fitness,self.fitness))
        self.best = self.memory[0]

    def Improvise(self):
        for it in range(self.memory.N):
            tHMCR = random()
            new_lick = []*self.memory.N
            if(tHMCR <= self.HSettings.HMCR):
                idx = randint(0,self.memory.HMS)
                new_lick[it] = self.memory[idx][it]

                tPAR = random()
                if(tPAR <= self.HSettings.PAR):
                    if(choice([-1,1]) == 1):
                        bw = rand()
                        if(new_lick[it] + bw <= self.constraints[it]):
                            new_lick[it] = new_lick[it] + bw
                    else:
                        bw = rand()
                        if(new_lick[it] - bw >= self.constraints[it]):
                            new_lick[it] = new_lick[it] - bw

            else:
                bw = randint(self.constraints[it],self.constraints[it])
                new_lick = bw

    def Update_HM(self):

