# 46.	Задача: STUDENTS
# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
# *(прямая отсылка к первому семинару “введение в базы данных”)

# •	В рамках этого обсуждения студентам надо нарисовать “архитектуру” (например, в виде блок-схемы, https://app.diagrams.net/) для работы данного приложения.
# •	Выделяются роли: 
# - Тим-лид - “главный”, который создает репозиторий. В этот репозиторий должен попасть весь код, написанный командой (вспоминаем работу с гитом)
# - Студенты делят между собой модули программы. Каждый студент пишет свой модуль.
# Например:
# •	Первый студент может выступать в качестве эксперта, консультируя остальных по вопросам связанных с тем, как, например, складывать числа, или делить комплексные числа
# •	Второй студент пишет модуль работы с комплексными числами
# •	Третий студент пишет модуль работы с рациональными числами
# •	Четвертый студент описывает пользовательское меню и UI для работы с калькулятором. (в качестве UI используется консоль)


import controller
import os
os.system('cls')

controller.run()