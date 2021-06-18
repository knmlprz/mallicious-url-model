# WSTEPNA ANALIZA CEN DOMEN

#setwd(...)

prices <- read.csv('cos_dziwnego.txt',
                   header = TRUE,
                   sep = "\t")
RegPrice <- rep(c(0), length(prices$Registration.Price))
prices1 <- prices
prices1 <- cbind(prices1, RegPrice)

for (i in c(1:length(prices$TLD))){
  prices1$RegPrice[i] <- unlist( strsplit(prices1$Registration.Price[i], '\\s') )[1]
  prices1$RegPrice[i] <- as.numeric( substring(prices1$RegPrice[i], first = 2 ) )
}
prices <- prices1
rm(prices1)

urls <- read.csv('out.csv',
                 header = TRUE,
                 sep = ',')
urls$dom <- paste0('.',urls$dom)

names(urls)[13] <- 'TLD'
urls_prices <- merge(x = urls, y = prices[c(1,5)], by = 'TLD',
                     all.x = TRUE)

urls_prices_good <- urls_prices[urls_prices$label=='good',]
urls_prices_bad <- urls_prices[urls_prices$label=='bad',]

urls_prices_bad$RegPrice <- as.numeric(urls_prices_bad$RegPrice)
urls_prices_good$RegPrice <- as.numeric(urls_prices_good$RegPrice)

mean(urls_prices_bad$RegPrice[!is.na(urls_prices_bad$RegPrice)])
mean(urls_prices_good$RegPrice[!is.na(urls_prices_good$RegPrice)])
length(urls_prices_bad$TLD)

par(mfrow = c(1,2))
hist(urls_prices_bad$RegPrice[!is.na(urls_prices_bad$RegPrice)],
     main = 'Bad URLs prices histogram')
hist(urls_prices_good$RegPrice[!is.na(urls_prices_good$RegPrice)],
     main = 'Good URLs prices histogram')
