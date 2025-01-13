import time
import threading
from datetime import timedelta


def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}" + "\n")
            time.sleep(0.1)
    return print(f"Завершилась запись в файл {file_name}")


started_at = time.time()
data = {10: "example1.txt", 30: "example2.txt", 200: "example3.txt", 100: "example4.txt"}
for key, value in data.items():
    write_words(key, value)
ended_at = time.time()
elapsed = timedelta(seconds=(ended_at - started_at))
print(f'Работа потоков {elapsed}')

threads = []
start_time = time.time()

thread_args = [
    (10, "example5.txt"),
    (30, "example6.txt"),
    (200, "example7.txt"),
    (100, "example8.txt"),]

for args in thread_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

ended_at = time.time()
elapsed = timedelta(seconds=(ended_at - start_time))
print(f'Работа потоков {elapsed}')
