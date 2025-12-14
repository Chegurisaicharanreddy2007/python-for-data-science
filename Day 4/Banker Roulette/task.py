import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
num = random.randint(0,4)
x=friends[num]

print(f"the bill shd be paid by {friends[num]}")
print(f"the bill is gona be paid by {x}")
print(f"the bill is gona paid by {random.choice(friends)}")