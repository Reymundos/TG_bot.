 # namedtuple


# tuple ni ochib uning ichidan ma'lumotlarni olishni osonlashtirish:

# class Employees:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
# employees = [
#     (1, 'Toxir', 'Toxirov', 23, 'toir@gmail.com'),
#     (2, 'Zokir', 'Yokibov', 33, 'zokir@gmail.com')
# ]
#
# for employee in employees:
#     em = Employees(*employee)
#     em.name = 'Komil'
#     print(em.id, em.name, em.lastname, em.age, em.email)

# Bu xolatda ma'lumotni loish osonlashadi lekin uni o'zgatirish ham mumkin. 
 # Quyidagi xolatda namedtuple dan foydalanamiz




# --> Vazifa

# -- 1.1 --

# class Books:
#      def __init__(self, id, name, p_year, publisher, author):
#          self.id = id
#          self.name = name
#          self.p_year = p_year
#          self.publisher = publisher
#          self.author =author
#
# books = [
#     (1, 'Molxona', 2020, 'Yosh kitobxon', 'John Owel'),
#     (2, 'Jamila', 2018, 'Toshkent', 'Chingiz Aytmatov'),
#     (3, 'Evrilish', 2022, "O'qituvchi", 'Franz Kafka'),
#     (4, 'Alvido Gulsari', 2018, 'Toshkent', 'Chingiz Aytmatov')
# ]
#
# for book in books:
#     bk = Books(*book)
#     print(bk.id, bk.name, bk.p_year, bk.publisher, bk.author)

# -- 1.2 --

from collections import namedtuple

Books = namedtuple('Books', 'id name p_year publisher author')

books = [
    (1, 'Molxona', 2020, 'Yosh kitobxon', 'John Owel'),
    (2, 'Jamila', 2018, 'Toshkent', 'Chingiz Aytmatov'),
    (3, 'Evrilish', 2022, "O'qituvchi", 'Franz Kafka'),
    (4, 'Alvido Gulsari', 2018, 'Toshkent', 'Chingiz Aytmatov')
]
for book in books:
    bk = Books(*book)
    print(bk.id, bk.name, bk.p_year, bk.publisher, bk.author)