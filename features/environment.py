from playwright.sync_api import sync_playwright
from Config import API_BASE_URL

def before_all(context):
    context.playwright = sync_playwright().start()
    
def before_scenario(context, scenario):
    tags = scenario.tags

    if "ui" in tags:
        context.browser = context.playwright.chromium.launch(headless=False)
        context.browser_context = context.browser.new_context(no_viewport=True)
        context.browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)

    if "api" in tags:
        context.api = context.playwright.request.new_context(
            base_url=API_BASE_URL
        )

def after_scenario(context, scenario):
    tags = scenario.tags

    if "ui" in tags:
        if hasattr(context, "browser_context"):
            context.browser_context.tracing.stop(path='logs/trace.zip')
    
        if hasattr(context, "browser"):
            context.browser.close()

    if "api" in tags:
        context.api.dispose()

def after_all(context):
    if hasattr(context, "playwright"):
        context.playwright.stop()