"""STIX 2 Common Data Types and Properties"""

from .base import _STIXBase
from .properties import Property, BooleanProperty, ReferenceProperty, ListProperty
from .utils import NOW

COMMON_PROPERTIES = {
    # 'type' and 'id' should be defined on each individual type
    'created': Property(default=lambda: NOW),
    'modified': Property(default=lambda: NOW),
    'external_references': Property(),
    'revoked': BooleanProperty(),
    'created_by_ref': ReferenceProperty(type="identity"),
    'object_marking_refs': ListProperty(ReferenceProperty, element_type="marking-definition"),
    'granular_markings': ListProperty(Property)
}


class ExternalReference(_STIXBase):
    _properties = {
        'source_name': Property(required=True),
        'description': Property(),
        'url': Property(),
        'external_id': Property(),
    }


class KillChainPhase(_STIXBase):
    _properties = {
        'kill_chain_name': Property(required=True),
        'phase_name': Property(required=True),
    }
