from faker import Faker

fake = Faker()

t = fake.name()
h = fake.address()
print(t)
print(h)