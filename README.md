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

To add this extension to your app:

1. Download or Clone the extension, unzip the file if downloaded

2. Create a New Extension

**Linux:**
```bash
./repo.sh template new
```

**Windows:**
```powershell
.\repo.bat template new
```

3. Follow the prompt instructions:
- **? Select with arrow keys what you want to create:** Extension
- **? Select with arrow keys your desired template:**: Python UI Extension
- **? Enter name of extension [name-spaced, lowercase, alphanumeric]:**: omni.example.spawn_prims
- **? Enter extension_display_name:**: Spawn Primitives
- **? Enter version:**: 0.1.0

4. Add the Extension to an Application

In the newly created extension, **copy and paste** the `omni.example.spawn_prims` folder that was cloned into `kit-app-template/sources/extensions/omni.example.spawn_prims`.

You will be prompted if you want to replace files, **select** `Replace All`.

To add your extension to an application, declare it in the dependencies section of the application's `.kit` file:

```toml
[dependencies]
"omni.example.spawn_prims" = {}
```

5. Build with New Extensions
After a new extension has been added to the `.kit` file, the application should be rebuilt to ensure extensions are populated to the build directory.

**Linux:**
```bash
./repo.sh build
```

**Windows:**
```powershell
.\repo.bat build
```

## Contributing
The source code for this repository is provided as-is and we are not accepting outside contributions.