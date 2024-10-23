# Stripe

## Setup

You need to setup the following env variables. Theses varialbes can be found on the [stripe's developer dashboard](https://dashboard.stripe.com/test/apikeys).

- STRIPE_PUBLISHABLE_KEY
- STRIPE_SECRET_KEY
- STRIPE_ENDPOINT_SECRET (optional) : Is used for testing webhooks in local. This variable is generated with the commande `make stripe`.

Then, you need to adjust the `checkout_session` and `webhook` method in the `api.StripeView` class, depending on your needs.