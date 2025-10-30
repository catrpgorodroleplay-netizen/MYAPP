[app]
title = My Kivy App
package.name = myapp
package.domain = org.test

version = 1.0
requirements = python3, kivy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b

android.accept_sdk_license = True
android.skip_build_app = False

android.permissions = INTERNET

[buildozer]
log_level = 2
