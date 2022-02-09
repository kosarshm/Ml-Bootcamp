import random as rand
a = rand.randint(1, 20)
#print(a)

guess_count = 0
for i in range(1, 6):

    b = int(input())
    guess_count +=1
    if b == a:
        print("You Win")
        break

if guess_count == 5:
    print("Game Over")
