# Python code to sort the tuples using second element 
# of sublist Inplace way to sort using sort() 
def Sort(sub_li): 

	# reverse = None (Sorts in Ascending order) 
	# key is set to sort using second element of 
	# sublist lambda has been used 
	sub_li.sort(key = lambda x: x[3], reverse=True) 
	return sub_li 

seq = []

# Function to find the waiting 
# time for all processes

def findWaitingTime(processes): 

	Sort(processes)
	print(processes)


	# calculating waiting time 
	for i in range(0, len(processes)): 
		seq.append([processes[i][0],processes[i][2]])

	print(seq) 



# Driver code 
if __name__ =="__main__": 
	
	# process id's 
	processes = [ 1, 2, 3] 
	n = len(processes)
	processes1=[[1,3,2,6],[2,2,4,5],[3,6,3,4],[4,8,1,3],[5,4,3,2],[6,5,4,1]] #[process_id, arrival time, burst_time, priority]
	print(processes1) 

	# Burst time of all processes 
	burst_time = [10, 5, 8] 

	findWaitingTime(processes1)
