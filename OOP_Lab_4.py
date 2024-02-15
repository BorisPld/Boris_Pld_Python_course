if __name__ == "__main__":
    class Apple_iPhone_11:
        """ Базовый класс, описывающий Айфон 11. """

        Apple_iPhone_11_Pro_number_of_cameras = 3

        def __init__(self, capacity: int, model: str, number_of_cameras: int) -> None:
            """
            Создание и подготовка к работе объекта "Айфон 11"

            :param capacity: Объём памяти
            :param model: Модель
            :param number_of_cameras: Количество камер

            Пример:
            >>> iPhone_11 = Apple_iPhone_11(64, "Apple iPhone 11", 2)
            """
            self.capacity = capacity
            self.model = model
            if not isinstance(number_of_cameras, int):
                raise TypeError
            if number_of_cameras < 0:
                raise ValueError
            self.number_of_cameras = number_of_cameras
            self.additional_sales()
            self.flattery()

        def __str__(self) -> str:
            """
            Функция, которая выводит информацию о телефоне

            :return: Информация о телефоне в формате строки
            """
            return f"Модель: {self.model}. Количество камер: {self.number_of_cameras}."

        def __repr__(self) -> str:
            """
            Ещё одна функция, которая выводит информацию о телефоне

            :return: Информация о телефоне в формате repr
            """
            return f"{self.__class__.__name__}(model={self.model!r}, number_of_cameras={self.number_of_cameras!r})"

        def additional_sales(self) -> None:
            """ Функция, которая стремится токсично продать пользователю телефон с 3 камерами, если у него их меньше 3. """
            cls = self.__class__
            if self.number_of_cameras < cls.Apple_iPhone_11_Pro_number_of_cameras:
                print("Ваш телефон отстой. Пора переходить на iPhone 11 Pro - у него и камер больше и выглядит лучше.")
            else:
                print("Ваш телефон пока ещё в тренде. Проверяйте его актуальность на официальном сайте хотя бы раз в неделю, чтобы не огорчать своих подписчиков некачественными фото.")


        def flattery(self) -> None:
            """ Функция, которая токсично убеждает пользователя в уникальности используемого бренда. """
            print("Вы пользуетесь отличным телефоном лучшего бренда. Ваш телефон почти iPhone 11 Pro.")

    class Apple_iPhone_11_Pro(Apple_iPhone_11):
        """ Дочерний класс Айфона 11 Pro. """

        Apple_iPhone_11_Pro_number_of_cameras = 3

        def __init__(self, capacity: int, model: str, number_of_cameras: int, superiority: bool) -> None:
            """
            Создание и подготовка к работе объекта "Айфона 11 Pro".

            Конструктор базового класса был унаследован и расширен дополнительным параметром.
            Поскольку конструктор был унаследован, то вызываемые в нём методы вызовутся и здесь.

            :param capacity: Объём памяти
            :param model: Модель
            :param number_of_cameras: Количество камер
            :param superiority: Превосходство модели над остальными

            Пример:
            >>> iPhone_11_Pro = Apple_iPhone_11_Pro(64, "Apple iPhone 11 Pro", 3, True)
            """
            super().__init__(capacity, model, number_of_cameras)
            self.superiority = superiority


        def __str__(self) -> str:
            """
            Функция, которая выводит информацию о телефоне.
            Метод был перезагружен с вызовом конструктора базового класса.

            :return: Информация о Айфоне 11 Pro в формате строки
            """
            return f"{super().__str__()} Превосходство модели над остальными: {self.superiority}"

        def __repr__(self) -> str:
            """
            Ещё одна функция, которая выводит информацию о телефоне.
            Метод был перезагружен с вызовом конструктора базового класса.

            :return: Информация о Айфоне 11 Pro в формате repr
            """
            return f"{super().__repr__().replace(')', '')}, content={self.superiority!r})"

        def flattery(self) -> None:
            """ Функция, которая убеждает пользователя в уникальности используемого бренда.
                Этот метод был перезагружен, так как нет необходимости токсично показать пользователю, что есть телефон лучше, поскольку у него и так последяя модель."""

            print("Вы пользуетесь последней моделью телефона лучшего бренда: iPhone 11 Pro!")

        # print(Auto("ВАЗ", "2121", 11))
        # print(Truck("ЗИЛ", "130", 11, "Пшено"))
        # Write your solution here


    pass

print(Apple_iPhone_11_Pro(64, "Apple iPhone 11 Pro", 3, True))
