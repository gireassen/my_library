import requests

def hello_world(n):
    for i in range(n):
        yield 'hello world'

def my_range(start, finish):

    while start < finish:
        yield start
        start += 1

def get_swapi_people():
    next_page = 'https://swapi.dev/api/people/'

    while next_page:
        result = requests.get(next_page).json()
        next_page = result['next']
        for character in result['results']:
            yield character

if __name__ == '__main__':
    for item in hello_world(4):
        print(item)
    for item in my_range(1, 5):
        print(item)
    for item in get_swapi_people():
        print(item)

# функция-генератор отдаёт не только своё значение, которое он сгенерировал, но и контроль выполнения программы
# и отдаёт его в то место, где была вызвана функция