# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/message.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14protos/message.proto\"\x16\n\x03msg\x12\x0f\n\x07message\x18\x01 \x01(\t2#\n\tMessenger\x12\x16\n\x06getMsg\x12\x04.msg\x1a\x04.msg\"\x00\x62\x06proto3'
)




_MSG = _descriptor.Descriptor(
  name='msg',
  full_name='msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='msg.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=24,
  serialized_end=46,
)

DESCRIPTOR.message_types_by_name['msg'] = _MSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

msg = _reflection.GeneratedProtocolMessageType('msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'protos.message_pb2'
  # @@protoc_insertion_point(class_scope:msg)
  })
_sym_db.RegisterMessage(msg)



_MESSENGER = _descriptor.ServiceDescriptor(
  name='Messenger',
  full_name='Messenger',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=48,
  serialized_end=83,
  methods=[
  _descriptor.MethodDescriptor(
    name='getMsg',
    full_name='Messenger.getMsg',
    index=0,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSENGER)

DESCRIPTOR.services_by_name['Messenger'] = _MESSENGER

# @@protoc_insertion_point(module_scope)
