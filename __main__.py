from core.common.sections import section_selection
from core.common.sections import sections
import sys


choice = int(input("Выберите режим работы "
                "(Графический интерфейс - 1 ;"
                " Консольный режим - 2 ;"))
match choice:
    case 1:
        from gui.run_gui_file import run_gui
        
        if __name__ == "__main__":
            run_gui()
        else:
            sys.exit()
    case 2:
        section = int(input("Выберите раздел физики "
                    "(Механика - 1 ;"
                    " Термодинамика и статистическая физика - 2 ;"
                    " Электродинамика - 3 ;"
                    " Оптика - 4;"))

        section_selection(sections[section], section)