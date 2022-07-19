<p align="center">
      <img src="Project Logo Url" width="726">
</p>

## О проекте 

В данном проекте реализована система автоматического сбора профильной информации с применением технологии BOLT.  При использовании профильных оптимизаций производительность компилятора Clang повышается до 30%, после сбора профиля необходимо передать его компилятору для повторной оптимизации, но во многих случаях перекомпиляция не возможна. BOLT – технология, которая решает эту проблему. BOLT позволяет получить существенное ускорение без перекомпиляции.  

Perfd реализован, как скрипт на языке Python. Он зарегистрирован в системе как сервис при помощи systemd. Сбор профиля использует системную утилиту Linux perf.
В качестве базы данных используется sqlite.

## Документация

### BOLT:
- **-** **`BOLT`** - это оптимизатор пост-компоновки, разработанный для ускорения работы больших приложений.

### SQL30:
-  **`SQL30`** - это нуливое значение ORM(Object–relational mapping) для sqlite3 в Python.
-  **`ORM(Object–relational mapping)`** - это метод для преобразования данных  между типов систем с использованием объектно ориентированных языков программирования.
### Systemd:
-  **`Systemd`** - это менеджер демонов в Linux, который позволяет управлять запуском сервисов и обеспечивает такие функции, как мониторинг и логирование.

## Установка
### BOLT:
    > ` git clone https://github.com/facebookincubator/BOLT llvm-bolt`
    >`mkdir build`
    > `cd build`
    > `cmake -G Ninja ../llvm-bolt/llvm -DLLVM_TARGETS_TO_BUILD="X86;AArch64" -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=ON -DLLVM_ENABLE_PROJECTS="clang;lld;bolt"`
    > `ninja`

### SQL30:
-  **`pip install sql30`**

### Systemd:
    > `apt-get update -y`
    > `apt-get install -y systemd`

## Разработчики

- [Amir Ayupov](https://github.com/aaupov)
- [Maxim Shcherbakov](https://github.com/M4RFF)

## Лицензия:

Проект Linux-perfd распространяется под лицензией MIT license
