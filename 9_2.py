# Task_2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см = " \
               f"{(self._length * self._width * weight * thickness) // 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())

# class Road:
#     def __init__(self, le, wi):
#         self._length = le
#         self._width = wi
#
#     def calc(self, weight=25, thickness=5):
#         print(f'Масса асфальта - {self._length * self._width * weight * thickness / 1000} тонн')
#
#
# def main():
#     while True:
#         try:
#             road_1 = Road(int(input('Введите длину дороги в метрах: ')), int(input('Введите ширину дороги в метрах: ')))
#             road_1.calc()
#             break
#         except ValueError:
#             print('Только целые числа!')
