def get_zipped_races(lines):
    times, distances = lines[0].split(), lines[1].split()
    return zip(map(int, times[1:]), map(int, distances[1:]))

def get_single_race(lines):
    time, distance = "".join(lines[0].split()[1:]), "".join(lines[1].split()[1:])
    return [(int(time), int(distance))]

def find_possible_wins(race):
    possible_wins = 0
    time, distance = race
    for held_count, time_remaining in zip(range(1, time), reversed(range(1, time))):
        if held_count * time_remaining > distance:
            possible_wins += 1
    return possible_wins


def beat_record(races):
    wins = 1
    for race in races:
        wins *= find_possible_wins(race)
    return wins


if __name__ == "__main__":
    times = []
    distances = []
    with open("input.txt", "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    races = get_zipped_races(lines)
    print(beat_record(races))
    single_race = get_single_race(lines)
    print(beat_record(single_race))
