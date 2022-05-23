import random
from faker import Faker
fake = Faker()
import datetime


class MotionPicture:
    mp_library = []

    def __init__ (self, title, year, genre, time_played):
        self.title = title
        self.year = year
        self.genre = genre
        self.time_played = time_played
        self.mp_library.append(self)


    def play(self):
        self.time_played += 1


class Movie(MotionPicture):
    def __str__(self):
        return f'{self.title} ({self.year})'


    def __repr__(self):
        return f"Movie({self.title}, {self.year}, {self.genre}, {self.time_played})"
        
class Series(MotionPicture):
    def __init__ (self, title, year, genre, time_played, episode_numb, season_numb):
        super().__init__(title, year, genre, time_played)
        self.episode_numb = episode_numb
        self.season_numb = season_numb
    
    def __str__(self):
        return f'{self.title} S{str(self.season_numb).zfill(2)}E{str(self.episode_numb).zfill(2)}'


    def __repr__(self):
        return f"Series({self.title}, {self.year}, {self.genre}, {self.time_played}, S{self.season_numb}, E{self.episode_numb})"


        
def get_movies():
    m_list = []
    for obj in MotionPicture.mp_library:
        if isinstance(obj, Movie) == True:
            m_list.append(obj) 
        else:
            pass
    m_list = sorted(m_list, key= lambda obj: obj.title)
    return print(m_list)


def get_series():
    s_list = []
    for obj in MotionPicture.mp_library:
        if isinstance(obj, Series) == True:
            s_list.append(obj) 
        else:
            pass
    s_list = sorted(s_list, key= lambda obj: obj.title)
    for ser in s_list:
        print(ser)


def search(ask_title = None):
    ask_title = input('What are you looking for (title)? ')
    for obj in MotionPicture.mp_library:
        if obj.title == ask_title.title():
            print(obj.title)
            break

def ten_times(func):
    def wrapper():
        for i in range(10):
            func()
    return wrapper


@ten_times
def generate_views():
    obj = random.choice(MotionPicture.mp_library)
    obj.time_played += random.randint(1,100)

def msg_top(func):
    intro = 'Biblioteka filmów'
    print(intro)
    x = datetime.datetime.now()
    date = f'{x.day}.{x.month}.{x.year}'
    best = f'Najpopularniejsze filmy i seriale dnia {date}'
    print(best)


def top_titles(how_many, content_type=None):
    content_type = input('Do you want popular (m)ovies or (s)eries?: ')
    top_movies = []
    top_series = []
    if content_type == 's':
        for obj in MotionPicture.mp_library:
            if isinstance(obj, Series) == True:
                top_series.append(obj) 
                top_series = sorted(top_series, key= lambda obj: obj.time_played, reverse= True)[:(how_many)]
            else:
                pass
    elif content_type == 'm':
        for obj in MotionPicture.mp_library:
            if isinstance(obj, Movie) == True:
                top_movies.append(obj) 
                top_movies = sorted(top_movies, key= lambda obj: obj.time_played, reverse= True)[:(how_many)]
            else:
                pass
    else: 
        print('Wrong input')


    if content_type == 's':
        for s in top_series:
            print(s)
    else:
        for m in top_movies:
            print(m)
    

def create_series():
    for _ in range(20):
        title = fake.text(max_nb_chars=10)[:-1]
        year = random.randint(1950,2022)
        genre = fake.word(ext_word_list=['Action','Comedy','Drama','Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller', 'Western'])
        time_played = 0
        episode_numb = random.randint(1, 24)
        season_numb = random.randint(1, 6)
        s_title = Series(title, year,  genre, time_played, episode_numb, season_numb)


def create_movie():
    for _ in range (20):
        title = fake.text(max_nb_chars=10)[:-1]
        year = random.randint(1930,2022)
        genre = fake.word(ext_word_list=['Action','Comedy','Drama','Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller', 'Western'])
        time_played = 0
        m_title = Movie(title, year, genre, time_played) 



create_movie()
create_series()
generate_views()
msg_top()
top_titles(3)



