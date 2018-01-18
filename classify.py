import math
#Dylan Hubble
#Classification algorithm that works off assigning weights based on distance seperatinf points
#works for any amount of dimensions and points


# main array is positions
# everything for calculating is done on the fly and nothing is saved between runs
def classify(x,y):

    if len(y) != dimensions(x):
    	print "not equal dimensions"
    	return

    totalname = groups(x)#this is not the real totals this is an array of the number coresponding to the group
    totals = [0 for i in range(len(totalname))]


    for i in range(numofpoints(x)):# for each point find the distance to the point being classified
     totalstraight = 0 # the lines seperating the points with no effect on it        
     for j in range(dimensions(x)):      
         first = int(x[i][j]) - int(y[j]) # finds distance seperating

         first = math.pow(first,2) # squares
         totalstraight += first

     totalstraight = math.sqrt(totalstraight)#total distance
     
     
     totalstraight -= 1
     totalstraight = -totalstraight
     totalstraight = math.pow(2,totalstraight)
     totals[totalname.index(x[i][dimensions(x)])] += totalstraight #adds the total to the right spot in the totals array that coresponds with the totalname class


    return totalname[totals.index(max(totals))]   



#find dimensions for classifacation
def dimensions(input):
    return len(input[0])-1



#finds how many points total
def numofpoints(input):
    return len(input)

#def groups
def groups(input):

    #finds the titles for the different groups
    num = []#for the amount of groups
    for i in range(numofpoints(input)):
        if input[i][dimensions(input)] not in num:# changed input from "x"
            num.append(input[i][dimensions(input)])

    return num # returns an array with all of the seperate groups
