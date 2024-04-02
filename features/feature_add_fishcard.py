import os

class NewFishcardSet:

    def __init__(self,path,fishcard_set_name):
        self.path=path
        self.fishcard_set_name=fishcard_set_name
        self.is_uploaded=False
        self.chceck_status=True
        self.dictionary = self.csv_to_dict()

    def csv_to_dict(self):
        import csv
        with open(self.path, mode='r',encoding="windows-1250") as infile:
            reader = csv.DictReader(infile)
            data = {row['angielski']:row['polski'] for row in reader}
        return data

    def generate_files_list(self):
        files = os.listdir('../tlumaczenia/')
        files_file = [f for f in files if os.path.isfile(os.path.join('../tlumaczenia/', f))]
        return(files_file)

    def set_of_checks(self):
        self.check_duplicate_set_name()
        self.check_correct_path()
        self.check_space_in_set_name()

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


    def check_correct_path(self):
        if self.path[-4:] !='.csv':
            print(' format inny niz .csv')
            self.chceck_status=False
        else:
            print('correct')
            self.save_fishcard_set(self.dictionary)

    def check_duplicate_fishcard(self): # spr czy nazwa pliku juz istnieje
        # duplikat w kluczu
        #duplikat w atrybucie

        pass
    def check_duplicate_fishcard(self): # spr dlugosc nazwy
        # duplikat w kluczu
        #duplikat w atrybucie

        pass


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

