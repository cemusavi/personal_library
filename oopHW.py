import os
from termcolor import colored

os.system('cls')
class Book:
    def __init__(self, title, author, publish_year, pages, language, price,status='',progress=0):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.progress=progress
    
    def read(self, input_page):
        if input_page == self.pages:
            self.status='Finished'
            self.progress=100
        elif input_page > self.pages:
            print('!!!')
            self.progress=None
        elif input_page < self.pages:
            left = self.pages - input_page
            self.progress=round(((input_page)/self.pages)*100,2)
            self.status='Reading'
            print(f'{left} pages are left.')
        elif input_page==0:
            self.status='Unread'
            self.progress=0

    def get_status(self):
        print('status: ',self.status)

    def progress_(self):
        print(self.progress,'%')

    def __str__(self):
        return f'Title:"{self.title}"  Author(s): "{self.author}"   Publish_Year:{self.publish_year} ' \
               f'Pages: {self.pages} Language:{self.language} Price: {self.price}$'

class Magazine(Book):
    def __init__(self, title, author, publish_year, pages, language, price, issue,status='',progress=0):
        super().__init__(title, author, publish_year, pages, language, price,status='',progress=0)
        self.issue = issue

    def __str__(self): 
        return f'Title:"{self.title}"  Author(s): "{self.author}"   Publish_Year:{self.publish_year} ' \
               f'Pages: {self.pages} Language:{self.language} Price: {self.price}$ Issue: {self.issue}'

class Podcast:
    def __init__(self, title, publish_year, language, price, speaker, time, status='',progress=0):
        self.title = title
        self.publish_year = publish_year
        self.language = language
        self.price = price
        self.speaker=speaker
        self.time=time
        self.status=status
        self.progress=progress

    def listen(self, input_time):
        if input_time == self.time:
            self.status='Finished'
            self.progress=100
        elif input_time > self.time:
            print('!!!')
            self.progress=None
        elif input_time < self.time:
            left = self.time - input_time
            self.progress=round(((input_time)/self.time)*100,2)
            self.status='Listening'
            print(f'{left} minutes are left.')
        elif input_time==0:
            self.status='Not Listened'
            self.progress=0

    def get_status(self):
        print('status: ',self.status)

    def progress_(self):
        print(self.progress,'%')

    def __str__(self):
        return f'Title:"{self.title}"  Speaker(s): "{self.speaker}"   Publish_Year:{self.publish_year} ' \
               f'Pages: {self.time} Language:{self.language} Price: {self.price}$'

class AudioBook(Podcast):
    def __init__(self, title, speaker, author, publish_year,language, audio_language, time, pages, price,status='',progress=0):
        super().__init__(title, publish_year, language, price, speaker, time, status='',progress=0)
        self.audio_language=audio_language
    def __str__(self):
        return f'Title:"{self.title}"  Speaker(s): "{self.speaker}"   Publish_Year:{self.publish_year} ' \
            f'Pages: {self.time} Language:{self.language} Audio Language:{self.audio_language} Price: {self.price}$'
bookshelf=[]
def get_data():
    media_type = input('Please Choose your media("B" for Book "M" for Magazine "P" for Podcast '
                       '"A" for AudioBook) "Quit" to Stop\n')

    if media_type == 'B':
        n=input('Enter title, author, publish year, pages, language, price respectively : ').split(',')
        for i in range(len(n)):
            if n[i].isdigit():
                n[i]=float(n[i])
        bookshelf.append(Book(*n))

    elif media_type == 'M':
        n=input('Enter title, author, publish year, pages, language, price, issue respectively: ').split(',')
        for i in range(len(n)):
            if n[i].isdigit():
                n[i]=float(n[i])
        bookshelf.append(Magazine(*n))
    elif media_type == 'P':
        n=input('Enter title, speaker, publish year, time, language, price respectively : ').split(',')
        for i in range(len(n)):
            if n[i].isdigit():
                n[i]=float(n[i])
        bookshelf.append(Podcast(*n))
    elif media_type == 'A':
        n=input('title, speaker, author, publish year, book language, audio language, time, pages, price: ').split(',')
        for i in range(len(n)):
            if n[i].isdigit():
                n[i]=float(n[i])
        bookshelf.append(Podcast(*n))
    elif media_type == 'Q':
        print('You are returned to the main menu')
        return None

