import re
import os
import csv
sent = {}
iter_1 = {}


# gets annotated files
def file_finder():
    # where = ['exam2015']
    where = ['exam2017', 'exam2016', 'exam2015', 'exam2014']
    for folder in where:
        file_address = '/Users/elizavetaersova/PycharmProjects/AWARL/POS REALEC/tags/' + folder
        files = os.listdir(file_address)
        txt_files = []
        for i in files:
            if i.endswith('.txt'):
                txt_files.append(i)
        search(txt_files, file_address)


# splits texts to get sentences and make a list from interrogative ones
def search(txt_files, file_address):
    for essay in txt_files:
        essay_address = file_address + '/' + essay
        with open(essay_address, 'r', encoding='utf-8') as file:
            text = file.read()
            sentences = text.split('@')
            for sentence in sentences:
                if '?' in sentence:
                    sent.update({sentence:essay})


# looks for all ,  wh-word sequences
def wh_search():
    wh_words = [', whether', ', if', ', what', ', when', ', where', ', who', ', whom', ', how']
    for i in sent:
        sentence = i.lower()
        for word in wh_words:
            if word in sentence:
                iter_1.update({i:sent[i]})
    print(len(iter_1))
    for a in iter_1:
        print(a)


# writes example sentences and the essays where they were found in the table
def csv_table_writer():
    for i in iter_1:
        sentence = i
        essay = iter_1[i]
        with open('tabletry2.csv', mode='a+', encoding="utf-8") as csv_file:
            fieldnames = ['sentence', 'essay']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
            writer.writerow({'sentence': sentence, 'essay': essay})


def main():
    file_finder()
    wh_search()
    csv_table_writer()


if __name__ == '__main__':
    main()