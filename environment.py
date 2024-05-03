from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.browser_context = context.browser.new_context(no_viewport=True)
    context.browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)

def after_all(context):
    context.browser_context.tracing.stop(path='logs/trace.zip')
    context.browser.close()
    context.playwright.stop()