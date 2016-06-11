'''
So this generated the file to hold the MAF and reference frequencies, to be later used when running the method
'''

#save secondline as header
#count from 1
#so i looks over the zeroes and ones, also correctly
#corresponds to its population
#maybe try freq out of population... so look at frequency in its specific population rather than out
#of the entire data seteg 200, 194, 132 instead of 2184
totalchroms = 2184

class SNP:
    def __init__(self):
        self.ASN = 0.0000
        self.EUR = 0.0000
        self.AMR = 0.0000
        self.AFR = 0.0000

snpdict = {}

locindex = []
counter = 0
gotheaders = False
with open("chr22glbsorted.txt", 'r') as opfile:
    for line in opfile:
        if not gotheaders:
            if counter == 1:
                locindex = line.strip().split('\t')
                gotheaders = True
            counter += 1
        else:
            iterate = line.strip().split('\t')
            locus = iterate[0]
            snpdict[locus] = SNP()
            for i in range(len(iterate)):
                if iterate[i] == '0':
                    if locindex[i] == 'EUR':
                        snpdict[locus].EUR += 1.0000
                    if locindex[i] == 'AFR':
                        snpdict[locus].AFR += 1.0000
                    if locindex[i] == 'AMR':
                        snpdict[locus].AMR += 1.0000
                    if locindex[i] == 'ASN':
                        snpdict[locus].ASN += 1.0000

eur, afr, amr, asn = 0.0000, 0.0000, 0.0000, 0.0000
with open("chr-22.ind", 'r') as opfile:
    for line in opfile:
        pop = line.strip().split('\t')[2].split(':')[1]
        if pop == 'EUR':
            eur += 1.0000
        elif pop =='ASN':
            asn += 1.0000
        elif pop == 'AFR':
            afr += 1.0000
        elif pop == 'AMR':
            amr += 1.0000



with open("chr22glbsnpfreqs.txt", 'w') as wfile:
    for key in snpdict.keys():
        wfile.write(str(key) + '\t' + "EUR:" + str(snpdict[key].EUR) + ":0:" + str(float(snpdict[key].EUR)/float(eur)) + ":1:" + str(1.0000 - float(snpdict[key].EUR)/float(eur)) + '\t'
        + "ASN:" + str(snpdict[key].ASN) + ":0:" + str(
            float(snpdict[key].ASN) / float(asn)) + ":1:" + str(1.0000 - float(snpdict[key].ASN) / float(asn)) + '\t'
        + "AMR:" + str(snpdict[key].AMR) + ":0:" + str(
            float(snpdict[key].AMR) / float(amr)) + ":1:" + str(1.0000 - float(snpdict[key].AMR) / float(amr)) + '\t'
        + "AFR:" + str(snpdict[key].AFR) + ":0:" + str(
            float(snpdict[key].AFR) / float(afr)) + ":1:" + str(1.0000 - float(snpdict[key].AFR) / float(afr)) + '\t')
        wfile.write('\n')

