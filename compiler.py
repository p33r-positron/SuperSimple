#!/usr/bin/python3

import os, sys, platform, re;

if len(sys.argv) < 2:
	print("Usage:\r\n\tcompiler <file.sssc> [-c [-e]|-e [-c]|-ce|-ec]");
	exit(1);

def typeof(word):
	return word[:3];

def getstr(word):
	if typeof(word) == "str":
		return word[:-1][6:];
	else:
		raise Exception("Error: Trying to get the string of a word that isn't a string | ABORTING...");

def getint(word):
	if typeof(word) == "int":
		return word[5:];
	else:
		raise Exception("Error: Trying to get the integer of a word that isn't a integer | ABORTING...");

def gen(pcode):
	final = "";
	start = "/*Generated by Python3 version of SuperSimple Compiler*/\r\n\r\nint main(int argc, char** argv)\r\n{\r\n";
	end = "}\r\n";
	output = "";
	includes = [];
	layer = 1;
	nword = len(pcode); #Oh
	i = 0;
	while i < nword:
		if pcode[i] == "PRINT":
			i+=1;
			if "stdio.h" in includes:
				pass;
			else:
				includes.append("stdio.h");
			if typeof(pcode[i]) == "str":
				output += layer*"\t" + "printf(\"%s\", \"" + getstr(pcode[i]) + "\\r\\n\");\r\n";
		elif pcode[i] == "RETURN":
			i+=1;
			if "stdio.h" in includes:
				pass;
			else:
				includes.append("stdio.h");
			if typeof(pcode[i]) == "int":
				output += layer*"\t" + "return " + getint(pcode[i]) + ";\r\n";
		i+=1;
	for module in includes:
		final += "#include <"+module+">\r\n";
	final += "\r\n";
	final += start;
	final += output;
	final += end;
	return final;

def parLex(code):
	tok = "";
	rstr = 0;
	wstr = "";
	toks = [];
	for char in code:
		tok += char;
		if tok == " " or tok == "\n" or tok == "\t" or tok == "\r":
			tok = "";
		elif tok.lower() == "print":
			toks.append("PRINT");
			tok = "";
		elif tok.lower() == "return":
			toks.append("RETURN");
			tok = "";
		elif tok == "\"":
			if rstr == 0:
				rstr = 1;
			elif rstr == 1:
				toks.append("str::\""+wstr+"\"");
				wstr = "";
				rstr = 0;
				tok = "";
		elif rstr == 1:
			wstr += char;
			tok = "";
		else:
			if len(re.findall("\\d", tok)) > 0:
				toks.append("int::"+tok);
	return toks;

def __main__():
	print("Trying to open the file provided...");
	file = open(sys.argv[1], "r").read();
	oname = sys.argv[1][:-5] + ".c";
	print("Lexing and Parsing...");
	parsed = parLex(file);
	print("Generating...");
	out = gen(parsed);
	print("Trying to open the output file...");
	nfile = open(oname, "w");
	print("(Over)writing the output file...");
	nfile.write(out);
	nfile.close();
	if len(sys.argv) < 3 or (len(sys.argv) >= 3and sys.argv[2] != "-c" and sys.argv[2] != "-ec" and sys.argv[2] != "-ce" and sys.argv[3] != "-c"):
		cyn = input("Would you like to compile the file with GCC (Install MinGW if you're on Windows) ? [Y/n]: ");
		if cyn.lower() != "n":
			if platform.system() == "Windows":
				os.system("gcc "+oname+" -o "+oname[:-2]+".exe");
			else:
				os.system("gcc "+oname+" -o "+oname[:-2]);
		else:
			print("Compile it yourself then !");
			return exit(0);
	else:
		if platform.system() == "Windows":
			os.system("gcc "+oname+" -o "+oname[:-2]+".exe");
		else:
			os.system("gcc "+oname+" -o "+oname[:-2]);
	if len(sys.argv) < 3 or (len(sys.argv) >=3 and sys.argv[2] != "-e" and sys.argv[2] != "-ce" and sys.argv[2] != "-ec" and sys.argv[3] != "-e"):
		eyn = input("Do you want me to execute the program ? [Y/n]: ");
		if eyn.lower() != "n":
			print("---STARTING PROGRAM OUTPUT---\r\n");
			if platform.system() == "Windows":
				os.system(".\\"+oname[:-2]+".exe");
			else:
				os.system("./"+oname[:-2]);
			print("\r\n---ENDING PROGRAM OUTPUT---");
		else:
			print("Execute it yourself then !");
			return exit(0);
	else:
		print("---STARTING PROGRAM OUTPUT---\r\n");
		if platform.system() == "Windows":
			os.system(".\\"+oname[:-2]+".exe");
		else:
			os.system("./"+oname[:-2]);
		print("\r\n---ENDIGN PROGRAM OUTPUT---");
	print("Goodbye !");
	return exit(0);

__main__();
