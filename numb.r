library(plyr)
library(rpart)
library(Deducer)

phone.us.srs <- function() {
  paste(c('001', sample(0:9, replace = TRUE)), collapse = '')
}

#' param phone numbers (character)
#' output data frame
as.data.frame.phone.number <- function(phone.numbers, response = NA) {
  df <- ldply(strsplit(phone.numbers, split = ''))
  df$V1 <- paste0(df$V1, df$V2, df$V3)
  df$V2 <- df$V3 <- NULL
  names(df) <- c('country','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10')
  if (!is.na(response)) {
    df$response <- response
  }
  df
}

test <- function() {
  n <- 100
  response <- as.logical(rbinom(n, 1, 0.3))
  numbers <- as.data.frame.phone.number(replicate(n, phone.us.srs()), response)


  fit.classify <- rpart(
    response ~ country + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10,
    method="class", data = numbers)

  numbers.count <- ddply(numbers,
    c('country','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10'), function(df) {
    c(response.count = sum(df$response))
  })


  fit.regress <- rpart(
    response.count ~ country + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10,
    method = 'anova', data = numbers.count)

  list(
    fit.classify = fit.classify,
    fit.regress = fit.regress
  )
}


bangladesh <- read.csv('Bangladesh.csv', header = FALSE, colClasses=c("character"))[,1]
responding.numbers <- as.data.frame.phone.number(bangladesh[nchar(bangladesh) == 13])
responding.numbers.counts <- ddply(responding.numbers,
      c('country','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10'), function(df) {
        c(response.count = sum(df$response))
      })
fit.regress <- rpart(
  response.count ~ country + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10,
  method = 'anova', data = responding.numbers.counts)
