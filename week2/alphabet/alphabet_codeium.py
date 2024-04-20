import memory_profiler
import timeit

@memory_profiler.profile
def alphabet_do(count_of_letters):
    id_of_last_letter = 65 + count_of_letters

    row_count = 0
    count_of_el = 0
    while count_of_letters > 0:
        count_of_el += 1                   
        row_count += 1
        count_of_letters -= count_of_el

    a_uppercase_unicode = 65

    row_length = row_count * 2 - 1

    for i in range(1, row_count):
        alphabet_chars = ' '.join(chr(a_uppercase_unicode + j) for j in range(i))
        a_uppercase_unicode += i
        row = f"{alphabet_chars:>{row_length}}"
        print(row)

    if a_uppercase_unicode < id_of_last_letter:
        count_letter_in_last_row = id_of_last_letter - a_uppercase_unicode
        alphabet_chars = ' '.join(chr(a_uppercase_unicode + k) if k != count_letter_in_last_row - 1 else chr(a_uppercase_unicode + k) for k in range(count_letter_in_last_row))
        print(alphabet_chars)

if __name__ == "__main__":
    num = int(input("Enter the number of letters: "))

    execution_time_seconds = timeit.timeit(lambda: alphabet_do(num), number=1)
    execution_time_milliseconds = execution_time_seconds * 1000

    print(f"Execution time: {execution_time_milliseconds:.4f} milliseconds")