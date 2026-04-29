#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import lib_fixups

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.fixups_blob import (
    blob_fixups_user_type,
    blob_fixup,
)
from extract_utils.module import lib_fixups_user_type

namespace_imports = [
    'hardware/qcom-caf/sm8550',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/sony/sm8550-common',
    "hardware/qcom-caf/common/libqti-perfd-client",
]

blob_fixups: blob_fixups_user_type = {
    (
	'odm/etc/customization/A301SO/config.prop',
	'odm/etc/customization/SO-51D/config.prop',
	'odm/etc/customization/SOG10_jp_kdi/config.prop',
	'odm/etc/customization/XQ-DQ44/config.prop',
	'odm/etc/customization/XQ-DQ54_EEA/config.prop',
	'odm/etc/customization/XQ-DQ62/config.prop',
	'odm/etc/customization/XQ-DQ72/config.prop',
	'odm/etc/customization/XQ-DQ72_CN/config.prop'
    ): blob_fixup().
        regex_replace('vendor', 'odm'),
    'vendor/lib64/libarcsoft_hdr_adapter.so': blob_fixup()
    .add_needed(
        'liblog.so',
    )
    .add_needed(
        'libcutils.so',
    ),
    'vendor/lib64/libcammw.so': blob_fixup()
    .replace_needed(
        'android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'
    ),
    'vendor/lib64/camx.provider-impl.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
}

module = ExtractUtilsModule(
    'pdx234',
    'sony',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8550-common', module.vendor
    )
    utils.run()
