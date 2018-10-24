# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_video.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_video.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x19steammessages_video.proto\x1a steammessages_unified_base.proto\"\x81\x01\n CVideo_ClientGetVideoURL_Request\x12\x1e\n\x08video_id\x18\x01 \x01(\x04\x42\x0c\x82\xb5\x18\x08Video ID\x12=\n\rclient_cellid\x18\x02 \x01(\rB&\x82\xb5\x18\"Cell ID of client, zero if unknown\"r\n!CVideo_ClientGetVideoURL_Response\x12\x1e\n\x08video_id\x18\x01 \x01(\x04\x42\x0c\x82\xb5\x18\x08Video ID\x12-\n\tvideo_url\x18\x02 \x01(\tB\x1a\x82\xb5\x18\x16URL for video manifest\"\xaa\x04\n\rVideoBookmark\x12\x1a\n\x06\x61pp_id\x18\x01 \x01(\rB\n\x82\xb5\x18\x06\x41pp ID\x12]\n\x1cplayback_position_in_seconds\x18\x02 \x01(\rB7\x82\xb5\x18\x33How many seconds into the video the bookmark is for\x12/\n\x0evideo_track_id\x18\x03 \x01(\x04\x42\x17\x82\xb5\x18\x13video track choice.\x12/\n\x0e\x61udio_track_id\x18\x04 \x01(\x04\x42\x17\x82\xb5\x18\x13\x61udio track choice.\x12\x43\n\x12timedtext_track_id\x18\x05 \x01(\x04\x42\'\x82\xb5\x18#timedtimed or subtitle track choice\x12O\n\rlast_modified\x18\x06 \x01(\rB8\x82\xb5\x18\x34when we recorded it was last modified. Not settable.\x12U\n\x17hide_from_watch_history\x18\x07 \x01(\x08:\x05\x66\x61lseB-\x82\xb5\x18)Whether I want to show this in my history\x12O\n\x11hide_from_library\x18\x08 \x01(\x08:\x05\x66\x61lseB-\x82\xb5\x18)Whether I want to show this in my library\"r\n$CVideo_SetVideoBookmark_Notification\x12J\n\tbookmarks\x18\x01 \x03(\x0b\x32\x0e.VideoBookmarkB\'\x82\xb5\x18#list of bookmarks we want to store.\"\x81\x02\n CVideo_GetVideoBookmarks_Request\x12_\n\x06\x61ppids\x18\x01 \x03(\rBO\x82\xb5\x18KList of App IDs to grab bookmarks for. Can be empty if using updated_since.\x12|\n\rupdated_since\x18\x02 \x01(\rBe\x82\xb5\x18\x61Only return results after time. Min value is 1. (seconds since epoch January 1st, 1970 Unix Time)\"u\n!CVideo_GetVideoBookmarks_Response\x12P\n\tbookmarks\x18\x01 \x03(\x0b\x32\x0e.VideoBookmarkB-\x82\xb5\x18)List of bookmarks we found. Can be empty.\":\n CVideo_UnlockedH264_Notification\x12\x16\n\x0e\x65ncryption_key\x18\x01 \x01(\x0c\"\x85\x01\n(CFovasVideo_ClientGetOPFSettings_Request\x12\x1a\n\x06\x61pp_id\x18\x01 \x01(\rB\n\x82\xb5\x18\x06\x41pp ID\x12=\n\rclient_cellid\x18\x02 \x01(\rB&\x82\xb5\x18\"Cell ID of client, zero if unknown\"|\n)CFovasVideo_ClientGetOPFSettings_Response\x12\x1a\n\x06\x61pp_id\x18\x01 \x01(\rB\n\x82\xb5\x18\x06\x41pp ID\x12\x33\n\x0copf_settings\x18\x02 \x01(\tB\x1d\x82\xb5\x18\x19JSON blob of OPF Settings2\xb5\x04\n\x05Video\x12\x8e\x01\n\x11\x43lientGetVideoURL\x12!.CVideo_ClientGetVideoURL_Request\x1a\".CVideo_ClientGetVideoURL_Response\"2\x82\xb5\x18.Get the initial URL to begin streaming a video\x12\xc1\x01\n\x10SetVideoBookmark\x12%.CVideo_SetVideoBookmark_Notification\x1a\x0b.NoResponse\"y\x82\xb5\x18uBookmarks the locations in the video the user has reached. As as record playback settings per video. Fire and forget.\x12\xc3\x01\n\x11GetVideoBookmarks\x12!.CVideo_GetVideoBookmarks_Request\x1a\".CVideo_GetVideoBookmarks_Response\"g\x82\xb5\x18\x63Returns the video bookmarks locations for the specific videos. Includes playback settings per video\x1a\x11\x82\xb5\x18\rVideo methods2\x9e\x01\n\x0bVideoClient\x12\x88\x01\n\x12NotifyUnlockedH264\x12!.CVideo_UnlockedH264_Notification\x1a\x0b.NoResponse\"B\x82\xb5\x18>Notification from server to client that h264 has been unlocked\x1a\x04\xc0\xb5\x18\x02\x32\xf3\x01\n\nFovasVideo\x12\xc3\x01\n\x14\x43lientGetOPFSettings\x12).CFovasVideo_ClientGetOPFSettings_Request\x1a*.CFovasVideo_ClientGetOPFSettings_Response\"T\x82\xb5\x18PRetrieve the OPF settings JSON blob. Available via the Client for 360 Player App\x1a\x1f\x82\xb5\x18\x1b\x46ovas Video Service MethodsB\x03\x90\x01\x01')
  ,
  dependencies=[steammessages__unified__base__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CVIDEO_CLIENTGETVIDEOURL_REQUEST = _descriptor.Descriptor(
  name='CVideo_ClientGetVideoURL_Request',
  full_name='CVideo_ClientGetVideoURL_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='CVideo_ClientGetVideoURL_Request.video_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\010Video ID'))),
    _descriptor.FieldDescriptor(
      name='client_cellid', full_name='CVideo_ClientGetVideoURL_Request.client_cellid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\"Cell ID of client, zero if unknown'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=193,
)


_CVIDEO_CLIENTGETVIDEOURL_RESPONSE = _descriptor.Descriptor(
  name='CVideo_ClientGetVideoURL_Response',
  full_name='CVideo_ClientGetVideoURL_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='CVideo_ClientGetVideoURL_Response.video_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\010Video ID'))),
    _descriptor.FieldDescriptor(
      name='video_url', full_name='CVideo_ClientGetVideoURL_Response.video_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\026URL for video manifest'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=309,
)


_VIDEOBOOKMARK = _descriptor.Descriptor(
  name='VideoBookmark',
  full_name='VideoBookmark',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='VideoBookmark.app_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\006App ID'))),
    _descriptor.FieldDescriptor(
      name='playback_position_in_seconds', full_name='VideoBookmark.playback_position_in_seconds', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0303How many seconds into the video the bookmark is for'))),
    _descriptor.FieldDescriptor(
      name='video_track_id', full_name='VideoBookmark.video_track_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\023video track choice.'))),
    _descriptor.FieldDescriptor(
      name='audio_track_id', full_name='VideoBookmark.audio_track_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\023audio track choice.'))),
    _descriptor.FieldDescriptor(
      name='timedtext_track_id', full_name='VideoBookmark.timedtext_track_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030#timedtimed or subtitle track choice'))),
    _descriptor.FieldDescriptor(
      name='last_modified', full_name='VideoBookmark.last_modified', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0304when we recorded it was last modified. Not settable.'))),
    _descriptor.FieldDescriptor(
      name='hide_from_watch_history', full_name='VideoBookmark.hide_from_watch_history', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030)Whether I want to show this in my history'))),
    _descriptor.FieldDescriptor(
      name='hide_from_library', full_name='VideoBookmark.hide_from_library', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030)Whether I want to show this in my library'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=866,
)


_CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION = _descriptor.Descriptor(
  name='CVideo_SetVideoBookmark_Notification',
  full_name='CVideo_SetVideoBookmark_Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bookmarks', full_name='CVideo_SetVideoBookmark_Notification.bookmarks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030#list of bookmarks we want to store.'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=868,
  serialized_end=982,
)


_CVIDEO_GETVIDEOBOOKMARKS_REQUEST = _descriptor.Descriptor(
  name='CVideo_GetVideoBookmarks_Request',
  full_name='CVideo_GetVideoBookmarks_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appids', full_name='CVideo_GetVideoBookmarks_Request.appids', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030KList of App IDs to grab bookmarks for. Can be empty if using updated_since.'))),
    _descriptor.FieldDescriptor(
      name='updated_since', full_name='CVideo_GetVideoBookmarks_Request.updated_since', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030aOnly return results after time. Min value is 1. (seconds since epoch January 1st, 1970 Unix Time)'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=985,
  serialized_end=1242,
)


_CVIDEO_GETVIDEOBOOKMARKS_RESPONSE = _descriptor.Descriptor(
  name='CVideo_GetVideoBookmarks_Response',
  full_name='CVideo_GetVideoBookmarks_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bookmarks', full_name='CVideo_GetVideoBookmarks_Response.bookmarks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030)List of bookmarks we found. Can be empty.'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1244,
  serialized_end=1361,
)


_CVIDEO_UNLOCKEDH264_NOTIFICATION = _descriptor.Descriptor(
  name='CVideo_UnlockedH264_Notification',
  full_name='CVideo_UnlockedH264_Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encryption_key', full_name='CVideo_UnlockedH264_Notification.encryption_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1363,
  serialized_end=1421,
)


_CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST = _descriptor.Descriptor(
  name='CFovasVideo_ClientGetOPFSettings_Request',
  full_name='CFovasVideo_ClientGetOPFSettings_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='CFovasVideo_ClientGetOPFSettings_Request.app_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\006App ID'))),
    _descriptor.FieldDescriptor(
      name='client_cellid', full_name='CFovasVideo_ClientGetOPFSettings_Request.client_cellid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\"Cell ID of client, zero if unknown'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1424,
  serialized_end=1557,
)


_CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE = _descriptor.Descriptor(
  name='CFovasVideo_ClientGetOPFSettings_Response',
  full_name='CFovasVideo_ClientGetOPFSettings_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='CFovasVideo_ClientGetOPFSettings_Response.app_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\006App ID'))),
    _descriptor.FieldDescriptor(
      name='opf_settings', full_name='CFovasVideo_ClientGetOPFSettings_Response.opf_settings', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\031JSON blob of OPF Settings'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1559,
  serialized_end=1683,
)

_CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION.fields_by_name['bookmarks'].message_type = _VIDEOBOOKMARK
_CVIDEO_GETVIDEOBOOKMARKS_RESPONSE.fields_by_name['bookmarks'].message_type = _VIDEOBOOKMARK
DESCRIPTOR.message_types_by_name['CVideo_ClientGetVideoURL_Request'] = _CVIDEO_CLIENTGETVIDEOURL_REQUEST
DESCRIPTOR.message_types_by_name['CVideo_ClientGetVideoURL_Response'] = _CVIDEO_CLIENTGETVIDEOURL_RESPONSE
DESCRIPTOR.message_types_by_name['VideoBookmark'] = _VIDEOBOOKMARK
DESCRIPTOR.message_types_by_name['CVideo_SetVideoBookmark_Notification'] = _CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION
DESCRIPTOR.message_types_by_name['CVideo_GetVideoBookmarks_Request'] = _CVIDEO_GETVIDEOBOOKMARKS_REQUEST
DESCRIPTOR.message_types_by_name['CVideo_GetVideoBookmarks_Response'] = _CVIDEO_GETVIDEOBOOKMARKS_RESPONSE
DESCRIPTOR.message_types_by_name['CVideo_UnlockedH264_Notification'] = _CVIDEO_UNLOCKEDH264_NOTIFICATION
DESCRIPTOR.message_types_by_name['CFovasVideo_ClientGetOPFSettings_Request'] = _CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST
DESCRIPTOR.message_types_by_name['CFovasVideo_ClientGetOPFSettings_Response'] = _CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE

CVideo_ClientGetVideoURL_Request = _reflection.GeneratedProtocolMessageType('CVideo_ClientGetVideoURL_Request', (_message.Message,), dict(
  DESCRIPTOR = _CVIDEO_CLIENTGETVIDEOURL_REQUEST,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:CVideo_ClientGetVideoURL_Request)
  ))
_sym_db.RegisterMessage(CVideo_ClientGetVideoURL_Request)

CVideo_ClientGetVideoURL_Response = _reflection.GeneratedProtocolMessageType('CVideo_ClientGetVideoURL_Response', (_message.Message,), dict(
  DESCRIPTOR = _CVIDEO_CLIENTGETVIDEOURL_RESPONSE,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:CVideo_ClientGetVideoURL_Response)
  ))
_sym_db.RegisterMessage(CVideo_ClientGetVideoURL_Response)

VideoBookmark = _reflection.GeneratedProtocolMessageType('VideoBookmark', (_message.Message,), dict(
  DESCRIPTOR = _VIDEOBOOKMARK,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:VideoBookmark)
  ))
