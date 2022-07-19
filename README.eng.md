![linux-perfd](https://user-images.githubusercontent.com/94864283/179859682-de27c527-184f-4ee3-8eb8-7dce1fb2ffe7.png)


## About
In the framework of this project, an automatic profile information collection system using BOLT technology was introduced. When using profile optimizations, Clang compiler performance increases up to 30%, after the profile has been collected, it should be passed to the compiler for re-optimization, but in many cases recompilation is't possible. 
BOLT is the technology that solves this problem. BOLT allows for significant acceleration without recompiling.

Perfd is implemented as a Python script. It is registered in the system as a service using systemd. Profile collection uses Linux perf system utility.The database is sqlite.

## Documentation

### BOLT:
-  **`BOLT`** - is a post-link optimizer developed to speed up large applications. It achieves the improvements by optimizing application's code layout based on execution profile gathered by sampling profiler, such as Linux perf tool.

### SQL30:
-  **`SQL30`** - is a zero weight ORM(Object–relational mapping) for sqlite3 in Python.
-  **`ORM(Object–relational mapping)`** - in computer science is a programming technique for converting data between type systems using object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language. 
### Systemd:
-  **`Systemd`** - это менеджер демонов в Linux. Этот демон позволяет управлять запуском сервисов и обеспечивает такие функции, как мониторинг и логирование.

## Installation
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


## Developers

- [Amir Ayupov](https://github.com/aaupov)
- [Maxim Shcherbakov](https://github.com/M4RFF)

## License
Project Linux-perfd is distributed under the MIT license.
