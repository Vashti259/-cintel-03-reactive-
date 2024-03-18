from shiny.express import input, ui
from shinywidgets import render_altair

ui.input_selectize("var", "Vashti's reactive value", choices=["bill_length_mm", "body_mass_g"])


@render_altair
def hist():
    import altair as alt
    from palmerpenguins import load_penguins

    df = load_penguins()
    return (
        alt.Chart(df)
        .mark_bar()
        .encode(x=alt.X(f"{input.var()}:Q", bin=True), y="count()")
    )


from shiny import reactive
from shiny.express import input, render, ui

val = reactive.value(0)


@reactive.effect
@reactive.event(input.minus)
def _():
    newVal = val.get() - 1
    val.set(newVal)


@reactive.effect
@reactive.event(input.plus)
def _():
    newVal = val.get() + 1
    val.set(newVal)


with ui.sidebar():
    ui.input_action_button("minus", "-1")
    ui.input_action_button("plus", "+1")


@render.text
def value():
    return str(val.get())

