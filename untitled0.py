

from graphics import* 
import random

win = GraphWin("Aprendendo graphics", 525,700)
color_background = win.setBackground('white')
quadrantes = []
img = []

# movimentaçao

def movimentacao(ponto):
    X = ponto.getX()
    Y = ponto.getY()
    print(X,Y)
    z = 0
    if 0 <= X <= 75 and 100 <= Y <= 175: #quadrante 0
        keyMov = win.getKey()
        if keyMov == "s":
            
            z = quadrantes[0]
            quadrantes[0] = quadrantes [7]
            quadrantes[7] = z
           
            img[0].undraw()
            img[7].undraw()
            print(quadrantes[0])
            print(quadrantes[7])
        elif keyMov == "d":
            z = quadrantes[0]
            quadrantes[0] =  quadrantes[1]
            quadrantes[1] = z
            img[0].undraw()
            img[1].undraw()
        else: 
            print("movimento invalido")
        return
			
    if (75 <= X <= 150) and (100 <= Y <= 175) : #quadrante 1
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[1]
            quadrantes[1] = quadrantes [0]
            quadrantes[0] = z
            img[0].undraw()
            img[1].undraw()
        elif keyMov == "d":
            z = quadrantes[1]
            quadrantes[2] =  quadrantes[1]
            quadrantes[2] = z
            img[2].undraw()
            img[1].undraw()
        if keyMov == "s":
            z = quadrantes[1]
            quadrantes[1] = quadrantes[8]
            quadrantes[8] = z
            img[1].undraw()
            img[8].undraw()
        else:
            print("movimento invalido")
        print(quadrantes)
        return
            
    if (150 < X <= 225) and (100 <= Y <= 175) : #quadrante 2
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[2]
            quadrantes[2] = quadrantes [1]
            quadrantes[1] = z
            img[2].undraw()
            img[1].undraw()
        if keyMov == "d":
            z = quadrantes[2]
            quadrantes[2] =  quadrantes[3]
            quadrantes[3] = z
            img[2].undraw()
            img[3].undraw()
        if keyMov == "s":
            z = quadrantes[2]
            quadrantes[2] = quadrantes[9]
            quadrantes[9] = z
            img[2].undraw()
            img[9].undraw()
        else:
            print("movimento invalido")
        return
    if (225 < X <= 300) and (100 <= Y <= 175) : #quadrante 3
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[3]
            quadrantes[3] = quadrantes [2]
            quadrantes[2] = z
            img[2].undraw()
            img[3].undraw()
        if keyMov == "d":
            z = quadrantes[3]
            quadrantes[3] =  quadrantes[4]
            quadrantes[4] = z
            img[3].undraw()
            img[4].undraw()
        if keyMov == "s":
            z = quadrantes[3]
            quadrantes[3] = quadrantes[10]
            quadrantes[10] = z
            img[10].undraw()
            img[3].undraw()
        else:
            print("movimento invalido")
        return
    if (300 < X <= 375) and (100 <= Y <= 175) : #quadrante 4
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[4]
            quadrantes[4] = quadrantes [3]
            quadrantes[3] = z
            img[4].undraw()
            img[3].undraw()
        if keyMov == "d":
            z = quadrantes[4]
            quadrantes[4] = quadrantes [5]
            quadrantes[5] = z
            img[4].undraw()
            img[5].undraw()
        if keyMov == "s":
            z = quadrantes[4]
            quadrantes[4] = img[11]
            quadrantes[11] = z
            img[4].undraw()
            img[11].undraw()
        else:
            print("movimento invalido")
        return
    if (375 < X <= 450) and (100 <= Y <= 175) : #quadrante 5
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[5]
            quadrantes[5] = quadrantes [4]
            quadrantes[4] = z
            img[5].undraw()
            img[4].undraw()
        if keyMov == "d":
            z = quadrantes[5]
            quadrantes[5] = quadrantes [6]
            quadrantes[6] = z
            img[5].undraw()
            img[6].undraw()
        if keyMov =="s" :
            z = quadrantes[5]
            quadrantes[5] = quadrantes[12]
            quadrantes[12] = z
            img[5].undraw()
            img[12].undraw()
        else:
            print("movimento invalido")
        return
    if (450 <= X <= 525) and (100 <= Y <= 175) : #quadrante 6
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[6]
            quadrantes[6] = quadrantes [5]
            quadrantes[5] = z
            img[6].undraw()
            img[5].undraw()
        if keyMov == "s":
            z = quadrantes[6]
            quadrantes[6] = quadrantes[13]
            quadrantes[13] = z
            img[6].undraw()
            img[13].undraw()
        else:
            print("movimento invalido")
        return
    if (75 <= X <= 150) and (175 < Y <= 250) : #quadrante 7
        keyMov = win.getKey()
        if keyMov == "w":                
            z = quadrantes[7]
            quadrantes[7] = quadrantes [0]
            quadrantes[0] = z
            img[7].undraw()
            img[0].undraw()
        if keyMov =="s" :
            z = quadrantes[7]
            quadrantes[7] = quadrantes[14]
            quadrantes[14] = z
            img[14].undraw()
            img[7].undraw()
        if keyMov =="d":
            z = quadrantes[7]
            quadrantes[7] = img[8]
            quadrantes[8] = z
            img[8].undraw()
            img[7].undraw()
        else:
            print("movimento invalido")
        return
    if (75 < X <= 150) and (175 < Y <= 250) : #quadrante 8
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[8]
            quadrantes[8] = img[7]
            quadrantes[7] = z
            img[8].undraw()
            img[7].undraw()
        if keyMov == "d":
            z = quadrantes[8]
            quadrantes[8] = quadrantes [9]
            quadrantes[9] = z
            img[8].undraw()
            img[9].undraw()
        if keyMov == "s":
            z = quadrantes[8]
            quadrantes[8] = quadrantes[15]
            quadrantes[15] = z
            img[8].undraw()
            img[15].undraw()
        if keyMov == "w":
            z = quadrantes[8]
            quadrantes[8] = quadrantes [1]
            quadrantes[1] = z
            img[8].undraw()
            img[1].undraw()
        else:
            print("movimento invalido")
        return    
    if (150 < X <= 225) and (175 < Y <= 250) : #quadrante 9
        keyMov = win.getKey()
        if keyMov == "a" :
            z = quadrantes[9]
            quadrantes[9] = quadrantes [8]
            quadrantes[8] = z
            img[9].undraw()
            img[8].undraw()
        if keyMov == "d":
            z = quadrantes[9]
            quadrantes[9] = quadrantes [10]
            quadrantes[10] = z
            img[9].undraw()
            img[10].undraw()
        if keyMov == "s":
            z = quadrantes[9]
            quadrantes[9] = quadrantes[16]
            quadrantes[16] = z
            img[9].undraw()
            img[16].undraw()
        if keyMov == "w":
            z = quadrantes[9]
            quadrantes[9] = quadrantes [2]
            quadrantes[2] = z
            img[9].undraw()
            img[2].undraw()
        else:
            print("movimento invalido")
        return
    if (225 < X <= 300) and (175 < Y <= 250) : #quadrante 10
        keyMov = win.getKey()
        if keyMov == "a" :
            z = quadrantes[10]
            quadrantes[10] = quadrantes [9]
            quadrantes[9] = z
            img[10].undraw()
            img[9].undraw()
        if keyMov == "d":
            z = quadrantes[10]
            quadrantes[10] = quadrantes[11]
            quadrantes[11] = z
            img[10].undraw()
            img[11].undraw()
        if keyMov == "s":
            z = quadrantes[10]
            quadrantes[10] = quadrantes[17]
            quadrantes[17] = z
            img[10].undraw()
            img[17].undraw()
        if keyMov == "w":
            z = quadrantes[10]
            quadrantes[10] = quadrantes [3]
            quadrantes[3] = z
            img[10].undraw()
            img[3].undraw()
        else:
            print("movimento invalido")
        return
    if (300 < X <= 375) and (175 < Y <= 250) : #quadrante 11
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[11]
            quadrantes[11] = quadrantes [10]
            quadrantes[10] = z
            img[11].undraw()
            img[10].undraw()
        if keyMov == "d":
            z = quadrantes[11]
            quadrantes[11] = quadrantes[12]
            quadrantes[12] = z
            img[11].undraw()
            img[12].undraw()
        if keyMov == "s":
            z = quadrantes[11]
            quadrantes[11] = quadrantes[18]
            quadrantes[18] = z
            img[11].undraw()
            img[18].undraw()
        if keyMov == "w":
            z = quadrantes[11]
            quadrantes[11] = quadrantes [4]
            quadrantes[4] = z
            img[11].undraw()
            img[4].undraw()
        else:
            print("movimento invalido")
        return
    if (375 <= X <= 450) and (175 < Y <= 250) : #quadrante 12
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[12]
            quadrantes[12] = quadrantes[11]
            quadrantes[11] = z
            img[12].undraw()
            img[11].undraw()
        if keyMov == "d":
            z = quadrantes[12]
            quadrantes[12] = img[13]
            quadrantes[13] = z
            img[12].undraw()
            img[13].undraw()
        if keyMov == "s":
            z = quadrantes[12]
            quadrantes[12] = quadrantes[19]
            quadrantes[19] = z
            img[12].undraw()
            img[19].undraw()
        if keyMov == "w":
            z = quadrantes[12]
            quadrantes[12] = quadrantes [5]
            quadrantes[5] = z
            img[12].undraw()
            img[5].undraw()
        else:
            print("movimento invalido")
        return
    if (450 <= X <= 525) and (175 < Y <= 250) : #quadrante 13
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[13]
            quadrantes[13] = quadrantes[12]
            quadrantes[12] = z
            img[13].undraw()
            img[12].undraw()
        
        if keyMov == "s":
            z = quadrantes[13]
            quadrantes[13] = quadrantes[20]
            quadrantes[20] = z
            img[13].undraw()
            img[20].undraw()
        if keyMov == "w":
            z = quadrantes[13]
            quadrantes[13] = quadrantes [6]
            quadrantes[6] = z
            img[13].undraw()
            img[6].undraw()
        else:
            print("movimento invalido")
        return
    if (0 <= X <= 75) and (250 < Y <= 325) : #quadrante 14
        keyMov = win.getKey()
        if keyMov == "d":
            z = img[14]
            quadrantes[14] = quadrantes [15]
            quadrantes[15] = z
            img[14].undraw()
            img[15].undraw()
        if keyMov == "s":
            z = quadrantes[14]
            quadrantes[14] = quadrantes[21]
            quadrantes[21] = z
            img[14].undraw()
            img[21].undraw()
        if keyMov == "w":
            z = quadrantes[14]
            quadrantes[14] = quadrantes [7]
            quadrantes[7] = z
            img[14].undraw()
            img[7].undraw()
        else:
            print("movimento invalido")
        return
    if (75 < X <= 150) and (250 < Y <= 325) : #quadrante 15
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[15]
            quadrantes[15] = quadrantes[14]
            quadrantes[14] = z
            img[15].undraw()
            img[14].undraw()
        if keyMov == "d":
            z = quadrantes[15]
            quadrantes[15] = quadrantes[16]
            quadrantes[16] = z
            img[15].undraw()
            img[16].undraw()
        if keyMov == "s":
            z = quadrantes[15]
            quadrantes[15] = quadrantes[22]
            quadrantes[22] = z
            img[15].undraw()
            img[22].undraw()
        if keyMov == "w":
            z = quadrantes[15]
            quadrantes[15] = quadrantes [8]
            quadrantes[8] = z
            img[15].undraw()
            img[8].undraw()
        else:
            print("movimento invalido")
        return
    if (150 < X <= 225) and (250 < Y <= 325) : #quadrante 16
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[16]
            quadrantes[16] = quadrantes [15]
            quadrantes[15] = z
            img[16].undraw()
            img[15].undraw()
        if keyMov == "d":
            z = quadrantes[16]
            quadrantes[16] = quadrantes[17]
            quadrantes[17] = z
            img[16].undraw()
            img[17].undraw()
        if keyMov == "s":
            z = quadrantes[16]
            quadrantes[16] = quadrantes[23]
            quadrantes[23] = z
            img[16].undraw()
            img[23].undraw()
        if keyMov == "w":
            z = quadrantes[16]
            quadrantes[16] = quadrantes [9]
            quadrantes[9] = z
            img[16].undraw()
            img[9].undraw()
        else:
            print("movimento invalido")
        return
    if (225 <= X <= 300) and (250 < Y <= 325) : #quadrante 17 
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[17]
            quadrantes[17] = quadrantes[16]
            quadrantes[16] = z
            img[17].undraw()
            img[16].undraw()
        if keyMov == "d":
            z = quadrantes[17]
            quadrantes[17] = quadrantes[18]
            quadrantes[18] = z
            img[17].undraw()
            img[18].undraw()
        if keyMov == "s":
            z = quadrantes[17]
            quadrantes[17] = quadrantes[24]
            quadrantes[24] = z
            img[17].undraw()
            img[24].undraw()
        if keyMov == "w":
            z = quadrantes[17]
            quadrantes[17] = quadrantes [10]
            quadrantes[10] = z
            img[17].undraw()
            img[10].undraw()
        else:
            print("movimento invalido")
        return
    if (300 < X <= 375) and (250 < Y <= 325) : #quadrante 18
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[18]
            quadrantes[18] = quadrantes[17]
            quadrantes[17] = z
            img[18].undraw()
            img[17].undraw()
        if keyMov == "d":
            z = quadrantes[18]
            quadrantes[18] = quadrantes[19]
            quadrantes[19] = z
            img[18].undraw()
            img[19].undraw()
        if keyMov == "s":
            z = quadrantes[18]
            quadrantes[18] = quadrantes[25]
            quadrantes[25] = z
            img[18].undraw()
            img[25].undraw()
        if keyMov == "w":
            z = quadrantes[18]
            quadrantes[18] = quadrantes[11]
            quadrantes[11] = z
            img[18].undraw()
            img[11].undraw()
        else:
            print("movimento invalido")
        return
    if (375 <= X <= 450) and (250 < Y <= 325) : #quadrante 19
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[19]
            quadrantes[19] = quadrantes[18]
            quadrantes[18] = z
            img[19].undraw()
            img[18].undraw()
        if keyMov == "d":
            z = quadrantes[19]
            quadrantes[19] = quadrantes[20]
            quadrantes[20] = z
            img[19].undraw()
            img[20].undraw()
        if keyMov == "s":
            z = quadrantes[19]
            quadrantes[19] = quadrantes[26]
            quadrantes[26] = z
            img[19].undraw()
            img[26].undraw()
        if keyMov == "w":
            z = quadrantes[19]
            quadrantes[19] = quadrantes[12]
            quadrantes[12] = z
            img[19].undraw()
            img[12].undraw()
        else:
            print("movimento invalido")
        return
    if (450 < X <= 525) and (250 < Y <= 325) : #quadrante 20
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[20]
            quadrantes[20] = quadrantes[19]
            quadrantes[19] = z
            img[20].undraw()
            img[19].undraw()
    
        if keyMov == "s":
            z = quadrantes[20]
            quadrantes[20] = quadrantes[27]
            quadrantes[27] = z
            img[20].undraw()
            img[27].undraw()
        if keyMov == "w":
            z = quadrantes[20]
            quadrantes[20] = quadrantes[13]
            quadrantes[13] = z
            img[20].undraw()
            img[13].undraw()
        else:
            print("movimento invalido")
        return
    if (0 <= X <= 75) and (325 < Y <= 400) : #quadrante 21
        keyMov = win.getKey()
        if keyMov == "d":
            z = quadrantes[21]
            quadrantes[21] = quadrantes[22]
            quadrantes[22] = z
            img[21].undraw()
            img[22].undraw()
        if keyMov == "s":
            z = quadrantes[21]
            quadrantes[21] = quadrantes[28]
            quadrantes[28] = z
            img[21].undraw()
            img[28].undraw()
        if keyMov == "w":
            z = quadrantes[21]
            quadrantes[21] = quadrantes[14]
            quadrantes[14] = z
            img[21].undraw()
            img[14].undraw()
        else:
            print("movimento invalido")
        return
    if (75< X <= 150) and (325 < Y <= 400) : #quadrante 22
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[22]
            quadrantes[22] = quadrantes[21]
            quadrantes[21] = z
            img[22].undraw()
            img[21].undraw()
        if keyMov == "d":
            z = quadrantes[22]
            quadrantes[22] = quadrantes[23]
            quadrantes[23] = z
            img[22].undraw()
            img[23].undraw()
        if keyMov == "s":
            z = quadrantes[22]
            quadrantes[22] = quadrantes[29]
            quadrantes[29] = z
            img[22].undraw()
            img[29].undraw()
        if keyMov == "w":
            z = quadrantes[22]
            quadrantes[22] = quadrantes [15]
            quadrantes[15] = z
            img[22].undraw()
            img[15].undraw()
        else:
            print("movimento invalido")
        return
    if (150 < X <= 225) and (325 < Y <= 400) : #quadrante 23
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[23]
            quadrantes[23] = quadrantes[22]
            quadrantes[22] = z
            img[23].undraw()
            img[22].undraw()
        if keyMov == "d":
            z = quadrantes[23]
            quadrantes[23] = quadrantes[24]
            quadrantes[24] = z
            img[23].undraw()
            img[24].undraw()
        if keyMov == "s":
            z = quadrantes[23]
            quadrantes[23] = quadrantes[30]
            quadrantes[30] = z
            img[23].undraw()
            img[30].undraw()
        if keyMov == "w":
            z = quadrantes[23]
            quadrantes[23] = quadrantes[16]
            quadrantes[16] = z
            img[23].undraw()
            img[16].undraw()
        else:
            print("movimento invalido")
        return
    if (225 < X <= 300) and (325 < Y <= 400) : #quadrante 24
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[24]
            quadrantes[24] = quadrantes[23]
            quadrantes[23] = z
            img[24].undraw()
            img[23].undraw()
        if keyMov == "d":
            z = quadrantes[24]
            quadrantes[24] = quadrantes[25]
            quadrantes[25] = z
            img[24].undraw()
            img[25].undraw()
        if keyMov == "s":
            z = quadrantes[24]
            quadrantes[24] = quadrantes[31]
            quadrantes[31] = z
            img[24].undraw()
            img[31].undraw()
        if keyMov == "w":
            z = quadrantes[24]
            quadrantes[24] = quadrantes[17]
            quadrantes[17] = z
            img[24].undraw()
            img[17].undraw()
        else:
            print("movimento invalido")
        return
    if (300 < X <= 375) and (325 < Y <= 400) : #quadrante 25
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[25]
            quadrantes[25] = quadrantes[24]
            quadrantes[24] = z
            img[25].undraw()
            img[24].undraw()
        if keyMov == "d":
            z = quadrantes[25]
            quadrantes[25] = quadrantes[26]
            quadrantes[26] = z
            img[25].undraw()
            img[26].undraw()
        if keyMov == "s":
            z = quadrantes[25]
            quadrantes[25] = quadrantes[32]
            quadrantes[32] = z
            img[25].undraw()
            img[32].undraw()
        if keyMov == "w":
            z = quadrantes[25]
            quadrantes[25] = quadrantes[18]
            quadrantes[18] = z
            img[25].undraw()
            img[18].undraw()
        else:
            print("movimento invalido")
        return
    if (375<= X <=450) and (325 < Y <= 400) : #quadrante 26
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[26]
            quadrantes[26] = quadrantes[25]
            quadrantes[25] = z
            img[26].undraw()
            img[25].undraw()
        if keyMov == "d":
            z = quadrantes[26]
            quadrantes[26] = quadrantes[27]
            quadrantes[27] = z
            img[26].undraw()
            img[27].undraw()
        if keyMov == "s":
            z = quadrantes[26]
            quadrantes[26] = quadrantes[33]
            quadrantes[33] = z
            img[26].undraw()
            img[33].undraw()
        if keyMov == "w":
            z = quadrantes[26]
            quadrantes[26] = quadrantes[19]
            quadrantes[19] = z
            img[26].undraw()
            img[19].undraw()
        else:
            print("movimento invalido")
        return
    if (450<= X <= 525) and (325 < Y <= 400) : #quadrante 27
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[27]
            quadrantes[27] = quadrantes[26]
            quadrantes[26] = z
            img[27].undraw()
            img[26].undraw()
        
        if keyMov == "s":
            z = quadrantes[27]
            quadrantes[27] = quadrantes[34]
            quadrantes[34] = z
            img[27].undraw()
            img[34].undraw()
        if keyMov == "w":
            z = quadrantes[27]
            quadrantes[27] = quadrantes[20]
            quadrantes[20] = z
            img[27].undraw()
            img[20].undraw()
        else:
            print("movimento invalido")
        return
    if (0 <= X <= 75) and (400 < Y <= 475) : #quadrante 28
        keyMov = win.getKey()
            
            
        if keyMov == "d":
            z = quadrantes[28]
            quadrantes[28] = quadrantes[29]
            quadrantes[29] = z
            img[28].undraw()
            img[29].undraw()
        
        if keyMov == "w":
            z = quadrantes[28]
            quadrantes[28] = quadrantes[21]
            quadrantes[21] = z
            img[28].undraw()
            img[21].undraw()
        else:
            print("movimento invalido")
        return
    if (75 <= X <= 150) and (400 < Y <= 475) : #quadrante 29
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[29]
            quadrantes[29] = quadrantes[28]
            quadrantes[28] = z
            img[29].undraw()
            img[28].undraw()
        if keyMov == "d":
            z = quadrantes[29]
            quadrantes[29] = quadrantes[30]
            quadrantes[30] = z
            img[29].undraw()
            img[30].undraw()
        if keyMov == "s":
            z = quadrantes[29]
            quadrantes[29] = quadrantes [36]
            quadrantes[36] = z
            img[29].undraw()
            quadrantes[36].draw(win)
        if keyMov == "w":
            z = quadrantes[29]
            quadrantes[29] = quadrantes[22]
            quadrantes[22] = z
            img[29].undraw()
            img[22].undraw()
        else:
            print("movimento invalido")
        return
    if (150 <= X <= 225) and (400 < Y <= 475) : #quadrante 30
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[30]
            quadrantes[30] = quadrantes[29]
            quadrantes[29] = z
            img[30].undraw()
            img[29].undraw()
        if keyMov == "d":
            z = quadrantes[30]
            quadrantes[30] = quadrantes[31]
            quadrantes[31] = z
            img[30].undraw()
            img[31].undraw()
         
        if keyMov == "w":
            z = quadrantes[30]
            quadrantes[30] = quadrantes[23]
            quadrantes[23] = z
            img[30].undraw()
            img[23].undraw()
        else:
            print("movimento invalido")
        return
    if (225 < X <= 300) and (400 < Y <= 475) : #quadrante 31
        keyMov = win.getKey()            
        if keyMov == "a":
            z = quadrantes[31]
            quadrantes[31] = quadrantes[30]
            quadrantes[30] = z
            img[31].undraw()
            img[30].undraw()
        if keyMov == "d":
            z = quadrantes[31]
            quadrantes[31] = quadrantes[32]
            quadrantes[32] = z
            img[31].undraw()
            img[32].undraw()
        
        if keyMov == "w":
            z = quadrantes[31]
            quadrantes[31] = quadrantes[24]
            quadrantes[24] = z
            img[31].undraw()
            img[24].undraw()
        else:
            print("movimento invalido")
        return
    if (300 <= X <= 375) and (400 < Y <= 475) : #quadrante 32
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[32]
            quadrantes[32] = quadrantes[31]
            quadrantes[31] = z
            img[32].undraw()
            img[31].undraw()
        if keyMov == "d":
            z = quadrantes[32]
            quadrantes[32] = quadrantes[33]
            quadrantes[33] = z
            img[32].undraw()
            img[33].undraw()
        
        
        if keyMov == "w":
            z = quadrantes[32]
            quadrantes[32] = quadrantes[25]
            quadrantes[25] = z
            img[32].undraw()
            img[25].undraw()
        else:
            print("movimento invalido")
        return
    if (375< X <= 450) and (400 < Y <= 475) : #quadrante 33
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[33]
            quadrantes[33] = quadrantes[32]
            quadrantes[32] = z
            img[33].undraw()
            img[32].undraw()
        if keyMov == "d":
            z = quadrantes[33]
            quadrantes[33] = quadrantes[34]
            quadrantes[34] = z
            img[33].undraw()
            img[34].undraw()
           
        if keyMov == "w":
            z = quadrantes[33]
            quadrantes[33] = quadrantes[26]
            quadrantes[26] = z
            img[33].undraw()
            img[26].undraw()
        else:
            print("movimento invalido")
        return
    if (450 < X <= 525) and (400 < Y <= 475) : #quadrante 34
        keyMov = win.getKey()
        if keyMov == "a":
            z = quadrantes[34]
            quadrantes[34] = quadrantes[33]
            quadrantes[33] = z
            img[34].undraw()
            img[33].undraw()
     
        if keyMov == "w":
            z = quadrantes[34]
            quadrantes[34] = quadrantes[27]
            quadrantes[27] = z
            img[34].undraw()
            img[27].undraw()
        else:
            print("movimento invalido")
        return
