from playwright.async_api import async_playwright
import json


async def scrape_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        browser1 = await p.chromium.launch(channel="msedge", headless=False)
        browser2 = await p.firefox.launch(headless=False)
        browser3 = await p.webkit.launch(headless=False)

        page = await browser.new_page()

        number_page = 3
        page_url = f"https://simple.ripley.com.pe/calzado/zapatillas/urbanas?s=mdco&page={number_page}"
        await page.goto(page_url)

        scroll_delay = 500  # 500ms
        page_height = await page.evaluate("document.body.scrollHeight")
        scroll_position = 0

        while scroll_position < page_height:
            await page.evaluate(f"window.scrollTo(0, {scroll_position})")
            await page.wait_for_timeout(scroll_delay)
            scroll_position += 500

        selectors = {
            "etiquetaPrincipal": "#product-border .catalog-product-item",
            "selectorNombre": ".catalog-product-details .catalog-product-details__name",
            "selectorMarca": ".catalog-product-details .catalog-product-details__logo-container .brand-logo span",
            "selectorPrecioOferta": ".catalog-product-details .catalog-product-details__prices .catalog-prices__list .catalog-prices__offer-price",
            "selectorPrecioNormal": ".catalog-product-details .catalog-product-details__prices .catalog-prices__list .catalog-prices__list-price",
            "selectorImagen": ".proportional-image-wrapper .images-preview .images-preview-item img",
        }

        prendas = await page.eval_on_selector_all(
            selectors["etiquetaPrincipal"],
            f"""
            (products) => products.map((product) => {{
                const nombre = product.querySelector('{selectors["selectorNombre"]}')?.innerText.trim() ?? '';
                const marca = product.querySelector('{selectors["selectorMarca"]}')?.innerText.trim() ?? '';
                const precio_oferta = product.querySelector('{selectors["selectorPrecioOferta"]}')?.innerText.trim() ?? '';
                const precio_normal = product.querySelector('{selectors["selectorPrecioNormal"]}')?.innerText.trim() ?? '';
                const imagen = product.querySelector('{selectors["selectorImagen"]}')?.src ?? '';
                const genero = nombre.toUpperCase().includes("HOMBRE") ? "Hombre" : nombre.toUpperCase().includes("MUJER") ? "Mujer" : nombre.toUpperCase().includes("NIÑO") ? "Niño" : nombre.toUpperCase().includes("NIÑA") ? "Niña" : nombre.toUpperCase().includes("UNISEX") ? "Unisex" : "";
                return {{ nombre, marca, precio_oferta, precio_normal, genero, imagen }};
            }})
            """,
        )

        await browser.close()
        prendas_json = json.dumps([prenda for prenda in prendas])
        return prendas_json
