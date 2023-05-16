#!/usr/bin/python
#coding: utf-8

#_autor_: Hallan Souza

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics 
import csv
import pathlib
import os

from decimal import Decimal

#===========================================================
#===========================================================

def qualmes(mes, dia, hora):
    if mes == 1:
    	dias = int(0)
    if mes == 2:
    	dias = int(31)
    if mes == 3:
    	dias = int(59)
    if mes == 4:
    	dias = int(90)
    if mes == 5:
    	dias = int(120)
    if mes == 6:
    	dias = int(151)
    if mes == 7:
    	dias = int(181)
    if mes == 8:
    	dias = int(212)
    if mes == 9:
    	dias = int(243)
    if mes == 10:
    	dias = int(273)
    if mes == 11:
    	dias = int(304)
    if mes == 12:
    	dias = int(334)

    djuliano = round( dia + dias + hora/24, 3)

    return djuliano

#--

def stringFloat(variable):
    if variable == 'nan':
        variable = np.nan
    elif variable == '':
        variable = np.nan
    elif variable == variable:
        variable = float(variable)
        variable = round(variable, 4)
    return variable

def stringInt(variable):
    if variable == 'nan':
        variable = str('nan')
    elif variable == np.nan:
        variable = str('nan')
    elif variable == '':
        variable = str('nan')
    elif variable == variable:
        variable = int(float(variable))
    return variable

#--------

direct_xls = '/home/hallan/pesquisa/hsj.github/IFTO.INFO/norte/'

arr = os.listdir(direct_xls)

arq = []

#----
#----

for file in arr:

    arq.append(file)

    cod_inmet = str( file[6:10] )

    arquivos = '/home/hallan/pesquisa/hsj.github/IFTO.INFO/norte/'+ file +''

    #----
    #----

    print(file, cod_inmet)

    dframe = []

    #----
    #----

    with open(arquivos) as csv_file_clds:
                    
        csv_reader_file_clds = csv.reader(csv_file_clds, delimiter=',')
        
        for dt in csv_reader_file_clds:

            #print( dt )

            ano          = stringInt(   dt[1]  )
            mes          = stringInt(   dt[2]  )
            dia          = stringInt(   dt[3]  )
            hora         = stringInt(   dt[4]  )

            precipitacao_hr                         = stringFloat( dt[6]  )         # mm
            pressao_atmosferica_nivel_estacao_hr    = stringFloat( dt[7]  )         # mB
            pressao_atmosferica_maxima              = stringFloat( dt[8]  )         # mB
            pressao_atmosferica_minima              = stringFloat( dt[9]  )         # mB
            radiacao_global                         = stringFloat( dt[10]  )  * (1000/3600)       # Kj/m²
            temperatura_ar_bulbo_seco               = stringFloat( dt[11] )         # °C
            temperatura_ponto_orvalho               = stringFloat( dt[12] )         # °C
            temperatura_maxima                      = stringFloat( dt[13] )         # °C         
            temperatura_minima                      = stringFloat( dt[14] )         # °C
            temperatura_ponto_orvalho_maxima        = stringFloat( dt[15] )         # °C
            temperatura_ponto_orvalho_minima        = stringFloat( dt[16] )         # °C
            umidade_relativa_maxima_porcentagem     = stringFloat( dt[17] )         # %
            umidade_relativa_minima_porcentagem     = stringFloat( dt[18] )         # %
            umidade_relativa_ar_porcentagem         = stringFloat( dt[19] )         # %
            vento                                   = stringFloat( dt[20] )         # m/s

            #---
            #---

            dia_juliano = qualmes(mes, dia, hora)

            #print( dia_juliano, radiacao_global )


            dados = [ cod_inmet, ano, mes, dia, hora, dia_juliano,\
                      precipitacao_hr, pressao_atmosferica_nivel_estacao_hr, pressao_atmosferica_maxima, pressao_atmosferica_minima, \
                      radiacao_global, temperatura_ar_bulbo_seco, temperatura_ponto_orvalho, temperatura_maxima, temperatura_minima, \
                      temperatura_ponto_orvalho_maxima, temperatura_ponto_orvalho_minima, umidade_relativa_maxima_porcentagem, \
                      umidade_relativa_minima_porcentagem, umidade_relativa_ar_porcentagem, vento ]

            #-----------------------------------------------------------
            #
            # ESTA PARTE É PARA VOCÊS MANIPULAREM OS DADOS DE VOCÊS!!!
            #
            # PENSEM EM COMO CALCULAR O QUE ESTÁ SENDO PEDIDO!!
            #
            # TENDO DÚVIDAS, ME CHAME!
            #
            #-----------------------------------------------------------



            #-----------------------------------------------------------
            #-----------------------------------------------------------
            #-----------------------------------------------------------


            dframe.append(dados)

#            print( dados )

df = pd.DataFrame(dframe, columns=['cod_inmet','ano','mes','dia','hora', 'dia_juliano',\
                                  'prec','pr_atm','pr_atm_max','pr_atm_min','rad_global','temp_bulbo_seco','temp_ponto_orvalho','temp_max','temp_min', \
                                  'temp_ponto_orvalho_max','temp_ponto_orvalho_min','um_rel_max_porc','um_rel_min_porc','um_rel_ar_porc','vento'])

lenr = len(df['rad_global'])

for i in range(lenr):

    print( type(df['rad_global'][i]) )

#df.to_csv('diretorio_para_salvar_seus_dados/')

#---


plt.subplots(1, 1, figsize=(15, 6), dpi=80)

plt.subplot(1,1,1)
plt.plot(   df['dia_juliano'], df['temp_max'], color='red',   label='temp. maxima') #marker='o', 
plt.plot(   df['dia_juliano'], df['temp_min'], color='blue',  label='temp. minima')
plt.legend(fontsize=8)
#plt.xlim(0,   365)
#plt.ylim(0, 1200)

#plt.subplot(4,1,2)
#plt.plot( df['dia_juliano'], df['rad_global'], color='black')   #,  marker='o'
#plt.legend(fontsize=8)
#plt.xlim(0,   365)
#plt.ylim(-750,  750)

#plt.subplot(4,1,3)
#plt.bar( df['dia_juliano'], df['prec'], color='magenta')   #,  marker='o'
#plt.legend(fontsize=8)
#plt.xlim(0,   365)
#plt.ylim(-750,  750)

#plt.subplot(4,1,4)
#plt.plot( df['dia_juliano'], df['vento'], color='cyan')   #,  marker='o'
#plt.legend(fontsize=8)
#plt.xlim(0,   365)
#plt.ylim(-750,  750)


#plt.fill_between(djj, mjj-std, mjj+std, color='b', alpha=0.2)
plt.show()