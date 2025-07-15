# Write code below 💖

print('Answer the questions using the number of the option.')

g = 0
r = 0
h = 0
s = 0

a1 = int(input('Q1) Which one do you like? \n 1)Dawn \n 2)Dusk? \n Ans: '))

if a1 == 1:
  g += 1
  r += 1
elif a1 == 2:
  h += 1
  s += 1
else:
  print('Wrong input.')

a2 = int(input('Q2) When I’m dead, I want people to remember me as: \n 1)The Good \n 2)The Great \n 3)The Wise \n 4)The Bold \n Ans: '))
if a2 == 1:
  h += 2
elif a2 == 2:
  s += 2
elif a2 == 3:
  r += 2
elif a2 == 4:
  g += 2
else:
  print('Wrong input.')

a3 = int(input('Q3) Which kind of instrument most pleases your ear? \n 1)The violin \n 2)The trumpet \n 3)The piano \n 4)The drum \n Ans: '))
if a3 == 1:
  s += 4
elif a3 == 2:
  h += 4
elif a3 == 3:
  r += 4
elif a3 == 4:
  g += 4
else:
  print('Wrong input.')
print('\nResult:')
print(f"Gryffindor: {g}\nRavenclaw: {r}\nHufflepuff: {h}\nSlytherin: {s}\n")
if g > r and g > s and g > h:
  print('Gryffindor wins!')
if r > g and r > s and r > h:
  print('Ravenclaw wins!')
if s > r and s > g and s > h:
  print('Slytherin wins!')
else:
  print('Hufflepuff wins!')