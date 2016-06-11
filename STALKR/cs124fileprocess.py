#I basically just used this script to manipulate the data into a format I wanted to work with


with open("baseline100k4pop.txt", 'r') as opfile:
    for line in opfile:
        print (line.strip().split('\t')[0] + line.strip().split('\t')[-1])



"""
counter = 0
with open("chr22glbsnpindividsorted.txt", 'r') as opfile:
    for line in opfile:
        counter += 1
        print (line.strip().split('\t'))[:19]
        if counter == 9:
            break



counter = 0
lines = []

snpdict = {}
with open("chr22glbsnpindivid.txt", 'r') as opfile:
    for line in opfile:
        counter += 1
        if counter == 100000:
            print "Recorded 100k"
        elif counter == 200000:
            print "recorded 200k"
        elif counter == 300000:
            print "recorded 300k"
        if line.strip().split('\t')[0].isdigit() == False:
            continue
        locus = int(line.strip().split('\t')[0])
        snps = line.strip().split('\t')[1:]
        snpdict[locus] = snps

counter = 0

with open("chr22glbsnpindividsorted.txt", 'w') as wfile:
    for snp in sorted(snpdict.keys()):
        counter += 1
        wfile.write(str(snp) + '\t')
        for entry in snpdict[snp]:
            wfile.write(entry + '\t')
        wfile.write('\n')
        if counter == 100000:
            print "wrote 100k"
        elif counter == 200000:
            print "wrote 200k"
        elif counter == 300000:
            print "wrote 300k"


'''
with open('chr22glbsnpindivid.txt', 'w') as wfile:
    with open("chr22snpindivid.txt", 'r') as opfile:
        for line in opfile:
            iterate = line.strip().split('\t')
            newline = []
            newline.append(iterate[0])
            iterate = iterate[1:]
            for entry in iterate:
                parts = entry.split(':')
                country = parts[1]
                pop =''
                if country == 'GBR':
                    pop = 'EUR'
                elif country == 'FIN':
                    pop = 'EUR'
                elif country == 'CHS':
                    pop = 'ASN'
                elif country == 'PUR':
                    pop = 'AMR'
                elif country == 'CLM':
                    pop = 'AMR'
                elif country == 'IBS':
                    pop = 'EUR'
                elif country == 'CEU':
                    pop = 'EUR'
                elif country == 'YRI':
                    pop = 'AFR'
                elif country == 'CHB':
                    pop = 'ASN'
                elif country == 'JPT':
                    pop = 'ASN'
                elif country == 'LWK':
                    pop = 'AFR'
                elif country == 'ASW':
                    pop = 'AFR'
                elif country == 'MXL':
                    pop = 'AMR'
                elif country == 'TSI':
                    pop = 'EUR'
                snp = parts[0] + ':' + pop + ':' + parts[2]
                newline.append(snp)
            lines.append(newline)
    for lin in lines:
        for part in lin:
            wfile.write(part + '\t')
        wfile.write('\n')


counter = 0
snploci = []
individs = []
locs = []
individs.append("holder")
locs.append("holder")
with open("chr-22.snp", 'r') as opfile:
    for line in opfile:
        snploci.append(line.strip().split(' ')[3])
print ("snpsize w holders = " + str(len(snploci)))
with open("chr-22.ind", 'r') as opfile:
    for line in opfile:
        individs.append(line.strip().split('\t')[0])
        locs.append(line.strip().split('\t')[2].split(':')[1])
print ("individ size = " + str(len(individs)) + ":locsize" + str(len(locs)))
counter = 0
firstline = True
with open("chr22sorted.txt", 'w') as wfile:
    for individ in individs:
        wfile.write(individ + '\t')
    wfile.write('\n')
    for loc in locs:
        wfile.write(loc + '\t')
    wfile.write('\n')
    with open("chr-22.geno.csv", 'r') as opfile:
        for line in opfile:
            if firstline:
                print ("columnnums = " + str(len(line.strip().split(','))))
                firstline = False
            wfile.write(snploci[counter] + '\t')
            bins = line.strip().split(',')
            for num in bins:
                wfile.write(num + '\t')
            wfile.write('\n')
            counter += 1
print ("genolines = " + str(counter))
print ("snp size = " + str(len(snploci)))
print ("individsize = " + str(len(individs)))
"""