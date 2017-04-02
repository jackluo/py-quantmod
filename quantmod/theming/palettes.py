"""RGBA color palettes

Used to dynamically link to theme colors rather than rely on hardcoding
of greyscale traces.

For readability, files under theming do not follow PEP8 guideline of
no space between assignment of named arguments.

"""
# flake8: noqa

# Palette for lighter themes
LIGHT_PALETTE = dict(
    white = '#FFFFFF',
    black = '#000000',
    transparent = 'rgba(0, 0, 0, 0.00)',
    grey02 = 'rgba(0, 0, 0, 0.02)',
    grey05 = 'rgba(0, 0, 0, 0.05)',
    grey10 = 'rgba(0, 0, 0, 0.10)',
    grey15 = 'rgba(0, 0, 0, 0.15)',
    grey20 = 'rgba(0, 0, 0, 0.20)',
    grey25 = 'rgba(0, 0, 0, 0.25)',
    grey30 = 'rgba(0, 0, 0, 0.30)',
    grey35 = 'rgba(0, 0, 0, 0.35)',
    grey40 = 'rgba(0, 0, 0, 0.40)',
    grey45 = 'rgba(0, 0, 0, 0.45)',
    grey50 = 'rgba(0, 0, 0, 0.50)',
    grey55 = 'rgba(0, 0, 0, 0.55)',
    grey60 = 'rgba(0, 0, 0, 0.60)',
    grey65 = 'rgba(0, 0, 0, 0.65)',
    grey70 = 'rgba(0, 0, 0, 0.70)',
    grey75 = 'rgba(0, 0, 0, 0.75)',
    grey80 = 'rgba(0, 0, 0, 0.80)',
    grey85 = 'rgba(0, 0, 0, 0.85)',
    grey90 = 'rgba(0, 0, 0, 0.90)',
    grey95 = 'rgba(0, 0, 0, 0.95)',
    grey98 = 'rgba(0, 0, 0, 0.98)',
)


# Palette for darker themes
DARK_PALETTE = dict(
    white = '#FFFFFF',
    black = '#000000',
    transparent = 'rgba(255, 255, 255, 0.00)',
    grey02 = 'rgba(255, 255, 255, 0.98)',
    grey05 = 'rgba(255, 255, 255, 0.95)',
    grey10 = 'rgba(255, 255, 255, 0.90)',
    grey15 = 'rgba(255, 255, 255, 0.85)',
    grey20 = 'rgba(255, 255, 255, 0.80)',
    grey25 = 'rgba(255, 255, 255, 0.75)',
    grey30 = 'rgba(255, 255, 255, 0.70)',
    grey35 = 'rgba(255, 255, 255, 0.65)',
    grey40 = 'rgba(255, 255, 255, 0.60)',
    grey45 = 'rgba(255, 255, 255, 0.55)',
    grey50 = 'rgba(255, 255, 255, 0.50)',
    grey55 = 'rgba(255, 255, 255, 0.45)',
    grey60 = 'rgba(255, 255, 255, 0.40)',
    grey65 = 'rgba(255, 255, 255, 0.35)',
    grey70 = 'rgba(255, 255, 255, 0.30)',
    grey75 = 'rgba(255, 255, 255, 0.25)',
    grey80 = 'rgba(255, 255, 255, 0.20)',
    grey85 = 'rgba(255, 255, 255, 0.15)',
    grey90 = 'rgba(255, 255, 255, 0.10)',
    grey95 = 'rgba(255, 255, 255, 0.05)',
    grey98 = 'rgba(255, 255, 255, 0.02)',
)
