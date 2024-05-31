from django.http import HttpResponse
from playwright.async_api import async_playwright
from asgiref.sync import sync_to_async

@sync_to_async
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

def scrape(request):
    title = scrape_async()
    return HttpResponse(title)
