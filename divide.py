import csv
__author__ = 'Shih-Ting Huang', 'Wei-Yao Ku'

"""
CSCI-630: Final Project
Author: Shih-Ting Huang (sh3964), Wei-Yao Ku(wxk6489)

Extract dog and cat data
"""


def main():
    """
    Extract dog and cat data
    :return: None
    """
    i = 0
    filename = input()
    with open(filename + '.csv', newline='') as f:
        reader = csv.reader(f)
        dog = []
        cat = []
        for row in reader:
            if i is 0:
                title = row
            if row[1] == 'CAT':
                cat.append(row)
            if row[1] == 'DOG':
                dog.append(row)
            i += 1
    dog.sort(key=lambda tup: tup[0])
    cat.sort(key=lambda tup: tup[0])
    with open('dog.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(title)
        for i in range(len(dog)):
            writer.writerow(dog[i])
    with open('cat.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(title)
        for i in range(len(cat)):
            writer.writerow(cat[i])

if __name__ == '__main__':
    main()
