import random
import note

def main():

    # dictionary of numeric representation of all 12 unique pitches in Western Classical Music and the major scale built off that pitch where 0 = "C".
    # This way we can abstract out accidentals and enharmonic spellings of notes.  We will convert these later to letter names
    major_keys = {
        0: [0, 2, 4, 5, 7, 9, 11, 0],
        1: [1, 3, 5, 6, 8, 10, 0, 1],
        2: [2, 4, 6, 7, 9, 11, 1, 2],
        3: [3, 5, 7, 8, 10, 0, 2, 3],
        4: [4, 6, 8, 9, 11, 1, 3, 4],
        5: [5, 7, 9, 10, 0, 2, 4, 5],
        6: [6, 8, 10, 11, 1, 3, 5, 6],
        7: [7, 9, 11, 0, 2, 4, 6, 7],
        8: [8, 10, 0, 1, 3, 5, 7, 8],
        9: [9, 11, 1, 2, 4, 6, 8, 9],
        10: [10, 0, 2, 3, 5, 7, 9, 10],
        11: [11, 1, 3, 4, 6, 8, 10, 11]
    }
    
    key_center = input("Key Center: ")
    print(major_keys.get(int(key_center)))

    scale = generate_key()
    print(chr(ord('C') + 1))


def output(piece):
    pass

def generate_key():
    # Western Classical Music makes use of 12 unique pitches separated by half steps
    half_steps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    major_intervals = ['w', 'w', 'h', 'w', 'w', 'w', 'h']

    i = 0
    scale = []
    scale.append(half_steps[0])
    
    for interval in major_intervals:
        if i == 11:
            i = 0
            scale.append(half_steps[i])
        elif interval == 'w':
            i += 2
            scale.append(half_steps[i])
        else:
            i += 1
            scale.append(half_steps[i])

    # returns a 'scale' of the intervals between each note.  You could later map letter names to these intervals bases on what key is chosen
    return scale


if __name__ == "__main__":
    main()


# C _ D _ E F _ G _ A _ B C