'''
This was used to simulate F2 individuals
it basically makes three breakpoints by randomly choosing an individual from the .geno
Then it takes ~1/4th of their snps, and combines them to make a new individual
since it randomly selects individuals, it randomly selects populations
'''


import random
#snps = []
#snp = random.choice(snps)

individuals = []
counter = 0
numberofindivids = 10
for i in range(numberofindivids):
    with open("chr22glbsnpindividsorted.txt", 'r') as opfile:
        firstnumberOsnps = random.randint(90, 110)
        secondnumberOsnps = random.randint(90, 110)
        thirdnumberOsnps = random.randint(90, 110)
        fourthnumberOsnps = random.randint(90, 110)
        firstindex = random.randint(0, 97413) #half 194786, in fourths 97413 third 129884
        secondindex = random.randint(97414, 194826) #389652 thirds 259768, 4th
        thirdindex = random.randint(194827, 292239)
        fourthindex = random.randint(292240, 389652)
        firstrandompop = random.randint(1, 1092)
        secondrandompop = random.randint(1, 1092)
        thirdrandompop = random.randint(1, 1092)
        fourthrandompop = random.randint(1, 1092)
        counter = 0
        individualtoadd = []
        for line in opfile:
            counter += 1
            if counter >= firstindex and counter <= (firstindex + firstnumberOsnps):
                elements = line.strip().split('\t')
                individualtoadd.append(str(elements[0]) + ':' + str(elements[firstrandompop]))
            if len(individualtoadd) == firstnumberOsnps:
                break
        for line in opfile:
            counter += 1
            if counter >= secondindex and counter <= (secondindex + secondnumberOsnps):
                elements = line.strip().split('\t')
                individualtoadd.append(str((elements[0]) + ':' + str(elements[secondrandompop])))
            if len(individualtoadd) == secondnumberOsnps + firstnumberOsnps:
                break
        for line in opfile:
            counter += 1
            if counter >= thirdindex and counter <= (thirdindex + thirdnumberOsnps):
                elements = line.strip().split('\t')
                individualtoadd.append(str((elements[0]) + ':' + str(elements[thirdrandompop])))
            if len(individualtoadd) == secondnumberOsnps + firstnumberOsnps + thirdnumberOsnps:
                break
        for line in opfile:
            counter += 1
            if counter >= fourthindex and counter <= (fourthindex + fourthnumberOsnps):
                elements = line.strip().split('\t')
                individualtoadd.append(str((elements[0]) + ':' + str(elements[fourthrandompop])))
            if len(individualtoadd) == secondnumberOsnps + firstnumberOsnps + thirdnumberOsnps + fourthnumberOsnps:
                break
        individuals.append(individualtoadd)
        print("processed: " + str(len(individuals)) + " out of " + str(numberofindivids))
with open("glbtestindivids1004pop.txt", 'w') as wfile:
    for individ in individuals:
        for entry in individ:
            wfile.write(entry + '\t')
        wfile.write('\n')
