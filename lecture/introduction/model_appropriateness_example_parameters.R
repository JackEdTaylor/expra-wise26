library(tibble)
library(dplyr)
library(purrr)
library(ggplot2)
library(gganimate)
library(gifski)
theme_set(theme_classic())
set.seed(1)

# function for generating data
gen_sw <- function(n=250, amplitude=3.7, offset=0, noise_sd=1, frame_id=NULL) {
  tibble(
    # randomly sample x values from 0 to 25
    x = runif(n=n, min=0, max=25),
    # generate the perfect sine wave
    s = offset + amplitude * sin(x),
    # generate random noise of desired sd
    e = rnorm(n=n, mean=0, sd=noise_sd),
    # add the sine wave to the noise to simulate observations
    y = s + e,
    # ID for the current frame,
    frame_id = frame_id
  )
}

# animation settings
n_frames <- 60  # should be divisible by 4
fps <- 10
point_size <- 0.5
width_px <- 250
height_px <- 250
ylims <- c(-15, 15)

# amplitude example
amp_change <- 12.5
min_amp <- - amp_change
max_amp <- amp_change

amps <- c(
  seq(min_amp, max_amp, length.out=n_frames/2),
  seq(max_amp, min_amp, length.out=n_frames/2)
)

d_amp <- map_df(1:length(amps), function(i) gen_sw(amplitude=amps[[i]], frame_id=i))

pl_amp <- d_amp |>
  ggplot(aes(x, y)) +
  geom_point(size=point_size) +
  transition_manual(frame_id) +
  ylim(ylims) +
  labs(title="Effect of changing Amplitude")

anim_amp <- animate(
  pl_amp,
  renderer = gifski_renderer(),
  device = "png",
  type = "cairo",
  nframes = n_frames,
  fps = fps,
  width = width_px,
  height = height_px,
  units = "px"
)

# offset example
offset_start <- 0
offset_change <- 8
min_offset <- offset_start - offset_change
max_offset <- offset_start + offset_change

offsets <- c(
  seq(offset_start, max_offset, length.out=n_frames/4),
  seq(max_offset, min_offset, length.out=n_frames/2),
  seq(min_offset, offset_start, length.out=n_frames/4)
)

d_offset <- map_df(1:length(amps), function(i) gen_sw(offset=offsets[[i]], frame_id=i))

pl_offset <- d_offset |>
  ggplot(aes(x, y)) +
  geom_point(size=point_size) +
  transition_manual(frame_id) +
  ylim(ylims) +
  labs(title="Effect of changing Offset")

anim_offset <- animate(
  pl_offset,
  renderer = gifski_renderer(),
  device = "png",
  type = "cairo",
  nframes = n_frames,
  fps = fps,
  width = width_px,
  height = height_px,
  units = "px"
)

# noise example
min_noise <- 0
max_noise <- 4
signal_amp <- 8

noise_sds <- c(
  seq(min_noise, max_noise, length.out=n_frames/2),
  seq(max_noise, min_noise, length.out=n_frames/2)
)

d_noise <- map_df(1:length(amps), function(i) gen_sw(noise_sd=noise_sds[[i]], frame_id=i, amplitude=signal_amp))

pl_noise <- d_noise |>
  ggplot(aes(x, y)) +
  geom_point(size=point_size) +
  transition_manual(frame_id) +
  ylim(ylims) +
  labs(title="Effect of changing Noise SD")

anim_noise <- animate(
  pl_noise,
  renderer = gifski_renderer(),
  device = "png",
  type = "cairo",
  nframes = n_frames,
  fps = fps,
  width = width_px,
  height = height_px,
  units = "px"
)

# save to file
anim_save("model_appropriateness_amplitude.gif", anim_amp)
anim_save("model_appropriateness_offset.gif", anim_offset)
anim_save("model_appropriateness_noise.gif", anim_noise)
