from playwright.sync_api import sync_playwright, expect
from behave import Given, Then

@Given("Llamo al endpoint {endpoint}")
def api_request(context, endpoint):
    context.response = context.api.get(endpoint)

@Then("El status code debe ser {expected_response:d}")
def check_response(context, expected_response):
    actual_status = context.response.status
    assert actual_status == expected_response