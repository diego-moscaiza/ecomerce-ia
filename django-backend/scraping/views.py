from django.http import HttpResponse
from playwright.async_api import async_playwright
import asyncio
import json

async def scrape_async():
    async with async_playwright() as p:
        browser = None

        if await p.chromium.launch() is not None:
            browser = await p.chromium.launch(headless=False)
        elif await p.msedge.launch() is not None:
            browser = await p.msedge.launch(headless=False)
        elif await p.firefox.launch() is not None:
            browser = await p.firefox.launch(headless=False)
        else:
            print("No browser available")
            return None

        context = await browser.new_context()
        page = await context.new_page()
        link : str = "https://simple.ripley.com.pe/calzado/zapatillas/urbanas?s=mdco"
        await page.goto(link)

        etiqueta_inicial: str = ".catalog-product-details"

        # Obtener todos los elementos con la clase "catalog-product-details"
        prendas = await page.eval_on_selector_all(
            f"{etiqueta_inicial}",
            """
            (products) => products.map((product) => {
                const title = product.querySelector(".catalog-product-details__name").innerText.trim();
                return { title };
            })
            """,
        )

        await browser.close()
        prendas_json = json.dumps([prenda for prenda in prendas])
        return prendas_json

def scrape(request):
    prendas = asyncio.run(scrape_async())
    return HttpResponse(str(prendas))
