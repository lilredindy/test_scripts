import stripe 

stripe.api_key = "sk_test_xpZRxrGa0KttcEwzuhCry5Aj00CZpHQnB3"

# list charges
stripe.Charge.list()

# retrieve single charge
print stripe.Charge.retrieve("ch_1FHBoZIUVycxzRV4rWBtyivU")
