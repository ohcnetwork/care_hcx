# Care Hcx

[![Release Status](https://img.shields.io/pypi/v/care_hcx.svg)](https://pypi.python.org/pypi/care_hcx)
[![Build Status](https://github.com/coronasafe/care_hcx/actions/workflows/build.yaml/badge.svg)](https://github.com/coronasafe/care_hcx/actions/workflows/build.yaml)

Care Hcx is a plugin for care to add voice auto fill support using external services like OpenAI whisper and Google Speech to Text.

## Features

- Voice auto fill support for care
- Support for OpenAI whisper and Google Speech to Text

## Installation

https://care-be-docs.coronasafe.network/pluggable-apps/configuration.html

https://github.com/coronasafe/care/blob/develop/plug_config.py

To install care hcx, you can add the plugin config in [care/plug_config.py](https://github.com/coronasafe/care/blob/develop/plug_config.py) as follows:

```python
...

hcx_plug = Plug(
    name="hcx",
    package_name="git+https://github.com/coronasafe/care_hcx.git",
    version="@master",
    configs={
        "HCX_PROTOCOL_BASE_PATH": "",
        "HCX_AUTH_BASE_PATH": "",
        "HCX_PARTICIPANT_CODE": "",
        "HCX_USERNAME": "",
        "HCX_PASSWORD": "",
        "HCX_ENCRYPTION_PRIVATE_KEY_URL": "",
        "HCX_IG_URL": "",
        "AUTH_USER_MODEL": "users.User"
    },
)
plugs = [hcx_plug]
...
```

## Configuration

The following configurations variables are available for Care Hcx:

- `HCX_PROTOCOL_BASE_PATH`: The base path for the HCX service.
- `HCX_AUTH_BASE_PATH`: The base path for the HCX auth service.
- `HCX_PARTICIPANT_CODE`: The participant code for the HCX service.
- `HCX_USERNAME`: The username for the HCX service.
- `HCX_PASSWORD`: The password for the HCX service.
- `HCX_ENCRYPTION_PRIVATE_KEY_URL`: The URL to get the encryption private key for the HCX service.
- `HCX_IG_URL`: The URL for the HCX IG service.
- `AUTH_USER_MODEL`: The user model to use for the HCX service.

The plugin will try to find the API key from the config first and then from the environment variable.

## License

This project is licensed under the terms of the [MIT license](LICENSE).

---

This plugin was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) using the [coronasafe/care-plugin-cookiecutter](https://github.com/coronasafe/care-plugin-cookiecutter).
