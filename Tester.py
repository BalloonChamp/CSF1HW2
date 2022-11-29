import main

oam = main.OAM(True)


# for i in range(7):
#     print("Test {}\n".format(str(i)))
#     oam.load("test{}.oam".format(str(i)))
#     print("\n\n")

oam.load("test3.oam")
oam.run()
oam.dump()
