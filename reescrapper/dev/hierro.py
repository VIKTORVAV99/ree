from reescrapper import GenerationHierro, DemandHierro

demand = DemandHierro().get()
print(demand)

generation = GenerationHierro().get()
print(generation)
