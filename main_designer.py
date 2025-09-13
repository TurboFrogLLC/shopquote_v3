# main_designer.py — launch Taipy Designer with all pages
# Taipy 4.1.0

from taipy.gui import Gui
from taipy.designer import Page

pages = {
    "Home": Page("pages/home.xprjson"),
    "Part Summary": Page("pages/part_summary.xprjson"),
    "Operations": Page("pages/operations.xprjson"),
    "Quote Breakdown": Page("pages/quote_breakdown.xprjson"),
    "Quote Summary": Page("pages/quote_summary.xprjson"),
    "Settings": Page("pages/settings.xprjson"),
}

if __name__ == "__main__":
    Gui(pages=pages, title="ShopQuote v3 — Designer").run(design=True)
