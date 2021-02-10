###Author:Aditya Jadhav
###Class:CSC110
###Description:This program takes 6 inputs from the user with regards to body part sizes of a spaceship
###            and the number of layers of a particular body part. Then it prints out the patter of nebulon spaceship
###            from star wars using ASCII characters of specified measurement
large_layers=int(input('Large Layers on bottom:\n'))
medium_layers=int(input('Medium Layers on bottom:\n'))
small_layers=int(input('Small Layers on bottom:\n'))
front_length=int(input('Front length:\n'))
middle_length=int(input('Middle length:\n'))
back_length=int(input('Back length:\n\n'))


print("  /="+'-'*front_length+'\\'+'        '+' '*middle_length+' /'+'-'*back_length+'|')
print(" /=="+'/'*front_length+'==\\\\\\'+'    '+' '*middle_length+'|='+'='*back_length+'|')
print("|==-"+'\\'*front_length+'======\--'+'='*middle_length+'=='+'='*back_length+'|')
print(" \=="+'='*front_length+'==-------'+'-'*middle_length+'--'+'-'*back_length+'|')
print("  \="+'-'*front_length+'=///'+'     '+' '*middle_length+'\='+'='*back_length+'/')
print(('''   /'''+'-'*(front_length-3)+'''|
   \\'''+'='*(front_length-3)+'''|\n''')*large_layers,end='')
print((''' '''*((front_length-3)-int(front_length/2)+3)+'''/'''+'+'*(int(front_length/2))+'''|
'''+''' '''*((front_length-3)-int(front_length/2)+3)+'''\\'''+'-'*(int(front_length/2))+'''|\n''')*medium_layers,end='')
print((''' '''*((front_length)-int(front_length//3)-1)+'''\\'''+'<'*(int(front_length//3))+'''|
'''+''' '''*((front_length)-int(front_length//3))+'<'*(int(front_length//3))+'''|\n''')*small_layers,end='')