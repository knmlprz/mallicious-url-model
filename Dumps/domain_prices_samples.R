# KILKA TESTOW "NA KOLANIE"
# CENY DOMEN


# setwd('...')

prices <- read.csv('cos_dziwnego.txt',
                 header = TRUE,
                 sep = "\t")

bad_urls <- read.csv('ISCX_phishing.csv', header = FALSE)
good_urls <- read.csv('ISCX_benign.csv', header = FALSE)
malware_urls <- read.csv('ISCX_malware.csv', header = FALSE)

bad_urls_sample <- bad_urls[ round( runif(min=1, max=length(bad_urls$V1), n=20) ), ]
bad_urls_sample

good_urls_sample <- good_urls[ round( runif(min=1, max=length(good_urls$V1), n=20) ), ]
good_urls_sample

malware_urls_sample <- malware_urls[ round( runif(min=1, max=length(malware_urls$V1), n=20) ), ]
malware_urls_sample

prices[prices$TLD=='.ru',]

RegPrice <- rep(c(0), length(prices$Registration.Price))
prices1 <- prices
prices1 <- cbind(prices1, RegPrice)

for (i in c(1:length(prices$TLD))){
  prices1$RegPrice[i] <- unlist( strsplit(prices1$Registration.Price[i], '\\s') )[1]
  prices1$RegPrice[i] <- as.numeric( substring(prices1$RegPrice[i], first = 2 ) )
}


