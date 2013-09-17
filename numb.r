phone.us.srs <- function() {
  paste(c('001', sample(0:9, replace = TRUE)), collapse = '')
}

#' param phone numbers (character)
#' output data frame
as.data.frame.phone.number <- function(phone.numbers) {
  df <- dply(strsplit(phone.numbers, split = ''))
  names(df) <- c('country','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','response')
}

replicate(100, phone.us.srs())
