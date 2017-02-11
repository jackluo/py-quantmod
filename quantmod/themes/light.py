from . import skeleton
from . import colors
from . import colorscales

light = dict(

    trace = dict(
        marker = dict(
            color = "444444",
        ),
        line = dict(
            color = "444444"
        )
    )

)

theme.update(light)
layout['margins'] = dict(l=0, r=4)
