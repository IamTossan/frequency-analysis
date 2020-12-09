import sys
import json
from functools import reduce

config_file = open('./config/english.json', 'r')
english_letter_frequencies = json.load(config_file)
config_file.close()

def char_rot(src: str, rot_value: int) -> str:
    if not (src.isalpha and src.islower()):
        return src
    return chr(((ord(src) + rot_value - ord('a')) % 26) + ord('a'))

def str_rot(src: str, rot_value: int) -> str:
    return ''.join([char_rot(i, rot_value) for i in src])

def count_letter(acc: dict, char: chr) -> dict:
    if not (char.isalpha and char.islower()):
        return acc

    acc.setdefault(char, 0)
    acc[char] += 1
    return acc

def compare_letter_frequency(config: dict, src_length: int):
    def compare(acc: dict, char):
        expected_count = config[char[0]] * src_length / 100
        acc[char[0]] = (char[1] - expected_count) ** 2 / expected_count
        return acc
    return compare

def get_chi_squared_score(src: str) -> float:
    letters_count = reduce(count_letter, src, {})
    letters_scores = reduce(
      compare_letter_frequency(english_letter_frequencies, len(src.strip(' '))),
      letters_count.items(),
      {}
    )
    return sum(letters_scores.values())

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print('source: ', line)
        for i in range(26):
            decoded_string = str_rot(line.strip('\n'), i)
            get_chi_squared_score(decoded_string)
            print(
                'rot:',
                '{:2d}'.format(i),
                'output:',
                decoded_string[0:15],
                '| score:',
                '{0:3.2f}'.format(get_chi_squared_score(decoded_string)).rjust(10, ' ')
            )