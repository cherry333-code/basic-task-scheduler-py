from collections import deque

class Task:
    """Represents a process/task for CPU scheduling."""

    def __init__(self, name, burst_time, priority=0):
        self.name = name
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time  # For Round Robin
        self.start_time = None
        self.finish_time = None

    def __repr__(self):
        return f"{self.name}(burst={self.burst_time}, priority={self.priority})"


class Scheduler:
    """Handles different CPU scheduling algorithms."""

    def __init__(self):
        self.tasks = []

    def get_user_tasks(self):
        """Accepts task inputs from the user."""
        num_tasks = int(input("Enter number of tasks: "))
        for i in range(num_tasks):
            name = input(f"Task {i + 1} name: ")
            burst = int(input(f"{name}'s burst time: "))
            priority = int(input(f"{name}'s priority (lower = higher priority): "))
            self.tasks.append(Task(name, burst, priority))

    def reset_tasks(self):
        """Resets timing attributes before re-running an algorithm."""
        for task in self.tasks:
            task.remaining_time = task.burst_time
            task.start_time = None
            task.finish_time = None

    def fcfs(self):
        """First-Come, First-Serve Scheduling."""
        print("\n--- First-Come, First-Serve ---")
        current_time = 0
        for task in self.tasks:
            task.start_time = current_time
            current_time += task.burst_time
            task.finish_time = current_time
            print(f"{task.name}: Start = {task.start_time}, Finish = {task.finish_time}")

    def round_robin(self, quantum):
        """Round Robin Scheduling."""
        print("\n--- Round Robin ---")
        queue = deque(self.tasks)
        current_time = 0

        while queue:
            task = queue.popleft()
            if task.start_time is None:
                task.start_time = current_time

            if task.remaining_time > quantum:
                current_time += quantum
                task.remaining_time -= quantum
                queue.append(task)
            else:
                current_time += task.remaining_time
                task.remaining_time = 0
                task.finish_time = current_time
                print(f"{task.name}: Start = {task.start_time}, Finish = {task.finish_time}")

    def priority_scheduling(self):
        """Non-Preemptive Priority Scheduling."""
        print("\n--- Priority Scheduling ---")
        tasks = sorted(self.tasks, key=lambda x: x.priority)
        current_time = 0
        for task in tasks:
            task.start_time = current_time
            current_time += task.burst_time
            task.finish_time = current_time
            print(f"{task.name} (Priority {task.priority}): Start = {task.start_time}, Finish = {task.finish_time}")

    def main_menu(self):
        """Displays algorithm options and executes selection."""
        while True:
            print("\nChoose Scheduling Algorithm:")
            print("1. FCFS (First-Come, First-Serve)")
            print("2. Round Robin")
            print("3. Priority Scheduling")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")
            self.reset_tasks()

            if choice == "1":
                self.fcfs()
            elif choice == "2":
                quantum = int(input("Enter time quantum: "))
                self.round_robin(quantum)
            elif choice == "3":
                self.priority_scheduling()
            elif choice == "4":
                print("Exiting Scheduler. Bye!")
                break
            else:
                print("Invalid input. Try again.")


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.get_user_tasks()
    scheduler.main_menu()
