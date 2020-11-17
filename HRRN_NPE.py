#process[][0] - Process ID
#process[][1] - Arrival Time
#process[][2] - Burst Time
#process[][3] - Completion Time
#process[][4] - Waiting Time
#process[][5] - Turnaround Time
#process[][6] - Status (Completed or Not)


def swap(process,i,j):
	
	for k in range(7):
		process[i][k], process[j][k]=process[j][k], process[i][k]


def sort_arrival_time(process,num):
	
	for i in range(num):
		for j in range(num-i-1):
			if(process[j][1]>process[j+1][1]):
				swap(process,j,j+1)
	

def update_completion_time(process,num,time):
	for i in range(num):
		if(process[i][6]!=1):
				process[i][3]+=time


def HRRN(process,num):
	sum_bt=0
	
	print("\nBefore Arrange...\n")
	print("Process ID\tArrival Time\tBurst Time\n")
	
	for i in range(num):
		print(process[i][0],"\t\t",process[i][1],"\t\t",process[i][2])
		sum_bt+=process[i][2]
		
	sort_arrival_time(process,num)
	print("\n")
	
	t=0
	completion_time=0
	print("\nAfter Arrange...\n")
	print("Process ID\tCompletion Time\n")
	
	while(t<sum_bt):
		hrr=-1
		flag=0
		for i in range(num):
			if(process[i][6]!=1):
				if(completion_time>=process[i][1]):
					flag=1
					temp=float(float((completion_time-process[i][1])+process[i][2])/process[i][2])
					if(temp>hrr):
						hrr=temp
						loc=i
		if(flag==0):
			i=0
			while(i<num):
				if(process[i][6]!=1):
					break
				i=i+1
			time=process[i][1]-completion_time
			update_completion_time(process,num,time)
			completion_time+=time
			print(-1,"\t\t",completion_time)
			
		else:
			t+=process[loc][2]
			completion_time+=process[loc][2]
			process[loc][4]=completion_time-process[loc][1]-process[loc][2]
			process[loc][5]=completion_time-process[loc][1]
			update_completion_time(process,num,process[loc][2])
			process[loc][6]=1
			print(process[loc][0],"\t\t",process[loc][3])


x=input("Enter number of Processes : ")
num=int(x)
process=[]

for i in range(num):
	a=[]
	a.append(int(input("Enter Process ID : ")))
	a.append(int(input("Enter Arrival Time : ")))
	a.append(int(input("Enter Burst Time : ")))
	a.append(int(0))
	a.append(int(0))
	a.append(int(0))
	a.append(int(0))
	process.append(a)

HRRN(process,num)
