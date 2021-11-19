from textwrap import wrap
import bcolors


def checkCount(self, count, bin):
    if count == 1:
        if bin == '1':
            self.series1_1 = self.series1_1 + 1
        else:
            self.series1_0 = self.series1_0 + 1
    elif count == 2:
        if bin == '1':
            self.series2_1 = self.series2_1 + 1
        else:
            self.series2_0 = self.series2_0 + 1
    elif count == 3:
        if bin == '1':
            self.series3_1 = self.series3_1 + 1
        else:
            self.series3_0 = self.series3_0 + 1
    elif count == 4:
        if bin == '1':
            self.series4_1 = self.series4_1 + 1
        else:
            self.series4_0 = self.series4_0 + 1
    elif count == 5:
        if bin == '1':
            self.series5_1 = self.series5_1 + 1
        else:
            self.series5_0 = self.series5_0 + 1
    else:
        if bin == '1':
            self.series6_1 = self.series6_1 + 1
        else:
            self.series6_0 = self.series6_0 + 1
        if self.maxCount < count:
            self.maxCount = count


class StandardTests(object):

    def __init__(self, path=""):
        with open(path) as f:
            self.binStr = f.read()
            f.close()

        if len(self.binStr) < 20000:
            print(f"{bcolors.bcolors.WARNING}Długość ciągu jest za krótka{bcolors.bcolors.ENDC}")
        if len(self.binStr) > 20000:
            print(f"{bcolors.bcolors.WARNING}Długość ciągu jest za duża - pobrano początkowe 20000 znaków{bcolors.bcolors.ENDC}")
            self.binStr = self.binStr[0:20000]

        self.series1_0 = 0
        self.series2_0 = 0
        self.series3_0 = 0
        self.series4_0 = 0
        self.series5_0 = 0
        self.series6_0 = 0
        self.series1_1 = 0
        self.series2_1 = 0
        self.series3_1 = 0
        self.series4_1 = 0
        self.series5_1 = 0
        self.series6_1 = 0
        self.maxCount = 0

    def oneBitTest(self):
        if len(self.binStr) != 20000:
            print("Nie podano prawidłowego ciągu!")
            return

        oneCount = self.binStr.count("1")
        result = "TAK" if (oneCount > 9725 and oneCount < 10275) else "NIE"
        print(f"{bcolors.bcolors.OKCYAN}Test pojedynczego bitu:{bcolors.bcolors.ENDC} \nLiczba jedynek: {oneCount} \nPomyślny: {result}\n")

    def seriesTest(self):
        if len(self.binStr) != 20000:
            print("Nie podano prawidłowego ciągu!")
            return

        lastValue = ''
        count = 0

        for bin in self.binStr:
            if lastValue == '':
                lastValue = bin
                count = 1
                continue

            if bin == lastValue:
                count = count + 1
            else:
                checkCount(self, count, bin)
                count = 1
                lastValue = bin

        checkCount(self, count, lastValue)

        result = "TAK" if \
                (2315 <= self.series1_0 <= 2685 and 2315 <= self.series1_1 <= 2685
                and 1114 <= self.series2_0 <= 1386 and 1114 <= self.series2_1 <= 1386
                and 527 <= self.series3_0 <= 723 and 527 <= self.series3_1 <= 723
                and 240 <= self.series4_0 <= 384 and 240 <= self.series4_1 <= 384
                and 103 <= self.series5_0 <= 209 and 103 <= self.series5_1 <= 209
                and 103 <= self.series6_0 <= 209 and 103 <= self.series6_1 <= 209) \
                else "NIE"

        print(f"{bcolors.bcolors.OKCYAN}Test serii:{bcolors.bcolors.ENDC}")

        print("Seria 1: \t Seria 2: \t Seria 3: \t Seria 4:")
        print("0:" + str(self.series1_0) + "\t \t 0:" + str(self.series2_0) + "\t\t 0:" + str(self.series3_0) + "\t\t 0:" + str(self.series4_0))
        print("1:" + str(self.series1_1) + "\t \t 1:" + str(self.series2_1) + "\t\t 1:" + str(self.series3_1) + "\t\t 1:" + str(self.series4_1))
        print(f"Pomyślny: {result}\n")


    def longSeriesTest(self):
        if len(self.binStr) != 20000:
            print("Nie podano prawidłowego ciągu!")
            return

        count = max(self.binStr.count(26*"0"), self.binStr.count(26*"1"))
        result = "TAK" if count == 0 < 26 else "NIE"
        print(f"{bcolors.bcolors.OKCYAN}Test długiej serii:{bcolors.bcolors.ENDC} \nPomyślny: {result}\n")


    def pokerTest(self):
        if len(self.binStr) != 20000:
            print("Nie podano prawidłowego ciągu!")
            return
        print(f"{bcolors.bcolors.OKCYAN}Test pokerowy:{bcolors.bcolors.ENDC}")
        segmentsCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for val in wrap(self.binStr, 4):
            segVal = int(val, 2)
            segmentsCount[segVal] = segmentsCount[segVal] + 1
        testVal = (16 / 5000 * sum(x * x for x in segmentsCount)) - 5000

        for i in range(0, 15):
            print("Ilość wystąpień '" + bin(i)[2:].zfill(4) + "' - " + str(segmentsCount[i]))

        print("X = " + str(testVal))
        result = "TAK" if 2.16 <= testVal <= 46.17 else "NIE"
        print(f"Pomyślny: {result}\n")

