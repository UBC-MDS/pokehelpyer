library(tidyverse)
library(latex2exp)

alpha <- 3/4
beta <- 3/2

dat = tibble(
  delta = seq(-8, 8),
  y_pos = delta^alpha,
  y_neg = -(-delta)^beta
)
head(dat, 20)

type_advantage_plot <- ggplot(dat, aes(x = delta)) + 
  geom_point(aes(y = y_neg), color = 'blue', size = 2.5) +
  geom_line(aes(y = y_neg), lwd = 0.8) +
  geom_point(aes(y = y_pos), color = 'red', size = 2.5) +
  geom_line(aes(y = y_pos), lwd = 0.8) +
  geom_vline(xintercept = 0) +
  geom_hline(yintercept = 0) +
  scale_x_continuous(n.breaks = 18) +
  scale_y_continuous(n.breaks = 18) +
  ggtitle("Type-Advantage Function") +
  labs(
    x = TeX(r"($ \overset{\delta_{type}}{(\phantom{.}_{=\ resistance_{type}\ -\ weakness_{type}\ })} $)"),
    y = "Type-Advantage"
  ) +
  theme_bw(base_size = 14) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    axis.title = element_text(size = 15),
    axis.text.x = element_text(size = 13),
    axis.text.y = element_text(size = 13)
  )

type_advantage_plot

