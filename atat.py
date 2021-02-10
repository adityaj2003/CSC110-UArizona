###Author:Aditya Jadhav
###Class:CSC 110
###Description:This program takes 3 inputs about the user of the measurement of 3 body parts
###            from the user then makes a design of AT-AT from Star Wars with the specified
###            body measurements

neck_length=int(input("Neck Length:\n"))
body_height=int(input("Body Height:\n"))
leg_height=int(input("Leg Height:\n\n"))


print('     _,.-Y  |  |  Y-._')
print(' .-~"   ||  |  |  |   "-.')
print(' |______________________|\n'*body_height,end=' ')
print('|______________________|'+'    '+' '*neck_length+'_____')
print(' L______________________[---'+'-'*neck_length+'I\" .-{\"-.')
print('I____________________ [__L]'+'_'*neck_length+'[I_/r(=}=-P')
print('L________________________j~ '+' '*neck_length+"'-=c_]/=-^")
print('\________________________]')
print('  [___________________]')
print('     I--I\"~~\"\"\"~~\"I--I')
print('     |\\n|         |\\n|\n'*leg_height,end=' ')
print('    ([])         ([])')
print('    /|..|\       /|..|\\')
print('   |=}--{=|     |=}--{=|')
print('  .-^--e-^-.   .-^--e-^-.')
