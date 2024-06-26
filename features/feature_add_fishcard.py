import os
import csv
import json

class NewFishcardSet:

    def __init__(self,path,fishcard_set_name):
        self.path=path
        self.fishcard_set_name=fishcard_set_name
        self.fishcard_language1 = ''
        self.fishcard_language2 = ''
        self.is_uploaded=False
        self.chceck_status=True
        self.dictionary = {}
        self.fishcards_list = []
        self.message = ''

    def csv_to_dict(self):
        with open(self.path, mode='r', encoding="UTF-8") as content:
            reader = csv.DictReader(content)
            data = {row[self.fishcard_language1]: row[self.fishcard_language2] for row in reader}
        return data

    def csv_to_list(self):
        fishcards_list = []
        with open(self.path, mode='r',encoding="UTF-8") as content:
            self.fishcard_language1, self.fishcard_language2 = (content.readline().strip().replace('"','').split(','))
            for line in content.readlines():
                word_language1, word_language2 = line.strip().replace('"','').split(',')
                fishcards_list.append(word_language1)
                fishcards_list.append(word_language2)
        return fishcards_list

    def generate_files_list(self):          #generuje liste plikow w folderu all_fishcards
        files = os.listdir('../all_fishcards/')
        files_file = [f for f in files if os.path.isfile(os.path.join('../all_fishcards/', f))]
        return(files_file)

    def set_of_checks(self):
        self.check_quantity_fishcard_list()
        if self.chceck_status == True:
            self.chceck_if_correct_path()
            if self.chceck_status == True:
                self.check_if_file_csv()
                if self.chceck_status == True:
                    self.fishcards_list = self.csv_to_list()
                    self.check_duplicate_words()
                    self.check_the_longest_word()
                    self.check_quantity_of_pairs()
                    self.check_name_length()
                    self.check_duplicate_set_name()
                    self.dictionary = self.csv_to_dict()
                    if self.chceck_status == True:
                        self.save_fishcard_set()

#------------------------sprawdzenie ilosci zbiorow fiszek ---------------------------
    def check_quantity_fishcard_list(self):
        list_of_fishcard = self.generate_files_list()
        if len(list_of_fishcard)>=10:
            self.chceck_status = False
            self.message = 'Jest za dużo zbiorów fiszek. Usuń zbiór żeby dodać nowy - zrobisz to w LIŚCIE FISZEK'

#-----------------------------sprawdzenia nazwy pliku------------------------
    def check_duplicate_set_name(self):
        if (self.fishcard_set_name+'.json') in self.generate_files_list():
            self.message = 'Istnieje już zestaw fiszek o tej nazwie. Zmień nazwę, aby dodać swój zbiór.'
            self.chceck_status = False

    def check_name_length(self):
        if len(self.fishcard_set_name)>30:
            self.message = 'Nazwa zbioru fiszek jest za długa. Ogranicz się do 30 znaków.'
            self.chceck_status = False

    def check_if_file_csv(self):
        if self.path[-4:] !='.csv':
            self.message = 'Format jest inny niz .csv. Wgraj plik w formacie .csv.'
            self.chceck_status=False

#-------------------------sprawdzenia zawartosci pliku-------------------------
    def check_duplicate_words(self):
        if len(self.fishcards_list)>len(set(self.fishcards_list)):
            self.message =('W pliku są słowa które się powtarzają. Usuń je, aby wgrać zbiór fiszek.')
            self.chceck_status = False

    def check_quantity_of_pairs(self):
        if (len(self.dictionary))>25:
            self.message =('W pliku jest za dużo fiszek. Ogranicz się do 25 par, aby wgrać plik.')
            self.chceck_status = False

    def check_the_longest_word(self):
        if len(max(self.fishcards_list))>=40:
            self.message =('W pliku jest słowo, które jest za długie. Ogranicz się do 40 znaków, aby wgrać plik')
            self.chceck_status = False

#---------------------------sprawdz poprawnosc sciezki------------------------------
    def chceck_if_correct_path(self):
        try:
            open(self.path,'r')
        except FileNotFoundError:
            self.message = 'Nie odnaleziono pliku. Sprawdź czy ścieżka jest poprawna.'
            self.chceck_status=False

    def save_fishcard_set(self):

        filename = '../all_fishcards/'+self.fishcard_set_name+'.json'
        with open(filename, 'w') as f:
            json.dump(self.dictionary,f)
        f.close()
        self.status_message()

    def status_message(self):
        file_list = self.generate_files_list()
        if (self.fishcard_set_name+'.json') in file_list:
            self.message = f'Zbiór fiszek {self.fishcard_set_name} został dodany'
            self.is_uploaded=True


