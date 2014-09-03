import pygame,sys
import random
from pygame.locals import *
from math import *

"""
Represents a neuron, with number of inputs and an array
of weights where the first index is the weight of bias.
"""
class Neuron:
    numInputs = 0
    weights = []
    func = ""
    
    """ 
    Initialize weights to match the number of inputs plus one
    with random float values between -1 and 1.
    """
    def __init__(self, numInputs):
        self.numInputs = numInputs
        self.weights = []
        for i in xrange(0, numInputs+1):
            self.weights.append(random.uniform(-100,100))
        self.func = "add"
    
    """
    Set the number of inputs for the neuron and its weights to
    given values.
    """
    def setNeuron(self, numInputs, weights):
        self.numInputs = numInputs
        self.weights = weights
        
    def function(self, inputs):
        if self.func == "add":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
        elif self.func == "multiply":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result *= self.weights[j] * inputs[j-1]
        elif self.func == "divide":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result /= self.weights[j] * inputs[j-1]
        if result < -255:
            result = -255
        elif result > 255:
            result = 255
        return result
        
"""
A layer of neurons, using an array of Neurons.
"""
class NeuronLayer:
    numNeurons = 0
    numInputsPerNeuron = 0
    neurons = []
    """
    Initialize neurons array to be filled with the given number
    of neurons, created with the given number of inputs.
    """
    def __init__(self, numNeurons, numInputsPerNeuron):
        self.neurons = []
        self.numNeurons = numNeurons
        self.numInputsPerNeuron = numInputsPerNeuron
        for i in xrange(0, numNeurons):
            self.neurons.append(Neuron(numInputsPerNeuron))
            
"""
The neural net, which contains a set of inputs, outputs,
and hidden layers between.
"""
class NeuralNet:
    layers = []
    numInputs = 0
    numOutputs = 0
    numHiddenLayers = 0
    neuronsPerLayer = 0
    """
    Initialize number of inputs, outputs, hidden layers, and neurons per layer
    to the given values.
    """
    def createNet(self, numInputs, numOutputs, numHiddenLayers, neuronsPerLayer):
        self.layers = []
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.numHiddenLayers = numHiddenLayers
        self.neuronsPerLayer = neuronsPerLayer
        if numHiddenLayers > 0:
            self.layers.append(NeuronLayer(neuronsPerLayer, numInputs))
        if numHiddenLayers > 1:
            for i in xrange(1, numHiddenLayers-1):
                self.layers.append(NeuronLayer(neuronsPerLayer, neuronsPerLayer))
        if numHiddenLayers == 0:
            self.layers.append(NeuronLayer(numOutputs, numInputs))
        else:
            self.layers.append(NeuronLayer(numOutputs, neuronsPerLayer))
    
    """ 
    Get the weights from the network, starting with first indexed neuron
    on layer closest to input, and ending with last indexed output neuron.
    """    
    def getWeights(self):
        weights = []
        for x in self.layers:
            for y in x.neurons:
                for z in y.weights:
                    weights.append(z)
        return weights
        
    """ 
    Put the given weights into the network, starting with first indexed neuron
    on layer closest to input, and ending with last indexed output neuron.
    """    
    def putGenome(self, genome):
        index = 0
        weights = genome.weights
        for x in self.layers:
            for y in x.neurons:
                for j in xrange(0, len(y.weights)):
                    y.weights[j] = weights[index]
                    index = index + 1
    
    """
    Activation function. If result >=1, output is 1. Otherwise 0.
    """
    def function(self, activation):
        if activation < 0:
            activation = 0
        elif activation >255:
            activation = 255
        return activation
    
    """
    Takes the given input(s), runs it through the network, and returns
    the corresponding output(s).
    """
    def update(self, inputs):
        outputs = []
        if len(inputs) != self.numInputs:
            print("ERROR: invalid number of inputs given")
            return outputs
        
        # loop through each layer
        for i in xrange(0, self.numHiddenLayers):
            if i > 0:
                inputs = outputs
            outputs = []
            
            # loop through each neuron
            for x in self.layers[i].neurons:
                outputs.append(x.function(inputs))

        return outputs

"""
The genome used in genetic algorithm, with a set of weights
and a given fitness for these weights.
"""
class Genome:
    weights = []
    genomeFitness = 0
    
    def __init__(self, weights, genomeFitness):
        self.weights = weights
        self.genomeFitness = genomeFitness
        
