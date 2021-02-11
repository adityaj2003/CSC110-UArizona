###Author:Aditya Jadhav
###Course:CSC110
###Description: This program prints out a target and the location of arrows hit on the target.
###             The location of the hits on target is provided by the user
###             in form of a string input.

import os
target_string=input("Hit string: \n")
while len(target_string)<=3 or len(target_string)%4 != 0:
    print("Please provide a valid hit string.")
    target_string = input("Hit string: \n")
hit_marker=input("Marker: \n")

while len(hit_marker)!=1:
    print("Please provide a valid marker. ")
    hit_marker = input("Marker: \n")
number_of_markers=len(target_string)//4
number_of_markers_printed=0              ###To find out how many hits are given in input
index_row=-5                             ### Required in below code so string input
i=0                                      ### doesn't go out of range
while index_row<6:
    index_column = -7
    while index_column<8:
        ##Below lines determine the x and y location of hit
        current_hit_x = int(target_string[i] + target_string[i + 1])
        current_hit_y = int(target_string[i + 2] + target_string[i + 3])
        if index_column==current_hit_x and index_row==-current_hit_y:
            if index_column==7:
                print(hit_marker+'\n',end='')
            else:
                print(hit_marker,end='')
            number_of_markers_printed+=1
            if number_of_markers_printed<number_of_markers:  # This is so that string index doesnt
                i+=4                                         # go out of range after all hits
                                                             # are printed
                ## Above i+=4 so that it moves on to next hit location
        elif index_row==0 and index_column==7:
            print('-\n',end='')
        elif index_row==0 and index_column!=0:
            print('-',end='')
        elif index_column == 0:                ## These are all the cases defining which
            print("|",end='')                  ## character must be printed in which case
        elif index_column==7:                  ## to print out the target and hits.
            print(" \n",end='')
        else:
            print(' ',end='')
        index_column+=1                     # To keep both while loops running and
    index_row+=1                            # move to next column or row


