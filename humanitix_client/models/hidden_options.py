from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.hidden_options_when import HiddenOptionsWhen
from ..types import UNSET, Unset

T = TypeVar("T", bound="HiddenOptions")


@_attrs_define
class HiddenOptions:
    """
    Attributes:
        hidden (bool | Unset): Whether hiding is enabled for this ticket type. When true, the `when` field determines
            the condition under which the ticket is actually hidden.
        when (HiddenOptionsWhen | Unset): The condition under which the ticket type is hidden.
        start_date (datetime.datetime | Unset):  Example: 2021-02-01T23:26:13.485Z.
        end_date (datetime.datetime | Unset):  Example: 2021-02-01T23:26:13.485Z.
        ticket_ids (list[str] | Unset): Ticket type IDs that conditionally reveal this ticket type (only applicable when
            `when` is `conditional`).
    """

    hidden: bool | Unset = UNSET
    when: HiddenOptionsWhen | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    ticket_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hidden = self.hidden

        when: str | Unset = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.value

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        ticket_ids: list[str] | Unset = UNSET
        if not isinstance(self.ticket_ids, Unset):
            ticket_ids = self.ticket_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if when is not UNSET:
            field_dict["when"] = when
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if ticket_ids is not UNSET:
            field_dict["ticketIds"] = ticket_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hidden = d.pop("hidden", UNSET)

        _when = d.pop("when", UNSET)
        when: HiddenOptionsWhen | Unset
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = HiddenOptionsWhen(_when)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        ticket_ids = cast(list[str], d.pop("ticketIds", UNSET))

        hidden_options = cls(
            hidden=hidden,
            when=when,
            start_date=start_date,
            end_date=end_date,
            ticket_ids=ticket_ids,
        )

        hidden_options.additional_properties = d
        return hidden_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
