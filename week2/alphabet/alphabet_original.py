import memory_profiler
import timeit

@memory_profiler.profile
def alphabet_do(count_of_letters):
    id_of_last_letter = 65 + count_of_letters
    # шукаю скільки рядків має містити трикутник
    row_count = 0
    count_of_el = 0
    while count_of_letters > 0:
        count_of_el += 1                   
        row_count += 1
        count_of_letters -= count_of_el

    a_uppercase_unicode = 65

    row_length = row_count * 2 - 1

    for i in range(1, row_count):
        alphabet_chars = ""
        for j in range(i):
            alphabet_chars += f" {chr(a_uppercase_unicode)}"
            a_uppercase_unicode += 1
        row = f"{alphabet_chars:>{row_length}}"
        print(row)

    if a_uppercase_unicode < id_of_last_letter:
        count_letter_in_last_row = id_of_last_letter - a_uppercase_unicode
        alphabet_chars = ""
        for k in range(count_letter_in_last_row):
            if k == count_letter_in_last_row - 1:
                alphabet_chars += f"{chr(a_uppercase_unicode)}"
            else:
                alphabet_chars += f"{chr(a_uppercase_unicode)} "
            a_uppercase_unicode += 1
        print(alphabet_chars)



if __name__ == "__main__":
    num = int(input("Enter the number of letters: "))

    execution_time_seconds = timeit.timeit(lambda: alphabet_do(num), number=1)
    execution_time_milliseconds = execution_time_seconds * 1000

    print(f"Execution time: {execution_time_milliseconds:.4f} milliseconds")