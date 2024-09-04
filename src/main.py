from models import *
from controllers import *

if __name__ == '__main__':
    sample = AVLTree()
    sample.insert(search_in_csv("What the #*! Do We (K)now!?"))
    sample.insert(search_in_csv("Kinsey"))
    sample.insert(search_in_csv("Four Brothers"))
    sample.insert(search_in_csv("xXx: State of the Union"))
    sample.insert(search_in_csv("Wallace & Gromit: The Curse of the Were0Rabbit"))
    sample.insert(search_in_csv("Madagascar"))
    sample.insert(search_in_csv("Charlie and the Chocolate Factory"))
    sample.insert(search_in_csv("The Core"))
    sample.insert(search_in_csv("A Walk to Remember"))
    sample.insert(search_in_csv("Doraemon: Nobita and the Robot Kingdom"))
    sample.insert(search_in_csv("Gangs of New York"))
    sample.insert(search_in_csv("China: The Panda Adventure"))
    sample.insert(search_in_csv("Godzilla Mothra and King Ghidorah: Giant Monsters All0Out Attack"))
    sample.insert(search_in_csv("Drowning Mona"))
    sample.insert(search_in_csv("Boiler Room"))
    sample.insert(search_in_csv("Saving Grace"))
    sample.insert(search_in_csv("Mission to Mars"))
    sample.insert(search_in_csv("Nutty Professor II: The Klumps"))
    sample.insert(search_in_csv("Silent Love"))
    sample.insert(search_in_csv("Me Contro Te - Il film: Operazione Spie"))
    sample.insert(search_in_csv("Jesus Thirsts: The Miracle of the Eucharist"))
    sample.insert(search_in_csv("The Good Teacher"))
    sample.insert(search_in_csv("Let's Go! Anpanman: Baikinman and Lulun"))
    sample.insert(search_in_csv("Pare parecchio Parigi"))
    sample.insert(search_in_csv("How to Make Millions Before Grandma Dies"))
    sample.insert(search_in_csv("Columbia 100th Anniversary Series Columbia 100th Anniversary Series"))
    sample.insert(search_in_csv("SUGA: Agust D Tour 'D-DAY' the Movie"))
    sample.insert(search_in_csv("Ducobu passe au vert!"))
    sample.insert(search_in_csv("Drive-Away Dolls"))
    sample.insert(search_in_csv("Uma Musume: Pretty Derby - Beginning of a New Era"))
    
    print(sample)
    
    sample.print_balance_inorder(sample.root)
        
    
    