"""
The genetic algorithm which is used to evolve a neural network
to produce a desired output. Some functions are specific to
3-input, 1-output networks for this version.
"""
class GenAlg:
    net = NeuralNet()
    pop = []
    popSize = 0
    chromosomeLength = 0
    totalPopFitness = 0
    mutationRate = .5
    mutateFunctionRate = .5
    randomRate = 0
    crossoverRate = 0
    elitismRate = 0
    cGeneration = 0
    
    def __init__(self, popSize, net):
        self.net = net
        self.popSize = popSize
        
    """ Fitness determination unnecessary. """
    def fitness(self, weights):
        return 1    
    
    """
    Takes mother and father genomes, and returns two children genomes.
    Crossover takes random ratio of the weights from each parent,
    with 50% chances for each to get a weight.
    """
    def crossover(self, mom, dad):
        weights1 = []
        weights2 = []
        if len(mom.weights) != len(dad.weights):
            print ("ERROR: incompatible parents for crossover")
            return []
        for i in xrange(0, len(mom.weights)):
            if random.randint(0, 2) == 1:
                weights1.append(mom.weights[i])
            else:
                weights1.append(dad.weights[i])
            if random.randint(0, 2) == 1:
                weights2.append(mom.weights[i])
            else:
                weights2.append(dad.weights[i])
        child1 = Genome(weights1, self.fitness(weights1))
        child2 = Genome(weights2, self.fitness(weights2))
        return [child1, child2]
        
    """
    Takes an old genome and returns a slightly mutated version.
    Mutation changes random weights by a value between -2 and 2.
    """
    def mutate(self, genome):
        newGenome = Genome([], 1)
        for weight in genome.weights:
            if random.randint(0,10) == 1:
                if random.randint(0,2) == 1:
                    if random.randint(0,2) == 1:
                        weight += random.uniform(-100,100)
                    else:
                        weight -= random.uniform(-100,100)
                else:
                    weight = random.uniform(-1,1)
            newGenome.weights.append(weight)
        return newGenome
    
    """
    Mutates an old net's functions by switching two of its current
    neuron's activation functions.
    """
    #def mutateFunction(self, genome):
    
    """ Sorts the pop in descending fitness and calculates total fitness. """
    def calculateSort(self):
        self.pop = sorted(self.pop, key=lambda mem: mem.genomeFitness, reverse=True)
        self.totalPopFitness = 0
        for x in self.pop:
            self.totalPopFitness += x.genomeFitness
            
    """ Returns a sorted version of the given population of genomes. """        
    def sort(self, population):
        return sorted(population, key=lambda mem: mem.genomeFitness, reverse=True)
    
    """
    Runs GA for one generation - takes old pop of genomes,
    and returns the new pop of genomes.
    """
    def epoch(self, oldPop):
        self.pop = oldPop
        newPop = []
        
        # Pick new population
        i = 0
        while i < self.popSize:
            parentRange = self.popSize
            # Chance of next 2 genomes being crossovers
            if (random.uniform(0,1) <= self.crossoverRate) and (i != self.popSize-1):
                crossoverChildren = self.crossover(self.pop[random.randint(0, parentRange-1)], self.pop[random.randint(0, parentRange-1)])
                newPop.append(crossoverChildren[0])
                newPop.append(crossoverChildren[1])
                i += 1
            # Chance of new random genome
            elif random.uniform(0,1) <= self.randomRate:
                tempNet = NeuralNet()
                tempNet.createNet(self.net.numInputs, self.net.numOutputs, self.net.numHiddenLayers, self.net.neuronsPerLayer)
                weights = tempNet.getWeights()
                newPop.append(Genome(weights, self.fitness(weights)))
            # Otherwise randomly chosen from parent range
            else:
                newPop.append(self.pop[random.randint(0, parentRange - 1)])
            # Mutate new pop
            if random.uniform(0,1) <= self.mutationRate:
                newPop[i] = self.mutate(newPop[i])
            i += 1
        self.cGeneration += 1
        return newPop
    
    def averageFitness(self):
        return self.totalPopFitness / self.popSize

pygame.init()

#run game at 30 frames per second
FPS = 100
FPSCLOCK = pygame.time.Clock()

#set up display
display = pygame.display.set_mode((400,400),0,32)
pygame.display.set_caption('preview')

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

#set up neural network
net = NeuralNet()
net.createNet(2, 3, 2, 2)
ga = GenAlg(2, net)

playing = True

#initial image
display.fill(WHITE)
pop = []
for i in xrange(0,2):
    genome = Genome(net.getWeights(), 1)
    pop.append(genome)
    net.putGenome(genome)
    for x in xrange(-50,50):
        for y in xrange(-50,50):
            colors = net.update([x,y])
            pygame.draw.rect(display, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (4*x+50, 4*y+50, 4, 4), 0)

#game loop
while playing==True:
    
    #handle events
    for event in pygame.event.get():
        if event.type==QUIT:
            playing = False
        if event.type==KEYDOWN:
            next = True
        else:
            next = False

    #display and image creation
    if True:
        display.fill(WHITE)
        pop = []
        for i in xrange(0,2):
            genome = Genome(net.getWeights(), 1)
            pop.append(genome)
            net.putGenome(genome)
        pop = ga.epoch(pop)
        net.putGenome(pop[0])
        for x in xrange(-50,50):
            for y in xrange(-50,50):
                colors = net.update([x,y])
                pygame.draw.rect(display, (abs(colors[0]),abs(colors[1]),abs(colors[2])), (4*x+200, 4*y+200, 4, 4), 0)
    
    pygame.display.update()
    FPSCLOCK.tick(FPS)

pygame.quit()
sys.exit()
