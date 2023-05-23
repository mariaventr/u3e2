from claseManejaHelados import ManejadorHelado
from claseManejaSabores import ManejadorSabores
from claseMenu import Menu

if __name__=="__main__":
    menu=Menu()
    ManejadorS=ManejadorSabores()
    listaS=ManejadorS.cargarDatos()
    ManejadorH=ManejadorHelado()
    menu.ejecutar(listaS, ManejadorH)