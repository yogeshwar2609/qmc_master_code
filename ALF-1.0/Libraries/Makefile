FC=$(f90)
FLAGS=$(FL)

all:
	(cd Modules;make -f Makefile FC=$(FC) FLAGS="$(FLAGS)")
	(cd libqrref; make FC=$(FC) FLAGS="$(FLAGS)")

cleanmodules:
	(cd Modules; make -f Makefile clean; cd ..)

cleanqrref:
	(cd libqrref; make clean)

clean: cleanmodules cleanqrref
