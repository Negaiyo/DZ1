# 1. Создайте класс Human.
# 2. Определите для него два статических поля: default_name и default age.
# 3. Создайте метод ＿init (), который помимо self принимает еще два параметра: name и age.
# Для этих параметров задайте значения по умолчанию, используя свойства default name и default_age. В методе ＿ init ()
# определите четыре свойства: Публичные - name и age. Приватные - money и house.
# 4. Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# 5. Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
# 6. Реализуйте метод earn money(), увеличивающий значение свойства money.



class Human:

    default_name = ""
    default_age = 0

    def __init__(self, name, age,
                 money, house):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        print(self.name, self.age, self.__house, self.__money)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self):
        self.__money += 10

c = Human("Valera", 22, 1000, "House")
c.earn_money()
c.info()

