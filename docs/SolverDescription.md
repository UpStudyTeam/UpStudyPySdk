# SolverDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Descriptive information | [optional] 
**format** | [**SolverDescriptionFormat**](SolverDescriptionFormat.md) |  | [optional] 

## Example

```python
from upstudy_py_sdk.models.solver_description import SolverDescription

# TODO update the JSON string below
json = "{}"
# create an instance of SolverDescription from a JSON string
solver_description_instance = SolverDescription.from_json(json)
# print the JSON string representation of the object
print(SolverDescription.to_json())

# convert the object into a dict
solver_description_dict = solver_description_instance.to_dict()
# create an instance of SolverDescription from a dict
solver_description_from_dict = SolverDescription.from_dict(solver_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


