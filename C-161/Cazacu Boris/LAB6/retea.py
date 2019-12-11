import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))



#	datele pentru antrenare
training_inputs = np.array([[0,0,1],
                            [0,1,1],
                            [1,1,1],
			    [1,0,1]])
training_outputs = np.array([[0,0,1,1]]).T

#	generam ponderele random
np.random.seed(1)
synaptic_whieghts = 2 * np.random.random((3,1)) - 1


#	antrenam reteaua
for i in range(10000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_whieghts))

    err = training_outputs - outputs
    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_whieghts += adjustments


#	afisam rezultatele dupa antrenare
print("\nPonderile dupa invatare: ")
print(synaptic_whieghts)

print("\nRezultat dupa invatare: ")
print(outputs)


#	dam o situatie noua
new_inputs = np.array([[1,0,0]])
output = sigmoid(np.dot(new_inputs, synaptic_whieghts))
print("\nVolori noi: ")
print(output)


# Concluzie:
#La aceasta lucrare de laborator am implementat o simpla retea neurala,
#am invatato si iam dat niste valori noi si am observat ca nea prezis rezultatul corect.