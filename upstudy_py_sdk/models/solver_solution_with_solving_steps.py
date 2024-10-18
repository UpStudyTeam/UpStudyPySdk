# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from upstudy_py_sdk.models.solver_description import SolverDescription
from upstudy_py_sdk.models.solver_step import SolverStep
from typing import Optional, Set
from typing_extensions import Self

class SolverSolutionWithSolvingSteps(BaseModel):
    """
    SolverSolutionWithSolvingSteps
    """ # noqa: E501
    block_name: Optional[SolverDescription] = Field(default=None, description="Block name: e.g., Function/Solve the equation")
    results: Optional[List[SolverStep]] = Field(default=None, description="Results, possibly multiple, e.g., {\\frac{1}{4},0.25}")
    solution_name: Optional[SolverDescription] = Field(default=None, description="Specific solution name under the block classification: e.g., Block: Function, Solution: Find the slope")
    solving_steps: Optional[List[SolverStep]] = Field(default=None, description="Steps to obtain the solution")
    __properties: ClassVar[List[str]] = ["block_name", "results", "solution_name", "solving_steps"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SolverSolutionWithSolvingSteps from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of block_name
        if self.block_name:
            _dict['block_name'] = self.block_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item_results in self.results:
                if _item_results:
                    _items.append(_item_results.to_dict())
            _dict['results'] = _items
        # override the default output from pydantic by calling `to_dict()` of solution_name
        if self.solution_name:
            _dict['solution_name'] = self.solution_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in solving_steps (list)
        _items = []
        if self.solving_steps:
            for _item_solving_steps in self.solving_steps:
                if _item_solving_steps:
                    _items.append(_item_solving_steps.to_dict())
            _dict['solving_steps'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SolverSolutionWithSolvingSteps from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "block_name": SolverDescription.from_dict(obj["block_name"]) if obj.get("block_name") is not None else None,
            "results": [SolverStep.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "solution_name": SolverDescription.from_dict(obj["solution_name"]) if obj.get("solution_name") is not None else None,
            "solving_steps": [SolverStep.from_dict(_item) for _item in obj["solving_steps"]] if obj.get("solving_steps") is not None else None
        })
        return _obj


