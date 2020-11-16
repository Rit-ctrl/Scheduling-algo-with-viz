# Python code to sort the tuples using second element 
# of sublist Inplace way to sort using sort() 
def Sort(sub_li, index, rev): 

	# reverse = None (Sorts in Ascending order) 
	# key is set to sort using second element of 
	# sublist lambda has been used 
	sub_li.sort(key = lambda x: x[index], reverse=rev) 
	return sub_li 

def maxIndex(li):
    if(len(li)>0):
        return li.index(max(li, key = lambda x : x[3]))
    else:
        return 0


seq = []
time = 0

# Function to find the waiting 
# time for all processes

def findWaitingTime(processes):
    Sort(processes,1,False)
    print(processes)

    empty = 1

    if processes[0][1]==0:
        time = 0
    else:
        empty = 0
        time = processes[0][1]
    
    dummy = processes
    Sort(dummy,3,True)

    if(empty==0):
        seq.append([-1,time])

    for i in range(0,len(processes)):
        j = 0
        while(dummy[j][1] > time):
            j += 1
        
        seq.append([dummy[j][0],dummy[j][2]])
        time += dummy[j][2]
        dummy.pop(j)

    print(seq)
    return processes,seq
    




# Driver code 
if __name__ =="__main__": 
	
	# process id's 
	processes = [ 1, 2, 3] 
	n = len(processes)
	processes1=[[1,3,2,1],[2,1,4,2],[3,6,3,3],[4,8,1,4],[5,4,3,5],[6,5,4,6]] #[process_id, arrival time, burst_time, priority]
	print(processes1) 

	# Burst time of all processes 
	burst_time = [10, 5, 8] 

	findWaitingTime(processes1)
