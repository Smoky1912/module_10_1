# импорт необход. модулей и ф-ий
import threading
from time import sleep, time

def write_words(word_count, file_name):
    # откр. файл для записи
    with open(file_name, 'w', encoding='utf-8') as file:
        # записываем слова в файл с паузой в 0.1 секунду после каждого слова
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    # вывод сообщ. о заверш. записи в файл
    print(f"Завершилась запись в файл {file_name}")

# взятие текущ. времени
start_time = time()

# запуск ф-ий с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# взятие текущ. времени
end_time = time()

# вывод разницы начала и конца работы ф-ий
print(f"Работа функций: {end_time - start_time:.6f} секунд")

# взятие текущ. времени
start_time = time()

# создание и запуск потоков с аргументами из задачи
threads = [
    threading.Thread(target=write_words, args=(10, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(200, 'example7.txt')),
    threading.Thread(target=write_words, args=(100, 'example8.txt'))
]

# запуск потоков
for thread in threads:
    thread.start()

# ожид-е завершения всех потоков
for thread in threads:
    thread.join()

# взятие текущ. времени
end_time = time()

# вывод разницы начала и конца работы потоков
print(f"Работа потоков: {end_time - start_time:.6f} секунд")