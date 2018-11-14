import csv, io

# The field names in the order they appear in the CSV file
headers = ["inventory_id", "id", "date", "cost", "product", "team", "columbia", "coat", "cost", "department", "hash",
           "number"]
users = ["user_id", "first_name", "last_name", "email", "age", "address", "state", "country", "lat", "long",
         "department"]


def map_headers(headers, event, table_destination):
    string = event['message']
    metadata = event['_metadata']
    f = io.StringIO(string)
    reader = csv.reader(f, delimiter=',')
    event = {}
    fields = list(reader)[0]
    event['data'] = dict(zip(headers[:len(fields)], fields))
    # event['data']['email'] = "haarthi@looker.com"
    event['num_fields'] = len(fields)
    event['expected_fields'] = len(headers)
    event['_metadata'] = metadata
    event['_metadata']['event_type'] = "PUBLIC.test_users"
    return event


def transform(event):
    # if "inventory_items" in event["_metadata"]["file_name"]:
    #   event = map_headers(headers, event, "PUBLIC.test_inventory_items")
    if "user" in event["_metadata"]["file_name"]:
        event = map_headers(users, event, "PUBLIC.test_users")

    return event