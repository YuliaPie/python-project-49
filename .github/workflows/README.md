### Hexlet tests and linter status:
[![Actions Status](https://github.com/YuliaPie/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/YuliaPie/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/86f36ebddad41482df90/maintainability)](https://codeclimate.com/github/YuliaPie/python-project-49/maintainability)


Описание

«Игры разума» — набор из пяти консольных игр. 
Каждая игра задает вопросы, на которые нужно дать правильные ответы. 
После трех правильных ответов считается, что игра пройдена. 
Неправильные ответы завершают игру и предлагают пройти ее заново. 

Игры:

- Калькулятор. Арифметические выражения, которые необходимо вычислить
- Прогрессия. Поиск пропущенных чисел в последовательности чисел
- Определение четного числа
- Определение наибольшего общего делителя
- Определение простого числа

Минимальные требования:
- Python версии 3.6 или выше. 
- pip версии 19 или выше. 
- пакетный менеджер poetry версии 1.2.0 или выше.

Установка и запуск:

- Склонируйте репозиторий локально.
- В командной строке из корневой директории выполните следующие команды:
  * poetry build
  * poetry publish --dry-run (возможно придется ввести имя пользователя и пароль)
  * python3 -m pip install --user dist/*.whl

- Игры можно запускать из командной строки следующими командами: 

  * brain-even - Определение четного числа
  * brain-gcd - Определение наибольшего общего делителя
  * brain-calc  - Калькулятор
  * brain-progression  - Прогрессия
  * brain-prime  - Определение простого числа

Далее приведены asciinema для иллюстрации запуска игр:

[![asciicast](https://asciinema.org/a/J2GGHZEg4eKqQsyRgp0Xb8XVu.svg)](https://asciinema.org/a/J2GGHZEg4eKqQsyRgp0Xb8XVu)

[![asciicast](https://asciinema.org/a/KnhhEMZYVKaYNKPgobKHD3VBS.svg)](https://asciinema.org/a/KnhhEMZYVKaYNKPgobKHD3VBS)

[![asciicast](https://asciinema.org/a/Z1qmZNq7eiwYGilHNJG91d7bq.svg)](https://asciinema.org/a/Z1qmZNq7eiwYGilHNJG91d7bq)

[![asciicast](https://asciinema.org/a/WHVO1Uy0CNNSssCKlF0TVDUwK.svg)](https://asciinema.org/a/WHVO1Uy0CNNSssCKlF0TVDUwK)

[![asciicast](https://asciinema.org/a/UPo5imtAhTict5UoJ3C3gUB1u.svg)](https://asciinema.org/a/UPo5imtAhTict5UoJ3C3gUB1u)
