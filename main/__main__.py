from sections.main import section_selection
from sections.enum import sections
import sys


choice = int(input("Выберите режим работы "
                "(Графический интерфейс - 1 ;"
                " Консольный режим - 2 ;"))
match choice:
    case 1:
        from gui import run_gui
        run_gui()


        def main_cli():

            return choice


        if __name__ == "__main__":
            if "--gui" in sys.argv:
                from gui import run_gui

                run_gui()
            else:
                main_cli()
    case 2:
        section = int(input("Выберите раздел физики "
                    "(Механика - 1 ;"
                    " Термодинамика и статистическая физика - 2 ;"
                    " Электродинамика - 3 ;"
                    " Оптика - 4;"))

        section_selection(sections[section], section)




