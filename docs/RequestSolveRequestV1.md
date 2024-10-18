# RequestSolveRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** | Mathematical expression input, must be in Latex format, e.g., \\frac{x+1}{2} \\leq 0 | 
**lang** | [**RequestSolveRequestV1Lang**](RequestSolveRequestV1Lang.md) |  | [optional] 

## Example

```python
from upstudy_py_sdk.models.request_solve_request_v1 import RequestSolveRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of RequestSolveRequestV1 from a JSON string
request_solve_request_v1_instance = RequestSolveRequestV1.from_json(json)
# print the JSON string representation of the object
print(RequestSolveRequestV1.to_json())

# convert the object into a dict
request_solve_request_v1_dict = request_solve_request_v1_instance.to_dict()
# create an instance of RequestSolveRequestV1 from a dict
request_solve_request_v1_from_dict = RequestSolveRequestV1.from_dict(request_solve_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


