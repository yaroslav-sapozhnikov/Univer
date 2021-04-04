from FileManager import FileHandler


def main():
    # Экземпляр обработчика файлов
    file_processing = FileHandler()

    while True:

        command = input("\n//:").split(" ")

        # Остановка работы программы
        if command[0] == "exit":
            break

        # Получаем результат существования команды
        result = file_processing.router(command[0])
        # Если есть такая команда
        if result:
            try:
                result(*command[1:])
            except TypeError:
                print(f"Команда {command[0]} была вызвана с некорректными аргументами")

        else:
            commands_str = "\n".join(
                [
                    f"{key} - {value}"
                    for (key, value) in FileHandler.get_commands().items()
                ]
            )
            print(f"Команда {command[0]} не найдена! Список команд:\n{commands_str}")

    print("Произведен выход из программы.")


if __name__ == "__main__":
    main()