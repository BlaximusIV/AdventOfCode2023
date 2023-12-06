from threading import Thread
import time

class map_range:
    def __init__(self, destination, source, range_size):
        self.source = source
        self.destination = destination
        self.range_size = range_size

class map:
    def __init__(self, ranges, input, output):
        # ranges is a list of tuples, each tuple is a range of destination values and a range of source values
        self.ranges = ranges
        self.input = input
        self.output = output

    def get_mapped_value(self, value):
        # Check if the value is any of the source ranges, and if it is, return the destination value
        for range in self.ranges:
            if value >= range.source and value <= range.source + range.range_size - 1:
                return range.destination + value - range.source
            
        # Otherwise, return the value
        return value

def make_map(ranges_lines, input, output):
    ranges = []
    for line in ranges_lines:
        if line == '':
            continue
        parts = [int(num) for num in line.strip().split(' ')]
        ranges.append(map_range(parts[0], parts[1], parts[2]))
    ranges.sort(key=lambda x: x.source)

    return map(ranges, input, output)

def build_maps(text_parts):
    maps = {}
    maps['seed'] = make_map(text_parts[1].split('\n')[1:], 'seed', 'soil')
    maps['soil'] = make_map(text_parts[2].split('\n')[1:], 'soil', 'fertilizer')
    maps['fertilizer'] = make_map(text_parts[3].split('\n')[1:], 'fertilizer', 'water')
    maps['water'] = make_map(text_parts[4].split('\n')[1:], 'water', 'light')
    maps['light'] = make_map(text_parts[5].split('\n')[1:], 'light', 'temperature')
    maps['temperature'] = make_map(text_parts[6].split('\n')[1:], 'temperature', 'humidity')
    maps['humidity'] = make_map(text_parts[7].split('\n')[1:], 'humidity', 'location')
    return maps

def get_location(maps, seed):
    soil = maps['seed'].get_mapped_value(seed)
    fertilizer = maps['soil'].get_mapped_value(soil)
    water = maps['fertilizer'].get_mapped_value(fertilizer)
    light = maps['water'].get_mapped_value(water)
    temperature = maps['light'].get_mapped_value(light)
    humidity = maps['temperature'].get_mapped_value(temperature)
    location = maps['humidity'].get_mapped_value(humidity)
    return location

def get_min_location(maps, seed_range, min_locations):
    min_location = get_location(maps, seed_range[0])
    for seed in seed_range:
        location = get_location(maps, seed)
        if location < min_location:
            min_location = location
    min_locations.append(min_location)
    print(f'Finished range {seed_range[0]}-{seed_range[-1]}')

start = time.time()
file = open('input.txt', 'r')
text = file.read()
file.close()

text_parts = text.split('\n\n')

maps = build_maps(text_parts)

seed_range_numbers = [int(num) for num in text_parts[0].split(' ')[1:]]
seed_ranges = []
for i in range(0, len(seed_range_numbers)):
    if i % 2 == 0:
        seed_ranges.append(range(seed_range_numbers[i], seed_range_numbers[i] + seed_range_numbers[i + 1] - 1))

min_locations = []
threads = []
for range in seed_ranges:
    t = Thread(target=get_min_location, args=(maps, range, min_locations))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f'Closest location: {min(min_locations)}')
end = time.time()
print(f'Time taken: {end - start}s')