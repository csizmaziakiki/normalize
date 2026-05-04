#
# This file is a part of the normalize python library
#
# normalize is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# normalize is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# MIT License for more details.
#
# You should have received a copy of the MIT license along with
# normalize.  If not, refer to the upstream repository at
# http://github.com/hearsaycorp/normalize
#

from __future__ import absolute_import

from src.normalize.coll import DictCollection
from src.normalize.coll import ListCollection
from src.normalize.diff import DiffOptions
from src.normalize.diff import DiffTypes
import src.normalize.exc as exc
from src.normalize.property import LazyProperty
from src.normalize.property import LazySafeProperty
from src.normalize.property import make_property_type
from src.normalize.property import Property
from src.normalize.property import ROProperty
from src.normalize.property import SafeProperty
from src.normalize.property import V1Property
from src.normalize.property.coll import DictProperty
from src.normalize.property.coll import ListProperty
from src.normalize.property.json import JsonProperty
from src.normalize.property.json import JsonDictProperty
from src.normalize.property.json import JsonListProperty
from src.normalize.property.json import JsonCollectionProperty
from src.normalize.property.json import SafeJsonProperty
from src.normalize.property.types import DateProperty
from src.normalize.property.types import DatetimeProperty
from src.normalize.property.types import FloatProperty
from src.normalize.property.types import IntegerProperty
from src.normalize.property.types import IntProperty
from src.normalize.property.types import LongProperty
from src.normalize.property.types import NumberProperty
from src.normalize.property.types import StringProperty
from src.normalize.property.types import UnicodeProperty
from src.normalize.record import Record
from src.normalize.record.meta import RecordMeta
from src.normalize.record.json import AutoJsonRecord
from src.normalize.record.json import from_json
from src.normalize.record.json import JsonRecord
from src.normalize.record.json import JsonRecordList
from src.normalize.record.json import NCAutoJsonRecord
from src.normalize.record.json import to_json
from src.normalize.selector import FieldSelector
from src.normalize.selector import FieldSelectorException
from src.normalize.selector import MultiFieldSelector
from src.normalize.subtype import subtype
from src.normalize.visitor import Visitor
from src.normalize.visitor import VisitorPattern


RecordList = ListCollection
JsonCollection = ListCollection


__all__ = [
    "AutoJsonRecord",
    "DateProperty",
    "DatetimeProperty",
    "DictCollection",
    "DictProperty",
    "DiffOptions",
    "DiffTypes",
    "exc",
    "FieldSelector",
    "FieldSelectorException",
    "FloatProperty",
    "from_json",
    "IntegerProperty",
    "IntProperty",
    "JsonCollection",  # deprecated - use JsonRecordList
    "JsonCollectionProperty",  # deprecated
    "JsonDictProperty",
    "JsonListProperty",
    "JsonProperty",
    "JsonRecord",
    "JsonRecordList",
    "LazyProperty",
    "LazySafeProperty",
    "ListCollection",
    "ListProperty",
    "LongProperty",
    "make_property_type",
    "MultiFieldSelector",
    "NCAutoJsonRecord",
    "NumberProperty",
    "Property",
    "ROProperty",
    "Record",
    "RecordList",
    "RecordMeta",
    "SafeJsonProperty",
    "SafeProperty",
    "StringProperty",
    "subtype",
    "to_json",
    "UnicodeProperty",
    "V1Property",
    "Visitor",
    "VisitorPattern",
]
