from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("capacity_volume должен быть типа int или float")
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("occupied_volume должен быть типа int или float")

        if capacity_volume <= 0:
            raise ValueError("capacity_volume должен быть больше нуля")
        if occupied_volume < 0:
            raise ValueError("occupied_volume не может быть отрицательным")
        if occupied_volume > capacity_volume:
            raise ValueError("occupied_volume не может превышать capacity_volume")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def __repr__(self):
        return f"Glass(capacity_volume={self.capacity_volume}, occupied_volume={self.occupied_volume})"
        # TODO инициализировать объект "Стакан"


if __name__ == "__main__":
    glass1 = Glass(250, 100)
    glass2 = Glass(350, 150)
    print(glass1)
    print(glass2)

    # Некорректная инициализация
    try:
        glass_invalid1 = Glass("250", 100)
    except Exception as e:
        print(f"Ошибка: {e}")

    try:
        glass_invalid2 = Glass(250, -50)
    except Exception as e:
        print(f"Ошибка: {e}")

    try:
        glass_invalid3 = Glass(250, 300)
    except Exception as e:
        print(f"Ошибка: {e}")
    # TODO инициализировать два объекта типа Glass

    # TODO попробовать инициализировать не корректные объекты
