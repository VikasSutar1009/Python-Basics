jobs = deque(["Job1", "Job2", "Job3"])
while jobs:
    print("Processing:", jobs.popleft())