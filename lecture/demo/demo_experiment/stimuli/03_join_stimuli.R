library(readr)
library(dplyr)
library(tidyr)
set.seed(1)

words <- read_csv("01_words.csv")
candidate_pseudowords <- read_csv("02_pseudowords.csv")
prac_words <- read_csv("01_practice_words.csv")
candidate_prac_pseudowords <- read_csv("02_practice_pseudowords.csv")
subtlex <- read_csv("subtlex_de_cleaned.csv")

# randomly select pseudowords, and then join to the words data
stim_wide <- candidate_pseudowords |>
  filter(!pseudoword %in% subtlex$word) |>
  group_by(word) |>
  slice_sample(n = 1) |>
  ungroup() |>
  rename_with(function(x) sprintf("pseudoword_%s", x), -c("word", "segments", "pseudoword")) |>
  full_join(words, by="word") |>
  rename(
    word_ZipfSUBTLEX = ZipfSUBTLEX,
    word_fpmwSUBTLEX = fpmwSUBTLEX
  ) |>
  mutate(item_nr = row_number()) |>
  select(
    item_nr, word, pseudoword,
    starts_with("word"),
    starts_with("pseudoword")
  )

# also get in long format with
stim_long <- stim_wide |>
  select(item_nr, word, pseudoword) |>
  pivot_longer(c("word", "pseudoword"), names_to="condition", values_to="text") |>
  mutate(
    corr_ans = ifelse(condition=="word", "ralt", "lalt"),
    is_practice_trial = FALSE
  )

# write to file
write_csv(stim_wide, "stim_wide.csv")
write_csv(stim_long, "stim_long.csv")

# now also do the practice trials
prac_stim_wide <- candidate_prac_pseudowords |>
  filter(!pseudoword %in% subtlex$word) |>
  group_by(word) |>
  slice_sample(n = 1) |>
  ungroup() |>
  rename_with(function(x) sprintf("pseudoword_%s", x), -c("word", "segments", "pseudoword")) |>
  full_join(prac_words, by="word") |>
  rename(
    word_ZipfSUBTLEX = ZipfSUBTLEX,
    word_fpmwSUBTLEX = fpmwSUBTLEX
  ) |>
  mutate(item_nr = row_number()) |>
  select(
    item_nr, word, pseudoword,
    starts_with("word"),
    starts_with("pseudoword")
  )

# also get in long format with
prac_stim_long <- prac_stim_wide |>
  select(item_nr, word, pseudoword) |>
  pivot_longer(c("word", "pseudoword"), names_to="condition", values_to="text") |>
  mutate(
    corr_ans = ifelse(condition=="word", "ralt", "lalt"),
    is_practice_trial = TRUE
  )

# write to file
write_csv(prac_stim_wide, "practice_stim_wide.csv")
write_csv(prac_stim_long, "practice_stim_long.csv")
