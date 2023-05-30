from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid Scrolling Performance",
)

text1 = """
# Scrolling Performance


The grid is fast. However, the grid can also be configured and extended in many ways. This page explains how you can make the grid go faster.


## Setting Expectations

The grid can be as fast as demonstrated in the demo application [Demo Application](https://www.ag-grid.com/example). You can resize the demo application to the same size as the grid in your application by resizing the browser, then navigate around the grid (scroll, filter etc) and see how fast the demo grid is compared to your own implementation. If the demo grid is going faster, then there is room for performance improvements.

## Check Cell Renderers

The grid can be slowed down by custom <dccLink href="/components/cell-renderer" children="Cell Renderers"/>. To test this, remove all Cell Renderers from the grid and compare the speed again. If the grid does improve it's speed by removing Cell Renderers, introduce the Cell Renderers one by one to find out which ones are adding the most overhead.

## If Possible, Avoid Cell Renderers

Cell Renders result in more DOM. More DOM means more CPU processing to render, regardless of what Framework is used to generate the DOM.

Ask the question, do you really need the Cell Renderer?

If you are only manipulating the value rather than creating complex DOM, would a <dccLink href="/rendering/value-getters" children="Value Getters"/> or <dccLink href="/rendering/value-formatters-intro" children="Value Formatters"/> achieve what you want instead? Value Getters and Value Formatters do not result in more DOM.



## Avoid Auto Height

<dccLink href="/layout/grid-size" children="Auto Height"/> is a great feature that we love. However it also creates more complex DOM inside each Cell.

If you are looking for ways to squeeze performance, consider turning this feature off. As with all suggestions here, it is paramount you profile your own application with this suggestion to see how much of a difference it makes and if the trade off is worth it for your application.

## Turn Off Animations

[Row Animation](https://www.ag-grid.com/react-data-grid/row-animation/) and [Column Animation](https://www.ag-grid.com/react-data-grid/column-moving/#moving-animation) make for a great user experience. However not all browsers are as good at animations as others. Consider checking the client's browser and turning off row and column animation for slower browsers.

## Configure Row Buffer

The `rowBuffer` property sets the number of rows the grid renders outside of the viewable area. The default is 10. For example, if your grid is showing 50 rows (as that's all the fits on your screen without scrolling), then the grid will actually render 70 in total (10 extra above and 10 extra below). Then when you scroll the grid will already have 10 rows ready waiting to show so the user will not see a redraw (not all browsers show the redraw, only the slower ones).

Setting a low row buffer will make initial draws of the grid faster (eg when data is first loaded, or after filtering, grouping etc). Setting a high row buffer will reduce the redraw visible vertically scrolling.

## Compare Browsers

Performance of the grid can vary between browsers due to their underlying implementations. At the time of writing Chromium based browsers (Google Chrome, Microsoft Edge) have the best performance. However, it may be outside of your control to recommend which browser users of your application have installed.

## Understand Data Updates

For fast changing data, consider using [Batch Update Transactions](https://www.ag-grid.com/react-data-grid/data-update-high-frequency/) which allows the grid to take very large amounts of updates without bringing the browser to a crawl. This is also demonstrated in the blog
[Streaming Updates in JavaScript Datagrids](https://medium.com/ag-grid/how-to-test-for-the-best-html5-grid-for-streaming-updates-53545bb9256a) that shows hundreds of thousands of updates per second.

## Debounce Vertical Scroll

By default, there is no debouncing of the vertical scroll. However, in some rare circumstances, you may wish to debounce the vertical scroll so that the grid only scrolls after the user has finished updating the scroll position. 

To debounce the vertical scroll, set grid property `debounceVerticalScrollbar=True`.

"""


layout = html.Div(
    [
        make_md(text1),

    ],
)
