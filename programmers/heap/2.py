import heapq


def solution(jobs):
    total_count = len(jobs)
    work_finish_time = 0
    i = 0

    jobs = [[job[1], job[0]] for job in jobs]
    jobs = sorted(jobs, key=lambda x: x[1])
    print(jobs)
    remain_jobs = []
    total_delay_time = 0
    for i in range(len(jobs)):


        while remain_jobs and jobs[i][1] != jobs[i-1][1] and jobs[i][1] > work_finish_time:
            #print(remain_jobs, "current jobs")
            job = heapq.heappop(remain_jobs)
            #print("min job ", job)
            if work_finish_time >= job[1]:
                work_finish_time += job[0]
            else:
                work_finish_time = job[0] + job[1]
            total_delay_time += work_finish_time - job[1]
        heapq.heappush(remain_jobs, jobs[i])
    while remain_jobs :
        #print(remain_jobs, "current jobs")
        job = heapq.heappop(remain_jobs)
        #print("min job ", job)
        if work_finish_time >= job[1]:
            work_finish_time += job[0]
        else:
            work_finish_time = job[0] + job[1]

        total_delay_time += work_finish_time - job[1]

    return total_delay_time // total_count