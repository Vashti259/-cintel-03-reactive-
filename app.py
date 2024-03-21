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



