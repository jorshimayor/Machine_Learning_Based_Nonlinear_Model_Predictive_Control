# Import
from apm import *
    
# Select server
s = 'http://byu.apmonitor.com'

##################################
# set up reactor simulator
##################################
a = 'reactor4'
# Clear previous application
apm(s,a,'clear all')
# Load model file
apm_load(s,a,'cstr.apm')
# Load time points for future predictions
csv_load(s,a,'cstr.csv')
# APM Variable Classification
# class = FV, MV, SV, CV
#   F or FV = Fixed value - parameter may change to a new value every cycle
#   M or MV = Manipulated variable - independent variable over time horizon
#   S or SV = State variable - model variable for viewing
#   C or CV = Controlled variable - model variable for control
#Parameters
FVs = 'SP','Cooling_Temp','Flow','Feed_Conc','Feed_Temp'
MVs = '---'
#Variables
SVs = 'Concentration','---'
CVs = 'Temperature','---'
# Set up variable classifications for data flow
for x in FVs: apm_info(s,a,'FV',x)
for x in MVs: apm_info(s,a,'MV',x)
for x in SVs: apm_info(s,a,'SV',x)
for x in CVs: apm_info(s,a,'CV',x)
# Options
# turn on historization to see past results in web-viewer
apm_option(s,a,'nlc.hist_hor',100)
# set web plot update frequency
apm_option(s,a,'nlc.web_plot_freq',3)
# set number of nodes for collocation
apm_option(s,a,'nlc.nodes',3)
# imode (1=ss, 2=mpu, 3=rto, 4=sim, 5=mhe, 6=nlc)
# initialize with steady state
apm_option(s,a,'nlc.imode',1)
solver_output = apm(s,a,'solve')
# swith to dynamic simulation
apm_option(s,a,'nlc.imode',4)

# retrieve steady state cooling temperature and reactor temperature
Tc = apm_tag(s,a,'cooling_temp.newval')
T = apm_tag(s,a,'temperature.model')

# set point
Tsp = 310.0

# Tc upper and lower limits
Tc_upper = 350.0
Tc_lower = 250.0

##################################
# set up linear MPC
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
apm_option(s,c,'Temperature.fstatus',1)
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

for isim in range(151):

    # Nonlinear MPC Controller ######################
    if isim==2:
        # don't re-center reference trajectory each cycle
        apm_option(s,c,'Temperature.tr_init',1)
    # Change temperature set point
    if (isim==10):
        Tsp = 330.0
    elif (isim==50):
        Tsp = 370.0
    elif (isim==100):    
        # widen temperature control and minimize concentration
        apm_option(s,c,'Concentration.cost',1.0)
        delta = 20.0

    # Input setpoint and measurements
    apm_meas(s,c,'Temperature',T)
    apm_option(s,c,'Temperature.sphi',Tsp+delta)
    apm_option(s,c,'Temperature.splo',Tsp-delta)
    
    # Solve
    output = apm(s,c,'solve')
    print(output)
    
    # Output MV new value, check if good solution
    if (apm_tag(s,a,'nlc.appstatus')==1):
        Tc = apm_tag(s,c,'Cooling_Temp.newval')
    else:
        Tc = 280.0
    # #####################################

    # Insert Cooling temperature and setpoint
    apm_meas(s,a,'Cooling_Temp',Tc)

    # Run on server
    solver_output = apm(s,a,'solve')

    # Read reactor temperature and concentration
    T = apm_tag(s,a,'Temperature.model')
    Ca = apm_tag(s,a,'Concentration.model')

    # Print data for import into Excel
    print('{0:2f} {1:2f} {2:2f} {3:2f}'.format(time,Tc,T,Ca))

    # Increment time
    time = time + dt

    if (isim==1):
        # Open Web Viewers
        url = apm_web(s,a)
        url = apm_web(s,c)
