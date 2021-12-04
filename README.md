# Marifel's Portfolio and Blogging Site
My personal portfolio and blogging site, built with [Pelican](https://github.com/getpelican/pelican) using the [Pelicanyan](https://github.com/thomaswilley/pelicanyan) theme.

View the site here: https://mrbarbasa.github.io.

## Installation
Note: Pelican recommends having Python 3.6+ installed.

To install Pelican, run the following commands in your terminal:
```
python -m pip install "pelican[markdown]"
python -m pip install typogrify
```

## Usage

1. After making your changes, run the following to preview them locally:
    ```
    make clean && make devserver && open http://localhost:8000
    ```
1. Commit and push your changes up to the `src` branch. Then merge into `master` and push.
