library(readr)    # for reading the data into R
library(purrr)    # for easily importing multiple files
library(dplyr)    # for wrangling data (e.g., adding/renaming columns)
library(afex)     # for fitting a repeated measures anova
library(emmeans)  # for summarising factorial cells

library(ggplot2)  # for visualising data

# load the demographics
demog <- read_csv("demo_demog.csv")

# load stimuli
stim <- read_csv("demo_stimuli.csv")

# import all trials
data_paths <- list.files("trials", full.names=TRUE)

raw_data_separate <- lapply(data_paths, read_csv)

raw_data <- list_rbind(raw_data_separate)

# join demographics to raw data
all_dat <- raw_data |>
  left_join(demog) |>
  left_join(stim)

# calculate the accuracy for each trial
all_dat <- mutate(all_dat, accuracy = as.numeric(response == correct_response))

participant_avg <- all_dat |>
  filter(phase == "main") |>
  group_by(participant_id) |>
  summarise(mean_acc = mean(accuracy)) |>
  ungroup()

# only keep participants with accuracy higher than 75%
okay_participants <- participant_avg |>
  filter(mean_acc > 0.75) |>
  pull(participant_id)

trials_clean <- all_dat |>
  filter(
    # exclude fast responses
    rt_ms >= 100,
    # exclude slow responses
    rt_ms < 2500,
    # accuracy exclusion
    accuracy == 1,
    # exclude participants with low accuracy
    participant_id %in% okay_participants,
    # keep main trials (exclude pracice trials)
    phase == "main"
  )

# number of trials lost to cleaning
nrow(all_dat) - nrow(trials_clean)

# get a clean copy of the demographics
demog_clean <- filter(demog, participant_id %in% okay_participants)

# number of males and females
count(demog_clean, participant_gender)

# summarise ages
summarise(
  demog_clean,
  mean_age = mean(participant_age),
  sd_age = sd(participant_age)
)

# hemifield * lexicality effect

participant_avgs <- trials_clean |>
  group_by(participant_id, side, lexicality) |>
  summarise(median_rt = median(rt_ms)) |>
  ungroup()

anova_hemi_lex <- aov_4(median_rt ~ 1 + (lexicality * side | participant_id), data=participant_avgs)

emmeans(anova_hemi_lex, ~ side)

emmeans(anova_hemi_lex, ~ lexicality)

emmeans(anova_hemi_lex, ~ lexicality * side)

# plot the effects
participant_avgs |>
  ggplot(aes(x=side, y=median_rt, fill=lexicality)) +
  geom_boxplot()

