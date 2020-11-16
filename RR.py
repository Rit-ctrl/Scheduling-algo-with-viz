def index(e):
    return e[1]

def sim():
    processes=[[1,3,2],[2,2,4],[3,6,3],[4,8,1],[5,4,3],[6,5,4]] #[process_id,arrival time,burst_time]
    processes,seq,q=calcwaitingtime(processes,len(processes),2)
    return processes,seq,q

def calcwaitingtime(processes,n,quantum):
    rem_time=[0]*n
    seq=[]
    #print(seq)
    
   
    for i in range(n):
      processes.sort(key=index)

    for i in range(n):  
      rem_time[i] = processes[i][2] 

    t=0
    arrival=0
    q=[]

    rq=[]
    while True:
        done = True
        check = False
        last_guy=-1
        for i in range(n):
            if rem_time[i]>0:
                done=False
                #print("hi")
                if processes[i][1] <= t: #check if process should be in rq or not
                    if(check==False):    # check if some process hasn't already eaten up this time quantum
                        if len(rq) == 0 or rq[0]==processes[i][0]: #if rq is empty or rq head is process i
                            if(rem_time[i]>quantum):
                                t+=quantum
                                rem_time[i]-=quantum
                                seq.append([processes[i][0],quantum])
                                last_guy=processes[i][0]
                                #rq.append(i)
                            else:
                                t+=rem_time[i]
                                seq.append([processes[i][0],rem_time[i]])
                                rem_time[i]=0
                            if(len(rq)>1):
                                rq.remove(processes[i][0])
                            check=True
                    else:
                        if processes[i][0] not in rq: 
                            rq.append(processes[i][0])
        #print("iter ")
        if done == True:
            print("op")
            print(seq)
            print(q)
            return processes,seq,q
            #break
        if last_guy !=-1:
            rq.append(last_guy)
        
        q.append(rq[:])
        

        if len(rq)==0:
            seq.append([-1,quantum])
            t+=quantum


sim();