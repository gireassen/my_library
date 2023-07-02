# Стэк

Стек – это структура данных, в которой элементы хранятся в порядке поступления. Его еще часто называют LIFO (Last-In/First-Out). Это отличает его от очереди, в которой элементы хранятся в порядке «первым пришел / первым обслужен» (FIFO).

![primer1](data:image/png;base64,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)

## Стэк вызовов

**Стек вызовов** (call stack) — стек, хранящий информацию для возврата управления из подпрограмм (функций) в программу или подпрограмму (при вложенных или рекурсивных вызовах).

![primer2](https://foxford.ru/uploads/tinymce_image/image/2803/%D1%81%D1%82%D0%B5%D0%BA_%D0%B2%D1%8B%D0%B7%D0%BE%D0%B2%D0%BE%D0%B22.png)

При вызове подпрограммы в стек заносится адрес возврата — адрес в памяти следующей инструкции приостанавливаемой программы, а управление передается подпрограмме. При последующем вложенном или рекурсивном вызове в стек заносится очередной адрес возврата и так далее.

При возврате из подпрограммы адрес возврата снимается со стека, и управление передается на следующую инструкцию приостановленной программы (или подпрограммы).

Предположим, имеется простая функция greet():

```
def greet(name):
    print f"Hello", +name+ "!"
    greet2(name)
    print("rdy to say goodbye")
    bye()

def greet2(name):
    print("how are you," + name + "?")

def bye():
    print("ok, bye!")
```

В программе используется вызов greet("Volodya"). Сначала компьютер выделяет блок памяти для этого вызова функции.

![Alt text](https://github.com/gireassen/my_library/blob/main/lib/groc_alg/stack/image.png?raw=true)

Затем эта память используется. Переменной *name* присваивается значение **Volodya**, оно должно быть сохранено в памяти. 

![Alt text](https://github.com/gireassen/my_library/blob/main/lib/groc_alg/stack/image-1.png?raw=true)

Каждый раз, когда вызываем фун-ю, компьютер сохраняет в памяти значение всех перерменных для этого вызова.
Далее выводится приветствие **Hello Volodya!**, после чего следует второй вызов **greet2(Volodya)**.
И снова пк выделяет блок памяти для вызова функции.

![Alt text](https://github.com/gireassen/my_library/blob/main/lib/groc_alg/stack/image-2.png?raw=true)

Пк объединяет эти блоки в стек. Второй блок создаётся над первым. Мы выводим сообщение **how are you, Volodya?**, после чего возвращаете управление из вызова функции. Когда это происходит, блок на верншине стека извлекается из него.

![Alt text](https://github.com/gireassen/my_library/blob/main/lib/groc_alg/stack/image-3.png?raw=true)

Теперь верхний блок относится к функции **greet()**, это означает, что вы вернулись к функции **greet()**. При вызове функции **greet2()** функция **greet()** еще <u>*не была завершена*</u>.
Здесь-то и скрывается истинный смысл Стэка вызовов:
<u>*Когда вы вызываете функцию, из другой функции, вызывающая функция приостанавливается в частично завершенном состоянии.*</u>
Все значения переменных этой функции остаются в памяти. А когда выполнение функции **greet2()** закончится, тогда веремся к функции **greet()** и продолжим её выполнение с того места, где оно прервалось.

![Alt text](https://github.com/gireassen/my_library/blob/main/lib/groc_alg/stack/image-4.png?raw=true)

Выводится сообщение ***rdy to say goodbye***, после вызывается функция **bye()**.

Блок для этой функции добавляетя на ввершину стека. Далее выводится сообщение ***ok, bye!*** с выходом из вызова функции.

![Alt text](https://github.com/gireassen/my_library/blob/main/lib/groc_alg/stack/image-5.png?raw=true)

Управление снова возвращается функции **greet()**.

[Назад](https://github.com/gireassen/my_library)