from plotnine.themes.elements.element_base import element_base
from plotnine import theme, theme_grey, element_rect, element_line, element_text


def theme_foundation(base_size=12, base_family=""):
    thm = theme_grey(base_size=base_size, base_family=base_family)
    for name, entry in thm.themeables.items():
        if not isinstance(entry.theme_element, element_base):
            continue

        props = entry.theme_element.properties
        if "color" in props:
            props["color"] = None
        if "fill" in props:
            props["fill"] = None
    return thm + theme(
        panel_border=element_rect(fill=None),
        legend_background=element_rect(colour=None),
        line=element_line(colour="black"),
        rect=element_rect(fill="white", colour="black"),
        text=element_text(colour="black"),
    )
