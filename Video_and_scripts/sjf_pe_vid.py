from manimlib.imports import *
import os
import pyclbr

class SJF(Scene):

    def construct(self):
        
        heading=TextMobject("SJF PE")
        heading.to_edge(UP+LEFT)
        self.play(Write(heading),run_time=2)

        time=0
        p,seq=sim()
        
        text1=[]
        text2=[]
        clk=TextMobject("time ={}".format(str(time)))
        clk.next_to(heading,DOWN,buff=0.5)
        clk.scale(0.8)
        self.add(clk)
        self.play(Write(clk))

        rq=[]
        
        for i in range(len(seq)):
            if(seq[i][0]==-1):
                text1.append(TextMobject("E"))
            else:
                text1.append(TextMobject("P{}".format(str(seq[i][0]))))
            text2.append(TextMobject(str(seq[i][1])))
        
        
        for i in range(len(seq)):
            if i==0:
                text1[i].to_edge(LEFT)
                text2[i].next_to(text1[i],DOWN,buff=1)
            else:
                text1[i].next_to(text1[i-1],RIGHT,buff=1)
                text2[i].next_to(text1[i],DOWN,buff=1)
            
            counter=0
            while(counter<seq[i][1]):
                time+=1
                self.play(Transform(clk,TextMobject("time ={}".format(str(time))).next_to(heading,DOWN,buff=0.5).scale(0.8)))
                self.play(Write(text1[i]))

                # r=""
                # for i in range(len(p)):
                #     if(p[i][1]<=time):
                #         r+="P{} ".format(str(p[i][0]))
                # if(len(r)>0):      
                #     self.play(Write(TextMobject(r).to_corner(RIGHT+UP).scale(0.5)))
                # print(r)
                # print("\n")                   
                counter+=1
                

            self.play(Write(text2[i]))           
            self.wait(2)
def index(e):
    return e[1]

# do sjf pe 
def sim():
    processes=[[1,3,4],[2,4,2],[3,5,1],[4,2,6],[5,1,8],[6,2,4]]
    n = 6
    
    processes.sort(key=index)

    print(processes)
    wt=[0]*n
    seq=findWaitingTime(processes,n,wt)
    return processes,seq
    #print(wt)
    #return processes


def findWaitingTime(processes, n, wt):  
    rt = [0] * n 
    seq=[]
    # Copy the burst time into rt[]  
    for i in range(n):  
        rt[i] = processes[i][2] 
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
  
    # Process until all processes gets  
    # completed  
    while (complete != n): 
          
        # Find process with minimum remaining  
        # time among the processes that  
        # arrives till the current time
        for j in range(n): 
            if ((processes[j][1] <= t) and 
                (rt[j] < minm) and rt[j] > 0): 
                minm = rt[j] 
                short = j 
                check = True
        if (check == False): 
            t += 1
            if(len(seq)>0 and seq[-1][0]==-1):
                seq[-1][1]+=1
            else:
                seq.append([-1,1])
            continue
              
        # Reduce remaining time by one  
        if(len(seq)>0 and seq[-1][0]==processes[short][0]):
            seq[-1][1]+=1
        else:
            seq.append([processes[short][0],1])
        rt[short] -= 1
  
        # Update minimum  
        minm = rt[short]  
        if (minm == 0):  
            minm = 999999999
  
        # If a process gets completely  
        # executed  
        if (rt[short] == 0):  
  
            # Increment complete  
            complete += 1
            check = False
  
            # Find finish time of current  
            # process  
            fint = t + 1
  
            # Calculate waiting time  
            wt[short] = (fint - processes[short][1] -    
                                processes[short][2]) 
  
            if (wt[short] < 0): 
                wt[short] = 0
          
        # Increment time  
        t += 1
    print(seq)
    return seq