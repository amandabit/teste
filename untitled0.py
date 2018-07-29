
from graphics import* 
import random
#from movimentacao import Movimentacao
win = GraphWin("Aprendendo graphics", 525,475)
color_background = win.setBackground('white')
quadrantes = []

#distribuindo bolinhas
def distribuicao(ponto):
    X = ponto.getX()
    Y = ponto.getY()

    if 0 <= X <= 75 and 100 <= Y <= 175: #quadrante 0
        if quadrantes[0] == 1:
            quadrantes[0] = Image(Point(37.5,137.5))
            quadrantes[0].draw(win)
        return
			
    if (75 <= X <= 150) and (100 <= Y <= 175) : #quadrante 1
        if quadrantes[1] == 1:
            quadrantes[1] = Image(Point(112.5,137.5))
            quadrantes[1].draw(win)
        return
            
    if (150 <= X <= 225) and (100 <= Y <= 175) : #quadrante 2
        if quadrantes[2] == 1:
            quadrantes[2] = Image(Point(187.5,137.5))
            quadrantes[2].draw(win)
        return     
    if (225 <= X <= 300) and (100 <= Y <= 175) : #quadrante 3
        if quadrantes[3] == 1:
            quadrantes[3] = Image(Point(262.5,137.5))
            quadrantes[3].draw(win)
        return
    if (300 <= X <= 375) and (100 <= Y <= 175) : #quadrante 4
        if quadrantes[4] == 1:
            quadrantes[4]= Image(Point(337.5,137.5))
            quadrantes[4].draw(win)
        return
    if (375 <= X <= 450) and (100 <= Y <= 175) : #quadrante 5
        if quadrantes[5] == 1:
            quadrantes[5] = Image(Point(412.5,137.5))
            quadrantes[5].draw(win)
        return
    if (450 <= X <= 525) and (100 <= Y <= 175) : #quadrante 6
        if quadrantes[6] == 1 :  
            quadrantes[6] = Image(Point(487.5,137.5))
            quadrantes[6].draw(win)
        return
        
    if (75 <= X <= 150) and (175 < Y <= 250) : #quadrante 7
        if quadrantes[7] == 1:
            quadrantes[7] = Image(Point(112.5,212.5))
            quadrantes[7].draw(win)
        return            
    if (150 <= X <= 225) and (175 < Y <= 250) : #quadrante 8
        if quadrantes[8] == 1:
            quadrantes [8] = Image(Point(187.5,212.5))
            quadrantes[8].draw(win)
        return
    if (225 <= X <= 300) and (175 < Y <= 250) : #quadrante 9
        if quadrantes[9] == 1:
            quadrantes [9] = Image(Point(262.5,212.5))
            quadrantes[9].draw(win)
        return
    if (300 <= X <= 375) and (175 < Y <= 250) : #quadrante 10
        if quadrantes[10] == 1:
            quadrantes [10] = Image(Point(337.5,212.5))
            quadrantes[10].draw(win)
        return    
    if (375 <= X <= 450) and (175 < Y <= 250) : #quadrante 11
        if quadrantes[11] == 1:
            quadrantes [11] = Image(Point(412.5,212.5))
            quadrantes[11].draw(win)
        return
    if (450 <= X <= 525) and (175 < Y <= 250) : #quadrante 12
        if quadrantes[12] == 1:
            quadrantes [12] = Image(Point(487.5,212.5))
            quadrantes[12].draw(win)
        return
    if (525 <= X <= 600) and (175 < Y <= 250) : #quadrante 13
        if quadrantes[13] == 1:
            quadrantes [13] = Image(Point(562.5,212.5))
            quadrantes[13].draw(win)
        return
    if (75 <= X <= 150) and (250 < Y <= 325) : #quadrante 14
        if quadrantes[14] == 1:
            quadrantes [14] = Image(Point(112.5,212.5))
            quadrantes[14].draw(win)
        return
    if (150 <= X <= 225) and (250 < Y <= 325) : #quadrante 15
        if quadrantes[15] == 1:
            quadrantes [15] = Image(Point(187.5,212.5))
            quadrantes[15].draw(win)
        return
    if (225 <= X <= 300) and (250 < Y <= 325) : #quadrante 16
        if quadrantes[16] == 1:
            quadrantes [16] = Image(Point(262.5,212.5))
            quadrantes[16].draw(win)
        return
    if (300 <= X <= 375) and (250 < Y <= 325) : #quadrante 17
        if quadrantes[17] == 1:
            quadrantes [17] = Image(Point(337.5,212.5))
            quadrantes[17].draw(win)
        return
    if (375 <= X <= 450) and (250 < Y <= 325) : #quadrante 18
        if quadrantes[18] == 1:
            quadrantes [18] = Image(Point(412.5,212.5))
            quadrantes[18].draw(win)
        return
    if (450 <= X <= 525) and (250 < Y <= 325) : #quadrante 19
        if quadrantes[19] == 1:
            quadrantes [19] = Image(Point(487.5,212.5))
            quadrantes[19].draw(win)
        return
    if (525 <= X <= 600) and (250 < Y <= 325) : #quadrante 20
        if quadrantes[20] == 1:
            quadrantes [20] = Image(Point(562.5,212.5))
            quadrantes[20].draw(win)
        return
    if (75 <= X <= 150) and (325 < Y <= 400) : #quadrante 21
        if quadrantes[21] == 1:
            quadrantes [21] = Image(Point(112.5,212.5))
            quadrantes[21].draw(win)
        return   
    if (150 <= X <= 225) and (325 < Y <= 400) : #quadrante 22
        if quadrantes[22] == 1:
            quadrantes [22] = Image(Point(187.5,212.5))
            quadrantes[22].draw(win)
        return   
    if (225 <= X <= 300) and (325 < Y <= 400) : #quadrante 23
        if quadrantes[23] == 1:
            quadrantes [23] = Image(Point(262.5,212.5))
            quadrantes[23].draw(win)
            
    if (300 <= X <= 375) and (325 < Y <= 400) : #quadrante 24
        if quadrantes[24] == 1:
            quadrantes [24] = Image(Point(337.5,212.5))
            quadrantes[24].draw(win)
        return   
    if (375 <= X <= 450) and (325 < Y <= 400) : #quadrante 25
        if quadrantes[25] == 1:
            quadrantes [25] = Image(Point(412.5,212.5))
            quadrantes[25].draw(win)
        return    
    if (450 <= X <= 525) and (325 < Y <= 400) : #quadrante 26
        if quadrantes[26] == 1:
            quadrantes [26] = Image(Point(487.5,212.5))
            quadrantes[26].draw(win)
        return    
    if (525 <= X <= 600) and (325 < Y <= 400) : #quadrante 27
        if quadrantes[27] == 1:
            quadrantes [27] = Image(Point(562.5,212.5))
            quadrantes[27].draw(win)
        return    
    if (75 <= X <= 150) and (400 < Y <= 475) : #quadrante 28
        if quadrantes[28] == 1:
            quadrantes [28] = Image(Point(112.5,212.5))
            quadrantes[28].draw(win)
        return    
    if (150 <= X <= 225) and (400 < Y <= 475) : #quadrante 29
        if quadrantes[29] == 1:
            quadrantes [29] = Image(Point(187.5,212.5))
            quadrantes[29].draw(win)
        return    
    if (225 <= X <= 300) and (400 < Y <= 475) : #quadrante 30
        if quadrantes[30] == 1:
            quadrantes [30] = Image(Point(262.5,212.5))
            quadrantes[30].draw(win)
        return    
    if (300 <= X <= 375) and (400 < Y <= 475) : #quadrante 31
        if quadrantes[31] == 1:
            quadrantes [31] = Image(Point(337.5,212.5))
            quadrantes[31].draw(win)
        return    
    if (375 <= X <= 450) and (400 < Y <= 475) : #quadrante 32
        if quadrantes[32] == 1:
            quadrantes [32] = Image(Point(412.5,212.5))
            quadrantes[32].draw(win)
        return    
    if (450 <= X <= 525) and (400 < Y <= 475) : #quadrante 33
        if quadrantes[33] == 1:
            quadrantes [33] = Image(Point(487.5,212.5))
            quadrantes[33].draw(win)
        return    
    if (525 <= X <= 600) and (400 < Y <= 475) : #quadrante 34
        if quadrantes[34] == 1:
            quadrantes [34] = Image(Point(562.5,212.5))
            quadrantes[34].draw(win)
        return
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
    
    for i in range(35):
        n = random.randint(1,5)
        quadrantes.append(n)
    print(quadrantes)
    
    while 1 in quadrantes == True:
        distribucao(win.getMouse())
    
#para fechar    
    time.sleep(2)
    
    
main()
