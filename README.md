# Plotnine CLI

This is a small wrapper around the [plotnine](https://plotnine.org/) library for creating ggplots from the command line. 

## Installation

`pip3 install .`

## Examples

Save as png:

`p9 plot 'ggplot(mtcars, aes("wt", "mpg"))+ geom_point()' > cars.png`

![test](https://github.com/natefduncan/p9cli/assets/30030731/f3965e25-c476-41d4-99a1-f9f2123f4830)

Display in command line:

`p9 plot 'ggplot(mtcars, aes("wt", "mpg"))+ geom_point()' | timg -p kitty -`

CSV or JSON data from stdin:

`cat data.csv | p9 plot 'ggplot(df, ...)`
