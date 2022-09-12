"""Потребно е да се закаже состанок во петок за Марија, Петар и Симона. Симона како менаџер мора да присуствува на состанокот со најмалку уште една личност.
 Состанокот трае еден час, и може да се закаже во периодот од 12:00 до 20:00. Почетокот на состанокот може да биде на секој час,
  односно состанокот може да почне во 12:00, но не во 12:05, 12:10 итн. За секој од членовите дадени се времињата во кои се слободни:

	•	Симона слободни термини: 13:00-15:00, 16:00-17:00, 19:00-20:00
	•	Марија слободни термини: 14:00-16:00, 18:00-19:00
	•	Петар слободни термини: 12:00-14:00, 16:00-20:00
Потребно е менаџерот Симона да ги добие сите можни почетни времиња за состанокот.
 Даден е почетен код со кој е креирана класа за претставување на проблемот, на кој се додадени променливите.
  Потоа се повикува наоѓање на решение со BacktrackingSolver. Ваша задача е да ги додадете домените на променливите,
   како и да ги додадете ограничувањата (условите) на проблемот. """

"""
{'Simona_prisustvo': 1, 'Marija_prisustvo': 1, 'Petar_prisustvo': 0, 'vreme_sostanok': 14}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 19}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 16}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 13} """

from constraint import *


def check_valid(s, m, p, v):
    if s == 1 and m == 1 and p == 1:
        return False

    if s == 1 and (m == 1 or p == 1) and v in [13, 14, 16, 19]:
        if m == 1 and v in [14, 15, 18]:
            return True

        if p == 1 and v in [12, 13, 16, 17, 18, 19]:
            return True

    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [12, 13, 14, 15, 16, 17, 18, 19])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(check_valid, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])

    # ----------------------------------------------------

    for solution in problem.getSolutions():
        result = "{}'Simona_prisustvo': {}, 'Marija_prisustvo': {}, 'Petar_prisustvo': {}, 'vreme_sostanok': {}{}".format(
            "{", solution['Simona_prisustvo'], solution['Marija_prisustvo'], solution['Petar_prisustvo'],
            solution['vreme_sostanok'], "}")
        print(result)