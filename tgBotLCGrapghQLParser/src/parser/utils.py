from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport


def getLCClient() -> Client:
    transport: AIOHTTPTransport = AIOHTTPTransport(url="https://leetcode.com/graphql")
    client: Client = Client(transport=transport, fetch_schema_from_transport=False)
    return client
