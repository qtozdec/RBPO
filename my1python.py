import psutil
import os
import random
import json
import xml.etree.ElementTree as ET
import zipfile


def print_disk_info():
    disk_info = []

    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue

        usage = psutil.disk_usage(part.mountpoint)

        print("device:", part.device)
        print("total:", usage.total)
        print("used:", usage.used)
        print("free:", usage.free)
        print("percent:", usage.percent)
        print("fstype:", part.fstype)
        print("mountpoint:", part.mountpoint)
        print()


def work_with_file():
    filename = input('\nВведите название файла: \n')

    with open(filename, 'w+', encoding='utf-8') as g:
        d = input('\nВведите строку\n')
        g.write(d)

    with open(filename, 'r', encoding='utf-8') as g:
        read_data = g.read()
        print('Строка из файла: ' + read_data)

    choice = input('Do you want delete this file? - y: ')
    if choice == 'y':
        os.remove(filename)
        print("Successful")


class some_struct():
    def __init__(self, id, name, some_doubles):
        self.id = id
        self.name = name
        self.some_doubles = some_doubles


def get_some_struct():
    id = int(input("id = "))
    name = input("name = ")
    some_doubles = []
    for i in range(0, 5):
        some_doubles.append(random.random())

    return some_struct(id, name, some_doubles)


def work_with_json():
    filename = input('name: ')
    ss = get_some_struct()
    with open(filename, 'w+', encoding='utf-8') as g:
        g.write(json.dumps(ss.__dict__))

    with open(filename, 'r', encoding='utf-8') as g:
        read_data = g.read()
        print('Строка из файла: ' + read_data)
    choice = input('Do you want delete this file? - y: ')
    if choice == 'y':
        os.remove(filename)
        print("Successful")


def work_with_xml():
    ss = get_some_struct()
    data = ET.Element("some_struct")
    id_element = ET.SubElement(data, "id")
    id_element.text = str(ss.id)

    name_element = ET.SubElement(data, "name")
    name_element.text = ss.name

    some_doubles_element = ET.SubElement(data, "some_doubles")
    for some_double in ss.some_doubles:
        some_double_element = ET.SubElement(some_doubles_element, "some_double")
        some_double_element.text = str(some_double)

    filename = input('name: ')
    with open(filename, 'w+', encoding='utf-8') as g:
        ET.tostring(data).decode()

    with open(filename, 'r', encoding='utf-8') as g:
        read_data = g.read()
        print('Строка из файла: ' + read_data)
    choice = input('Do you want delete this file? - y: ')
    if choice == 'y':
        os.remove(filename)
        print("Successful")


def work_with_zip():
    filename = input('name: ')
    f = zipfile.ZipFile(filename, "w")
    f.close()
    f = zipfile.ZipFile(filename, "a")
    filename_file = input("Enter filename: ")
    f.write(filename_file)
    f.close()
    archive = zipfile.ZipFile(filename, "r")
    data = archive.read(filename_file)
    archive.close()
    print(data)
    f = open(filename_file, "w+b")
    f.write(data)
    f.close()
    print("size:", os.path.getsize(filename_file))
    print("modify timestamp:", os.path.getmtime(filename_file))


def main():
    while True:
        print('1 - disk info\n2 - file\n3-json\n4-xml\n5-zip')
        a = input()
        if a == '1':
            print_disk_info()
        if a == '2':
            work_with_file()
        if a == '3':
            work_with_json()
        if a == '4':
            work_with_xml()
        if a == '5':
            work_with_zip()


if __name__ == "__main__":
    main()
