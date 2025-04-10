#include<stdio.h>
#include<stdlib.h>
struct Process{
	char pid[2];
	int at;
	int ct;
	int bt;
	int tat;
	int wt;
};

int compare(const void *a,const void *b){
	struct Process *p1 = (struct Process *)a;
	struct Process *p2 = (struct Process *)b;

	if(p1->at > p2->at){
		return 1;
	}else if(p1->at < p2->at){
		return -1;
	}else{
		return (p1->bt > p2->bt ? 1:-1);
	}
}


void main(){
	int pno;
	struct Process p[100];
	float avgTat,avgWt;
	int currentTime=0,totalTat=0,totalWt=0;
	printf("First Come First Served Sheduling Algorithm\n");
	printf("How many processes you want to add: ");
	scanf("%d",&pno);
	
	for(int i=0;i<pno;i++){
		printf("Details about process %d\n",i);
		printf("Enter Process id: ");
		scanf("%s",p[i].pid);
		printf("Enter arrival Time:- ");
		scanf("%d",&p[i].at);
		printf("Enter burst time:- ");
		scanf("%d",&p[i].bt);
	}

	qsort(p,pno,sizeof(struct Process),compare);
        
	for(int i=0;i<pno;i++){
                if(currentTime < p[i].at){
                        currentTime = p[i].at;
                }

                p[i].ct = p[i].at + p[i].bt;
                p[i].tat = p[i].ct - p[i].at;
                p[i].wt = p[i].tat - p[i].at;
                currentTime += p[i].bt;
                totalTat += p[i].tat;
                totalWt += p[i].wt;
        }

	avgTat = totalTat / pno ;
	avgWt = totalWt /pno;
	
	printf("|PId|AT|BT|TAT|WT|\n");
	for(int i=0;i<pno;i++){
		printf("| %s | %d | %d | %d | %d |\n",p[i].pid,p[i].at,p[i].bt,p[i].tat,p[i].wt);
	}

	printf("Average Turn Around Time:- %.2f\n",avgTat);
	printf("Average Waiting Time:- %.2f\n",avgWt);

}
