class SNP:
    def __init__(self):
        self.zerofreq = {} #each population will be a key
        self.onefreq = {} #the value will be the frequency in that population

snpdict = {} #make a dictionary of snps, wherein the locus is the key

with open("chr22glbsnpfreqs.txt", 'r') as opfile:
    for line in opfile:
        locus = line.strip().split('\t')[0]
        snpinfo = line.strip().split('\t')[1:]
        snpdict[locus] = SNP()
        for info in snpinfo:
            zerof = float(info.split(':')[3])
            onef = float(info.split(':')[5])
            pop = info.split(':')[0]
            snpdict[locus].zerofreq[pop] = zerof #hold frequencies for the MAF and reference allele
            snpdict[locus].onefreq[pop] = onef

individuals = []

with open("glbtestindivids100k4pop.txt", 'r') as opfile:
    for line in opfile:
        individual = []
        allsnps = line.strip().split('\t')
        for snp in allsnps:
            individual.append((snp.split(':')[0], snp.split(':')[3], snp.split(':')[2]))
        individuals.append(individual)

#return the probabilities of the status at that locus
def getprob(locus, pop, status):
    prob = 1
    if status == 'homo1':
        prob *= snpdict[locus].onefreq[pop] ** 2
    elif status == 'homo0':
        prob *= snpdict[locus].zerofreq[pop] ** 2
    else:
        prob *= snpdict[locus].zerofreq[pop] * snpdict[locus].onefreq[pop]
    return prob

'''
The base line just looks at each SNP individually
It looks at which population is most likely to be a heterozygote, homozygous reference or homozygous SNP
at each locus, and calls that population for that SNP based on the highest likelihood
'''
def guess(individual):
    individualsnps = {}
    pops = ['AFR', 'AMR', 'ASN', 'EUR']
    guessind = []
    asn, amr, afr, eur = 1.000, 1.000, 1.000, 1.000
    for snp in individual: #snp[1] is population, snp[0] is locus
        probs = []
        locus = snp[0]
        status = snp[1]
        afr *= getprob(locus, 'AFR', status)
        amr *= getprob(locus, 'AMR', status)
        asn *= getprob(locus, 'ASN', status)
        eur *= getprob(locus, 'EUR', status)
        probs.append(afr)
        probs.append(amr)
        probs.append(asn)
        probs.append(eur)
        state = pops[probs.index(max(probs))]
        guessind.append((str(snp[0]), state))
    return guessind

guessindividuals = [guess(x) for x in individuals]
#generate percent correct

percentcorrect = []

#this line just calculates the correctedness of our guess individual
for i in range(len(guessindividuals)):
    numcorrect = 0.0000
    for k in range(len(guessindividuals[i])):
        guesspop = guessindividuals[i][k][1]
        actpop = individuals[i][k][2]
        if guessindividuals[i][k][1] == individuals[i][k][2]:
            numcorrect += 1.0000
    percentcorrect.append(str(100*(numcorrect / float(len(guessindividuals[i])))))


#write the output to a file, and calcuilate the average on the last line
with open("baseline100k4pop.txt", 'w') as wfile:
    for i in range(len(guessindividuals)):
        for snp in guessindividuals[i]:
            wfile.write(snp[0] + ':' + snp[1] + '\t')
        wfile.write(percentcorrect[i] + '%')
        wfile.write('\n')
    avg = 0.000
    for porcentaje in percentcorrect:
        avg += float(porcentaje)
    wfile.write('average' + str(float(avg / float(len(guessindividuals)))) + '%')

