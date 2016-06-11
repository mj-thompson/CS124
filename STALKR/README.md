# STALKR
Sectioned, Transitioned Ancestry-mapping, Locally, of Know Regions

STALKR is a really quick, implementation to local of ancestry mapping of known populations. For CS124, this was final project number 4 on medium difficulty. The project came out to be pretty time intensive, and I didn't get it to work how I had originally intended, but I'm happy with the results.

## How it works
STALKR basically reads in all of the frequencies of SNPs per population. It then initializes the individual by examining a few hundred of their SNPs at once, and using the maximum likelihood of the population that would give those SNPs. After itializing an individual, STALKR examines SNPs in smaller clusters of about ~25 at a time. STALKR also incorporates transition probabilities. This helps lower the chance of switching to a different population, since breakpoints aren't very common. I tested STALKR on 10 simulated F2 individuals, and scored STALKR based on its average % correct SNP guesses per ten individuals. STALKR does better as individuals increase in size, and there are more data and SNPs available to examine. I used chromosome 22, but would likely score a bit better than 87% accuracy on a longer chromosome.

## Generation of test data
This was an interesting thing to simulate. I basically decided to generate 3 breakpoints per individual, at random indices in the genome, using a pseudo-random number generator to select breakpoints around 1/4th the length of the chromosome. This provided 4 populations per individual, and the populations were also pseudo-randomly selected (implications here are that there could technically be breakpoints from individuals of the same population. Regardless, this still changes the DNA from one individual to another after a breakpoint is crossed) The output was 10 individuals, each who had around 3/4 of their DNA from a different individual. This may not be entirely biologically accurate, but this allows us to test STALKRs ability to transition between probabilities, and to still maintain accuracy when dealing with non-homogenous individuals.

## Conclusions
STALKR does really well, scoring around 87% when using the entire chromosome. If I were to spend more time solving this problem, I'd choose to use a Hidden Markov Model, along with Sparse PCA. I would use these, examining each SNP individually rather than as a cluster. The reason I didn't implement HMM was I couldn't really establish some of the auxiliary probabilities to be used. I used a constant transition probability, but I wasn't sure if it might make sense to increase or decrease the probability based on relatedness, eg if Americans were similar to Asians, they'd have a higher transition probability than Americans to Africans, as Americans more recently migrated from Asia than they did Africa. I haven't used PCA very much, but I would have liked to have a Sparse PCA analysis to try and use the most distinguishing SNPs when evaluating ancestry. Anyways, STALKR is very fast, and quite accurate. It took maybe a couple seconds to actually run the algorithm once the data (SNP frequencies) was read.



#### Updates
*April 28, I decided to do ancestry mapping*
*May 5, Zar recommended using thousand genomes project data*
*May 12, I got the data for chormmosome 22*
*May 19, I've come out with some general ideas for the algorithm*
*May 26, I've started to process the data, and am deciding what* 
*to use and which algorith I should implement, I'm thinking of using HMM*
*June 2, I've implemented the baseline, but HMM is somewhat of a mess*
*June 9, I've finished my implementation, I used a different method,* 
*that borrowed the idea of transition probabilities from HMM*
