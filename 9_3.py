# Task_3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

    def echo(self):
        print('my name is', self.name)
        print('my surname is', self.surname)
        print('my position is', self.position)
        print('i get {} + {} $ per month\n'.format(self._income.get('wage'), self._income.get('bonus')))


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        fullname = self.name + ' ' + self.surname
        print('Полное имя:', fullname)

    def get_total_income(self):
        full_income = self._income.get('wage') + self._income.get('bonus')
        print('Общий доход: {} $\n'.format(full_income))


a = Worker('Stan', 'Smith', 'driver', 80000, 15000)
a.echo()

b = Position('John', 'Travolta', 'CEO manager', 150000, 25000)
b.echo()
b.get_full_name()
b.get_total_income()

c = Position('Alex', 'Knyazev', 'CEO', 2000000, 500000)
c.echo()
c.get_full_name()
c.get_total_income()
