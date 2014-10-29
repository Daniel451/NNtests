

import numpy as np

from scipy.special import expit





class NeuralNet:

   def __init__(self):

      # Prnting
      print("\n### Starte Programm ###\n")

      # Weights
      self.W = []
      self.W.append(
            [np.random.uniform(0.1, 1.9, 2),
            np.random.uniform(0.1, 1.9, 2),
            np.random.uniform(0.1, 1.9, 2)
            ])
      self.W.append([np.random.uniform(0.1, 1.9, 3)])

      # Bias
      self.B = []
      self.B.append(np.random.uniform(0.1, 1.9, 3))
      self.B.append(np.random.uniform(0.1, 1.9, 1))

      
   def teach(self, teachcount=10000, epsilon=0.1):
      
      errorOut = [   ]


   def compute(self, inputList):
      
      if(len(inputList) != 2):
         print("Die inputList muss exakt Laenge 2 haben")
         return

      inputArray = np.array(inputList)
      self.inputArray = inputArray

      innerActivation = [ np.dot(item, inputList) 
         for item in self.W[0] ]

      innerBias = [ np.dot(item, innerActivation)
         for item in self.B[0] ]

      innerOut = [ expit(item)
         for item in innerBias ]

      OutputActivation = [ np.dot(item, innerOut)
         for item in self.W[1] ]

      OutputBias = np.dot(self.B[1], OutputActivation) 

      Output = [ expit(item)
         for item in OutputBias ]

      self.Output = Output

      print("Der Output ist: "
            + str(
               [ round(item,2) for item in Output ]
               )
            + " bei dem Input " + str(inputList))



   def printWeights(self):
      
      print("### Weights ###\n")
      
      layercount = 0
      for sublist in self.W:
        
         print("Layer: " + str(layercount))
         
         neuroncount = 0
         for array in sublist:
            print("-> " + str(array) + " (Neuron: " + str(neuroncount) + ")")
            neuroncount += 1
         layercount += 1
      
      print("\n")


   def printBias(self):
      print("### Bias ###")

      for item in self.B:
         print(item)

      print("\n")


nn = NeuralNet()

nn.printWeights()
nn.printBias()

nn.teach(1000)

nn.printWeights()
nn.printBias()

nn.compute([0, 0])
nn.compute([0, 1])
nn.compute([1, 0])
nn.compute([1, 1])
