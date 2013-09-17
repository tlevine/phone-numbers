phone.us.srs <- function() {
  paste(c('001', sample(0:9, replace = TRUE)), collapse = '')
}

#' param phone numbers (character)
#' output data frame
as.data.frame.phone.number <- function(phone.numbers) {
}

replicate(100, phone.us.srs())
