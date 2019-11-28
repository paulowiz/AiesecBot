import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import os
from dotenv import load_dotenv

class graphqlConsume:

    def __init__(self):

       #token_get_url = "http://token.aiesec.org.br/get_token.php?token=c0aa46e01d77fb212fe0195636fb515f8e43b530087399ec49f"
        #access_token_raw = requests.get(token_get_url)
        #access_token = access_token_raw.text.strip()
        #print('Setup complete! \nYour access token is ' + '"' + access_token + '"')
        load_dotenv()
        _transport = RequestsHTTPTransport(
            url='https://gis-api.aiesec.org/graphql?access_token='+str(os.getenv("API_TOKEN")),
                # str(access_token),
            use_json=True,

        )
        client = Client(
            transport=_transport,
            fetch_schema_from_transport=True,
        )
        self.client = client

    # Executa query graphql
    def executaGraphQL(self, input_query):
        client = self.client
        query = gql(input_query)
        query_json = client.execute(query)
        print('Query GraphQL executada com sucesso!')
        dados = json.dumps(query_json, indent=4)
        # print(dados)
        retorno = json.loads(dados)
        # print(retorno)
        return retorno


pass
