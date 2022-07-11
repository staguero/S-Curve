from copy import deepcopy
import numpy as np
from pyscurve import ScurvePlanner, plot_trajectory

if __name__ == "__main__":
    q0 = [0]
    q1 = [6.28318530718]
    v0 = [0]
    v1 = [0]
    v_max = 1.85
    a_max = 1.45
    j_max = 4.5

    p = ScurvePlanner()
    tr = p.plan_trajectory(q0, q1, v0, v1, v_max, a_max, j_max)
    perfiles,tiempo=plot_trajectory(tr, dt=0.01)
    
    tiemporep=deepcopy(tiempo)
    tiempor1=deepcopy(tiemporep)
    tiempor2=deepcopy(tiemporep)
    tiempor3=deepcopy(tiemporep)
    for i in range(len(tiemporep)):
        tiempo[i]+=5
        tiempor1[i]+=10
        tiempor2[i]+=15
    comp_tiempo=np.concatenate((tiempo, tiempor1, tiempor2), axis=0)
    comp_tiempo_2=deepcopy(comp_tiempo)
    comp_tiempo_3=deepcopy(comp_tiempo)
    comp_tiempo_4=deepcopy(comp_tiempo)
    comp_tiempo_5=deepcopy(comp_tiempo)
    comp_tiempo_6=deepcopy(comp_tiempo)
    comp_tiempo_7=deepcopy(comp_tiempo)
    comp_tiempo_8=deepcopy(comp_tiempo)
    comp_tiempo_9=deepcopy(comp_tiempo)
    comp_tiempo_10=deepcopy(comp_tiempo)
    comp_tiempo_11=deepcopy(comp_tiempo)
    comp_tiempo_12=deepcopy(comp_tiempo)
    for i in range(len(comp_tiempo)):
        comp_tiempo_2[i]+=20
        comp_tiempo_3[i]+=40
        comp_tiempo_4[i]+=60
        comp_tiempo_5[i]+=80
        comp_tiempo_6[i]+=100
        comp_tiempo_7[i]+=120
        comp_tiempo_8[i]+=140
        comp_tiempo_9[i]+=160
        comp_tiempo_10[i]+=180
        comp_tiempo_11[i]+=200
        comp_tiempo_12[i]+=220
    tiempo_ciclo=np.concatenate((comp_tiempo, comp_tiempo_2, comp_tiempo_3,comp_tiempo_4,comp_tiempo_5,comp_tiempo_6,comp_tiempo_7,comp_tiempo_8,comp_tiempo_9,comp_tiempo_10,comp_tiempo_11,comp_tiempo_12), axis=0)
    np.savetxt('time_ciclo.txt', tiempo_ciclo, fmt='%.6f', delimiter=',')   

    cresta=deepcopy(tiempo)
    for i in range(len(cresta)):
        cresta[i]=q1[0]
    reversed_arr = perfiles[0][2][::-1]
    comp_perfil=np.concatenate((perfiles[0][2], cresta, reversed_arr), axis=0)
    comp_perfil_2=deepcopy(comp_perfil)
    comp_perfil_3=deepcopy(comp_perfil)
    comp_perfil_4=deepcopy(comp_perfil)
    comp_perfil_5=deepcopy(comp_perfil)
    comp_perfil_6=deepcopy(comp_perfil)
    comp_perfil_7=deepcopy(comp_perfil)
    comp_perfil_8=deepcopy(comp_perfil)
    comp_perfil_9=deepcopy(comp_perfil)
    comp_perfil_10=deepcopy(comp_perfil)
    comp_perfil_11=deepcopy(comp_perfil)
    comp_perfil_12=deepcopy(comp_perfil)
    perfil_ciclo=np.concatenate((comp_perfil, comp_perfil_2, comp_perfil_3,comp_perfil_4,comp_perfil_5,comp_perfil_6,comp_perfil_7,comp_perfil_8,comp_perfil_9,comp_perfil_10,comp_perfil_11,comp_perfil_12), axis=0)    
    np.savetxt('pos_ciclo.txt', perfil_ciclo, fmt='%.6f', delimiter=',')

    cresta_w=deepcopy(tiempo)
    reversed_arr_w = deepcopy(perfiles[0][1][::-1])
    for i in range(len(cresta)):
        cresta_w[i]=0
        reversed_arr_w[i]=reversed_arr_w[i]*(-1)
    comp_perfil_w=np.concatenate((perfiles[0][1], cresta_w, reversed_arr_w), axis=0)
    comp_perfil_w_2=deepcopy(comp_perfil_w)
    comp_perfil_w_3=deepcopy(comp_perfil_w)
    comp_perfil_w_4=deepcopy(comp_perfil_w)
    comp_perfil_w_5=deepcopy(comp_perfil_w)
    comp_perfil_w_6=deepcopy(comp_perfil_w)
    comp_perfil_w_7=deepcopy(comp_perfil_w)
    comp_perfil_w_8=deepcopy(comp_perfil_w)
    comp_perfil_w_9=deepcopy(comp_perfil_w)
    comp_perfil_w_10=deepcopy(comp_perfil_w)
    comp_perfil_w_11=deepcopy(comp_perfil_w)
    comp_perfil_w_12=deepcopy(comp_perfil_w)
    perfil_w_ciclo=np.concatenate((comp_perfil_w, comp_perfil_w_2, comp_perfil_w_3,comp_perfil_w_4,comp_perfil_w_5,comp_perfil_w_6,comp_perfil_w_7,comp_perfil_w_8,comp_perfil_w_9,comp_perfil_w_10,comp_perfil_w_11,comp_perfil_w_12), axis=0)    
    np.savetxt('vel_ciclo.txt', perfil_w_ciclo, fmt='%.6f', delimiter=',')
    #[]