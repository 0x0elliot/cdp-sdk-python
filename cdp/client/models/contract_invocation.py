# coding: utf-8

"""
    Coinbase Platform API

    This is the OpenAPI 3.0 specification for the Coinbase Platform APIs, used in conjunction with the Coinbase Platform SDKs.

    The version of the OpenAPI document: 0.0.1-alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cdp.client.models.transaction import Transaction
from typing import Optional, Set
from typing_extensions import Self

class ContractInvocation(BaseModel):
    """
    A contract invocation onchain.
    """ # noqa: E501
    network_id: StrictStr = Field(description="The ID of the blockchain network.")
    wallet_id: StrictStr = Field(description="The ID of the wallet that owns the address.")
    address_id: StrictStr = Field(description="The onchain address of the address invoking the contract.")
    contract_invocation_id: StrictStr = Field(description="The ID of the contract invocation.")
    contract_address: StrictStr = Field(description="The onchain address of the contract.")
    method: StrictStr = Field(description="The method to be invoked on the contract.")
    args: StrictStr = Field(description="The JSON-encoded arguments to pass to the contract method. The keys should be the argument names and the values should be the argument values.")
    abi: Optional[StrictStr] = Field(default=None, description="The JSON-encoded ABI of the contract.")
    amount: StrictStr = Field(description="The amount to send to the contract for a payable method")
    transaction: Transaction
    __properties: ClassVar[List[str]] = ["network_id", "wallet_id", "address_id", "contract_invocation_id", "contract_address", "method", "args", "abi", "amount", "transaction"]

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
        """Create an instance of ContractInvocation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContractInvocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "network_id": obj.get("network_id"),
            "wallet_id": obj.get("wallet_id"),
            "address_id": obj.get("address_id"),
            "contract_invocation_id": obj.get("contract_invocation_id"),
            "contract_address": obj.get("contract_address"),
            "method": obj.get("method"),
            "args": obj.get("args"),
            "abi": obj.get("abi"),
            "amount": obj.get("amount"),
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None
        })
        return _obj


