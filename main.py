import csv
import re
from decorators import logger_


@logger_('log.txt')
def read_file(filename):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


@logger_('log.txt')
def format_phone_numbers(contacts_list):
    for row in contacts_list[1:]:
        pattern = r'(\+*\d)[\s(]*\(*(\d{3})[)|-]*\s*(\d{3})\-*\s*(\d{2})\-*\s*(\d{2})([\s(])*([доб.]*)\s*([\d{4}]*)(\))*'
        sub = r'+7(\2)\3-\4-\5 \7\8'
        row[5] = re.sub(pattern, sub, row[5]).strip()
    return contacts_list


if __name__ == '__main__':
    format_phone_numbers(read_file('phonebook_raw.csv'))
