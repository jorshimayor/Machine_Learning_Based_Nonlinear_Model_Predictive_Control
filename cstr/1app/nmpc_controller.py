# Import
from apm import *
    
# Select server
s = 'http://byu.apmonitor.com'

##################################
# set up nonlinear MPC
##################################
c = 'nmpc'
# Clear previous application
apm(s,c,'clear all')

# load model variables and equations
apm_load(s,c,'nmpc.apm')

# load data
csv_load(s,c,'nmpc.csv')

#  APM Variable Classification
apm_info(s,c,'MV','Cooling_Temp')
apm_info(s,c,'CV','Concentration')
apm_info(s,c,'CV','Temperature')

# Options
apm_option(s,c,'nlc.nodes',3)
apm_option(s,c,'nlc.hist_hor',200)
apm_option(s,c,'nlc.web_plot_freq',3)
apm_option(s,c,'nlc.mv_type',0)
# Bounds
apm_option(s,c,'Cooling_Temp.lower',250)
apm_option(s,c,'Cooling_Temp.upper',350)
# Turn on parameters to control
apm_option(s,c,'Cooling_Temp.status',1)
apm_option(s,c,'Cooling_Temp.dmax',10)
apm_option(s,c,'Cooling_Temp.fstatus',0)

apm_option(s,c,'Temperature.status',1)
apm_option(s,c,'Temperature.fstatus',0)
apm_option(s,c,'Temperature.tau',2.0)
apm_option(s,c,'Temperature.tr_init',2)
apm_option(s,c,'Concentration.wsphi',10.0)
apm_option(s,c,'Concentration.wsplo',10.0)

apm_option(s,c,'Concentration.status',1)
apm_option(s,c,'Concentration.fstatus',0)
apm_option(s,c,'Concentration.tr_init',0)
apm_option(s,c,'Concentration.sphi',0.2)
apm_option(s,c,'Concentration.splo',0.0)
apm_option(s,c,'Concentration.wsphi',10.0)
apm_option(s,c,'Concentration.wsplo',10.0)

# initialize with steady state simulation
apm_option(s,c,'nlc.imode',1)
solver_output = apm(s,c,'solve')
# switch back to dynamic optimization
apm_option(s,c,'nlc.imode',6)

# initialize values
time = 0.0
dt = 0.05
Tsp = 310.0
delta = 0.1

for isim in range(201):

    # Nonlinear MPC Controller ######################
    if isim==2:
        # don't re-center reference trajectory each cycle
        apm_option(s,c,'Temperature.tr_init',1)
    # Change temperature set point
    if (isim==10):
        Tsp = 330.0
    elif (isim==50):
        Tsp = 370.0
    elif (isim==150):    
        # widen temperature control and minimize concentration
        apm_option(s,c,'Concentration.cost',1.0)
        delta = 20.0

    # Input setpoints
    apm_option(s,c,'Temperature.sphi',Tsp+delta)
    apm_option(s,c,'Temperature.splo',Tsp-delta)
    
    # Solve
    output = apm(s,c,'solve')
    print(output)
    # #####################################

    # Read reactor temperature and concentration
    T = apm_tag(s,c,'Temperature.model')
    Ca = apm_tag(s,c,'Concentration.model')
    Tc = apm_tag(s,c,'Cooling_Temp.newval')
    
    # Print data for import into Excel
    print('{0:2f} {1:2f} {2:2f} {3:2f}'.format(time,Tc,T,Ca))

    # Increment time
    time = time + dt

    if (isim==1):
        # Open Web Viewers
        url = apm_web(s,c)
