image mio start = "cs/mio/mio_low.png"
image yui shocked = "cs/yui/yui_shocked.png"
image bg start = "bg/start.jpg"

# Игра начинается здесь.
label start:

    scene bg start

    with fade
    show mio start at right
    with dissolve
    mio "Привет!"


    show yui shocked at left, Shake(None, 2.0, dist=5)
    with dissolve
    yui "Ыээээ..."
    return