_sym_db.RegisterMessage(VideoBookmark)

CVideo_SetVideoBookmark_Notification = _reflection.GeneratedProtocolMessageType('CVideo_SetVideoBookmark_Notification', (_message.Message,), dict(
  DESCRIPTOR = _CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:CVideo_SetVideoBookmark_Notification)
  ))
_sym_db.RegisterMessage(CVideo_SetVideoBookmark_Notification)

CVideo_GetVideoBookmarks_Request = _reflection.GeneratedProtocolMessageType('CVideo_GetVideoBookmarks_Request', (_message.Message,), dict(
  DESCRIPTOR = _CVIDEO_GETVIDEOBOOKMARKS_REQUEST,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:CVideo_GetVideoBookmarks_Request)
  ))
_sym_db.RegisterMessage(CVideo_GetVideoBookmarks_Request)

CVideo_GetVideoBookmarks_Response = _reflection.GeneratedProtocolMessageType('CVideo_GetVideoBookmarks_Response', (_message.Message,), dict(
  DESCRIPTOR = _CVIDEO_GETVIDEOBOOKMARKS_RESPONSE,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:CVideo_GetVideoBookmarks_Response)
  ))
_sym_db.RegisterMessage(CVideo_GetVideoBookmarks_Response)

CVideo_UnlockedH264_Notification = _reflection.GeneratedProtocolMessageType('CVideo_UnlockedH264_Notification', (_message.Message,), dict(
  DESCRIPTOR = _CVIDEO_UNLOCKEDH264_NOTIFICATION,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:CVideo_UnlockedH264_Notification)
  ))
