from plotnine import theme, element_blank, element_line, element_rect, element_text

# from plotnine.scales.scale_discrete import scale_discrete
from mizani.palettes import manual_pal

from .theme_foundation import theme_foundation

# ggthemes_data
THEME_DATA = {
    "Dark Gray": "#3C3C3C",
    "Medium Gray": "#D2D2D2",
    "Light Gray": "#F0F0F0",
    "Red": "#FF2700",
    "Blue": "#008FD5",
    "Green": "#77AB43",
}


def theme_fivethirtyeight(base_size=12, base_family="sans") -> theme:
    colors = THEME_DATA
    new_theme = theme_foundation(base_size=base_size, base_family=base_family) + theme(
        line=element_line(colour="black"),
        rect=element_rect(
            fill=colors["Light Gray"],
            linetype=0,
            colour=None,
        ),
        text=element_text(colour=colors["Dark Gray"]),
        axis_title=element_blank(),
        axis_text=element_text(),
        axis_ticks=element_blank(),
        axis_line=element_blank(),
        legend_background=element_rect(),
        legend_position="bottom",
        legend_direction="horizontal",
        legend_box="vertical",
        panel_grid=element_line(colour=None),
        panel_grid_major=element_line(colour=colors["Medium Gray"]),
        panel_grid_minor=element_blank(),
        plot_title=element_text(hjust=0, size=1.5, face="bold"),
        plot_margin=element_blank(),
        strip_background=element_rect(),
    )

    return new_theme


def fivethirtyeight_pal() -> manual_pal:
    """FiveThirtyEight color palette
    The standard three-color FiveThirtyEight palette for line plots comprises
    blue, red, and green.
    """

    colors = THEME_DATA
    values = [colors["Blue"], colors["Red"], colors["Green"]]
    f = manual_pal(values)
    # TODO: the R program sets a max_n attr, then checks it with check_pal_n
    # max_n = len(values)
    # f.max_n = max_n

    return f


def scale_color_fivethirtyeight(*args, **kwargs):
    """Color scales using the colors in the FiveThirtyEight graphics."""
    # TODO: how to do this?
    # https://github.com/jrnold/ggthemes/blob/main/R/fivethirtyeight.R#L65
    # return scale_discrete(palette=fivethirtyeight_pal(), *args, **kwargs)
