import requests

class HelloWorld:
    '''
    В данном коде определен класс HelloWorld, который реализует итератор.\n
    Метод __init__ (или init) является конструктором класса и инициализирует его свойство n значением, переданным при создании объекта HelloWorld.\n
    Метод iter возвращает сам объект HelloWorld и также инициализирует свойство cursor значением 0. cursor - это переменная, которая будет использоваться для управления итерацией.\n
    Метод next вызывается при каждом следующем обращении к итератору. Если cursor превышает значение n, то генерируется исключение StopIteration, что означает окончание итерации. В противном случае, cursor увеличивается на 1 и возвращается строковое значение 'hello world'.\n
    Таким образом, объект класса HelloWorld может быть использован в цикле for-in или с функцией next(), чтобы итерировать и получать значения 'hello world', пока не будет сгенерировано исключение StopIteration.\n
    '''
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= self.n:
            print("StopIteration: ",HelloWorld.__name__)
            raise StopIteration
        self.cursor += 1
        return 'hello world'

class MyRange:
    '''
    В данном коде определен класс MyRange, который также реализует итератор.\n
    Метод __init__ (или init) является конструктором класса и инициализирует его свойства start и finish значениями, переданными при создании объекта MyRange.\n
    Метод iter возвращает сам объект MyRange и инициализирует свойство cursor значением start - 1. cursor - это переменная, которая будет использоваться для управления итерацией.\n
    Метод next вызывается при каждом следующем обращении к итератору. Сначала cursor увеличивается на 1. Затем проверяется, равен ли cursor значению finish. Если равен, то генерируется исключение StopIteration, что означает окончание итерации. Если не равен, то возвращается текущее значение cursor.\n
    В случае генерации исключения StopIteration, выводится сообщение "StopIteration: " вместе с именем класса (MyRange.name), чтобы указать, что итерация завершилась.\n
    Таким образом, объект класса MyRange может быть использован в цикле for-in или с функцией next(), чтобы итерировать и получать последовательность чисел от start до finish. При достижении значения finish, будет сгенерировано исключение StopIteration и итерация будет остановлена.\n
    '''
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.finish:
            print("StopIteration: ", MyRange.__name__)
            raise StopIteration
        return self.cursor

class SwapiPeople:
    '''
    В данном коде определен класс SwapiPeople, который также реализует итератор.\n
    base_url - это свойство класса, которое содержит базовый URL API https://swapi.dev/api/people/.\n
    Метод __init__ (или init) является конструктором класса. В данном случае он пустой, то есть не выполняет никаких действий при создании объекта.\n
    Метод iter возвращает сам объект SwapiPeople и инициализирует свойство next_page значением base_url. next_page - это переменная, которая будет использоваться для хранения URL следующей страницы результатов API. Также свойство chunk инициализируется пустым итератором iter([]). chunk - это переменная, которая будет использоваться для хранения текущей порции (частичного списка) персонажей.\n
    Метод next вызывается при каждом следующем обращении к итератору. Если значение next_page равно None, то генерируется исключение StopIteration, что означает окончание итерации. \n
    В противном случае, происходит попытка получить следующего персонажа из chunk. Если chunk уже исчерпан (генерируется исключение StopIteration), то происходит отправка GET-запроса на URL, указанный в next_page, и возвращается JSON-ответ в виде словаря. Затем, в свойство next_page записывается значение ключа 'next' в полученном ответе, которое содержит URL следующей страницы результатов. chunk инициализируется итератором по списку персонажей, полученных из ключа 'results'. В итоге, из chunk извлекается следующий персонаж и возвращается.\n
    Таким образом, объект класса SwapiPeople может быть использован в цикле for-in или с функцией next(), чтобы итерировать и получать по одному персонажу из API Star Wars. При достижении последней страницы результатов, будет сгенерировано исключение StopIteration и итерация будет остановлена.\n
    '''

    base_url = 'https://swapi.dev/api/people/'

    def __init__(self):

        pass

    def __iter__(self):
        self.next_page = self.base_url
        self.chunk = iter([])
        return self

    def __next__(self):
        if self.next_page is None:
            raise StopIteration
        try:
            character = next(self.chunk)
        except StopIteration:
            result = requests.get(self.next_page).json()
            self.next_page = result['next']
            self.chunk = iter(result['results'])
            character = next(self.chunk)
        return character

if __name__ == '__main__':
    for item in HelloWorld(4):
        print(item)

    for item in MyRange(1, 5):
        print(item)

    for item in SwapiPeople():
        print(item)


# Чтобы создать объект/класс в качестве итератора, вам необходимо реализовать методы __iter__() и __next__() для объекта.
# У всех классов есть функция под названием __init__(), которая позволяет вам делать инициализацию при создании объекта.
# Метод __iter__() действует аналогично, вы можете выполнять операции (инициализацию и т. Д.), Но всегда должны возвращать сам объект итератора. 
# Метод __next __ () также позволяет вам выполнять операции и должен возвращать следующий элемент в последовательности.

