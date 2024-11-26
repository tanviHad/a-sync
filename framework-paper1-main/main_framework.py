import os
import subprocess
import psutil
from codetiming import Timer
import matplotlib.pyplot as plt
import time

# Define the directory where the scripts are located
scripts_directory = 'LLMcode/synchronous/'

# Define the directory to store the usage reports and graphs
reports_directory = 'LLMcode/synchronous/reports/'
graphs_directory = 'LLMcode/synchronous/graphs/'
os.makedirs(reports_directory, exist_ok=True)
os.makedirs(graphs_directory, exist_ok=True)

# List all the Python files in the directory
python_files = [f for f in os.listdir(scripts_directory) if f.endswith('.py')]

# Prepare data for plotting
memory_usages = []
cpu_times = []
execution_times = []
script_names = []

# Execute each Python script and record the resource usage
for file in python_files:
    file_path = os.path.join(scripts_directory, file)

    # Start the timer for execution
    timer = Timer()
    timer.start()

    # Execute the script and create a process object
    process = subprocess.Popen(['python', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Create a psutil object to monitor CPU and memory usage
    proc = psutil.Process(process.pid)
    
    # Initialize CPU and memory usage variables
    cpu_time = None
    memory_usage = None

    # Poll process and update CPU and memory usage until the process completes
    while True:
        try:
            if cpu_time is None:  # Only update if we haven't gotten the CPU time yet
                cpu_times_proc = proc.cpu_times()
                cpu_time = cpu_times_proc.user + cpu_times_proc.system
            if memory_usage is None:  # Only update if we haven't gotten the memory usage yet
                memory_usage = proc.memory_info().rss
        except psutil.NoSuchProcess:
            break  # Process has finished and is no longer available
        if process.poll() is not None:
            break  # Process has finished
        time.sleep(0.1)  # Sleep briefly to avoid spamming

    # Wait for the process to complete if it's not done already
    process.communicate()
    timer.stop()

    # Check if we never got the CPU time (e.g., if the process finished before the first check)
    if cpu_time is None:
        cpu_time = 0
    if memory_usage is None:
        memory_usage = 0

    # Add data to lists for plotting
    memory_usages.append(memory_usage)
    cpu_times.append(cpu_time)
    execution_times.append(timer.last)
    script_names.append(file)

    # Write the usage report to a file
    report_path = os.path.join(reports_directory, f"report_{file.replace('.py', '.txt')}")
    with open(report_path, 'w') as report_file:
        report_file.write(f"Resource Usage Report for {file}:\n")
        report_file.write(f"Memory Usage (Bytes): {memory_usage}\n")
        report_file.write(f"CPU Time (Seconds): {cpu_time}\n")
        report_file.write(f"Execution Time (Seconds): {timer.last}\n")

# Plot and save the graphs
def plot_and_save(data, title, ylabel, filename):
    plt.figure(figsize=(10, 8))
    plt.barh(range(len(data)), data, tick_label=script_names)
    plt.title(title)
    plt.xlabel(ylabel)
    plt.tight_layout()  # Adjust layout to fit labels
    plt.savefig(os.path.join(graphs_directory, filename))
    plt.close()

# Plot and save memory usage graph
plot_and_save(memory_usages, "Memory Usage of Scripts", "Memory Usage (Bytes)", "memory_usage.png")

# Plot and save CPU time graph
plot_and_save(cpu_times, "CPU Time of Scripts", "CPU Time (Seconds)", "cpu_time.png")

# Plot and save execution time graph
plot_and_save(execution_times, "Execution Time of Scripts", "Execution Time (Seconds)", "execution_time.png")

print("Resource usage reports and graphs generated for all scripts.")
