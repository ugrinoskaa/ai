"""Потребно е да составите тим кој се состои од 1 тим лидер и 5 членови. Членовите се избираат од множество на N1 можни членови.
 Тим лидерот се избира од множество на N2 можни тим лидери. Притоа, секој член и тим лидер има одредена тежина
 (реална вредност помеѓу 0 и 100). Ваша задача е да креирате оптимален тим. Оптимален тим е тимот чија сума на тежини е највисока.
  Дополнително, сумата не треба да биде поголема од 100. Не е можно еден тим лидер или еден член да се избере повеќе од еднаш.
Од стандарден влез се чита бројот на можни членови, а потоа се читаат информации за секој член во следниот формат „тежина име“.
 Потоа, се чита бројот на можни тим лидери и информациите за секој тим лидер во следниот формат „тежина име“.
На стандарден излез да се испечати вкупната сума за формираниот тим. Потоа да се испечатат тим лидерот и членовите на тимот. """

from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    N1 = int(input())

    clenovi_tezina = []
    clenovi_ime = []
    for i in range(N1):
        clen = input()
        clen = clen.split(" ")
        clenovi_tezina.append(float(clen[0]))  # lista od tezinite -- domen
        clenovi_ime.append(clen[1])  # lista od iminjata na clenovite

    N2 = int(input())

    lideri_tezina = []
    lideri_ime = []
    for i in range(N2):
        lider = input()
        lider = lider.split(" ")
        lideri_tezina.append(float(lider[0]))  # -- domen
        lideri_ime.append(lider[1])

    problem.addVariable("Team leader", lideri_tezina)
    problem.addVariable("Participant 1", clenovi_tezina)
    problem.addVariable("Participant 2", clenovi_tezina)
    problem.addVariable("Participant 3", clenovi_tezina)
    problem.addVariable("Participant 4", clenovi_tezina)
    problem.addVariable("Participant 5", clenovi_tezina)

    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(MaxSumConstraint(100.0))

    solutions = problem.getSolutions()

    # tuka go naogjam maksimalniot total_score od site solutions
    # vo solution_found kje go imam solution-ot so najgolem total_score (kako sto e navedeno vo zadacata "Оптимален тим е тимот чија сума на тежини е највисока")
    max_total_score = 0
    #solution_found = dict()
    for solution in solutions:
        current_total = solution['Team leader'] + solution['Participant 1'] + solution['Participant 2'] + solution[
            'Participant 3'] + solution['Participant 4'] + solution['Participant 5']
        print(current_total)
        if current_total > max_total_score:
            max_total_score = current_total
            total_score = current_total
            solution_found = solution

    # ZA POSLEDNIOT TEST PRIMER, MOETO RESENIE NAOGJA POGOLEM TOTAL_SCORE (99.7)

    Team_leader = ""
    # da se zeme imeto na liderot
    for i in lideri_tezina:
        if solution_found['Team leader'] == i:
            index = lideri_tezina.index(i)
            Team_leader = lideri_ime[index]

    Participant_1 = ""
    Participant_2 = ""
    Participant_3 = ""
    Participant_4 = ""
    Participant_5 = ""
    # da se zeme imeto na sekoj clen
    for i in clenovi_tezina:
        if solution_found['Participant 1'] == i:
            index = clenovi_tezina.index(i)
            Participant_1 = clenovi_ime[index]
        if solution_found['Participant 2'] == i:
            index = clenovi_tezina.index(i)
            Participant_2 = clenovi_ime[index]
        if solution_found['Participant 3'] == i:
            index = clenovi_tezina.index(i)
            Participant_3 = clenovi_ime[index]
        if solution_found['Participant 4'] == i:
            index = clenovi_tezina.index(i)
            Participant_4 = clenovi_ime[index]
        if solution_found['Participant 5'] == i:
            index = clenovi_tezina.index(i)
            Participant_5 = clenovi_ime[index]

    print(f'Total score: {format(total_score, ".1f")}')
    print(f'Team leader: {Team_leader}')
    print(f'Participant 1: {Participant_1}')
    print(f'Participant 2: {Participant_2}')
    print(f'Participant 3: {Participant_3}')
    print(f'Participant 4: {Participant_4}')
    print(f'Participant 5: {Participant_5}')