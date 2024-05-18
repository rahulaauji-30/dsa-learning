#include <stdio.h>
#include <stdlib.h>

struct Process {
    char pid[10];
    int at;        // Arrival Time
    int ct;        // Completion Time
    int bt;        // Burst Time
    int tat;       // Turnaround Time
    int wt;        // Waiting Time
};

int compare(const void *a, const void *b) {
    struct Process *p1 = (struct Process *)a;
    struct Process *p2 = (struct Process *)b;

    if (p1->bt > p2->bt) {
        return 1;
    } else if (p1->bt < p2->bt) {
        return -1;
    } else {
        return (p1->at > p2->at ? 1 : -1);
    }
}

void  main() {
    int pno;
    struct Process p[100];
    float avgTat, avgWt;
    int currentTime = 0, totalTat = 0, totalWt = 0;

    printf("Shortest Job First Scheduling Algorithm\n");
    printf("How many processes you want to add: ");
    scanf("%d", &pno);

    for (int i = 0; i < pno; i++) {
        printf("Details about process %d\n", i + 1);
        printf("Enter Process ID: ");
        scanf("%s", p[i].pid);
        printf("Enter Arrival Time: ");
        scanf("%d", &p[i].at);
        printf("Enter Burst Time: ");
        scanf("%d", &p[i].bt);
    }

    qsort(p, pno, sizeof(struct Process), compare);

    for (int i = 0; i < pno; i++) {
        if (currentTime < p[i].at) {
            currentTime = p[i].at;
        }

        p[i].ct = currentTime + p[i].bt;
        p[i].tat = p[i].ct - p[i].at;
        p[i].wt = p[i].tat - p[i].bt;
        currentTime += p[i].bt;
        totalTat += p[i].tat;
        totalWt += p[i].wt;
    }

    avgTat = (float)totalTat / pno;
    avgWt = (float)totalWt / pno;

    printf("| PID | AT | BT | CT | TAT | WT |\n");
    printf("----------------------------------\n");
    for (int i = 0; i < pno; i++) {
        printf("| %3s | %2d | %2d | %2d | %3d | %2d |\n", p[i].pid, p[i].at, p[i].bt, p[i].ct, p[i].tat, p[i].wt);
    }

    printf("Average Turnaround Time: %.2f\n", avgTat);
    printf("Average Waiting Time: %.2f\n", avgWt);

}

