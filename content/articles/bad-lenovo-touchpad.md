Title: Soft-fixing Lenovo touchpad
lang: en
Category: Linux
Tags: hardware, planet-inuits
Slug: lenovo-touchpad

I have a new lenovo laptop but it has no physical button (the whole touchpad is
a button). It is almost impossible to right click and impossible to
middle-click, which is critical for me.

I solved this with the following `synclient` options:


    :::bash
    synclient TapButton1=1
    synclient TapButton2=2
    synclient TapButton3=3

When I click the touch pad with one finger, it will left-click, two will
middle-click and three will left-click.