def main(): 
    global win
    global quadrantes
    global img

# fazendo quadrantes

linha = Line(Point(0, 325), Point(0, 700))  # primeira coluna
linha.draw(win)

linha = Line(Point(75, 240), Point(75, 700))  # primeira coluna heroi
linha.draw(win)

linha = Line(Point(150, 240), Point(150, 700))  # segunda coluna
linha.draw(win)

linha = Line(Point(225, 240), Point(225, 700))  # terceira coluna
linha.draw(win)

linha = Line(Point(300, 240), Point(300, 700))  # quarta coluna
linha.draw(win)

linha = Line(Point(375, 240), Point(375, 700))  # quinta coluna
linha.draw(win)

linha = Line(Point(450, 240), Point(450, 700))  # ultima coluna heroi
linha.draw(win)

linha = Line(Point(525, 325), Point(525, 700))  # setima coluna
linha.draw(win)


linha = Line(Point(75, 240), Point(450, 240))  # primeira linha heroi
linha.draw(win)

linha = Line(Point(75, 315), Point(450, 315))  # segunda linha heroi mana
linha.draw(win)

linha = Line(Point(0, 325), Point(525, 325))  # primeira linha
linha.draw(win)

linha = Line(Point(0, 400), Point(525, 400))  # segunda linha
linha.draw(win)