_sym_db.RegisterMessage(CVideo_UnlockedH264_Notification)

CFovasVideo_ClientGetOPFSettings_Request = _reflection.GeneratedProtocolMessageType('CFovasVideo_ClientGetOPFSettings_Request', (_message.Message,), dict(
  DESCRIPTOR = _CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:CFovasVideo_ClientGetOPFSettings_Request)
  ))
_sym_db.RegisterMessage(CFovasVideo_ClientGetOPFSettings_Request)

CFovasVideo_ClientGetOPFSettings_Response = _reflection.GeneratedProtocolMessageType('CFovasVideo_ClientGetOPFSettings_Response', (_message.Message,), dict(
  DESCRIPTOR = _CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE,
  __module__ = 'steammessages_video_pb2'
  # @@protoc_insertion_point(class_scope:CFovasVideo_ClientGetOPFSettings_Response)
  ))
_sym_db.RegisterMessage(CFovasVideo_ClientGetOPFSettings_Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))
_CVIDEO_CLIENTGETVIDEOURL_REQUEST.fields_by_name['video_id'].has_options = True
_CVIDEO_CLIENTGETVIDEOURL_REQUEST.fields_by_name['video_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\010Video ID'))
_CVIDEO_CLIENTGETVIDEOURL_REQUEST.fields_by_name['client_cellid'].has_options = True
_CVIDEO_CLIENTGETVIDEOURL_REQUEST.fields_by_name['client_cellid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\"Cell ID of client, zero if unknown'))
_CVIDEO_CLIENTGETVIDEOURL_RESPONSE.fields_by_name['video_id'].has_options = True
_CVIDEO_CLIENTGETVIDEOURL_RESPONSE.fields_by_name['video_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\010Video ID'))
_CVIDEO_CLIENTGETVIDEOURL_RESPONSE.fields_by_name['video_url'].has_options = True
_CVIDEO_CLIENTGETVIDEOURL_RESPONSE.fields_by_name['video_url']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\026URL for video manifest'))
_VIDEOBOOKMARK.fields_by_name['app_id'].has_options = True
_VIDEOBOOKMARK.fields_by_name['app_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\006App ID'))
_VIDEOBOOKMARK.fields_by_name['playback_position_in_seconds'].has_options = True
_VIDEOBOOKMARK.fields_by_name['playback_position_in_seconds']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0303How many seconds into the video the bookmark is for'))
_VIDEOBOOKMARK.fields_by_name['video_track_id'].has_options = True
_VIDEOBOOKMARK.fields_by_name['video_track_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\023video track choice.'))
_VIDEOBOOKMARK.fields_by_name['audio_track_id'].has_options = True
_VIDEOBOOKMARK.fields_by_name['audio_track_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\023audio track choice.'))
_VIDEOBOOKMARK.fields_by_name['timedtext_track_id'].has_options = True
_VIDEOBOOKMARK.fields_by_name['timedtext_track_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030#timedtimed or subtitle track choice'))
_VIDEOBOOKMARK.fields_by_name['last_modified'].has_options = True
_VIDEOBOOKMARK.fields_by_name['last_modified']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0304when we recorded it was last modified. Not settable.'))
_VIDEOBOOKMARK.fields_by_name['hide_from_watch_history'].has_options = True
_VIDEOBOOKMARK.fields_by_name['hide_from_watch_history']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030)Whether I want to show this in my history'))
_VIDEOBOOKMARK.fields_by_name['hide_from_library'].has_options = True
_VIDEOBOOKMARK.fields_by_name['hide_from_library']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030)Whether I want to show this in my library'))
_CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION.fields_by_name['bookmarks'].has_options = True
_CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION.fields_by_name['bookmarks']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030#list of bookmarks we want to store.'))
_CVIDEO_GETVIDEOBOOKMARKS_REQUEST.fields_by_name['appids'].has_options = True
_CVIDEO_GETVIDEOBOOKMARKS_REQUEST.fields_by_name['appids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030KList of App IDs to grab bookmarks for. Can be empty if using updated_since.'))
_CVIDEO_GETVIDEOBOOKMARKS_REQUEST.fields_by_name['updated_since'].has_options = True
_CVIDEO_GETVIDEOBOOKMARKS_REQUEST.fields_by_name['updated_since']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030aOnly return results after time. Min value is 1. (seconds since epoch January 1st, 1970 Unix Time)'))
_CVIDEO_GETVIDEOBOOKMARKS_RESPONSE.fields_by_name['bookmarks'].has_options = True
_CVIDEO_GETVIDEOBOOKMARKS_RESPONSE.fields_by_name['bookmarks']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030)List of bookmarks we found. Can be empty.'))
_CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST.fields_by_name['app_id'].has_options = True
_CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST.fields_by_name['app_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\006App ID'))
_CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST.fields_by_name['client_cellid'].has_options = True
_CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST.fields_by_name['client_cellid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\"Cell ID of client, zero if unknown'))
_CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE.fields_by_name['app_id'].has_options = True
_CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE.fields_by_name['app_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\006App ID'))
_CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE.fields_by_name['opf_settings'].has_options = True
_CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE.fields_by_name['opf_settings']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\031JSON blob of OPF Settings'))

