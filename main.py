# CS1210: HW2
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the intructional team.
#
def signed():
    return (["pwkamp"])


######################################################################
# You may need the regular expression library.
import re


######################################################################
# The OAM class defines the OAM model.
class OAM():
    # The constructor defines three instance variables: the debug
    # flag, which regulates the level of output produced at runtime,
    # the labels dictionary, which defines the mapping from labels to
    # memory locations, and the list representing memory. It also
    # initializes the OAM memory (a list) and the label reference
    # table (a dictionary), with the standard names for I/O (stdin,
    # stdout) included.
    def __init__(self, debug=False):
        self.debug = debug  # Run time output
        self.pc = 1  # Program counter
        self.ar = '?'  # Address register
        self.ir = '?'  # Instruction register
        self.acc = '?'  # Accumulator
        self.b = '?'  # B register
        self.mem = []  # Memory
        self.labels = {'stdin': 0, 'stdout': 0}  # Labels, including I/O

    # The verbose() method toggles the debug variable, which governs
    # run time reporting status.
    def verbose(self):
        self.debug = not self.debug

    # The run() method initalizes the machine (but doesn't clear
    # memory or labels) and then implements the
    # fetch/increment/execute cycle.
    def run(self):
        self.pc = 1
        self.ar = '?'
        self.ir = '?'
        self.acc = '?'
        self.b = '?'
        while self.pc > 0:
            self.fetch()
            self.increment()
            self.execute()
        if self.debug:
            print("Processing halted.")

    # The fetch() method implements the fetch cycle.
    def fetch(self):
        self.ar = self.pc
        self.ir = self.read()
        if self.debug:
            print("Fetch: AR = {} IR = {}".format(self.ar, ' '.join(self.ir)))

    # The increment() method implements the increment cycle.
    def increment(self):
        self.pc = self.pc + 1
        if self.debug:
            print("  Increment: PC = {}".format(self.pc))

    # The execute() method implements the execute cycle, dispatching
    # to the appropriate method as per the first part of the
    # IR. Returns a Boolean indicating whether execution should
    # continue.
    def execute(self):
        # Check for a match, report an issue
        if self.debug:
            print("  Execute: IR = '{}'".format(self.ir))
        try:
            #print('self.' + self.ir[0] + '()')
            exec('self.' + self.ir[0] + '()')
        except Exception as e:
            print(e)
            if self.debug:
                print("Abort: ill-formed instruction IR = '{}'".format(self.ir))
            self.pc = 0

    # The resolve() method resolves a reference to a memory location,
    # which may be an integer or a reference label, such as may be
    # found in an instruction, and returns an int.
    def resolve(self, address):
        try:
            return int(address)
        except ValueError as e:
            return int(self.labels[address])

    # The read() method returns a value from the memory location
    # specified by the AR. If the AR value is 0, it returns a value
    # from keyboard input. If the AR value is a label, it returns the
    # value from memory at the label's reference. Otherwise, if the AR
    # value is a number, it returns the value of memory at that
    # location. If the memory location does not exist, it returns '?'.
    def read(self):
        address = self.resolve(self.ar)
        if address == 0:
            return int(input("Input: "))
        else:
            return self.mem[address]

    # The write() copies the value from the ACC into the
    # location specified by the AR. If the AR value is 0, it prints
    # the value to the screen. If the AR value is a label, it copies
    # the value from the ACC into the label's reference. Otherwise, if
    # the AR value is a number, it copies the value from the ACC to
    # memory at that location.
    def write(self):
        address = self.resolve(self.ar)
        if address == 0:
            print("Output: " + str(self.acc))
        else:
            while True:
                try:
                    self.mem[address] = self.acc
                    break
                except IndexError as e:
                    self.mem.append('?')

    # The add() method adds the B register to ACC and stores the
    # result in ACC.
    def add(self):
        self.acc = int(self.acc)
        self.b = int(self.mem[self.resolve(self.ir[1])])
        self.acc += self.b

    # The sub() method subtracts the B register from ACC and stores
    # the result in ACC.
    def sub(self):
        self.acc = int(self.acc)
        self.b = int(self.mem[self.resolve(self.ir[1])])
        self.acc -= self.b

    # The mlt() method multiplies the B register with ACC and stores
    # the result in ACC.
    def mlt(self):
        self.acc = int(self.acc)
        self.b = int(self.mem[self.resolve(self.ir[1])])
        self.acc *= self.b

    # The div() method divides the ACC with the B register and stores
    # the result in ACC.
    def div(self):
        self.acc = int(self.acc)
        self.b = int(self.mem[self.resolve(self.ir[1])])
        self.acc /= self.b

    # The set() method sets the ACC to the specified value from the
    # IR.
    def set(self):
        self.acc = int(self.ir[1])

    # The neg() method inverts the sign of the ACC.
    def neg(self):
        self.acc = int(self.acc)
        self.acc = -self.acc

    # The inc() method adds 1 to the ACC.
    def inc(self):
        self.acc = int(self.acc)
        self.acc += 1

    # The dec() method subtracts 1 from the ACC.
    def dec(self):
        self.acc = int(self.acc)
        self.acc -= 1

    # The lda() method sets the AR to the address from the IR and
    # reads the corresponding value from memory into ACC. Note that
    # the value in the IR might be a label, an integer, or 0 (meaning
    # read input). Use the resolve() method to disambiguate.
    def lda(self):
        self.ar = self.resolve(self.ir[1])
        self.acc = self.read()

    # The sta() method sets the AR to the address from the IR and
    # stores the value of ACC into the corresponding value in
    # memory. Note that the value in the IR might be a label, an
    # integer, or 0 (meaning read input). Use the resolve() method to
    # disambiguate.
    def sta(self):
        self.ar = self.resolve(self.ir[1])
        self.write()

    # The br() method sets the PC to the specified value.
    def br(self):
        self.pc = self.resolve(self.ir[1])

    # The brp() method sets the PC to the specified value if and only
    # if ACC > 0.
    def brp(self):
        if self.acc > 0:
            self.br()

    # The brz() method sets the PC to the specified value if and only
    # if ACC == 0.
    def brz(self):
        if self.acc == 0:
            self.br()

    # The bri() method sets the PC to the value of memory at the
    # location referenced. Note that the value in memory might be a
    # label, an integer, or 0 (meaning read input). Use the resolve()
    # method to disambiguate.
    def bri(self):
        self.pc = self.mem[self.resolve(self.ir[1])]

    # The brs() method stores the PC value in the memory location
    # referenced and then branches to one beyond that location
    # (remember the intervening increment phase).
    def brs(self):
        self.mem[self.resolve(self.ir[1])] = self.pc

    # The hlt() method stops the machine by setting the PC to 0.
    def hlt(self):
        self.pc = 0

    # The load(filename) method takes a file of OAM machine/assembly
    # code, initializes the OAM memory and label reference table, and
    # loads the contents of the file into memory starting at location
    # 1. Blank lines or lines that start with the comment character,
    # #, are skipped. Remaining lines that match the specified format
    # are written to OAM memory using the write() method (to properly
    # extend self.mem) as a tuple of one or two strings, as
    # appropriate.
    def load(self, filename):
        self.ar = 1
        self.mem.append('?')
        f = open(filename, "r")
        s = f.readlines()
        for line in s:
            line = line.lower()
            if line.find("#") != -1:
                line = line[0:line.find("#")]
            if line in "\n\b\t\r" or line in "" or line is None:
                continue
            if re.search("\w+,\s+([A-Za-z]{2,4})(\s+\w+)?", line) is not None:
                split = re.split(",\s+", re.search("\w+,\s+([A-Za-z]{2,4})(\s+\w+)?", line).group())
                self.labels[split[0]] = self.ar
                inst = tuple(re.split("\s+", split[1]))
                # print(str(inst))
                self.acc = inst
                self.write()

            elif re.search("([A-Za-z]{2,3})( \w+)?", line) is not None:
                instStr = re.search("([A-Za-z]{2,3})( \w+)?", line).group()
                inst = tuple(re.split("\s+", instStr))
                # print(str(inst))
                self.acc = inst
                self.write()

            else:
                pass
            self.ar += 1

    # The dump() method prints out a representation of the state of
    # the machine, followed by whatever is in memory and the label
    # references.
    def dump(self):
        print("State: PC={}; ACC={}; B={}; AR={}; IR={}".format(self.pc, self.acc, self.b, self.ar, self.ir))
        print("Memory:")
        for i in range(len(self.mem)):
            print("  {}: {}".format(i,str(self.mem[i])))
        print("Reference Table:")
        for x in self.labels:
            print("  {}: {}".format(x, str(self.labels[x])))
