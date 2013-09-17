library(plyr)

phone.us.srs <- function() {
  paste(c('001', sample(0:9, replace = TRUE)), collapse = '')
}

#' param phone numbers (character)
#' output data frame
as.data.frame.phone.number <- function(phone.numbers, response) {
  df <- ldply(strsplit(phone.numbers, split = ''))
  df$V1 <- paste0(df$V1, df$V2, df$V3)
  df$V2 <- df$V3 <- NULL
  names(df) <- c('country','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10')
  df$response <- response
  df
}

n <- 100
response <- as.logical(rbinom(n, 1, 0.3))
numbers <- as.data.frame.phone.number(replicate(n, phone.us.srs()), response)
