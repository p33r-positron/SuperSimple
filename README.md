# SuperSimple
A mini programming language that compiles into C through a compiler either writed in NodeJS, Java, or Python3

# Introduction
SuperSimple is a little programming language that looks like BASIC (Even if you can write the commands in lowercase), and compiles into C !
It's not a interpreted language (For now at least).
The goal is to make a simple programming langage but also to have the really great speed of C.
My challenge is to keep up-to-date three compilers in three different programming languages (NodeJS, Java and Python).
Happy coding, just keep in mind that this programming langage is not enough great for now to be used for real programming.

# About the compilers

NodeJS Compiler: Okay, up-to-date (v1.0.1)
Java Compiler: Not yet, WIP
Python3 Compiler: Okay up-to-date (v1.0.1)

# Documentation

Here is the basics of SuperSimple:

PRINT "TEXT"
Prints TEXT and a line return.

RETURN N
Returns the N integer

# Compiler Documentation

NodeJS Compiler:
  node <file> [-c]
  -c -> Automaticly compiles the program with GCC once translated/compiled.
  
Python3 Compiler:
  python3 <file> [-c [-e]|-e [-c]|-ce|-ec]
  -c -> Automaticly compiles the program with GCC once translated/compiled.
  -e -> Automaticly executes the program once (And if) compiled with GCC.
  -ce -> Both of -c and -e
  -ec -> Both of -c and -e
  
Java Compiler:
  Well...
