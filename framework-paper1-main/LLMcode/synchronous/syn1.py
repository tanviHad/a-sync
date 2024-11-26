import queue

# Create a queue
q = queue.Queue()

# Check for empty queue
if q.empty():
    print("Queue is empty")

# Enqueue some numbers
q.put(1)
q.put(2)
q.put(3)

# Process the queue sequentially
while not q.empty():
    # Dequeue a number from the queue
    num = q.get()

    # Count up to the number
    print("Counting up to", num)
    for i in range(1, num+1):
        print(i)

    # Report the work done
    print("Done counting up to", num)
    print("")

# Check for empty queue
if q.empty():
    print("Queue is empty")