import matplotlib.pyplot as plt

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        initial_position = int(lines[0].split('=')[1].strip())
        requests = list(map(int, lines[1].split('=')[1].strip().split(',')))
    return initial_position, requests

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

# FCFS Algorithm
def fcfs(initial_position, requests):
    current_position = initial_position
    total_head_movement = 0
    positions = [initial_position]

    for request in requests:
        head_movement = abs(current_position - request)
        total_head_movement += head_movement
        current_position = request
        positions.append(current_position)

    print(f"FCFS Total head movement: {total_head_movement}")
    plot_disk_movement(initial_position, requests, positions, "FCFS")
    return total_head_movement

# SSTF Algorithm
def sstf(initial_position, requests):
    current_position = initial_position
    total_head_movement = 0
    positions = [initial_position]
    requests = requests[:]

    while requests:
        closest_request = min(requests, key=lambda r: abs(current_position - r))
        head_movement = abs(current_position - closest_request)
        total_head_movement += head_movement
        current_position = closest_request
        positions.append(current_position)
        requests.remove(closest_request)

    print(f"SSTF Total head movement: {total_head_movement}")
    plot_disk_movement(initial_position, requests, positions, "SSTF")
    return total_head_movement

# SCAN Algorithm
def scan(initial_position, requests, disk_size=199):
    current_position = initial_position
    total_head_movement = 0
    positions = [initial_position]
    requests = sorted(requests)
    direction = 'up'

    while requests:
        if direction == 'up':
            next_requests = [r for r in requests if r >= current_position]
            if not next_requests:
                total_head_movement += abs(current_position - disk_size)
                current_position = disk_size
                direction = 'down'
                positions.append(current_position)
                continue
            closest_request = next_requests[0]
        else:
            next_requests = [r for r in requests if r <= current_position]
            if not next_requests:
                total_head_movement += abs(current_position - 0)
                current_position = 0
                direction = 'up'
                positions.append(current_position)
                continue
            closest_request = next_requests[-1]

        head_movement = abs(current_position - closest_request)
        total_head_movement += head_movement
        current_position = closest_request
        positions.append(current_position)
        requests.remove(closest_request)

    print(f"SCAN Total head movement: {total_head_movement}")
    plot_disk_movement(initial_position, requests, positions, "SCAN")
    return total_head_movement

# C-SCAN Algorithm
def c_scan(initial_position, requests, disk_size=199):
    current_position = initial_position
    total_head_movement = 0
    positions = [initial_position]
    requests = sorted(requests)

    while requests:
        next_requests = [r for r in requests if r >= current_position]
        if not next_requests:
            total_head_movement += abs(current_position - disk_size) + disk_size
            current_position = 0
            positions.append(disk_size)
            positions.append(current_position)
            continue
        closest_request = next_requests[0]
        head_movement = abs(current_position - closest_request)
        total_head_movement += head_movement
        current_position = closest_request
        positions.append(current_position)
        requests.remove(closest_request)

    print(f"C-SCAN Total head movement: {total_head_movement}")
    plot_disk_movement(initial_position, requests, positions, "C-SCAN")
    return total_head_movement

# LOOK Algorithm
def look(initial_position, requests):
    current_position = initial_position
    total_head_movement = 0
    positions = [initial_position]
    requests = sorted(requests)
    direction = 'up'

    while requests:
        if direction == 'up':
            next_requests = [r for r in requests if r >= current_position]
            if not next_requests:
                direction = 'down'
                continue
            closest_request = next_requests[0]
        else:
            next_requests = [r for r in requests if r <= current_position]
            if not next_requests:
                direction = 'up'
                continue
            closest_request = next_requests[-1]

        head_movement = abs(current_position - closest_request)
        total_head_movement += head_movement
        current_position = closest_request
        positions.append(current_position)
        requests.remove(closest_request)

    print(f"LOOK Total head movement: {total_head_movement}")
    plot_disk_movement(initial_position, requests, positions, "LOOK")
    return total_head_movement

# C-LOOK Algorithm
def c_look(initial_position, requests):
    current_position = initial_position
    total_head_movement = 0
    positions = [initial_position]
    requests = sorted(requests)

    while requests:
        next_requests = [r for r in requests if r >= current_position]
        if not next_requests:
            total_head_movement += abs(current_position - requests[0])
            current_position = requests[0]
            positions.append(current_position)
            requests.remove(current_position)
            continue
        closest_request = next_requests[0]
        head_movement = abs(current_position - closest_request)
        total_head_movement += head_movement
        current_position = closest_request
        positions.append(current_position)
        requests.remove(closest_request)

    print(f"C-LOOK Total head movement: {total_head_movement}")
    plot_disk_movement(initial_position, requests, positions, "C-LOOK")
    return total_head_movement

# Read input data from file
initial_position, requests = read_input_file('input_data.txt')

# Run all algorithms
fcfs_total = fcfs(initial_position, requests)
sstf_total = sstf(initial_position, requests)
scan_total = scan(initial_position, requests)
c_scan_total = c_scan(initial_position, requests)
look_total = look(initial_position, requests)
c_look_total = c_look(initial_position, requests)