_VIDEO = _descriptor.ServiceDescriptor(
  name='Video',
  full_name='Video',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\202\265\030\rVideo methods')),
  serialized_start=1686,
  serialized_end=2251,
  methods=[
  _descriptor.MethodDescriptor(
    name='ClientGetVideoURL',
    full_name='Video.ClientGetVideoURL',
    index=0,
    containing_service=None,
    input_type=_CVIDEO_CLIENTGETVIDEOURL_REQUEST,
    output_type=_CVIDEO_CLIENTGETVIDEOURL_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030.Get the initial URL to begin streaming a video')),
  ),
  _descriptor.MethodDescriptor(
    name='SetVideoBookmark',
    full_name='Video.SetVideoBookmark',
    index=1,
    containing_service=None,
    input_type=_CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION,
    output_type=steammessages__unified__base__pb2._NORESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030uBookmarks the locations in the video the user has reached. As as record playback settings per video. Fire and forget.')),
  ),
  _descriptor.MethodDescriptor(
    name='GetVideoBookmarks',
    full_name='Video.GetVideoBookmarks',
    index=2,
    containing_service=None,
    input_type=_CVIDEO_GETVIDEOBOOKMARKS_REQUEST,
    output_type=_CVIDEO_GETVIDEOBOOKMARKS_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030cReturns the video bookmarks locations for the specific videos. Includes playback settings per video')),
  ),
])

