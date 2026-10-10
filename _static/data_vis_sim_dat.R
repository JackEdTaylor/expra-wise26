library(dplyr)
library(readr)

set.seed(1)

n_subj <- 67

subj_intercepts <- tibble(
  subj_id = sprintf("s%02d", 1:n_subj),
  subj_intercept = rnorm(n_subj, 0, 7.5)
)

d <- tibble(
  subj_id = rep(sprintf("s%02d", 1:n_subj), 3),
  time = rep(c("morning", "midday", "evening"), each=n_subj),
  time_morn_dum = ifelse(time == "morning", 1, 0),
  time_eve_dum = ifelse(time == "evening", 1, 0),
) |>
  left_join(subj_intercepts, by="subj_id") |>
  mutate(
    read_score = 100 + time_morn_dum * -23 + time_eve_dum * -6 + subj_intercept + rnorm(n(), 0, 2.5),
    memory_score = (read_score - 100) * case_when(
      time == "morning" ~ 1.2,
      time == "midday" ~ 0,
      time == "evening" ~ 0.24
    ) + rnorm(n_subj, 0, 10) + 100
  ) |>
  select(-ends_with("dum"), -subj_intercept) |>
  mutate(
    read_score = round(read_score + rt(n(), 2, 0), 2),
    memory_score = round(memory_score + rt(n(), 2, 0), 2)
  ) |>
  arrange(subj_id)

write_csv(d, "data_vis_dat.csv")
