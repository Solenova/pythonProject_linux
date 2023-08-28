# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def mult_file (file_num: str, file_name: str):
    with (
        open(file_num, 'r+', encoding='utf-8') as f_n,
        open(file_name, 'r+', encoding='utf-8') as f_s,
        open('mult_file.txt', 'w', encoding='utf-8') as f_m
    ):
        len_f_n = len(f_n.readlines())
        len_f_s = len(f_s.readlines())

        for i in range(0, max(len_f_n, len_f_s)):
            temp_n = f_n.readline()
            temp_s = f_s.readline()
            if not temp_n:
                f_n.seek(0)
                temp_n = f_n.readline()
            if not temp_s:
                f_s.seek(0)
                temp_s = f_s.readline()

            temp = temp_n.split('|')
            mult = int(temp[0]) * float(temp[1])
            if mult < 0:
                f_m.write(f'{temp_s.lower()}  {mult.__round__(0)}\n')
            else:
                f_m.write(f'{temp_s.upper()}  {mult}\n')




if __name__ == '__main__':
    mult_file('../seminar_8/number.txt', '../seminar_8/data.txt')