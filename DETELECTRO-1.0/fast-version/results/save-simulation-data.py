import numpy as np
import copy
import os
import warnings
cwd = os.getcwd()

# Retrieve simulation parameters

simulation = np.genfromtxt('../temp-data/simulationParameters.csv')

simulationParameters = simulation[:, 1]

NSITES = int(simulationParameters[0])
dt = simulationParameters[1]
beta = simulationParameters[2]
L = int(simulationParameters[3])
t = simulationParameters[4]
U = simulationParameters[5]
mu = simulationParameters[6]
totalMCSweeps = int(simulationParameters[7])
freq = int(simulationParameters[8])
intsize = int(simulationParameters[9])
geom = int(simulationParameters[10])
ny = int(simulationParameters[11])

# Load configuration weights

weights = np.loadtxt('../temp-data/Log-weights.csv', skiprows = 1)

signs = np.loadtxt('../temp-data/Local-av-sign.csv', skiprows = 1)

scalarMeasurements = np.loadtxt('../temp-data/MeasurementsScalars.csv', skiprows = 1)

magCorrMeas = np.loadtxt('../temp-data/EqTimeSzCorrelations.csv', skiprows = 1)

try:
    UneqMagCorrMeas = np.loadtxt('../temp-data/UneqTimeSzCorrelations.csv', skiprows = 1)
except IOError:
    print("\nExisting data contains only equal time measurements")

directory1 = ('data/' + str(NSITES) + \
              'sites_L=' + str(L) + \
              '_beta=' + str(beta) + \
              '_dt_' + str(dt) + '_t_' + \
              str(t) + '_U_'+ str(U) + '_mu_' + str(mu))

directory2 = (directory1 + '/data-to-reproduce/' + \
              'totalMCSweeps_' + str(totalMCSweeps) + \
              '_freq_' + str(freq) + '_intsize_' + str(intsize) + \
              '_geom_' + str(geom) + '_ny_' + str(ny) )

directory3 = (directory1 + '/plots/' + \
              'totalMCSweeps_' + str(totalMCSweeps) + \
              '_freq_' + str(freq) + '_intsize_' + str(intsize) + \
              '_geom_' + str(geom) + '_ny_' + str(ny) )


if not os.path.exists(directory1):
    os.makedirs(directory1)

if not os.path.exists(directory2):
    os.makedirs(directory2)

if not os.path.exists(directory3):
    os.makedirs(directory3)

np.savetxt(directory2 + '/Log-weights.csv', (weights), header = "Configuration log weight")

np.savetxt(directory2 + '/Local-av-sign.csv', (signs), header = "Local average sign")

paramNames  = np.array(['Number of sites', 'dtau', 'beta', 'L',\
't', 'U', 'mu', 'Number of MC Sweeps', 'Frequency of recomputing G',\
'Number of multiplied Bs after stabilization', 'Geometry', 'Ny'])
namedParams = np.zeros(paramNames.size, dtype=[('pnames', 'U50'), ('params', float)])
namedParams['pnames'] = paramNames
namedParams['params'] = simulationParameters

np.savetxt(directory2 + '/simulationParameters.csv', namedParams, fmt="%50s %10.7f" )

measNames  = np.array(['Electron density <n>', 'Double occupancy <n+ n->'\
, 'ZZ AF Structure Factor'])
namedMeas = np.zeros(measNames.size, dtype=[('mnames', 'U50'), ('meas', float)])
namedMeas['mnames'] = measNames
namedMeas['meas'] = scalarMeasurements

np.savetxt(directory2 + '/MeasurementsScalars.csv', namedMeas, fmt="%50s %10.7f" )

np.savetxt(directory2 + '/EqTimeSzCorrelations.csv', (magCorrMeas), \
header = "<Sz_i Sz_j >")

try:
    np.savetxt(directory2 + '/UneqTimeSzCorrelations.csv', (UneqMagCorrMeas))
except NameError:
    print("\nIf you want unequal time measurements as well recompile the code \
and run the simulation again using\n\n\
make eq_or_uneq=src/mainUneqTime.cpp object\
=src/mainUneqTime.o\n\nand \n\n./simulation <U> <mu> <totalMCSweeps>\n")