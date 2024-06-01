from django.http import HttpResponse
from playwright.async_api import async_playwright # type: ignore
import asyncio

async def scrape_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://example.com')

        # Realiza el scraping aquí
        # Por ejemplo, obtener el título de la página
        title = await page.title()

        await browser.close()
        return title

async def scrape(request):
    title = await scrape_async()
    return HttpResponse(title)

# Otra forma de hacerlo utilizando asyncio.run()
def scrape(request):
    title = asyncio.run(scrape_async())
    return HttpResponse(title)
