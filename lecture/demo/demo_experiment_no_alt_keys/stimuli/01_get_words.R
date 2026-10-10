library(parallel)
library(parabar)
library(readr)
library(dplyr)
n_cores <- parallel::detectCores() - 1

# get a dataframe of words that are present in both the Wuggy database and SUBTLEX-DE

wuggy_db <- file.path("custom_orthographic_german", "orthographic_german.txt") |>
  read_tsv(col_names = c("word", "syllables", "fpmw"))

subtlex <- read_csv("subtlex_de_cleaned.csv") |>
  mutate(
    word_len = nchar(word),
    fpmwSUBTLEX = 10**(ZipfSUBTLEX-3)
  ) |>
  filter(word %in% wuggy_db$word, spell_check_ok==1) |>
  select(word, ZipfSUBTLEX, fpmwSUBTLEX, word_len)

# save some RAM
rm(wuggy_db)
gc()

# simulate random samples, and record the average KS statistic
n_words <- 150  # how many words to select
n_iter <- 1e6  # how many random samples to try
n_chunks <- n_cores*5  # use a chunking method of parallelisation for efficiency

set.seed(1)
iter_seeds <- sample(.Machine$integer.max, n_iter)
chunk_seeds <- split(iter_seeds, ceiling(seq_along(iter_seeds)/n_chunks))

# set up parallel backend
parabar::set_option("progress_track", TRUE)
parabar::configure_bar(type = "modern", format = "[:bar] :percent (eta :eta)")

backend <- parabar::start_backend(cores=n_cores, cluster_type="psock", backend_type="async")

backend_pkg <- parabar::evaluate(backend, {
  library(overlapping)
  library(dplyr)
})

backend_obj <- parabar::export(backend, c("subtlex", "n_words"))

# check the seeds
mean_ks <- par_lapply(backend, chunk_seeds, function(chunk) {
  sapply(chunk, function(s) {
    set.seed(s)
    
    d_s <- slice_sample(subtlex, n=n_words)
    
    # calculate KS stat between sample of stimuli and uniform distribution between min and max
    ks <- c("ZipfSUBTLEX", "word_len") |>
      sapply(function(x) {
        ks.test(
          x=d_s[[x]],
          "punif",
          min = min(subtlex[[x]]),
          max = max(subtlex[[x]])
        ) |>
          with(statistic)
      })
    
    mean(ks)
  })
})

# stop the parallel sessions
parabar::stop_backend(backend)

# get the best stimulus set
draws_res <- tibble(
  seed = iter_seeds,
  mean_ks = unlist(mean_ks)
)

# the best solution is that which is closest to an idealised uniform distribution, so that we have a good spread
best_solution <- filter(draws_res, mean_ks == min(mean_ks) )

# recreate the best stimulus set
set.seed(best_solution$seed)

words <- slice_sample(subtlex, n=n_words)

# write words to file
write_csv(words, "01_words.csv")

# now get the practice words
prac_words <- subtlex |>
  filter(ZipfSUBTLEX >= 3.25, !word %in% words$word) |>
  slice_sample(n=5)

# write practice words to file
write_csv(prac_words, "01_practice_words.csv")
