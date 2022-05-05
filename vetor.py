#!/bin/python3.8

#Python List = vetor

#Create
vetor = []

#print type of variable
print(type(vetor))

#Verify metodos
print(dir(vetor))

#Append in vetor
vetor.append(1)
vetor.append("apple")

#print every vetor, loop
for values in vetor:
    print(values)

#print size
print(len(vetor))

#print value in index
print(vetor[1])

#Change Value
vetor[0] = "banana"
print(vetor)

#Remove item
vetor.remove("apple")
print(vetor)

#Extend
vetorb = ["orange", "cherry", "limon"]
vetor.extend(vetorb)

print(vetor)