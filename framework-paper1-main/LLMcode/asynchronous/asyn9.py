import queue

def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()  # Retrieve a count value from the queue
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1  # Perform counting operation
            yield  # Yield control back to the main program
        print(f"Task {name} total: {total}")  # Print the total upon completion

def main():
    # Create a queue of 'work' and pre-populate it with count values
    work_queue = queue.Queue()
    for work in [15, 10, 5, 2]:  # These are the count values for the tasks
        work_queue.put(work)

    # Create tasks
    tasks = [task("One", work_queue), task("Two", work_queue)]

    # Run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)  # Run task until it yields control
            except StopIteration:
                # If the task is finished, remove it from the list of tasks
                tasks.remove(t)
            if len(tasks) == 0:
                done = True  # All tasks are done

if __name__ == "__main__":
    main()
