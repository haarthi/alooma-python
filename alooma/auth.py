import os
import alooma



api = alooma.Client(api_key=API_KEY, account_name=ACCOUNT_NAME)## We will use this api object throughout the documentation ##

print "elloWOrld"

print api


""" Retrieve All Event Types """
## Retrieve All Event Types with a Subset of Total Data
events = api.get_event_types()
# Returns a list of dictionaries (basically, a list of mapping objects but without the fields section)
# this one cannot be used in set_mapping()

# Print All Event Types
print '\n'.join([e['name'] for e in events])


# print api.get_inputs()




import alooma
# connect to Alooma API



# api = alooma.Client(ALOOMA_USERNAME, ALOOMA_PASSWORD, account_name=ACCOUNT_NAME, port=443)

# submit a code module, and name it 'submodule'.
# this module contains a dict called 'transform_names'
# and a method called 'transform_ft_to_mtr'


api.set_transform("""
transform_names = {'John': 'Jonathan',
                   'Bob': 'Robert',
                   'Rick': 'Richard'}

def transform_ft_to_mtr(x):
    return x * 0.3048

""", module_name='submodule')

# Now edit the main code to use 'submodule' by importing it.
# You can also perform this step via the Alooma UI
# by editing the code in the Code Engine.
# Note that it should only be run once - if you later re-submit the
# 'configs' module, it will be automatically re-loaded by
# the main module, so the code that runs in the production

api.set_transform("""
  import submodule

  def transform(event): 
    event['name'] = submodule.transform_names.get(event['name'], event['name'])  
    # The above line is equivalent to: # if event['name'] in submodule.transform_names: 
    #     event['name'] = submodule.transform_names[event['name']] 

    if 'value' in event:
      event['value'] = submodule.transform_ft_to_mtr(event['value'])
    return event

   """, module_name='main')