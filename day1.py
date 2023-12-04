import regex as re
from word2number import w2n

def get_sum():
    day1_sum = 0
    with open('day1-input.txt', 'r') as file:
        for line in file:
            first_digit = None
            last_digit = None
            for i, c in enumerate(line):
                if c.isdigit():
                    last_digit = c
                    if first_digit is None:
                        first_digit = c

            if last_digit is not None:
                day1_sum += 10 * int(first_digit) + int(last_digit)

    return day1_sum

def get_sum_complex():
    day1_sum = 0
    with open('day1-input.txt', 'r') as file:
        for line in file:
            all_digits = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
            if (all_digits is not None) and (len(all_digits) > 0):
                num1 = (10 * int(all_digits[0])) if all_digits[0].isnumeric() else (10 * w2n.word_to_num(all_digits[0]))
                num2 = int(all_digits[-1]) if all_digits[-1].isnumeric() else w2n.word_to_num(all_digits[-1])
                day1_sum += num1 + num2
                print(line.strip('\n') + " " + str(int(num1/10)) + " " + str(num2))
            else:
                print(line + " no digits")

    return day1_sum


if __name__ == '__main__':
    print(get_sum_complex())
