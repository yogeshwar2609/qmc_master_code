# -DMPI selects MPI.
# -DSTAB1  Alternative stabilization, using the singular value decomposition.
# -DSTAB2  Alternative stabilization, lapack QR with  manual pivoting. Packed form of QR factorization is not used.
# (Noflag) Default  stabilization, using lapack QR with pivoting. Packed form of QR factorization  is used. 
# -DQRREF  Enables reference lapack implementation of QR decomposition.
# Recommendation:  just use the -DMPI flag if you want to run in parallel or leave it empy for serial jobs.  
# The default stabilization, no flag, is generically the best. 
PROGRAMCONFIGURATION = -DMPI 
PROGRAMCONFIGURATION = 
f90 = gfortran
export f90
F90OPTFLAGS = -O3 -Wconversion  -fcheck=all
F90OPTFLAGS = -O3
export F90OPTFLAGS
F90USEFULFLAGS = -cpp -std=f2003
F90USEFULFLAGS = -cpp
export F90USEFULFLAGS
FL = -c ${F90OPTFLAGS} ${PROGRAMCONFIGURATION}
export FL
DIR = ${CURDIR}
export DIR
Libs = ${DIR}/Libraries/
export Libs
LIB_BLAS_LAPACK = -llapack -lblas
export LIB_BLAS_LAPACK

.PHONY: all lib ana program
all: lib ana program 

lib:
	cd Libraries && $(MAKE)
ana: lib
	cd Analysis && $(MAKE)
program: lib
	cd Prog && $(MAKE)

.PHONY: clean cleanall cleanprog cleanlib cleanana help
clean: cleanall
cleanall: cleanprog cleanlib cleanana
cleanprog:
	cd Prog && $(MAKE) clean
cleanlib:
	cd Libraries && $(MAKE) clean
cleanana:
	cd Analysis && $(MAKE) clean
help:
	@echo "The following are some of the valid targets of this Makefile"
	@echo "all, program, lib, ana, clean, cleanall, cleanprog, cleanlib, cleanana"
