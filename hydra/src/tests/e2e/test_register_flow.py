import os
import pytest
from playwright.async_api import async_playwright, Error

TARGET = os.getenv("TARGET_REGISTER_URL", "https://www.perplexity.ai/")


@pytest.mark.asyncio
async def test_register_flow():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(TARGET, timeout=60000)
            assert page.title(), "Strona się nie załadowała"
            await browser.close()
        except Error:
            pytest.skip("Brak przeglądarki Playwright")
