import HSCp as harsea
from objectiveFun import ObjectiveFun

from random import random, randint, choice

class StandardHarmonySearch():
    def __init__(self, HSettings, syms, expr, iters):
       self.cost = ObjectiveFun(syms, expr)
       self.HSettings = HSettings
       self.fitness = list()
       self.iters = iters
       self.best = None
       self.worst = None
       self.memory = HSettings.retrieveMem()
       self.constraints = HSettings.retrieveCons()
       
    def Jam(self):
        for it in range(self.memory.HMS):
            self.fitness.append(self.cost.evaluate([self.memory[it,x] for x in range(self.memory.N)]))
        
        self.best = min(range(len(self.fitness)), key=self.fitness.__getitem__)
        self.worst = max(range(len(self.fitness)), key=self.fitness.__getitem__)
        
        for es in range(self.iters):
            self.Improvise()
            self.Update_HM()

        print("Best lick found: {}\n".format([self.memory[self.best,x] for x in range(self.memory.N)]))
        print("= {}".format(self.fitness[self.best]))

    def Improvise(self):
        self.new_lick = [None]*self.memory.N
        for it in range(self.memory.N):
            tHMCR = random()
            if(tHMCR <= self.HSettings.HMCR):
                idx = randint(0, self.memory.HMS)
                self.new_lick[it] = self.memory[idx,it]

                tPR = random()
                if(tPR <= self.HSettings.PR):
                    if(random() < 0.5):
                        bw = random()*2 - 1
                        if(self.new_lick[it] - bw >= self.constraints[it][0]):
                            self.new_lick[it] = self.new_lick[it] - bw
                    else:
                        bw = random()*2 - 1
                        if(self.new_lick[it] + bw <= self.constraints[it][1]):
                            self.new_lick[it] = self.new_lick[it] + bw
            else:
                self.new_lick[it] = random()*10 - self.constraints[it][0]

    def Update_HM(self):
        new_lick_score = self.cost.evaluate(self.new_lick)
        worst_cost = self.cost.evaluate([self.memory[self.worst,x] for x in range(self.memory.N)])
        
        if(abs(new_lick_score) < abs(worst_cost)):
            
            for it in range(self.memory.N):
            	self.memory[self.worst,it] = self.new_lick[it]

            for it in range(self.memory.HMS):
                self.fitness[it] = self.cost.evaluate([self.memory[it,x] for x in range(self.memory.N)])

            self.best = min(range(len(self.fitness)), key=self.fitness.__getitem__)
            self.worst = max(range(len(self.fitness)), key=self.fitness.__getitem__)


