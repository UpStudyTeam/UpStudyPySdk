# SolverSelfFullResponseText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** | User&#39;s Latex input | [optional] 
**solutions** | [**List[SolverSolutionWithSolvingSteps]**](SolverSolutionWithSolvingSteps.md) | All solutions we can provide along with the steps to obtain the solutions | [optional] 

## Example

```python
from upstudy_py_sdk.models.solver_self_full_response_text import SolverSelfFullResponseText

# TODO update the JSON string below
json = "{}"
# create an instance of SolverSelfFullResponseText from a JSON string
solver_self_full_response_text_instance = SolverSelfFullResponseText.from_json(json)
# print the JSON string representation of the object
print(SolverSelfFullResponseText.to_json())

# convert the object into a dict
solver_self_full_response_text_dict = solver_self_full_response_text_instance.to_dict()
# create an instance of SolverSelfFullResponseText from a dict
solver_self_full_response_text_from_dict = SolverSelfFullResponseText.from_dict(solver_self_full_response_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


