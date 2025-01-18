import matplotlib.pyplot as plt

class FCFS:
    def __init__(self, initial_position):
        self.current_position = initial_position
        self.total_head_movement = 0
        self.head_positions = [initial_position]  # List to store head positions

    def process_requests(self, requests):
        for request in requests:
            self.total_head_movement += abs(request - self.current_position)
            self.current_position = request
            self.head_positions.append(self.current_position)  # Record current position

    def get_total_head_movement(self):
        return self.total_head_movement

    def get_head_positions(self):
        return self.head_positions


class SSTF:
    def __init__(self, initial_position):
        self.current_position = initial_position
        self.total_head_movement = 0
        self.head_positions = [initial_position]

    def process_requests(self, requests):
        requests = requests[:]
        while requests:
            closest_request = min(requests, key=lambda x: abs(x - self.current_position))
            self.total_head_movement += abs(closest_request - self.current_position)
            self.current_position = closest_request
            self.head_positions.append(self.current_position)
            requests.remove(closest_request)

    def get_total_head_movement(self):
        return self.total_head_movement

    def get_head_positions(self):
        return self.head_positions


class SCAN:
    def __init__(self, initial_position, direction="up"):
        self.current_position = initial_position
        self.direction = direction
        self.total_head_movement = 0
        self.head_positions = [initial_position]

    def process_requests(self, requests):
        requests.sort()
        left = [r for r in requests if r < self.current_position]
        right = [r for r in requests if r >= self.current_position]

        if self.direction == "up":
            sequence = right + left[::-1]
        else:
            sequence = left[::-1] + right

        for request in sequence:
            self.total_head_movement += abs(request - self.current_position)
            self.current_position = request
            self.head_positions.append(self.current_position)

    def get_total_head_movement(self):
        return self.total_head_movement

    def get_head_positions(self):
        return self.head_positions


class C_SCAN:
    def __init__(self, initial_position):
        self.current_position = initial_position
        self.total_head_movement = 0
        self.head_positions = [initial_position]

    def process_requests(self, requests):
        requests.sort()
        right = [r for r in requests if r >= self.current_position]
        left = [r for r in requests if r < self.current_position]

        sequence = right + left

        for request in sequence:
            self.total_head_movement += abs(request - self.current_position)
            self.current_position = request
            self.head_positions.append(self.current_position)

    def get_total_head_movement(self):
        return self.total_head_movement

    def get_head_positions(self):
        return self.head_positions


class LOOK:
    def __init__(self, initial_position, direction="up"):
        self.current_position = initial_position
        self.direction = direction
        self.total_head_movement = 0
        self.head_positions = [initial_position]

    def process_requests(self, requests):
        requests.sort()
        left = [r for r in requests if r < self.current_position]
        right = [r for r in requests if r >= self.current_position]

        if self.direction == "up":
            sequence = right + left[::-1]
        else:
            sequence = left[::-1] + right

        for request in sequence:
            self.total_head_movement += abs(request - self.current_position)
            self.current_position = request
            self.head_positions.append(self.current_position)

    def get_total_head_movement(self):
        return self.total_head_movement

    def get_head_positions(self):
        return self.head_positions


class C_LOOK:
    def __init__(self, initial_position):
        self.current_position = initial_position
        self.total_head_movement = 0
        self.head_positions = [initial_position]

    def process_requests(self, requests):
        requests.sort()
        right = [r for r in requests if r >= self.current_position]
        left = [r for r in requests if r < self.current_position]

        sequence = right + left

        for request in sequence:
            self.total_head_movement += abs(request - self.current_position)
            self.current_position = request
            self.head_positions.append(self.current_position)

    def get_total_head_movement(self):
        return self.total_head_movement

    def get_head_positions(self):
        return self.head_positions


def simulate_disk_scheduling(initial_position, requests, scheduler, direction="up"):
    disk_scheduler = scheduler(initial_position) if scheduler not in [SCAN, LOOK] else scheduler(initial_position, direction)
    disk_scheduler.process_requests(requests)
    return disk_scheduler.get_total_head_movement(), disk_scheduler.get_head_positions()


def plot_disk_movement(initial_position, requests, head_positions, title):
    plt.figure(figsize=(10, 6))
    plt.plot(head_positions, range(len(head_positions)), marker='o', linestyle='-', color='b')
    plt.title(f'Disk Head Movement ({title})')
    plt.xlabel('Disk Head Position')
    plt.ylabel('Request')
    plt.xlim(0, 199)
    plt.yticks([])
    plt.grid(True)
    plt.show()


def read_requests_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        initial_position = int(lines[0].split('=')[1].strip())
        requests = list(map(int, lines[1].split('=')[1].strip().split(',')))
    return initial_position, requests


def main():
    file_path = 'input_data.txt'
    initial_position, requests = read_requests_from_file(file_path)

    algorithms = {
        'FCFS': FCFS,
        'SSTF': SSTF,
        'SCAN': SCAN,
        'C-SCAN': C_SCAN,
        'LOOK': LOOK,
        'C-LOOK': C_LOOK
    }

    for name, algorithm in algorithms.items():
        direction = "up" if algorithm in [SCAN, LOOK] else None
        total_movement, head_positions = simulate_disk_scheduling(initial_position, requests, algorithm, direction)
        print(f"Total head movement for {name}: {total_movement}")
        plot_disk_movement(initial_position, requests, head_positions, name)


if __name__ == "__main__":
    main()
