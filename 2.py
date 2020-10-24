import random

NAMES = """ Августа
            Аврелія
            Аврора
            Агапія
            Агата
            Агафія
            Аглая
            Агнеса
            Агнешка
            Аделінда
            Адель
            Адріана
            Алена
            Алехандра
            Аліна
            Аліса
            Алісія
            Алла
            Альбіна
            Альона
            Амалія
            Анастасія
            Ангеліна
            Анетт
            Анжеліка
            Анна
            Антоніна
            Ассоль
            Аурика
            Б'янка
            Бажена
            Беатриса
            Белла
            Богдана
            Божена
            Бріттані
            Валерія
            Василина
            Васса
            Венера
            Вероніка
            Вікторія
            Віра
            Владислава
            Габрієль
            Гаїанія
            Галина
            Ганна
            Гертруда
            Гіларі
            Гремислава
"""


def binary_search(arr, l, r, x):
    mid = l + (r - l) // 2
    return -1 if r < l else mid if arr[mid] == x else binary_search(arr, l, mid-1, x) if arr[mid] > x else binary_search(arr, mid + 1, r, x)


if __name__ == "__main__":
    while True:
        names = sorted(NAMES.split())
        targer = random.choice(names)
        print(targer)
        index = binary_search(names, 0, len(names)-1, targer)
        print(index)
        print(names[index])
