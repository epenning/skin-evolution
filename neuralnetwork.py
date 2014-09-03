import random
import copy
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
            self.weights.append(random.uniform(-10,10))
        tempInt = random.randint(0,4)
        if tempInt == 0:
            self.func = "add"
        elif tempInt == 1:
            self.func = "multiply"
        else:
            othertemp = random.randint(0,9)
            if othertemp == 0:
                self.func = "sin"
            elif othertemp == 1:
                self.func = "cos"
            elif othertemp == 2:
                self.func = "tan"
            elif othertemp == 3:
                self.func = "tanh"
            elif othertemp == 4:
                #self.func = "bipolarSigmoid"
                self.func = "add"
            elif othertemp == 5:
                self.func = "gaussian"
            elif othertemp == 6:
                self.func = "ramp"
            elif othertemp == 7:
                self.func = "step"
            elif othertemp == 8:
                self.func = "spike"
            elif othertemp == 9:
                self.func = "inverse"
    
    """
    Set the number of inputs for the neuron and its weights to
    given values.
    """
    def setNeuron(self, numInputs, weights, func):
        self.numInputs = numInputs
        self.weights = weights
        self.func = func
        
    def function(self, inputs):
        if self.func == "add":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
        elif self.func == "multiply":
            result = 1 * self.weights[0]
            # loop through each input/weight and multiply
            for j in xrange(1, self.numInputs+1):
                result *= self.weights[j] * inputs[j-1]
        elif self.func == "sin":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            result = sin(result)
        elif self.func == "cos":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            result = cos(result)
        elif self.func == "tan":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            result = tan(result)
        elif self.func == "tanh":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            result = tanh(result)
        elif self.func == "bipolarSigmoid":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            result = (1.0-exp(-result)) / (1.0+exp(-result))
        elif self.func == "gaussian":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            result = exp(-1.0 * (result*result))
        elif self.func == "ramp":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            result = 1.0 - 2.0 * (result-floor(result))
        elif self.func == "step":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            if floor(result)%2 == 0:
                result = 1.0;    
            else:
                result = -1.0;
        elif self.func == "spike":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            if floor(result)%2 == 0:
                return 1.0 - 2.0 * (result-floor(result)); 
            else:
                return -1.0 + 2.0 * (result-floor(result));
        elif self.func == "inverse":
            result = 1 * self.weights[0]
            # loop through each input/weight and sum
            for j in xrange(1, self.numInputs+1):
                result += self.weights[j] * inputs[j-1]
            result = -result
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
    Get the functions from the network, starting with the first indexed neuron
    on layer closest to input, and ending with last indexed output neuron.
    """
    def getFunctions(self):
        functions = []
        for x in self.layers:
            for y in x.neurons:
                functions.append(y.func)
        return functions
        
    """ 
    Put the given weights into the network, starting with first indexed neuron
    on layer closest to input, and ending with last indexed output neuron.
    """    
    def putGenome(self, genome):
        index = 0
        findex = 0
        weights = genome.weights
        functions = genome.functions
        for x in self.layers:
            for y in x.neurons:
                y.func = functions[findex]
                findex+=1
                for j in xrange(0, len(y.weights)):
                    y.weights[j] = weights[index]
                    index = index + 1
    
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
    functions = []
    
    def __init__(self, weights, genomeFitness, functions):
        self.weights = weights
        self.genomeFitness = genomeFitness
        self.functions = functions
        
"""
The genetic algorithm which is used to evolve a neural network
to produce a desired output. Some functions are specific to
3-input, 1-output networks for this version.
"""
class GenAlg:
    net = NeuralNet()
    pop = []
    popSize = 0
    mutateWeightsRate = .4
    mutateFunctionsRate = .4
    crossoverRate = 0
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
        funcs1 = []
        funcs2 = []
        funcs1 = mom.functions
        funcs2 = dad.functions
        if len(mom.weights) != len(dad.weights):
            print ("ERROR: incompatible parents for crossover")
            return []
        for i in xrange(0, len(mom.weights)):
            if random.randint(0, 1) == 1:
                weights1.append(mom.weights[i])
            else:
                weights1.append(dad.weights[i])
            if random.randint(0, 1) == 1:
                weights2.append(mom.weights[i])
            else:
                weights2.append(dad.weights[i])
                
        for i in xrange(0, len(mom.functions)):
            if random.randint(0,1) == 1:
                funcs1.append(mom.functions[i])
            else:
                funcs1.append(dad.functions[i])
            if random.randint(0,1) == 1:
                funcs2.append(mom.functions[i])
            else:
                funcs2.append(dad.functions[i])
        child1 = Genome(weights1, self.fitness(weights1), funcs1)
        child2 = Genome(weights2, self.fitness(weights2), funcs2)
        return [child1, child2]
        
    """
    Takes an old genome and returns a slightly mutated version.
    Mutation changes random weights by a value between -2 and 2.
    """
    def mutateWeights(self, genome):
        newGenome = Genome([], 1, genome.functions)
        for iweight in genome.weights:
            weight = iweight
            if random.randint(0,10) == 1:
                if random.randint(0,2) == 1:
                    if random.randint(0,2) == 1:
                        weight += random.uniform(-10,10)
                    else:
                        weight -= random.uniform(-10,10)
                else:
                    weight = random.uniform(-1,1)
            newGenome.weights.append(weight)
        return newGenome
    
    """
    Mutates an old net's functions by switching two of its current
    neuron's activation functions.
    """
    def mutateFunctions(self, genome):
        newGenome = copy.deepcopy(genome)
        if random.randint(0,5) == 1:
            tempInt = random.randint(0,4)
            tempFunc = ""
            if tempInt == 0:
                tempFunc = "add"
            elif tempInt == 1:
                tempFunc = "multiply"
            else:
                othertemp = random.randint(0,9)
                if othertemp == 0:
                    tempFunc = "sin"
                elif othertemp == 1:
                    tempFunc = "cos"
                elif othertemp == 2:
                    tempFunc = "tan"
                elif othertemp == 3:
                    tempFunc = "tanh"
                elif othertemp == 4:
                    #tempFunc = "bipolarSigmoid"
                    tempFunc = "add"
                elif othertemp == 5:
                    tempFunc = "gaussian"
                elif othertemp == 6:
                    tempFunc = "ramp"
                elif othertemp == 7:
                    tempFunc = "step"
                elif othertemp == 8:
                    tempFunc = "spike"
                elif othertemp == 9:
                    tempFunc = "inverse"
            newGenome.functions[random.randint(0,len(genome.functions))-1] = tempFunc
        else:
            first = random.randint(0,len(genome.functions)-1)
            second = random.randint(0,len(genome.functions)-1)
            firstFunc = newGenome.functions[first]
            newGenome.functions[first] = newGenome.functions[second]
            newGenome.functions[second] = firstFunc        
        return newGenome
    
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
            parentRange = self.popSize-1
            # Chance of next 2 genomes being crossovers
            if (random.uniform(0,1) <= self.crossoverRate) and (i != self.popSize-1):
                crossoverChildren = self.crossover(self.pop[random.randint(0, parentRange)], self.pop[random.randint(0, parentRange)])
                newPop.append(crossoverChildren[0])
                newPop.append(crossoverChildren[1])
                i += 1
            # Otherwise randomly chosen from parent range
            else:
                newPop.append(self.pop[random.randint(0, parentRange)])
            # Mutate new pop
            if random.uniform(0,1) <= self.mutateWeightsRate:
                newPop[i] = self.mutateWeights(newPop[i])
            if random.uniform(0,1) <= self.mutateFunctionsRate:
                newPop[i] = self.mutateFunctions(newPop[i])
            i += 1
        self.cGeneration += 1
        return newPop
    
    """
    Runs GA for one generation, using the given parent, and
    returns the new population of its children.
    """
    def epochOne(self, parent):
        self.pop = parent
        newPop = []
        # Pick new population
        i = 0
        while i < self.popSize:
            # make entire pop same as parent
            newPop.append(parent)
            if i != 4:
                # Mutate new pop, except center
                if random.uniform(0,1) <= self.mutateWeightsRate:
                    newPop[i] = self.mutateWeights(newPop[i])
                if random.uniform(0,1) <= self.mutateFunctionsRate:
                    newPop[i] = self.mutateFunctions(newPop[i])
            i += 1
        self.cGeneration += 1
        return newPop
    
    
    