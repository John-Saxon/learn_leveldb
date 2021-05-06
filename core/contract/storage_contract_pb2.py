# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/contract/storage_contract.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='core/contract/storage_contract.proto',
  package='protocol',
  syntax='proto3',
  serialized_options=_b('\n\030org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/core'),
  serialized_pb=_b('\n$core/contract/storage_contract.proto\x12\x08protocol\"?\n\x17\x42uyStorageBytesContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\r\n\x05\x62ytes\x18\x02 \x01(\x03\":\n\x12\x42uyStorageContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\r\n\x05quant\x18\x02 \x01(\x03\"C\n\x13SellStorageContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x15\n\rstorage_bytes\x18\x02 \x01(\x03\"C\n\x17UpdateBrokerageContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x11\n\tbrokerage\x18\x02 \x01(\x05\x42\x45\n\x18org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')
)




_BUYSTORAGEBYTESCONTRACT = _descriptor.Descriptor(
  name='BuyStorageBytesContract',
  full_name='protocol.BuyStorageBytesContract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_address', full_name='protocol.BuyStorageBytesContract.owner_address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='protocol.BuyStorageBytesContract.bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=113,
)


_BUYSTORAGECONTRACT = _descriptor.Descriptor(
  name='BuyStorageContract',
  full_name='protocol.BuyStorageContract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_address', full_name='protocol.BuyStorageContract.owner_address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quant', full_name='protocol.BuyStorageContract.quant', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=173,
)


_SELLSTORAGECONTRACT = _descriptor.Descriptor(
  name='SellStorageContract',
  full_name='protocol.SellStorageContract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_address', full_name='protocol.SellStorageContract.owner_address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_bytes', full_name='protocol.SellStorageContract.storage_bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=242,
)


_UPDATEBROKERAGECONTRACT = _descriptor.Descriptor(
  name='UpdateBrokerageContract',
  full_name='protocol.UpdateBrokerageContract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_address', full_name='protocol.UpdateBrokerageContract.owner_address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brokerage', full_name='protocol.UpdateBrokerageContract.brokerage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=311,
)

DESCRIPTOR.message_types_by_name['BuyStorageBytesContract'] = _BUYSTORAGEBYTESCONTRACT
DESCRIPTOR.message_types_by_name['BuyStorageContract'] = _BUYSTORAGECONTRACT
DESCRIPTOR.message_types_by_name['SellStorageContract'] = _SELLSTORAGECONTRACT
DESCRIPTOR.message_types_by_name['UpdateBrokerageContract'] = _UPDATEBROKERAGECONTRACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuyStorageBytesContract = _reflection.GeneratedProtocolMessageType('BuyStorageBytesContract', (_message.Message,), dict(
  DESCRIPTOR = _BUYSTORAGEBYTESCONTRACT,
  __module__ = 'core.contract.storage_contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.BuyStorageBytesContract)
  ))
_sym_db.RegisterMessage(BuyStorageBytesContract)

BuyStorageContract = _reflection.GeneratedProtocolMessageType('BuyStorageContract', (_message.Message,), dict(
  DESCRIPTOR = _BUYSTORAGECONTRACT,
  __module__ = 'core.contract.storage_contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.BuyStorageContract)
  ))
_sym_db.RegisterMessage(BuyStorageContract)

SellStorageContract = _reflection.GeneratedProtocolMessageType('SellStorageContract', (_message.Message,), dict(
  DESCRIPTOR = _SELLSTORAGECONTRACT,
  __module__ = 'core.contract.storage_contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.SellStorageContract)
  ))
_sym_db.RegisterMessage(SellStorageContract)

UpdateBrokerageContract = _reflection.GeneratedProtocolMessageType('UpdateBrokerageContract', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEBROKERAGECONTRACT,
  __module__ = 'core.contract.storage_contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.UpdateBrokerageContract)
  ))
_sym_db.RegisterMessage(UpdateBrokerageContract)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
