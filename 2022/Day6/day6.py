
def read_signal(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.readline().strip()

def find_packet(signal: str, marker_len: int) -> int:
    for i in range(len(signal)):
        packet = signal[i:i+marker_len]
        if len(set(packet)) == marker_len:
            return i + marker_len


# Part 1

FILE = 'day6.txt'
signal = read_signal(FILE)
packet_start = find_packet(signal, 4)
print(packet_start)


# Part 2

message_start = find_packet(signal, 14)
print(message_start)