# rom abc import update_abstractmethods
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from pprint import pprint

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://api.linear.app/graphql", headers={"Authorization": ""})

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    query Me {
        viewer {
            id
            name
            email
        }
    }
"""
)

query2 = gql(
    """
    query Team {
        issues{
            nodes{
            title
                assignee{
                    id 
                }
            }
        }
    }
    
"""
)


result = client.execute(query)
title = client.execute(query2)

my_id = result['viewer']['id']



# assign_issue = issue['issues']['nodes']
t = title['issues']['nodes']

no = len(t)
for i in t:
    if i['assignee'] != None:
        s = i['assignee']['id']
        if  s == my_id:
            print(i['title'])

    
   