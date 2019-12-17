class Person:
    pass

persons = []

p1 = Person()
p1.name = "Alice"
p1.age = 32
p1.height = 159.3
p1.weight = 53.6
persons.append(p1)

p2 = Person()
p2.name = "Bob"
p2.age = 15
p2.height = 165.5
p2.weight = 63.3
persons.append(p2)

p3 = Person()
p3.name = "Calol"
p3.age = 43
p3.height = 169.7
p3.weight = 57.8
persons.append(p3)

p4 = Person()
p4.name = "David"
p4.age = 55
p4.height = 150.7
p4.weight = 50.2
persons.append(p4)

p5 = Person()
p5.name = "Eve"
p5.age = 41
p5.height = 152.5
p5.weight = 56.3
persons.append(p5)

bmi = []

for n in persons:
    b = n.weight/(n.height)**2
    bmi.append(b)

mi = bmi[0]
micount = 0

for p in range(len(bmi)):
    if mi > bmi[p]:
        mi = bmi[p]
        micount = p

print(persons[micount].name)
        




