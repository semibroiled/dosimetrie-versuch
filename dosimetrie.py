''' This file should include functions to quickly and efficiently
calculate the necessary parameters for the Dosimetrie und Strahlenschutz 
Experiment K3 '''

''' Grundlage:
i) Calculate the Netto Zählrate einmal von
    a) z_i = N_i / T_i
    with z: Zählrate
         N: Zerfalls Nummer gemessen mittels Zählroh und Messgerät
         T: Zeit/Dauer von Experiment
         '''

def find_z (N, r=10, del_r=0.5, T=60, del_T = 0):

    ''' The Arguments are the Ausfallsmenge N,
    the Abstand r in cm with a default value of 10 cm 
    with delta r being 0.5 cm, and the time elapsed T, 
    which has a default
    value of 60s with delta T being 0s'''
    import math

    if input('Do you have a different time elapsed than 1 minute? Enter to continue\n'):
        try:
            T = int(input('Give your time elapsed in min:\n'))
        except ValueError as ve:
            print('You probaly didn\'t input a number')
            print(ve)
        finally:
            T= T*60 #convert from min to s 
        del_T = float(input('What is you time uncertainty in s?\n'))
    value = input('What are you calculating? Background, Calibration or Unknown:\n')

    #calculating main value for zählrate
    z_i = N/T

    #Unsicheheiten

    del_N = math.sqrt(N)

    #Derivatives

    ddN = 1/T
    ddT = (-N ) / (T**2)

    #Gauss

    try:
        del_z = math.sqrt( ((ddN*del_N)**2) + ((ddT*del_T)**2) )
    except  ValueError as ve:
        print('Something went wrong with the Gaus error calculation')
        print(ve)

    print(f'Your Zählrate z_{value} is {z_i}±{del_z} Bq \n')

    return z_i, del_z

while True:
    try:
        n_value = int(input('What is you Zerfalls Rate?\n'))
    except ValueError as v:
        print('You need to enter something actionable for the Zerfallsrate')
        print(v)
    if n_value:
        get = find_z(n_value)
    else: 
        break
    
    