# shopify-square-connect

Simple interface for importing product and inventory information from shopify into square.

## Getting started

1. Install [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

1. Create a [square developer account](https://app.squareup.com/signup/en-US?return_to=https%3A%2F%2Fdeveloper.squareup.com%2Fconsole%2Fen%2Fapps&v=developers)

1. Create a new Application, copy the access token, and add it to a `.env` file
```shell
echo "SQUARE_ACCESS_TOKEN=<your access token> > .env"
```

1. Start the app
```shell
uv run quickstart.py
```