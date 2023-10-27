# Spawn Primitives Extension Sample

## [Spawn Primitives (omni.example.spawn_prims)](exts/omni.example.spawn_prims)

![previewImage2](exts/omni.example.spawn_prims/tutorial/images/spawnprim_tutorial7.gif)

### About
This repo shows how to build an extension in less than 10 minutes. The focus of this sample extension is to show how to create an extension and use omni.kit commands.

#### [README](exts/omni.example.spawn_prims/)
See the [README for this extension](exts/omni.example.spawn_prims/) to learn more about it including how to use it.

#### [Tutorial](exts/omni.example.spawn_prims/tutorial/tutorial.md)
Follow a [step-by-step tutorial](exts/omni.example.spawn_prims/tutorial/tutorial.md) that walks you through how to use omni.ui.scene to build this extension.

## Adding This Extension

To add this extension to your Omniverse app:
1. Go into: `Extension Manager` -> `Hamburger Icon` -> `Settings` -> `Extension Search Path`
2. Add this as a search path: `git://github.com/NVIDIA-Omniverse/kit-extension-sample-spawn-prims.git?branch=main&dir=exts`

Alternatively:
1. Download or Clone the extension, unzip the file if downloaded
2. Copy the `exts` folder path within the extension folder
    - i.e. `/home/.../kit-extension-sample-spawn-prims/exts` (Linux) or `C:/.../kit-extension-sample-spawn-prims/ext` (Windows)
3. Go into: `Extension Manager` -> `Hamburger Icon` -> `Settings` -> `Extension Search Path`
4. Add the `exts` folder path as a search path

Make sure no filter is enabled and in both cases you should be able to find the new extension in the `Third Party` tab list.

## Linking with an Omniverse app

For a better developer experience, it is recommended to create a folder link named `app` to the *Omniverse Kit* app installed from *Omniverse Launcher*. A convenience script to use is included.

Run:

```bash
# Windows
> link_app.bat
```

```shell
# Linux
~$ ./link_app.sh
```

If successful you should see `app` folder link in the root of this repo.

If multiple Omniverse apps are installed the script will select the recommended one. Or you can explicitly pass an app:

```bash
# Windows
> link_app.bat --app code
```

```shell
# Linux
~$ ./link_app.sh --app code
```

You can also pass a path that leads to the Omniverse package folder to create the link:

```bash
# Windows
> link_app.bat --path "C:/Users/bob/AppData/Local/ov/pkg/create-2022.1.3"
```

```shell
# Linux
~$ ./link_app.sh --path "home/bob/.local/share/ov/pkg/create-2022.1.3"
```

## Contributing
The source code for this repository is provided as-is and we are not accepting outside contributions.