import heapq
import random
import time

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.power = self.calculate_power(burst_time)

    def calculate_power(self, burst_time):
        return max(1, 5 - burst_time / 10)

    def __str__(self):
        return f"Process {self.pid}: Burst Time = {self.burst_time}ms, Power = {self.power}W"

def power_aware_cpu_scheduling(processes):
    processes.sort(key=lambda x: x.burst_time)
    
    total_power_consumption = 0
    total_time = 0

    for process in processes:
        print(f"\nScheduling {process}")
        print(f"Running Process {process.pid} with burst time {process.burst_time}ms and power {process.power}W")
        
        time.sleep(process.burst_time / 1000.0)
        total_power_consumption += process.power
        total_time += process.burst_time
        
    print(f"\nTotal Time taken for all processes: {total_time} ms")
    print(f"Total Power Consumption: {total_power_consumption} Watts")

def generate_processes(num_processes):
    processes = []
    for i in range(num_processes):
        burst_time = random.randint(50, 300)
        process = Process(i + 1, burst_time)
        processes.append(process)
    return processes

def main():
    num_processes = 5
    processes = generate_processes(num_processes)
    
    print("\nGenerated Processes:")
    for process in processes:
        print(process)
    
    print("\nRunning Power-Aware CPU Scheduling...\n")
    power_aware_cpu_scheduling(processes)

if __name__ == "__main__":
    main()