def choose_media():
    """
    This Function choose a media of the shown bookshelf by its number in list from user
    :return: chosen media by user
    """
    print('Choose the media title from list below or "0" to return to main menu :')
    for m in range(len(bookshelf)):
        print(f'\n {m + 1}){bookshelf[m].title}')
    media_type = int(input())   
    if media_type != 0:
        return bookshelf[media_type-1]   


def process_media(process):
    """
    This function does different process on a bookshelf(list of different media types)
    :param process: represents the action
    """
    if process == 'print':  
        for b in range(len(bookshelf)):
            print(f'{b + 1}: {bookshelf[b]}')
    elif process == 'read/listen':   
        while True:
            chosen_media = choose_media()  
            if chosen_media not in bookshelf:
                break
            else:
                 
                if isinstance(chosen_media, Book) or isinstance(chosen_media, Magazine):
                    chosen_media.read(
                        int(input(f'Hom many pages from "{chosen_media.title}" have you read?:  ')))
                elif isinstance(chosen_media, Podcast) or isinstance(chosen_media, AudioBook):
                    chosen_media.listen(
                        int(input(f'Hom many minutes from {chosen_media.title} have you listened?:  ')))
    elif process == 'get_status':  
        while True:
            chosen_media = choose_media()
            if chosen_media not in bookshelf:
                break
            else:
                chosen_media.get_status()

    elif process == 'progress':  
        while True:
            chosen_media = choose_media()
            if chosen_media not in bookshelf:
                break
            else:
                chosen_media.progress_()
    elif process == 'sort':  
        print('\nBookshelf sorted by progress:\n~~~~~~~~~~~~~~~~~~~~~`')
        sorted_bookshelf = sorted(bookshelf, key=lambda x: x.__getattribute__('progress'), reverse=True)
        for _ in sorted_bookshelf:
            class_name = type(_).__name__  
            print(f'<{class_name}> {_.title}, progress:{_.progress}%')

book1 = Book('No Friend But the Mountains', 'Behrouz Boochani', 2018, 347, 'Persian', 10)
book2 = Book('The Black Swan', 'Nassim Nicholas Taleb', 2007, 280, 'English', 20)
book3 = Book('Symphony of the Dead', 'Abbas Maroufi', 1989, 374, 'Persian', 126)
magazine1 = Magazine('Bukhara', 'Ali Dehbashi,Darioush Ashoori', 2020, 768, 'Persian', 55, 140)
podcast1 = Podcast('Ravaaq', 2020, 'English', 0, 'Farzin Ranjbar', 50)
audiobook1 = AudioBook('The Black Swan', 'Ali Bandari', 'Nassim Nicholas Taleb', 2020, 'English', 'Persian', 50, 62, 0)
bookshelf.extend((book1, book2, book3, magazine1, podcast1, audiobook1))

while True:
    print(colored('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                      'Select your action in list below:\n'
                      '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                      '1)Add a media\n'
                      '2)Show your bookshelf\n'
                      '3)Show a media status\n'
                      '4)Record your progress(Enter Read/Listened pages/time)\n'
                      '5)Show a media progress\n'
                      '6)Descending sort of bookshelf by progress\n'
                      'Enter Q to exit',attrs=['bold'],color='blue'))
    selection=input()

    if selection == 'Q':
        print(colored('"Good Luck"',color='yellow'))
        exit()
    elif selection == '1':
        get_data()
    elif selection == '2':
        process_media('print')
    elif selection == '3':
        process_media('get_status')
        continue
    elif selection == '4':
        process_media('read/listen')
    elif selection == '5':
        process_media('progress')
    elif selection == '6':
        process_media('sort')
get_data()