Video = service_reflection.GeneratedServiceType('Video', (_service.Service,), dict(
  DESCRIPTOR = _VIDEO,
  __module__ = 'steammessages_video_pb2'
  ))

Video_Stub = service_reflection.GeneratedServiceStubType('Video_Stub', (Video,), dict(
  DESCRIPTOR = _VIDEO,
  __module__ = 'steammessages_video_pb2'
  ))



_VIDEOCLIENT = _descriptor.ServiceDescriptor(
  name='VideoClient',
  full_name='VideoClient',
  file=DESCRIPTOR,
  index=1,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\300\265\030\002')),
  serialized_start=2254,
  serialized_end=2412,
  methods=[
  _descriptor.MethodDescriptor(
    name='NotifyUnlockedH264',
    full_name='VideoClient.NotifyUnlockedH264',
    index=0,
    containing_service=None,
    input_type=_CVIDEO_UNLOCKEDH264_NOTIFICATION,
    output_type=steammessages__unified__base__pb2._NORESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030>Notification from server to client that h264 has been unlocked')),
  ),
])

VideoClient = service_reflection.GeneratedServiceType('VideoClient', (_service.Service,), dict(
  DESCRIPTOR = _VIDEOCLIENT,
  __module__ = 'steammessages_video_pb2'
  ))

VideoClient_Stub = service_reflection.GeneratedServiceStubType('VideoClient_Stub', (VideoClient,), dict(
  DESCRIPTOR = _VIDEOCLIENT,
  __module__ = 'steammessages_video_pb2'
  ))



_FOVASVIDEO = _descriptor.ServiceDescriptor(
  name='FovasVideo',
  full_name='FovasVideo',
  file=DESCRIPTOR,
  index=2,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\202\265\030\033Fovas Video Service Methods')),
  serialized_start=2415,
  serialized_end=2658,
  methods=[
  _descriptor.MethodDescriptor(
    name='ClientGetOPFSettings',
    full_name='FovasVideo.ClientGetOPFSettings',
    index=0,
    containing_service=None,
    input_type=_CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST,
    output_type=_CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030PRetrieve the OPF settings JSON blob. Available via the Client for 360 Player App')),
  ),
])

FovasVideo = service_reflection.GeneratedServiceType('FovasVideo', (_service.Service,), dict(
  DESCRIPTOR = _FOVASVIDEO,
  __module__ = 'steammessages_video_pb2'
  ))

FovasVideo_Stub = service_reflection.GeneratedServiceStubType('FovasVideo_Stub', (FovasVideo,), dict(
  DESCRIPTOR = _FOVASVIDEO,
  __module__ = 'steammessages_video_pb2'
  ))


# @@protoc_insertion_point(module_scope)
