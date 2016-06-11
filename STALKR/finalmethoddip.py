'''
This is essentially the same thing as the actual final method, only this assumes HWE and uses frequencies
of heterozygotes, homozygous reference and homozygous SNPs
'''
class SNP:
    def __init__(self):
        self.zerofreq = {} #each population will be a key
        self.onefreq = {} #the value will be the frequency in that population
        self.heterofreq = {}

snpdict = {} #make a dictionary of snps, wherein the locus is the key

with open("chr22glbsnpfreqs.txt", 'r') as opfile:
    for line in opfile:
        locus = line.strip().split('\t')[0]
        snpinfo = line.strip().split('\t')[1:]
        snpdict[locus] = SNP()
        for info in snpinfo:
            zerof = float(info.split(':')[2])
            heterof = float(info.split(':')[4])
            onef = float(info.split(':')[6])
            pop = info.split(':')[0]
            snpdict[locus].zerofreq[pop] = zerof
            snpdict[locus].heterofreq[pop] = heterof
            snpdict[locus].onefreq[pop] = onef

individuals = []

with open("glbtestindivids4080.txt", 'r') as opfile:
    for line in opfile:
        individual = []
        allsnps = line.strip().split('\t')
        for snp in allsnps:
            individual.append((snp.split(':')[0], snp.split(':')[3], snp.split(':')[2]))
        individuals.append(individual)

def getprob(locus, pop, status):
    prob = 1
    if status == 'homo1':
        prob *= snpdict[locus].onefreq[pop]
    elif status == 'homo0':
        prob *= snpdict[locus].zerofreq[pop]
    else:
        prob *= snpdict[locus].heterofreq[pop]
    return prob


def guess(individual):
    individualsnps = {}
    pops = ['AFR', 'AMR', 'ASN', 'EUR']
    initprobs = []
    initamount = 7
    initialize = individual[:initamount]
    initasn, initamr, initafr, initeur = 1.000, 1.000, 1.000, 1.000
    for snp in initialize: #snp[1] is population, snp[0] is locus
        locus = snp[0]
        status = snp[1]
        initafr *= getprob(locus, 'AFR', status)
        initamr *= getprob(locus, 'AMR', status)
        initasn *= getprob(locus, 'ASN', status)
        initeur *= getprob(locus, 'EUR', status)
    initprobs.append(initafr)
    initprobs.append(initamr)
    initprobs.append(initasn)
    initprobs.append(initeur)
    state = pops[initprobs.index(max(initprobs))]
    guessind = [(x[0], state) for x in individual[:initamount]]
    clustersize = 3
    index = initamount
    while len(guessind) < len(individual):
        if index+clustersize > len(individual):
            tempclustersize = clustersize
            while (index+tempclustersize) > len(individual):
                tempclustersize -= 1
            clustersize = tempclustersize
        snpstocheck = individual[index:index+clustersize]
        asn, amr, afr, eur = 1.000, 1.000, 1.000, 1.000
        popprobs = []
        for snp in snpstocheck:
            locus = snp[0]
            status = snp[1]
            afr *= getprob(locus, 'AFR', status)
            amr *= getprob(locus, 'AMR', status)
            asn *= getprob(locus, 'ASN', status)
            eur *= getprob(locus, 'EUR', status)
        popprobs.append(afr)
        popprobs.append(amr)
        popprobs.append(asn)
        popprobs.append(eur)
        transprobs = []
        for i in range(len(popprobs)):
            if i == pops.index(state):
                transprobs.append(popprobs[i])
            else:
                transprobs.append(popprobs[i] * .01)
        #transprobs = [x * .01 if popprobs.index(x) != pops.index(state) else x for x in popprobs]
        #this list comprehension didn't work in cases where there were two maximum equal probabilities
        #in popprobs, so it would return the first index of the max, eg if asn was current state, but
        #asn and amr had the same probabilities, it would return the index of amr
        #statechange = state
        #(popprobs.index(max(popprobs)) != pops.index(state)) and  and popprobs[popprobs.index(max(popprobs))] != popprobs[pops.index(state)]:
        if max(popprobs) == 1.0 and popprobs[pops.index(state)] != 1.0:
            state = pops[popprobs.index(max(popprobs))]
        else:
            state = pops[transprobs.index(max(transprobs))]
        #if state != statechange:
         #   if transprobs[pops.index(state)] != transprobs[pops.index(statechange)]:
          #      state = statechange
        for snp in snpstocheck:
            guessind.append((snp[0], state))
        index += clustersize
    return guessind

guessindividuals = [guess(x) for x in individuals]

percentcorrect = []

for i in range(len(guessindividuals)):
    numcorrect = 0.0000
    for k in range(len(guessindividuals[i])):
        guesspop = guessindividuals[i][k][1]
        actpop = individuals[i][k][2]
        if guessindividuals[i][k][1] == individuals[i][k][2]:
            numcorrect += 1.0000
    percentcorrect.append(str(100*(numcorrect / float(len(guessindividuals[i])))))

with open("guesstestdips4080.txt", 'w') as wfile:
    for i in range(len(guessindividuals)):
        for snp in guessindividuals[i]:
            wfile.write(snp[0] + ':' + snp[1] + '\t')
        wfile.write(percentcorrect[i] + '%')
        wfile.write('\n')
    avg = 0.000
    for porcentaje in percentcorrect:
        avg += float(porcentaje)
    wfile.write('average' + str(float(avg / float(len(guessindividuals)))) + '%')


