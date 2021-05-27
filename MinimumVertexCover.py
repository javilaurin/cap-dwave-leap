import numpy as np
import dimod

# Especificar los coeficientes del problema que queremos resolver es muy sencillo
# Empezaremos con un caso muy simple

J = {(0,1):7,(0,2):7,(1,3):7,(2,3):7,(2,4):7,(3,4):7}
h = {15,15,22,22,15}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)

print("El modelo que vamos a resolver es")
print(model)
print()

# Resolver el modelo de forma exacta
from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
solution = sampler.sample(model)
print("La solucion exacta es")
print(solution)
print()


# Resolver el modelo con *simulated annealing*
sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print("La solucion con simulated annealing es")
print(response)
print()


# Resolver el modelo con el ordenador cuántico de D-Wave 
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("La solucion con el quantum annealer de D-Wave llamado",sampler_name,"es")
print(response)
