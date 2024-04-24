import sys
import math

def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)

class Signal:
    def __init__(self, name, signal):
        self.name = name
        self.signal = signal
    
    def __repr__(self):
        return f"{self.name} : {self.signal}"

class Output(Signal):
    def __init__(self, name, comm):
        super().__init__(name, "")
        self.command = comm
    
    def logic(self, name1:Signal, name2:Signal):
        if self.command == "AND":
            self.signal = bin_and(name1.signal, name2.signal)
        elif self.command == "OR":
            self.signal = bin_or(name1.signal, name2.signal)
        elif self.command == "XOR":
            self.signal = bin_xor(name1.signal, name2.signal)
        elif self.command == "NAND":
            self.signal = bin_nand(name1.signal, name2.signal)
        elif self.command == "NOR":
            self.signal = bin_nor(name1.signal, name2.signal)
        elif self.command == "NXOR":
            self.signal = bin_nxor(name1.signal, name2.signal)
    
def bin_and(sig1, sig2):
    output = ""
    for b in range(len(sig1)):
        if sig1[b] == "-" and sig2[b] == "-":
            output += "-"
        else:
            output += "_"
    return output

def bin_or(sig1, sig2):
    output = ""
    for b in range(len(sig1)):
        if sig1[b] == "-" or sig2[b] == "-":
            output += "-"
        else:
            output += "_"
    return output

def bin_xor(sig1, sig2):
    output = ""
    for b in range(len(sig1)):
        if sig1[b] == sig2[b]:
            output += "_"
        else:
            output += "-"
    return output

def bin_nand(sig1, sig2):
    output = ""
    for b in range(len(sig1)):
        if bin_and(sig1[b], sig2[b]) == "_":
            output += "-"
        else:
            output += "_"
    return output

def bin_nor(sig1, sig2):
    output = ""
    for b in range(len(sig1)):
        if bin_or(sig1[b], sig2[b]) == "_":
            output += "-"
        else:
            output += "_"
    return output

def bin_nxor(sig1, sig2):
    output = ""
    for b in range(len(sig1)):
        if bin_xor(sig1[b], sig2[b]) == "_":
            output += "-"
        else:
            output += "_"
    return output
        

n = int(input())
m = int(input())
signals = {}
output = []
for i in range(n):
    input_name, input_signal = input().split()
    sig = Signal(input_name, input_signal)
    signals[input_name] = sig
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    output.append((Output(output_name, _type), input_name_1, input_name_2))
log(signals)
log(output)
for i in output:
    out = i[0]
    name1 = i[1]
    name2 = i[2]
    out.logic(signals[name1], signals[name2])
    print(out.name, out.signal)
