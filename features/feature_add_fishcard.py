import os
import csv

class NewFishcardSet:

    def __init__(self,path,fishcard_set_name):
        self.path=path
        self.fishcard_set_name=fishcard_set_name
        self.is_uploaded=False
        self.chceck_status=True
        self.dictionary = self.csv_to_dict()
        self.fishcards_list = self.csv_to_list()

    def csv_to_dict(self):
        # import csv
        with open(self.path, mode='r',encoding="windows-1250") as content:
            reader = csv.DictReader(content)
            data = {row['angielski']:row['polski'] for row in reader}
        return data

    def csv_to_list(self):
        fishcards_list = []
        with open(self.path, mode='r',encoding="windows-1250") as content:
            for line in content.readlines():
                word_eng, word_pol = line.strip().replace('"','').split(',')
                fishcards_list.append(word_eng)
                fishcards_list.append(word_pol)
        return fishcards_list

    def generate_files_list(self):          #generuje liste plikow w folderu tlumaczenia
        files = os.listdir('../tlumaczenia/')
        files_file = [f for f in files if os.path.isfile(os.path.join('../tlumaczenia/', f))]
        return(files_file)

    def set_of_checks(self):
        self.check_duplicate_words()
        self.check_the_longest_word()
        self.check_quantity_of_pairs()
        self.check_duplicate_set_name()
        self.check_correct_path()
        self.check_space_in_set_name()

#-----------------------------sprawdzenia nazwy pliku------------------------
    def check_duplicate_set_name(self): # spr czy nazwa pliku juz istnieje
        print(self.fishcard_set_name)
        if (self.fishcard_set_name+'.py') in self.generate_files_list():
            message = 'Istnieje juz zestaw fiszek o tej nazwie'
            print(message)
            self.chceck_status = False
            print(self.chceck_status)

    def check_space_in_set_name(self):
        if (' ') in self.fishcard_set_name:
            print('empty space in name')
            self.chceck_status = False


    def check_correct_path(self): # zmien nazwe na spr czy plik csv
        if self.path[-4:] !='.csv':
            print(' format inny niz .csv')
            self.chceck_status=False
        else:
            print('correct')
            self.save_fishcard_set(self.dictionary)
#-------------------------sprawdzenia zawartosci pliku-------------------------
    def check_duplicate_words(self): # spr czy nazwa pliku juz istnieje
        if len(self.fishcards_list)==len(set(self.fishcards_list)):
            print('slowa są unikatowe')
        else:
            print('sa duplikaty w slowach')

    def check_quantity_of_pairs(self):
        if (len(self.dictionary))<=25:
            print('liczba par mniejsza rowna 25')
        else:
            print('liczba par wieksza niz 25')

    def check_the_longest_word(self): # spr dlugosc nazwy
        if len(max(self.fishcards_list))>=45:
            print('któreś ze slow ma więcej niz 45 znakow')
        else:
            print('slowa maja mniej niz 45 znakow')

#---------------------------sprawdz poprawnosc sciezki------------------------------
    def chceck_if_correct_path(self):
        pass
        # wyrzuc exception na plik nie istnieje w sciezce

    def save_fishcard_set(self,fishcard_dictionary):

        filename = '../tlumaczenia/'+self.fishcard_set_name+'.py'
        with open(filename, 'w') as f:
            print(dict(fishcard_dictionary))
            f.write(f"slownik = {dict(fishcard_dictionary)}")
        f.close()

        self.status_message()


    def status_message(self):
        file_list = self.generate_files_list()

        if (self.fishcard_set_name+'.py') in file_list:
            message= 'Fishcard added succesfully'
            print(message)
            self.is_uploaded=True

        else:
            message='abc'
            print(message)

