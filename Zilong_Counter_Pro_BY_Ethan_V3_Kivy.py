name: Build Zilong Counter APK

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - name: Setup Java
        uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "17"

      - name: Setup Android SDK
        uses: android-actions/setup-android@v3

      - name: Accept Android licenses
        run: yes | sdkmanager --licenses || true

      - name: Install Android SDK packages
        run: |
          sdkmanager "platform-tools" "platforms;android-35" "build-tools;35.0.0"

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install buildozer cython

      - name: Build APK
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: zilong-counter-apk
          path: bin/*.apk
