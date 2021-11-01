# Task_5

class Stationary:
    def __init__(self, title='Something that can draw'):
        self.title = title

    def draw(self):
        print(f'Start drawing! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Start drawing with {self.title} pen!')


class Pencil(Stationary):
    def draw(self):
        print(f'Start drawing with {self.title} pencil!')


class Handle(Stationary):
    def draw(self):
        print(f'Start drawing with {self.title} marker!')


stat = Stationary()
pen = Pen('Erich Krause')
pencil = Pencil('Faber-Castell')
marker = Handle('Copic')

office_supplies = [stat, pen, pencil, marker]

for i in office_supplies:
    i.draw()
