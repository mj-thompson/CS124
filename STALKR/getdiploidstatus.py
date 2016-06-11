'''This was used to generate the frequencies of heterozygotes and homozygotes
it didn't work as well because people are not in HWE'''



class SNP:
    def __init__(self):
        self.individs = []
snpdict = {}
individheader = []
popheader = []
gotheaders = False
with open("chr22sorted.txt", 'r') as opfile:
    counter = 0
    for line in opfile:
        if not gotheaders:
            if counter == 0:
                individheader = line.strip().split('\t')
            if counter == 1:
                popheader = line.strip().split('\t')
                gotheaders = True
            counter += 1
        if gotheaders:
            iterate = line.strip().split('\t')
            locus = iterate[0]
            snpdict[locus] = []
            status = ""
            for i in range(1, len(iterate)):
                status += iterate[i]
                if i % 2 != 0:
                    individ = individheader[i]
                    pop = popheader[i]
                    dip = ''
                    if status == '00':
                        dip = "homo0"
                    elif status == '11':
                        dip = "homo1"
                    else:
                        dip = "hetero"
                    snpdict[locus].append((individ, pop, dip))
                    status = ""
with open("chr22snpindivid.txt", 'w') as wfile:
    for snp in snpdict.keys():
        wfile.write(str(snp) + '\t')
        for individ in snpdict[snp]:
            wfile.write(str(individ[0]) + ':' + str(individ[1]) + ':' + str(individ[2]) + '\t')
        wfile.write('\n')

counter = 0
with open("chr22snpindivid.txt", 'r') as opfile:
    for line in opfile:
        print (line.strip().split('\t')[:12])
        counter += 1
        if counter == 5:
            break


snpdict = {}

class SNPdip:
    def __init__(self):
        self.AFR = [0.0000, 0.0000, 0.0000]
        self.AMR = [0.0000, 0.0000, 0.0000]
        self.ASN = [0.0000, 0.0000, 0.0000]
        self.EUR = [0.0000, 0.0000, 0.0000]


with open("chr22glbsnpindivid.txt", 'r') as opfile:
    for line in opfile:
        iterate = line.strip().split('\t')
        locus = iterate[0]
        inds = iterate[1:]
        snpdict[locus] = SNPdip()
        for ind in inds:
            pop = ind.split(':')[1]
            dip = ind.split(':')[2]
            if pop == 'AFR':
                if dip == 'homo0':
                    snpdict[locus].AFR[0] += 1.0000
                elif dip == 'homo1':
                    snpdict[locus].AFR[2] += 1.0000
                else:
                    snpdict[locus].AFR[1] += 1.0000
            elif pop == 'AMR':
                if dip == 'homo0':
                    snpdict[locus].AMR[0] += 1.0000
                elif dip == 'homo1':
                    snpdict[locus].AMR[2] += 1.0000
                else:
                    snpdict[locus].AMR[1] += 1.0000
            elif pop == 'ASN':
                if dip == 'homo0':
                    snpdict[locus].ASN[0] += 1.0000
                elif dip == 'homo1':
                    snpdict[locus].ASN[2] += 1.0000
                else:
                    snpdict[locus].ASN[1] += 1.0000
            elif pop == 'EUR':
                if dip == 'homo0':
                    snpdict[locus].EUR[0] += 1.0000
                elif dip == 'homo1':
                    snpdict[locus].EUR[2] += 1.0000
                else:
                    snpdict[locus].EUR[1] += 1.0000


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

eur = float(eur/2.0000)
afr = float(afr/2.0000)
asn = float(asn/2.0000)
amr = float(amr/2.0000)


with open("chr22glbdipfreqs.txt", 'w') as wfile:
    for key in snpdict.keys():
        wfile.write(str(key) + '\t' + "AFR:00:" + str(float(snpdict[key].AFR[0]) / float(afr)) + ":H:" + str(float(snpdict[key].AFR[1]) / float(afr)) + ":11:" + str(float(snpdict[key].AFR[2]) / float(afr)) + '\t'
                    + "ASN:00:" + str(float(snpdict[key].ASN[0]) / float(asn)) + ":H:" + str(float(snpdict[key].ASN[1]) / float(asn)) + ":11:" + str(
            float(snpdict[key].ASN[2]) / float(asn)) + '\t'
                    + "AMR:00:" + str(float(snpdict[key].AMR[0]) / float(amr)) + ":H:" + str(float(snpdict[key].AMR[1]) / float(amr)) + ":11:" + str(
            float(snpdict[key].AMR[2]) / float(amr)) + '\t'
                    + "EUR:00:" + str(float(snpdict[key].EUR[0]) / float(eur)) + ":H:" + str(
            float(snpdict[key].EUR[1]) / float(eur)) + ":11:" + str(
            float(snpdict[key].EUR[2]) / float(eur)) + '\t')
        wfile.write('\n')
