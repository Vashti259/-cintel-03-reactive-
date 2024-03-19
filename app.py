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



import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly

ui.page_opts(title="Vashti's Unique App", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")


from shiny.express import ui

with ui.sidebar(bg="#f8f8f8"):
    "Sidebar"

"Penguin content"

from palmerpenguins import load_penguins
from shiny import render
from shiny.express import ui

penguins = load_penguins()

ui.h2(" Data Grid")


@render.data_frame
def penguins_df():
    return render.DataGrid(penguins)


import seaborn as sns
from palmerpenguins import load_penguins
from shiny import render
from shiny.express import input, ui

penguins = load_penguins()

ui.input_slider("n", "Number of bins", 1, 100, 20)


@render.plot(alt="A Seaborn histogram on penguin body mass in grams.")
def plot():
    ax = sns.histplot(data=penguins, x="body_mass_g", bins=input.n())
    ax.set_title("Seaborn Penguins")
    ax.set_xlabel("Mass (g)")
    ax.set_ylabel("Count")
    return ax



