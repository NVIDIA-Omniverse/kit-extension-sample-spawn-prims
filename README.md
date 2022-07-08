# Spawn Primitives Extension Sample

## [Spawn Primitivies (omni.example.spawn_prims)](exts/omni.example.spawn_prims)

![previewImage2](exts/omni.example.spawn_prims/tutorial/images/spawnprim_tutorial7.gif)

### About
This extension shows how to build an extension in less than 10 minutes. The focus of this sample extension is to show how to create an extension and use omni.kit commands.

[Reference Video](https://www.youtube.com/watch?v=eGxV_PGNpOg) used as a base for this project.


### [README](exts/omni.example.spawn_prims/)
See the [README for this extension](exts/omni.example.spawn_prims/) to learn more about it including how to use it.

### [Tutorial](exts/omni.example.spawn_prims/tutorial/tutorial.md)
Follow a [step-by-step tutorial](exts/omni.example.spawn_prims/tutorial/tutorial.md) that walks you through how to use omni.ui.scene to build this extension.

## Adding This Extension

To add a this extension to your Omniverse app:
1. Go into: Extension Manager -> Gear Icon -> Extension Search Path
2. Add this as a search path: `git://github.com/NVIDIA-Omniverse/kit-extension-sample-spawn-prims.git?branch=main&dir=exts`

## Linking with an Omniverse app

For a better developer experience, it is recommended to create a folder link named `app` to the *Omniverse Kit* app installed from *Omniverse Launcher*. A convenience script to use is included.

Run:

```bash
> link_app.bat
```

There is also an analogous `link_app.sh` for Linux. If successful you should see `app` folder link in the root of this repo.

If multiple Omniverse apps is installed script will select recommended one. Or you can explicitly pass an app:

```bash
> link_app.bat --app code
```

You can also just pass a path to create link to:

```bash
> link_app.bat --path "C:/Users/bob/AppData/Local/ov/pkg/create-2022.1.3"
```

## Contributing
The source code for this repository is provided as-is and we are not accepting outside contributions.