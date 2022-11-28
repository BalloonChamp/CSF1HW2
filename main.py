# CS1210: HW2
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the intructional team.
#
def signed():
    return (["hawkid"])


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
            exec('self.' + self.ir[0] + '()')
        except:
            if self.debug:
                print("Abort: ill-formed instruction IR = '{}'".format(self.ir))
            self.pc = 0

    # The resolve() method resolves a reference to a memory location,
    # which may be an integer or a reference label, such as may be
    # found in an instruction, and returns an int.
    def resolve(self, address):
        pass

    # The read() method returns a value from the memory location
    # specified by the AR. If the AR value is 0, it returns a value
    # from keyboard input. If the AR value is a label, it returns the
    # value from memory at the label's reference. Otherwise, if the AR
    # value is a number, it returns the value of memory at that
    # location. If the memory location does not exist, it returns '?'.
    def read(self):
        pass

    # The write() copies the value a value from the ACC into the
    # location specified by the AR. If the AR value is 0, it prints
    # the value to the screen. If the AR value is a label, it copies
    # the value from the ACC into the label's reference. Otherwise, if
    # the AR value is a number, it copies the value from the ACC to
    # memory at that location.
    def write(self):
        pass

    # The add() method adds the B register to ACC and stores the
    # result in ACC.
    def add(self):
        pass

    # The sub() method subtracts the B register from ACC and stores
    # the result in ACC.
    def sub(self):
        pass

    # The mlt() method multiplies the B register with ACC and stores
    # the result in ACC.
    def mlt(self):
        pass

    # The div() method divides the ACC with the B register and stores
    # the result in ACC.
    def div(self):
        pass

    # The set() method sets the ACC to the specified value from the
    # IR.
    def set(self):
        pass

    # The neg() method inverts the sign of the ACC.
    def neg(self):
        pass

    # The inc() method adds 1 to the ACC.
    def inc(self):
        pass

    # The dec() method subtracts 1 from the ACC.
    def dec(self):
        pass

    # The lda() method sets the AR to the address from the IR and
    # reads the corresponding value from memory into ACC. Note that
    # the value in the IR might be a label, an integer, or 0 (meaning
    # read input). Use the resolve() method to disambiguate.
    def lda(self):
        pass

    # The sta() method sets the AR to the address from the IR and
    # stores the value of ACC into the corresponding value in
    # memory. Note that the value in the IR might be a label, an
    # integer, or 0 (meaning read input). Use the resolve() method to
    # disambiguate.
    def sta(self):
        pass

    # The br() method sets the PC to the specified value.
    def br(self):
        pass

    # The brp() method sets the PC to the specified value if and only
    # if ACC > 0.
    def brp(self):
        pass

    # The brz() method sets the PC to the specified value if and only
    # if ACC == 0.
    def brz(self):
        pass

    # The bri() method sets the PC to the value of memory at the
    # location referenced. Note that the value in memory might be a
    # label, an integer, or 0 (meaning read input). Use the resolve()
    # method to disambiguate.
    def bri(self):
        pass

    # The brs() method stores the PC value in the memory location
    # referenced and then branches to one beyond that location
    # (remember the intervening increment phase).
    def brs(self):
        pass

    # The hlt() method stops the machine by setting the PC to 0.
    def hlt(self):
        pass

    # The load(filename) method takes a file of OAM machine/assembly
    # code, initializes the OAM memory and label reference table, and
    # loads the contents of the file into memory starting at location
    # 1. Blank lines or lines that start with the comment character,
    # #, are skipped. Remaining lines that match the specified format
    # are written to OAM memory using the write() method (to properly
    # extend self.mem) as a tuple of one or two strings, as
    # appropriate.
    def load(self, filename):
        f = open(filename, "r")
        f.readlines()

    # The dump() method prints out a representation of the state of
    # the machine, followed by whatever is in memory and the label
    # references.
    def dump(self):
        print("PC={} IR={} AR={} ACC={} B={}".format(self.pc, self.ir, self.ar, self.acc, self.b))
