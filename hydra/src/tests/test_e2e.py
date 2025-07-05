import pytest
from playwright.sync_api import sync_playwright, Error


def test_strona():
    try:
        with sync_playwright() as p:
            przegladarka = p.firefox.launch()
            strona = przegladarka.new_page()
            strona.goto("https://example.com")
            assert "Example" in strona.title()
            przegladarka.close()
    except Error:
        pytest.skip("Brak przegladarki Playwright")
