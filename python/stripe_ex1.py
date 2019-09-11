import os

import stripe

stripe.api_key = "sk_test_xpZRxrGa0KttcEwzuhCry5Aj00CZpHQnB3"

print("Attempting charge...")

resp = stripe.Charge.create(
    amount=200,
    currency="usd",
    card="tok_visa",
    description="customer@gmail.com",
)

print("Success: %r" % (resp))

