import sys

#This code only takes a list as input
def pruefer(S):
    n=len(S)+2
    e=[]
    reps=dict((t, S.count(t)) for t in S)#count all repetitions in prufer code
    for i in range(n):
        i=i+1
        if 2>=len(S)+2:
            break#stop when there is 1 edge and 2 nodes left
        if reps.keys() != dict((t, S.count(t)) for t in S).keys() and rm!=S[0]:
            #check if any number of the prufer code is a leaf by comparing the initial number 
            #that was on the prufer code and if there are any left in the prufer code
            #if there are none left in the code (S), its a leaf
            e.append([rm, S[0]])
            rm=S.pop(0)
            if 2>=len(S)+2:#when using pop the list can be left with less than 2 elements,
                #and as it won't go over line 9 until the next iteration we have to check here
                #or there will be an error in line 26
                break
        if i in S: #if the vertice is in the prufer code we ignore it
            # this is to find the lowest vertice not in the code
            continue
        else: #if the lowest possible vertex is not in the code we find its edge 
            #with the first vertex of the code
            e.append([S[0], i])
            rm=S.pop(0)
    return(e)


#ls=[3,1,1,2,2,2,3,3]
#ls=[4,5,6,6,4,5,5,6]