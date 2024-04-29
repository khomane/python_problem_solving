"""
Given a list, write a Python program to swap first and last element of the list.
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

"""

def pair_sum(S, input_list):
    input_list.sort()
    li=0
    ri=len(input_list)-1

    while(li<=ri):
        sum=input_list[li]+input_list[ri]
        if(sum<S):
            li+=1
        elif(sum>S):
            ri-=1
        else:
            print(str(input_list[li])+","+str(input_list[ri]))
            li+=1
            ri-=1        


#driver:

lst=[2,-3,3,3,-2]
pair_sum(0,lst)