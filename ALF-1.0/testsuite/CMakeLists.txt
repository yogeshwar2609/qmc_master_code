cmake_minimum_required(VERSION 2.8.5)
Project(matmod.tests C Fortran)

add_subdirectory(matmod.tests)
add_subdirectory(Prog.tests)
enable_testing()
