import os

import shopify

from dotenv import load_dotenv

load_dotenv()


class ShopifyConnect:
    shop_url = "montavillafoodcoop.myshopify.com"
    api_version = "2024-07"

    def __init__(self):
        session = shopify.Session(
            self.shop_url, self.api_version, os.environ["SHOPIFY_ADMIN_ACCESS_TOKEN"]
        )
        shopify.ShopifyResource.activate_session(session)

    def __del__(self) -> None:
        shopify.ShopifyResource.clear_session()

    def tester(self):
        print(shopify.GraphQL().execute("{ shop { name id } }"))


# sh = ShopifyConnect()
# sh.tester()
