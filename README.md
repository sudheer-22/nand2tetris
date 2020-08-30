# nand2tetris
Assembler and VM Translator have been developed for a small 16-bit computer.Assembly language of this system consists three category of instructions A-type(address),C-type(compute), L-type(label).Assembler developed converts these assembly language instruction into a 16-bit machine code. The VM abstraction which this computer uses has five memory segments and one stack memory segment(for performing computations). VM translator developed coverts these VM language instructions into assembly language instructions. The VM language this computer uses broadly has five category of instructions Arithmetic/Logical commands(inludes add,sub,neg,eq,get,lt,and,or,not), Branching Commands(includes label name,goto label_name,if-goto label_name), Memory access commands(includes pop segment i,push segment i), Function commands(includes function functionName nVars,call functionName nArgs,return).
