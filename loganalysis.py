# A script that ingests server or application logs and extracts useful insights such as error counts, warnings, timestamps. It emails the report to the provided email in the args

# TODO: Accept File Input
# TODO: Count the number of log types and output that number into the report.log file


# TODO: Later down the road offer the availability to have the log emailed


def count_word_in_log_large(file_path, search_word):
    count = 0
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Converts all contents of the line to lower using line.lower()
                # Converts the search word to lower to ensure case-insensitive matching
                count += line.lower().count(search_word.lower())

        print(f"{search_word} appears {count} time(s)")
        return count
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


def lines(file_path):
    lines_scanned = 0
    try:
        with open(file_path, "r") as file:
            for line in file:
                lines_scanned += 1

        print(f"Lines Scanned: {lines_scanned}")
        return lines_scanned
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


log_file_path = input("Enter log file location: ")

fatal = "FATAL"
debug = "DEBUG"
info = "INFO"
error = "ERROR"
tracelog = "TRACE"
warn = "WARN"

count_word_in_log_large(log_file_path, warn)
count_word_in_log_large(log_file_path, debug)
count_word_in_log_large(log_file_path, info)
count_word_in_log_large(log_file_path, fatal)
count_word_in_log_large(log_file_path, error)
count_word_in_log_large(log_file_path, tracelog)

print("-----------------------")

lines(log_file_path)

"""
Expected Output:

WARN - 19
DEBUG - 26
INFO - 27
FATAL - 0
ERROR - 28
TRACE - 0
Lines Scanned: 100
_______________________
Actual Output:

Enter log file location: ./testdata.log
WARN appears 19 time(s)
DEBUG appears 26 time(s)
INFO appears 27 time(s)
FATAL appears 0 time(s)
ERROR appears 28 time(s)
TRACE appears 0 time(s)
-----------------------
Lines Scanned: 100

"""
