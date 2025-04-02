import os
import uuid

from dotenv import load_dotenv
from square.http.auth.o_auth_2 import BearerAuthCredentials
from square.client import Client

load_dotenv()


class SquareConnect:
    __client: Client

    def __init__(self) -> None:
        self.__auth()

    def __auth(self) -> None:
        self.__client = Client(
            bearer_auth_credentials=BearerAuthCredentials(
                access_token=os.environ["SQUARE_ACCESS_TOKEN"]
            ),
            environment="sandbox",
        )

    def get_client(self) -> Client:
        if not self.__client:
            self.__auth()
        return self.__client

    def print_result(self, result) -> None:
        if result.is_success():
            print(result.body)
        elif result.is_error():
            print(result.errors)

    def list_locations(self) -> None:
        result = self.get_client().locations.list_locations()

        if result.is_success():
            for location in result.body["locations"]:
                print(f"{location['id']}: ", end="")
                print(f"{location['name']}, ", end="")
                print(f"{location['address']['address_line_1']}, ", end="")
                print(f"{location['address']['locality']}")
        elif result.is_error():
            for error in result.errors:
                print(error["category"])
                print(error["code"])
                print(error["detail"])

    def upsert_item(self) -> None:
        idempotency_key = uuid.uuid4()

        self.print_result(
            self.get_client().catalog.upsert_catalog_object(
                body={
                    "idempotency_key": str(idempotency_key),
                    "object": {
                        "type": "ITEM",
                        "id": "#coffee",
                        "item_data": {
                            "name": "Coffee",
                            "description": "Coffee Drink",
                            "abbreviation": "Co",
                            "variations": [
                                {
                                    "type": "ITEM_VARIATION",
                                    "id": "#small_coffee",
                                    "item_variation_data": {
                                        "item_id": "#coffee",
                                        "name": "Small",
                                        "pricing_type": "FIXED_PRICING",
                                        "price_money": {
                                            "amount": 300,
                                            "currency": "USD",
                                        },
                                    },
                                },
                                {
                                    "type": "ITEM_VARIATION",
                                    "id": "#large_coffee",
                                    "item_variation_data": {
                                        "item_id": "#coffee",
                                        "name": "Large",
                                        "pricing_type": "FIXED_PRICING",
                                        "price_money": {
                                            "amount": 350,
                                            "currency": "USD",
                                        },
                                    },
                                },
                            ],
                        },
                    },
                }
            )
        )

    def get_item(self, id: str, version=None) -> None:
        self.print_result(
            self.get_client().catalog.retrieve_catalog_object(
                object_id=id, include_related_objects=False, catalog_version=version
            )
        )


# sqc = SquareConnect()
# sqc.get_item("5DRIUOIBZKCCZYFEC6KS4PLR")
