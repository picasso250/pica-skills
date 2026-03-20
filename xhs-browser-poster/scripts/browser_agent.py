import asyncio
import json
import re
import urllib.request

from playwright.async_api import Browser, BrowserContext, Page, async_playwright

BROWSER_ENDPOINT = "http://127.0.0.1:9222"


class BrowserAgent:
    def __init__(self):
        self.pw = None
        self.browser: Browser = None
        self.context: BrowserContext = None

    async def _get_ws_url(self):
        try:
            with urllib.request.urlopen(f"{BROWSER_ENDPOINT}/json/version") as response:
                data = json.loads(response.read().decode())
                return data.get("webSocketDebuggerUrl")
        except Exception as e:
            print(f"Error fetching WS URL: {e}")
            return None

    async def _get_browser(self):
        if not self.browser or not self.browser.is_connected():
            if not self.pw:
                self.pw = await async_playwright().start()

            ws_url = await self._get_ws_url()
            if ws_url:
                self.browser = await self.pw.chromium.connect_over_cdp(ws_url)
            else:
                self.browser = await self.pw.chromium.connect_over_cdp(BROWSER_ENDPOINT)

            self.context = self.browser.contexts[0]
        return self.browser

    async def _get_page(self, query: str) -> Page:
        await self._get_browser()
        pages = self.context.pages

        if re.match(r"^\d+$", query):
            index = int(query)
            if 0 <= index < len(pages):
                return pages[index]
            raise ValueError(f"Tab index {index} out of range (0-{len(pages)-1})")

        matches = [p for p in pages if query.lower() in p.url.lower()]
        if not matches:
            raise ValueError(f"Tab not found for query: {query}")

        return matches[0]

    async def open_tab(self, url: str) -> str:
        await self._get_browser()
        page = await self.context.new_page()
        await page.goto(url, wait_until="domcontentloaded")
        await asyncio.sleep(1)
        return f"Opened {url}"

    async def evaluate(self, tab_id: str, script: str):
        page = await self._get_page(tab_id)
        result = await page.evaluate(script)
        await asyncio.sleep(1)
        return result

    async def disconnect(self):
        if self.browser:
            await self.browser.close()
        if self.pw:
            await self.pw.stop()
        self.browser = None
        self.pw = None
