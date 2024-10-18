# SolverSelfSimpleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** | User&#39;s Latex input | [optional] 
**solution** | [**SolverSolution**](SolverSolution.md) | The solution we believe the user most likely wants | [optional] 

## Example

```python
from upstudy_py_sdk.models.solver_self_simple_response import SolverSelfSimpleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SolverSelfSimpleResponse from a JSON string
solver_self_simple_response_instance = SolverSelfSimpleResponse.from_json(json)
# print the JSON string representation of the object
print(SolverSelfSimpleResponse.to_json())

# convert the object into a dict
solver_self_simple_response_dict = solver_self_simple_response_instance.to_dict()
# create an instance of SolverSelfSimpleResponse from a dict
solver_self_simple_response_from_dict = SolverSelfSimpleResponse.from_dict(solver_self_simple_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


