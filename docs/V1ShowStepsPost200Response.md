# V1ShowStepsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SolverSelfFullResponseText**](SolverSelfFullResponseText.md) |  | [optional] 
**err_msg** | **str** |  | [optional] 

## Example

```python
from upstudy_py_sdk.models.v1_show_steps_post200_response import V1ShowStepsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ShowStepsPost200Response from a JSON string
v1_show_steps_post200_response_instance = V1ShowStepsPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1ShowStepsPost200Response.to_json())

# convert the object into a dict
v1_show_steps_post200_response_dict = v1_show_steps_post200_response_instance.to_dict()
# create an instance of V1ShowStepsPost200Response from a dict
v1_show_steps_post200_response_from_dict = V1ShowStepsPost200Response.from_dict(v1_show_steps_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


