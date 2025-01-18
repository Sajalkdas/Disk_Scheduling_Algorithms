import matplotlib.pyplot as plt


class SSTF:
    def __init__(self, initial_position):
        self.current_position = initial_position
        self.total_head_movement = 0
        self.head_positions = [initial_position]  # List to store head positions

    def process_requests(self, requests):
        while requests:
            closest_request = min(requests, key=lambda x: abs(x - self.current_position))
            self.total_head_movement += abs(closest_request - self.current_position)
            self.current_position = closest_request
            self.head_positions.append(self.current_position)  # Record current position
            requests.remove(closest_request)

    def get_total_head_movement(self):
        return self.total_head_movement

    def get_head_positions(self):
        return self.head_positions


def simulate_disk_scheduling(initial_position, requests, scheduler):
    disk_scheduler = scheduler(initial_position)
    disk_scheduler.process_requests(requests)
    return disk_scheduler.get_total_head_movement(), disk_scheduler.get_head_positions()


def plot_disk_movement(initial_position, requests, head_positions):
    plt.figure(figsize=(10, 6))
    plt.plot(head_positions, range(len(head_positions)), marker='o', linestyle='-', color='b')  # Switched x and y
    plt.title('Disk Head Movement (SSTF)')
    plt.xlabel('Disk Head Position')
    plt.ylabel('Request')
    plt.xlim(0, 199)
    plt.yticks(range(len(requests) + 1), ['Start'] + [str(req) for req in requests])
    plt.grid(True)
    plt.show()


def main():
    initial_position = 123
    requests = [98, 183, 37, 122, 14, 124, 65, 67]

    sstf_total_movement, head_positions = simulate_disk_scheduling(initial_position, requests, SSTF)

    print(f"Total head movement for SSTF: {sstf_total_movement}")

    plot_disk_movement(initial_position, requests, head_positions)


if __name__ == "__main__":
    main()
