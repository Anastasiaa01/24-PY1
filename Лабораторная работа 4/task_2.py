# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    json_data = []
    with open(INPUT_FILENAME) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            json_data.append(row)


    # Возвращаем результат в формате JSON
    # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, "w") as json_file:
        json.dump(json_data, json_file, indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
