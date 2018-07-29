
from graphics import* 
import random

win = GraphWin("Aprendendo graphics", 525,475)
color_background = win.setBackground('white')
quadrantes = []
    
def main(): 
    global win
    global quadrantes

    # fazendo quadrantes
    linha = Line(Point(75,100), Point(75,475))#primeira coluna
    linha.draw(win)
	
    linha = Line(Point(150,100), Point(150,475))#segunda coluna
    linha.draw(win)
    
    linha = Line(Point(225,100), Point(225,475))#terceira coluna
    linha.draw(win)
    
    linha = Line(Point(300,100), Point(300,475))#quarta coluna
    linha.draw(win)

    linha = Line(Point(375,100), Point(375,475))#quinta coluna
    linha.draw(win)
    
    linha = Line(Point(450,100), Point(450,475))#sexta coluna
    linha.draw(win)

    linha = Line(Point(525,100), Point(525,475))#setima coluna
    linha.draw(win)

    linha = Line(Point(0,100), Point(525,100)) #primeira linha
    linha.draw(win)
    
    linha = Line(Point(0,175), Point(525,175)) #segunda linha
    linha.draw(win)
    
    linha = Line(Point(0,250), Point(525,250))#terceira linha
    linha.draw(win)
    
    linha = Line(Point(0,325), Point(525,325))#quarta linha
    linha.draw(win) 
    
    linha = Line(Point(0,400), Point(525,400)) #quinta linha
    linha.draw(win)

    linha = Line(Point(0,475), Point(525,475)) #sexta linha
    linha.draw(win)
#fazendo o sorteio da distribuicao das bolinhas
    for i in range(35):
        n = random.randint(1,5)
        quadrantes.append(n)
    print(quadrantes)
    
#fazendo a primeira distribuicao de bolinhas
    for y in range (35):
        if quadrantes[0] == 1:
            quadrantes [0] = Image(Point(37.5,137.5),"carro1.gif")
            quadrantes[0].draw(win)
        if quadrantes[1] == 1:
            quadrantes [1] = Image(Point(112.5,137.5),"carro1.gif")
            quadrantes[1].draw(win)
        if quadrantes[2] == 1:
            quadrantes [2] = Image(Point(187.5,137.5),"carro1.gif")
            quadrantes[2].draw(win)
        if quadrantes[3] == 1:
            quadrantes [3] = Image(Point(262.5,137.5),"carro1.gif")
            quadrantes[3].draw(win)
        if quadrantes[4] == 1:
            quadrantes [4] = Image(Point(337.5,137.5),"carro1.gif")
            quadrantes[4].draw(win)
        if quadrantes[5] == 1:
            quadrantes [5] = Image(Point(412.5,137.5),"carro1.gif")
            quadrantes[5].draw(win)
        if quadrantes[6] == 1:
            quadrantes [6] = Image(Point(487.5,137.5),"carro1.gif")
            quadrantes[6].draw(win)
        if quadrantes[7] == 1:
            quadrantes [7] = Image(Point(37.5,212.5),"carro1.gif")
            quadrantes[7].draw(win)
        if quadrantes[8] == 1:
            quadrantes [8] = Image(Point(112.5,212.5),"carro1.gif")
            quadrantes[8].draw(win)
        if quadrantes[9] == 1:
            quadrantes [9] = Image(Point(187.5,212.5),"carro1.gif")
            quadrantes[9].draw(win)
        if quadrantes[10] == 1:
            quadrantes [10] = Image(Point(262.5,212.5),"carro1.gif")
            quadrantes[10].draw(win)
        if quadrantes[11] == 1:
            quadrantes [11] = Image(Point(337.5,212.5),"carro1.gif")
            quadrantes[11].draw(win)
        if quadrantes[12] == 1:
            quadrantes [12] = Image(Point(412.5,212.5),"carro1.gif")
            quadrantes[12].draw(win)
        if quadrantes[13] == 1:
            quadrantes [13] = Image(Point(487.5,212.5),"carro1.gif")
            quadrantes[13].draw(win)
        if quadrantes[14] == 1:
            quadrantes [14] = Image(Point(37.5,287.5),"carro1.gif")
            quadrantes[14].draw(win)
        if quadrantes[15] == 1:
            quadrantes [15] = Image(Point(112.5,287.5),"carro1.gif")
            quadrantes[15].draw(win)
        if quadrantes[16] == 1:
            quadrantes [16] = Image(Point(187.5,287.5),"carro1.gif")
            quadrantes[16].draw(win)
        if quadrantes[17] == 1:
            quadrantes [17] = Image(Point(262.5,287.5),"carro1.gif")
            quadrantes[17].draw(win)
        if quadrantes[18] == 1:
            quadrantes [18] = Image(Point(337.5,287.5),"carro1.gif")
            quadrantes[18].draw(win)
        if quadrantes[19] == 1:
            quadrantes [19] = Image(Point(412.5,287.5),"carro1.gif")
            quadrantes[19].draw(win)
        if quadrantes[20] == 1:
            quadrantes [20] = Image(Point(487.5,287.5),"carro1.gif")
            quadrantes[20].draw(win)
        if quadrantes[21] == 1:
            quadrantes [21] = Image(Point(37.5,362.5),"carro1.gif")
            quadrantes[21].draw(win)
        if quadrantes[22] == 1:
            quadrantes [22] = Image(Point(112.5,362.5),"carro1.gif")
            quadrantes[22].draw(win)
        if quadrantes[23] == 1:
            quadrantes [23] = Image(Point(187.5,362.5),"carro1.gif")
            quadrantes[23].draw(win)
        if quadrantes[24] == 1:
            quadrantes [24] = Image(Point(262.5,362.5),"carro1.gif")
            quadrantes[24].draw(win)
        if quadrantes[25] == 1:
            quadrantes [25] = Image(Point(337.5,362.5),"carro1.gif")
            quadrantes[25].draw(win)
        if quadrantes[26] == 1:
            quadrantes [26] = Image(Point(412.5,362.5),"carro1.gif")
            quadrantes[26].draw(win)
        if quadrantes[27] == 1:
            quadrantes [27] = Image(Point(487.5,362.5),"carro1.gif")
            quadrantes[27].draw(win)
        if quadrantes[28] == 1:
            quadrantes [28] = Image(Point(37.5,437.5),"carro1.gif")
            quadrantes[28].draw(win)
        if quadrantes[29] == 1:
            quadrantes [29] = Image(Point(112.5,437.5),"carro1.gif")
            quadrantes[29].draw(win)
        if quadrantes[30] == 1:
            quadrantes [30] = Image(Point(187.5,437.5),"carro1.gif")
            quadrantes[30].draw(win)
        if quadrantes[31] == 1:
            quadrantes [31] = Image(Point(262.5,437.5),"carro1.gif")
            quadrantes[31].draw(win)
        if quadrantes[32] == 1:
            quadrantes [32] = Image(Point(337.5,437.5),"carro1.gif")
            quadrantes[32].draw(win)
        if quadrantes[33] == 1:
            quadrantes [33] = Image(Point(412.5,437.5),"carro1.gif")
            quadrantes[33].draw(win)
        if quadrantes[34] == 1:
            quadrantes [34] = Image(Point(487.5,437.5),"carro1.gif")
            quadrantes[34].draw(win)

#para fechar    
 	win.getMouse()
	win.close()
    
    
main()
