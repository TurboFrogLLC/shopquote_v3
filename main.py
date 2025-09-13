from taipy.gui import Gui

pages = {
    "home": "pages/home.md",
    "part_summary": "pages/part_summary.md",
    "operations": "pages/operations.md",
    "quote_breakdown": "pages/quote_breakdown.md",
    "quote_summary": "pages/quote_summary.md",
    "settings": "pages/settings.md",
}

if __name__ == "__main__":
    Gui(pages=pages).run(title="ShopQuote v3")
