from models import *
from controllers import *

if __name__ == '__main__':
    """
        Testeos de mi commit:
            # Correción del insert
                tree.insert("titulo de la pelicula")
            + Método que imprime los balances en inorden
                tree.print_balances_inorder(node)
            # Corrección del balanceo
                + Método calculate_ascendance()
                # Corrección método calculate_node_balance()
            + Método csv_head(i)
                Retorna los primeros i elementos del csv en forma de list[str]
            + Método search in csv("titulo de la pelicula")
                Retorna si la pelicula se encuentra en el csv
                Usado en el AVLTree.insert()
            # csv_path como variable estática en csv_handler
    """
    sample = AVLTree()
    
    print("==============================INSERTS=====================")
    sample.insert("Boléro")
    sample.insert("La petite vadrouille")
    sample.insert("Let's Go! Anpanman: Baikinman and Lulun")
    sample.insert("Gondola")
    sample.insert("Boy Kills World")
    sample.insert("Lucky Winners")
    sample.insert("Baby boom or Eggnog 5")
    sample.insert("The Fabulous Four")
    sample.insert("The Lord of the Rings: The Two Towers 2024 Re-release")
    sample.insert("2024 Oscar Nominated Short Films: Documentary")
    sample.insert("The Good Teacher")
    sample.insert("Budda. Dzieciak '98")
    sample.insert("Loving Bali")
    sample.insert("The Long Game")
    sample.insert("Tri bogatyrya. Ni dnya bez podviga")
    sample.insert("White Bird")
    sample.insert("Kensuke's Kingdom")
    sample.insert("Voditel-oligarkh")
    sample.insert("Too Old for Fairy Tales 2")
    sample.insert("Siccin 7")
    sample.insert("Jesus Thirsts: The Miracle of the Eucharist")
    sample.insert("Buzz House: The Movie")
    sample.insert("We 12")
    sample.insert("Me Contro Te - Il film: Operazione Spie")
    sample.insert("Menudas piezas")
    sample.insert("Silent Love")
    
    print("=========tree===========")
    print(sample)
    
    print("=====balances inorder=====")
    sample.print_balances_inorder(sample.root)

    print("==============================DELETES=====================")
    sample.delete("Boléro")
    sample.delete("La petite vadrouille")
    sample.delete("Let's Go! Anpanman: Baikinman and Lulun")
    sample.delete("Boy Kills World")
    sample.delete("The Lord of the Rings: The Two Towers 2024 Re-release")
    sample.delete("2024 Oscar Nominated Short Films: Documentary")
    sample.delete("Kensuke's Kingdom")
    sample.delete("Voditel-oligarkh")
    sample.delete("Too Old for Fairy Tales 2")
    sample.delete("Siccin 7")
    sample.delete("Buzz House: The Movie")
    
    print("=========tree===========")
    print(sample)
    
    print("=====balances inorder=====")
    sample.print_balances_inorder(sample.root)

    for i in csv_head():
        print(i)