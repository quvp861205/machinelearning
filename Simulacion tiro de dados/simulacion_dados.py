import random
from bokeh.plotting import figure, show

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []    
    prob=[]
    sim=[]
    
    for n in range(numero_de_intentos):
    
        shots=[]
        for _ in range(n):
            secuencia_de_tiros = tirar_dado(numero_de_tiros)
            tiros.append(secuencia_de_tiros)
        
        prob_shot_1 = calcular_probabilidad(shots, n)
        prob.append(prob_shot_1)
        sim.append(n)    
         
        tiros_con_1 = 0
        for tiro in tiros:
            if 1 not in tiro:
                tiros_con_1 += 1     
                
    
    plot(sim, prob)
     
    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')

def plot(sim, prob):
    plot = figure(title='Probability get 1 with 1 shot',
                  x_axis_label='Attempts',
                  y_axis_label='Probability')
    
    plot.line(sim,prob)
    show(plot)
    
def calcular_probabilidad(shots, n_simulation):
    shot_1 = 0
    for shot in shots:
        if 1 in shot:
            shot_1 += 1
            
    result = 0
    if n_simulation>0:
        result = shot_1 / n_simulation
    
    return result

if __name__ == '__main__':

    numero_de_tiros = int(input('Cuantas tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)
   