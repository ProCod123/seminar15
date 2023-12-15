import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='file_info.log', level=logging.INFO)

# Создаем объект namedtuple для хранения информации о файле/директории
File = namedtuple('File', ['name', 'extension', 'is_dir', 'parent_dir'])


def get_file_info(path):
    try:
        # Получаем список содержимого директории
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            parent_dir = os.path.basename(path)
            is_dir = os.path.isdir(full_path)
            name, extension = os.path.splitext(item) if not is_dir else (item, None)
            
            # Создаем объект File и сохраняем информацию в лог-файл
            file_info = File(name, extension, is_dir, parent_dir)
            logging.info(f"File info: {file_info}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


path = input("Введите путь до директории: ")
get_file_info(path)
