import HSCp as harsea
from objectiveFun import ObjectiveFun

from random import random, randint, choice

class StandardHarmonySearch():
    def __init__(self, HSettings, iters):
       self.cost = objectiveFun()
       self.HSettings = HSettings()
       self.fitness = list()
       self.iters = iters
       self.best = None
       self.worst = None
       self.memory = HSettings.retrieveMem()
       self.constraints = HSettings.retrieveCons()
       
    def Jam(self):
        for it in range(memory.HMS):
            self.fitness.append(self.cost.evaluate(self.memory[it]))
        
        self.best = min(range(len(self.fitness)), key=self.fitness.__getitem__)
        self.worst = max(range(len(self.fitness)), key=self.fitness.__getitem__)
        
        for es in range(self.iters):
            self.Improvise()
            self.Update_HM()

        print("Best lick found: {},{}\n".format(self.memory(self.fitness),self.cost.evaluate(self.memory[self.fitness])))

    def Improvise(self):
        for it in range(self.memory.N):
            tHMCR = random()
            self.new_lick = []*self.memory.N
            if(tHMCR <= self.HSettings.HMCR):
                idx = randint(0,self.memory.HMS)
                self.new_lick[it] = self.memory[idx][it]

                tPAR = random()
                if(tPAR <= self.HSettings.PAR):
                    if(choice([-1,1]) == 1):
                        bw = rand()
                        if(self.new_lick[it] + bw <= self.constraints[it][1]):
                            self.new_lick[it] = self.new_lick[it] + bw
                    else:
                        bw = rand()
                        if(self.new_lick[it] - bw >= self.constraints[it][0]):
                            self.new_lick[it] = self.new_lick[it] - bw

            else:
                bw = randint(self.constraints[it][0],self.constraints[it][1])
                self.new_lick = bw

    def Update_HM(self):
        new_lick_score = self.cost.evaluate(self.new_lick)
        if(new_lick_score < self.cost.evaluate(self.memory[self.worst])):
            self.memory[self.worst] = self.new_lick

            for it in range(self.memory.HMS):
                self.fitness[it] = self.cost.evaluate(self.memory[it])

            self.best = min(range(len(self.fitness)), key=self.fitness.__getitem__)
            self.worst = max(range(len(self.fitness)), key=self.fitness.__getitem__)