linha = Line(Point(0, 475), Point(525, 475))  # terceira linha
linha.draw(win)

linha = Line(Point(0, 550), Point(525, 550))  # quarta linha
linha.draw(win)

linha = Line(Point(0, 625), Point(525, 625))  # quinta linha
linha.draw(win)

linha = Line(Point(0, 700), Point(525, 700))  # sexta linha
linha.draw(win)

#fazendo o sorteio da distribuicao das bolinhas
    for i in range(35):
        n = random.randint(1,5)
        quadrantes.append(n)
        img.append(n)
        
    print(quadrantes)

#fazendo a primeira distribuicao de bolinhas
    for y in range (35):
        if quadrantes[0] == 1:
            img[0] = Image(Point(37.5,362.5),"carro1.gif")
            img[0].draw(win)
        if quadrantes[0] == 2:
            img[0] = Image(Point(37.5,362.5), "bege.gif")
            img[0].draw(win)
        if quadrantes[0] == 3:
            img[0] = Image(Point(37.5,362.5), "cinza.gif")
            img[0].draw(win)
        if quadrantes[0] == 4:
            img[0] = Image(Point(37.5,362.5), "carro2.gif")
            img[0].draw(win)
        if quadrantes[0] == 5:
            img[0] = Image(Point(37.5,362.5), "marrom.gif")
            img[0].draw(win)

        if quadrantes[1] == 1:
            img[1] = Image(Point(112.5,362.5),"carro1.gif")
            img[1].draw(win)
        if quadrantes[1] == 2:
            img[1] = Image(Point(112.5,362.5), "bege.gif")
            img[1].draw(win)
        if quadrantes[1] == 3:
            img[1] = Image(Point(112.5,362.5), "cinza.gif")
            img[1].draw(win)
        if quadrantes[1] == 4:
            img[1] = Image(Point(112.5,362.5), "carro2.gif")
            img[1].draw(win)
        if quadrantes[1] == 5:
            img[1] = Image(Point(112.5,362.5), "marrom.gif")
            img[1].draw(win)

        if quadrantes[2] == 1:
            img[2] = Image(Point(187.5,362.5),"carro1.gif")
            img[2].draw(win)
        if quadrantes[2] == 2:
            img[2] = Image(Point(187.5,362.5), "bege.gif")
            img[2].draw(win)
        if quadrantes[2] == 3:
            img[2] = Image(Point(187.5,362.5), "cinza.gif")
            img[2].draw(win)
        if quadrantes[2] == 4:
            img[2] = Image(Point(187.5,362.5), "carro2.gif")
            img[2].draw(win)
        if quadrantes[2] == 5:
            img[2] = Image(Point(187.5,362.5), "marrom.gif")
            img[2].draw(win)

        if quadrantes[3] == 1:
            img[3] = Image(Point(262.5,362.5),"carro1.gif")
            img[3].draw(win)
        if quadrantes[3] == 2:
            img[3] = Image(Point(262.5,362.5), "bege.gif")
            img[3].draw(win)
        if quadrantes[3] == 3:
            img[3] = Image(Point(262.5,362.5), "cinza.gif")
            img[3].draw(win)
        if quadrantes[3] == 4:
            img[3] = Image(Point(262.5,362.5), "carro2.gif")
            img[3].draw(win)
        if quadrantes[3] == 5:
            img[3] = Image(Point(262.5,362.5), "marrom.gif")
            img[3].draw(win)

        if quadrantes[4] == 1:
            img[4] = Image(Point(337.5,362.5),"carro1.gif")
            img[4].draw(win)
        if quadrantes[4] == 2:
            img[4] = Image(Point(337.5,362.5), "bege.gif")
            img[4].draw(win)
        if quadrantes[4] == 3:
            img[4] = Image(Point(337.5,362.5), "cinza.gif")
            img[4].draw(win)
        if quadrantes[4] == 4:
            img[4] = Image(Point(337.5,362.5), "carro2.gif")
            img[4].draw(win)
        if quadrantes[4] == 5:
            img[4] = Image(Point(337.5,362.5), "marrom.gif")
            img[4].draw(win)

        if quadrantes[5] == 1:
            img[5] = Image(Point(412.5,362.5),"carro1.gif")
            img[5].draw(win)
        if quadrantes[5] == 2:
            img[5] = Image(Point(412.5,362.5), "bege.gif")
            img[5].draw(win)
        if quadrantes[5] == 3:
            img[5] = Image(Point(412.5,362.5), "cinza.gif")
            img[5].draw(win)
        if quadrantes[5] == 4:
            img[5] = Image(Point(412.5,362.5), "carro2.gif")
            img[5].draw(win)
        if quadrantes[5] == 5:
            img[5] = Image(Point(412.5,362.5), "marrom.gif")
            img[5].draw(win)

        if quadrantes[6] == 1:
            img[6] = Image(Point(487.5,362.5),"carro1.gif")
            img[6].draw(win)
        if quadrantes[6] == 2:
            img[6] = Image(Point(487.5,362.5), "bege.gif")
            img[6].draw(win)
        if quadrantes[6] == 3:
            img[6] = Image(Point(487.5,362.5), "cinza.gif")
            img[6].draw(win)
        if quadrantes[6] == 4:
            img[6] = Image(Point(487.5,362.5), "carro2.gif")
            img[6].draw(win)
        if quadrantes[6] == 5:
            img[6] = Image(Point(487.5,362.5), "marrom.gif")
            img[6].draw(win)

        if quadrantes[7] == 1:
            img[7] = Image(Point(37.5,437.5), "carro1.gif")
            img[7].draw(win)
        if quadrantes[7] == 2:
            img[7] = Image(Point(37.5,437.5), "bege.gif")
            img[7].draw(win)
        if quadrantes[7] == 3:
            img[7] = Image(Point(37.5,437.5), "cinza.gif")
            img[7].draw(win)
        if quadrantes[7] == 4:
            img[7] = Image(Point(37.5,437.5), "carro2.gif")
            img[7].draw(win)
        if quadrantes[7] == 5:
            img[7] = Image(Point(37.5,437.5), "marrom.gif")
            img[7].draw(win)
            
        if quadrantes[8] == 1:
            img[8] = Image(Point(112.5,437.5),"carro1.gif")
            img[8].draw(win)
        if quadrantes[8] == 2:
            img[8] = Image(Point(112.5,437.5), "bege.gif")
            img[8].draw(win)
        if quadrantes[8] == 3:
            img[8] = Image(Point(112.5,437.5), "cinza.gif")
            img[8].draw(win)
        if quadrantes[8] == 4:
            img[8] = Image(Point(112.5,437.5), "carro2.gif")
            img[8].draw(win)
        if quadrantes[8] == 5:
            img[8] = Image(Point(112.5,437.5), "marrom.gif")
            img[8].draw(win)
            
        if quadrantes[9] == 1:
            img[9] = Image(Point(187.5,437.5),"carro1.gif")
            img[9].draw(win)
        if quadrantes[9] == 2:
            img[9] = Image(Point(187.5,437.5), "bege.gif")
            img[9].draw(win)
        if quadrantes[9] == 3:
            img[9] = Image(Point(187.5,437.5), "cinza.gif")
            img[9].draw(win)
        if quadrantes[9] == 4:
            img[9] = Image(Point(187.5,437.5), "carro2.gif")
            img[9].draw(win)
        if quadrantes[9] == 5:
            img[9] = Image(Point(187.5,437.5), "marrom.gif")
            img[9].draw(win)
            
        if quadrantes[10] == 1:
            img[10] = Image(Point(262.5,437.5), "carro1.gif")
            img[10].draw(win)
        if quadrantes[10] == 2:
            img[10] = Image(Point(262.5,437.5), "bege.gif")
            img[10].draw(win)
        if quadrantes[10] == 3:
            img[10] = Image(Point(262.5,437.5), "cinza.gif")
            img[10].draw(win)
        if quadrantes[10] == 4:
            img[10] = Image(Point(262.5,437.5), "carro2.gif")
            img[10].draw(win)
        if quadrantes[10] == 5:
            img[10] = Image(Point(262.5,437.5), "marrom.gif")
            img[10].draw(win)
            
        if quadrantes[11] == 1:
            img[11] = Image(Point(337.5,437.5), "carro1.gif")
            img[11].draw(win)
        if quadrantes[11] == 2:
            img[11] = Image(Point(337.5,437.5), "bege.gif")
            img[11].draw(win)
        if quadrantes[11] == 3:
            img[11] = Image(Point(337.5,437.5), "cinza.gif")
            img[11].draw(win)
        if quadrantes[11] == 4:
            img[11] = Image(Point(337.5,437.5), "carro2.gif")
            img[11].draw(win)
        if quadrantes[11] == 5:
            img[11] = Image(Point(337.5,437.5), "marrom.gif")
            img[11].draw(win)
            
        if quadrantes[12] == 1:
            img[12] = Image(Point(412.5,437.5), "carro1.gif")
            img[12].draw(win)
        if quadrantes[12] == 2:
            img[12] = Image(Point(412.5,437.5), "bege.gif")
            img[12].draw(win)
        if quadrantes[12] == 3:
            img[12] = Image(Point(412.5,437.5), "cinza.gif")
            img[12].draw(win)
        if quadrantes[12] == 4:
            img[12] = Image(Point(412.5,437.5), "carro2.gif")
            img[12].draw(win)
        if quadrantes[12] == 5:
            img[12] = Image(Point(412.5,437.5), "marrom.gif")
            img[12].draw(win)
            
        if quadrantes[13] == 1:
            img[13] = Image(Point(487.5,437.5), "carro1.gif")
            img[13].draw(win)
        if quadrantes[13] == 2:
            img[13] = Image(Point(487.5,437.5), "bege.gif")
            img[13].draw(win)
        if quadrantes[13] == 3:
            img[13] = Image(Point(487.5,437.5), "cinza.gif")
            img[13].draw(win)
        if quadrantes[13] == 4:
            img[13] = Image(Point(487.5,437.5), "carro2.gif")
            img[13].draw(win)
        if quadrantes[13] == 5:
            img[13] = Image(Point(487.5,437.5), "marrom.gif")
            img[13].draw(win)

        if quadrantes[14] == 1:
            img[14] = Image(Point(37.5,512.5), "carro1.gif")
            img[14].draw(win)
        if quadrantes[14] == 2:
            img[14] = Image(Point(37.5,512.5), "bege.gif")
            img[14].draw(win)
        if quadrantes[14] == 3:
            img[14] = Image(Point(37.5,512.5), "cinza.gif")
            img[14].draw(win)
        if quadrantes[14] == 4:
            img[14] = Image(Point(37.5,512.5), "carro2.gif")
            img[14].draw(win)
        if quadrantes[14] == 5:
            img[14] = Image(Point(37.5,512.5), "marrom.gif")
            img[14].draw(win)
        if quadrantes[15] == 1:
            img[15] = Image(Point(112.5,512.5), "carro1.gif")
            img[15].draw(win)
        if quadrantes[15] == 2:
            img[15] = Image(Point(112.5,512.5), "bege.gif")
            img[15].draw(win)
        if quadrantes[15] == 3:
            img[15] = Image(Point(112.5,512.5), "cinza.gif")
            img[15].draw(win)
        if quadrantes[15] == 4:
            img[15] = Image(Point(112.5,512.5), "carro2.gif")
            img[15].draw(win)
        if quadrantes[15] == 5:
            img[15] = Image(Point(112.5,512.5), "marrom.gif")
            img[15].draw(win)
        if quadrantes[16] == 1:
            img[16] = Image(Point(187.5,512.5),"carro1.gif")
            img[16].draw(win)
        if quadrantes[16] == 2:
            img[16] = Image(Point(187.5,512.5), "bege.gif")
            img[16].draw(win)
        if quadrantes[16] == 3:
            img[16] = Image(Point(187.5,512.5), "cinza.gif")
            img[16].draw(win)
        if quadrantes[16] == 4:
            img[16] = Image(Point(187.5,512.5), "carro2.gif")
            img[16].draw(win)
        if quadrantes[16] == 5:
            img[16] = Image(Point(187.5,512.5), "marrom.gif")
            img[16].draw(win)
        if quadrantes[17] == 1:
            img[17] = Image(Point(262.5,512.5), "carro1.gif")
            img[17].draw(win)
        if quadrantes[17] == 2:
            img[17] = Image(Point(262.5,512.5), "bege.gif")
            img[17].draw(win)
        if quadrantes[17] == 3:
            img[17] = Image(Point(262.5,512.5), "cinza.gif")
            img[17].draw(win)
        if quadrantes[17] == 4:
            img[17] = Image(Point(262.5,512.5), "carro2.gif")
            img[17].draw(win)
        if quadrantes[17] == 5:
            img[17] = Image(Point(262.5,512.5), "marrom.gif")
            img[17].draw(win)
        if quadrantes[18] == 1:
            img[18] = Image(Point(337.5,512.5), "carro1.gif")
            img[18].draw(win)
        if quadrantes[18] == 2:
            img[18] = Image(Point(337.5,512.5), "bege.gif")
            img[18].draw(win)
        if quadrantes[18] == 3:
            img[18] = Image(Point(337.5,512.5), "cinza.gif")
            img[18].draw(win)
        if quadrantes[18] == 4:
            img[18] = Image(Point(337.5,512.5), "carro2.gif")
            img[18].draw(win)
        if quadrantes[18] == 5:
            img[18] = Image(Point(337.5,512.5), "marrom.gif")
            img[18].draw(win)
        elif quadrantes[19] == 1:
            img[19] = Image(Point(412.5,512.5), "carro1.gif")
            img[19].draw(win)
        if quadrantes[19] == 2:
            img[19] = Image(Point(412.5,512.5), "bege.gif")
            img[19].draw(win)
        if quadrantes[19] == 3:
            img[19] = Image(Point(412.5,512.5), "cinza.gif")
            img[19].draw(win)
        if quadrantes[19] == 4:
            img[19] = Image(Point(412.5,512.5), "carro2.gif")
            img[19].draw(win)
        if quadrantes[19] == 5:
            img[19] = Image(Point(412.5,512.5), "marrom.gif")
            img[19].draw(win)
            
        if quadrantes[20] == 1:
            img[20] = Image(Point(487.5,512.5), "carro1.gif")
            img[20].draw(win)
        if quadrantes[20] == 2:
            img[20] = Image(Point(487.5,512.5), "bege.gif")
            img[20].draw(win)
        if quadrantes[20] == 3:
            img[20] = Image(Point(487.5,512.5), "cinza.gif")
            img[20].draw(win)
        if quadrantes[20] == 4:
            img[20] = Image(Point(487.5,512.5), "carro2.gif")
            img[20].draw(win)
        if quadrantes[20] == 5:
            img[20] = Image(Point(487.5,512.5), "marrom.gif")
            img[20].draw(win)

        if quadrantes[21] == 1:
            img[21] = Image(Point(37.5,587.5), "carro1.gif")
            img[21].draw(win)
        if quadrantes[21] == 2:
            img[21] = Image(Point(37.5,587.5), "bege.gif")
            img[21].draw(win)
        if quadrantes[21] == 3:
            img[21] = Image(Point(37.5,587.5), "cinza.gif")
            img[21].draw(win)
        if quadrantes[21] == 4:
            img[21] = Image(Point(37.5,587.5), "carro2.gif")
            img[21].draw(win)
        if quadrantes[21] == 5:
            img[21] = Image(Point(37.5,587.5), "marrom.gif")
            img[21].draw(win)
        if quadrantes[22] == 1:
            img[22] = Image(Point(112.5,587.5), "carro1.gif")
            img[22].draw(win)
        if quadrantes[22] == 2:
            img[22] = Image(Point(112.5,587.5), "bege.gif")
            img[22].draw(win)
        if quadrantes[22] == 3:
            img[22] = Image(Point(112.5,587.5), "cinza.gif")
            img[22].draw(win)
        if quadrantes[22] == 4:
            img[22] = Image(Point(112.5,587.5), "carro2.gif")
            img[22].draw(win)
        if quadrantes[22] == 5:
            img[22] = Image(Point(112.5,587.5), "marrom.gif")
            img[22].draw(win)
        if quadrantes[23] == 1:
            img[23] = Image(Point(187.5,587.5), "carro1.gif")
            img[23].draw(win)
        if quadrantes[23] == 2:
            img[23] = Image(Point(187.5,587.5), "bege.gif")
            img[23].draw(win)
        if quadrantes[23] == 3:
            img[23] = Image(Point(187.5,587.5), "cinza.gif")
            img[23].draw(win)
        if quadrantes[23] == 4:
            img[23] = Image(Point(187.5,587.5), "carro2.gif")
            img[23].draw(win)
        if quadrantes[23] == 5:
            img[23] = Image(Point(187.5,587.5), "marrom.gif")
            img[23].draw(win)
        if quadrantes[24] == 1:
            img[24] = Image(Point(262.5,587.5), "carro1.gif")
            img[24].draw(win)
        if quadrantes[24] == 2:
            img[24] = Image(Point(262.5,587.5), "bege.gif")
            img[24].draw(win)
        if quadrantes[24] == 3:
            img[24] = Image(Point(262.5,587.5), "cinza.gif")
            img[24].draw(win)
        if quadrantes[24] == 4:
            img[24] = Image(Point(262.5,587.5), "carro2.gif")
            img[24].draw(win)
        if quadrantes[24] == 5:
            img[24] = Image(Point(262.5,587.5), "marrom.gif")
            img[24].draw(win)
        if quadrantes[25] == 1:
            img[25] = Image(Point(337.5,587.5), "carro1.gif")
            img[25].draw(win)
        if quadrantes[25] == 2:
            img[25] = Image(Point(337.5,587.5), "bege.gif")
            img[25].draw(win)
        if quadrantes[25] == 3:
            img[25] = Image(Point(337.5,587.5), "cinza.gif")
            img[25].draw(win)
        if quadrantes[25] == 4:
            img[25] = Image(Point(337.5,587.5), "carro2.gif")
            img[25].draw(win)
        if quadrantes[25] == 5:
            img[25] = Image(Point(337.5,587.5), "marrom.gif")
            img[25].draw(win)
        if quadrantes[26] == 1:
            img[26] = Image(Point(412.5,587.5), "carro1.gif")
            img[26].draw(win)
        if quadrantes[26] == 2:
            img[26] = Image(Point(412.5,587.5), "bege.gif")
            img[26].draw(win)
        if quadrantes[26] == 3:
            img[26] = Image(Point(412.5,587.5), "cinza.gif")
            img[26].draw(win)
        if quadrantes[26] == 4:
            img[26] = Image(Point(412.5,587.5), "carro2.gif")
            img[26].draw(win)
        if quadrantes[26] == 5:
            img[26] = Image(Point(412.5,587.5), "marrom.gif")
            img[26].draw(win)
        if quadrantes[27] == 1:
            img[27] = Image(Point(487.5,587.5), "carro1.gif")
            img[27].draw(win)
        if quadrantes[27] == 2:
            img[27] = Image(Point(487.5,587.5), "bege.gif")
            img[27].draw(win)
        if quadrantes[27] == 3:
            img[27] = Image(Point(487.5,587.5), "cinza.gif")
            img[27].draw(win)
        if quadrantes[27] == 4:
            img[27] = Image(Point(487.5,587.5), "carro2.gif")
            img[27].draw(win)
        if quadrantes[27] == 5:
            img[27] = Image(Point(487.5,587.5), "marrom.gif")
            img[27].draw(win)

        if quadrantes[28] == 1:
            img[28] = Image(Point(37.5,662.5), "carro1.gif")
            img[28].draw(win)
        if quadrantes[28] == 2:
            img[28] = Image(Point(37.5,662.5), "bege.gif")
            img[28].draw(win)
        if quadrantes[28] == 3:
            img[28] = Image(Point(37.5,662.5), "cinza.gif")
            img[28].draw(win)
        if quadrantes[28] == 4:
            img[28] = Image(Point(37.5,662.5), "carro2.gif")
            img[28].draw(win)
        if quadrantes[28] == 5:
            img[28] = Image(Point(37.5,662.5), "marrom.gif")
            img[28].draw(win)
        if quadrantes[29] == 1:
            img[29] = Image(Point(112.5,662.5), "carro1.gif")
            img[29].draw(win)
        if quadrantes[29] == 2:
            img[29] = Image(Point(112.5,662.5), "bege.gif")
            img[29].draw(win)
        if quadrantes[29] == 3:
            img[29] = Image(Point(112.5,662.5), "cinza.gif")
            img[29].draw(win)
        if quadrantes[29] == 4:
            img[29] = Image(Point(112.5,662.5), "carro2.gif")
            img[29].draw(win)
        if quadrantes[29] == 5:
            img[29] = Image(Point(112.5,662.5), "marrom.gif")
            img[29].draw(win)
        if quadrantes[30] == 1:
            img[30] = Image(Point(187.5,662.5), "carro1.gif")
            img[30].draw(win)
        if quadrantes[30] == 2:
            img[30] = Image(Point(187.5,662.5), "bege.gif")
            img[30].draw(win)
        if quadrantes[30] == 3:
            img[30] = Image(Point(187.5,662.5), "cinza.gif")
            img[30].draw(win)
        if quadrantes[30] == 4:
            img[30] = Image(Point(187.5,662.5), "carro2.gif")
            img[30].draw(win)
        if quadrantes[30] == 5:
            img[30] = Image(Point(187.5,662.5), "marrom.gif")
            img[30].draw(win)
        if quadrantes[31] == 1:
            img[31] = Image(Point(262.5,662.5),"carro1.gif")
            img[31].draw(win)
        if quadrantes[31] == 2:
            img[31] = Image(Point(262.5,662.5), "bege.gif")
            img[31].draw(win)
        if quadrantes[31] == 3:
            img[31] = Image(Point(262.5,662.5), "cinza.gif")
            img[31].draw(win)
        if quadrantes[31] == 4:
            img[31] = Image(Point(262.5,662.5), "carro2.gif")
            img[31].draw(win)
        if quadrantes[31] == 5:
            img[31] = Image(Point(262.5,662.5), "marrom.gif")
            img[31].draw(win)
        if quadrantes[32] == 1:
            img[32] = Image(Point(337.5,662.5), "carro1.gif")
            img[32].draw(win)
        if quadrantes[32] == 2:
            img[32] = Image(Point(337.5,662.5), "bege.gif")
            img[32].draw(win)
        if quadrantes[32] == 3:
            img[32] = Image(Point(337.5,662.5), "cinza.gif")
            img[32].draw(win)
        if quadrantes[32] == 4:
            img[32] = Image(Point(337.5,662.5), "carro2.gif")
            img[32].draw(win)
        if quadrantes[32] == 5:
            img[32] = Image(Point(337.5,662.5), "marrom.gif")
            img[32].draw(win)
        if quadrantes[33] == 1:
            img[33] = Image(Point(412.5,662.5), "carro1.gif")
            img[33].draw(win)
        if quadrantes[33] == 2:
            img[33] = Image(Point(412.5,662.5), "bege.gif")
            img[33].draw(win)
        if quadrantes[33] == 3:
            img[33] = Image(Point(412.5,662.5), "cinza.gif")
            img[33].draw(win)
        if quadrantes[33] == 4:
            img[33] = Image(Point(412.5,662.5), "carro2.gif")
            img[33].draw(win)
        if quadrantes[33] == 5:
            img[33] = Image(Point(412.5,662.5), "marrom.gif")
            img[33].draw(win)
        if quadrantes[34] == 1:
            img[34] = Image(Point(487.5,662.5), "carro1.gif")
            img[34].draw(win)
        if quadrantes[34] == 2:
            img[34] = Image(Point(487.5,662.5), "bege.gif")
            img[34].draw(win)
        if quadrantes[34] == 3:
            img[34] = Image(Point(487.5,662.5), "cinza.gif")
            img[34].draw(win)
        if quadrantes[34] == 4:
            img[34] = Image(Point(487.5,662.5), "carro2.gif")
            img[34].draw(win)
        if quadrantes[34] == 5:
            img[34] = Image(Point(487.5,662.5), "marrom.gif")
            img[34].draw(win)
        for g in range (3):  
        
            movimentacao(win.getMouse())

                    

#para fechar    
    
    
    
main()
win.getMouse()
win.close()
