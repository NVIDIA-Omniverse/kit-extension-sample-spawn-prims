![](images/logo.png)

# Make an Extension To Spawn Primitives

In this document you learn how to create an Extension inside of Omniverse. Extensions are what make up Omniverse. This tutorial is ideal for those who are beginners to Omniverse Kit.

## Learning Objectives

- Create an Extension
- Use Omni Commands in Omniverse
- Make a functional Button
- Update the Extension's title and description
- Dock the Extension Window

# Prerequisites

- [Set up your environment](https://github.com/NVIDIA-Omniverse/ExtensionEnvironmentTutorial/blob/master/Tutorial.md#4-create-a-git-repository)
- Omniverse Kit 105.1.1 or higher

## Step 1: Create an Extension

Omniverse is made up of all kinds of Extensions that were created by developers. In this section, you create an Extension and learn how the code gets reflected back in Omniverse.

### Step 1.1: Navigate to the Extensions List

In Omniverse, navigate to the *Extensions* Window:

![Click the Extensions panel](images/extensions_panel.png)

> **Note:** If you don't see the *Extensions* Window, enable **Window > Extensions**:
>
> ![Show the Extensions panel](images/window_extensions.png)

### Step 1.2: Create A New Extension Template Project

Click the **plus** icon, and select ```New Extension Template Project``` to create a extension:
    
![New Extension Template Project](images/spawnprim_tutorial2.png)

### Step 1.3: Choose a Location for Your Extension

In the following prompt, select the default location for your Extension, and click **Select**:

![Create Extension](images/spawnprim_tutorial4.png)

### Step 1.4: Name your Extension

Next, name your project "kit-exts-spawn-prims":

![Project name](images/spawnprim_tutorial5.png)

And name your Extension "my.spawn_prims.ext":

![Extension name](images/spawnprim_tutorial6.png)

> **Note:** You can choose a different Extension name when publishing. For example: "companyName.extdescrip1.descrip2"  
> You **may not** use omni in your extension id. 

After this, two things happen.

First, Visual Studio Code starts up, displaying the template Extension code:

![Visual Studio Code](images/spawnprim_tutorial7.png)

Second, a new window appears in Omniverse, called "My Window":

![My window](images/spawnprim_tutorial8.png)

If you click **Add** in *My Window*, the `empty` text changes to `count: 1`, indicating that the button was clicked. Pressing **Add** again increases the number for count. Pressing **Reset** will reset it back to `empty`:

![Console log](images/spawnprim_tutorial1.gif)

You use this button later to spawn a primitive.

> **Note:** If you close out of VSCode, you can reopen the extension's code by searching for it in the Extension Window and Click the VSCode Icon. This will only work if you have VSCode installed.
> ![vscode](images/spawnprim_tutorial16.png)

## Step 2: Update Your Extension's Metadata

With the Extension created, you can update the metadata in `extension.toml`. This is metadata is used in the Extension details of the *Extensions Manager*. It's also used to inform other systems of the Application. 

### Step 2.1: Navigate to `extension.toml`

Navigate to `config/extension.toml`:

![File browser](images/spawnprim_tutorial9.png)

### Step 2.2: Name and Describe your Extension

Change the Extension's `title` and `description`:

``` python
title = "Spawn Primitives"
description="Spawns different primitives utilizing omni kit's commands"
```

Save the file and head back over into Omniverse. 

### Step 2.3: Locate the Extension

Select the *Extension* Window, search for your Extension in *Third Party* tab, and select it in the left column to pull up its details:

![Extension details](images/spawnprim_tutorial10.png)

Now that your template is created, you can start editing the source code and see it reflected in Omniverse. 

## Step 3: Update Your Extension's Interface

Currently, your window is called "My Window", and there are two buttons that says, "Add" and "Reset". In this step, you make some changes to better reflect the purpose of your Extension.

### Step 3.1: Navigate to `extension.py`

In Visual Studio Code, navigate to `ext/my.spawn_prims.ext/my/spawn_prims/ext/extension.py` to find the following source code:

``` python
import omni.ext
import omni.ui as ui


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[my.spawn_prims.ext] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MySpawn_primsExtExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[my.spawn_prims.ext] my spawn_prims ext startup")

        self._count = 0

        self._window = ui.Window("My Window", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("")


                def on_click():
                    self._count += 1
                    label.text = f"count: {self._count}"

                def on_reset():
                    self._count = 0
                    label.text = "empty"

                on_reset()

                with ui.HStack():
                    ui.Button("Add", clicked_fn=on_click)
                    ui.Button("Reset", clicked_fn=on_reset)

    def on_shutdown(self):
        print("[my.spawn_prims.ext] my spawn_prims ext shutdown")

```

Next, change some values to better reflect what your Extension does. 

### Step 3.2: Update the Window Title

Initialize `ui.Window` with the title "Spawn Primitives", instead of "My window":

``` python
self._window = ui.Window("Spawn Primitives", width=300, height=300)
```

### Step 3.3: Remove the Label and Reset Functionality

Remove the following lines and add `pass` inside `on_click()`

``` python
def on_startup(self, ext_id):
    print("[my.spawn_prims.ext] my spawn_prims ext startup")

    self._count = 0 # DELETE THIS LINE

    self._window = ui.Window("Spawn Primitives", width=300, height=300)
    with self._window.frame:
        with ui.VStack():
            label = ui.Label("") # DELETE THIS LINE


            def on_click():
                pass # ADD THIS LINE
                self._count += 1 # DELETE THIS LINE
                label.text = f"count: {self._count}" # DELETE THIS LINE

            def on_reset(): # DELETE THIS LINE
                self._count = 0 # DELETE THIS LINE
                label.text = "empty" # DELETE THIS LINE

            on_reset() # DELETE THIS LINE

            with ui.HStack():
                ui.Button("Add", clicked_fn=on_click)
                ui.Button("Reset", clicked_fn=on_reset) # DELETE THIS LINE
```

What your code should look like after removing the lines:
``` python
def on_startup(self, ext_id):
    print("[my.spawn_prims.ext] my spawn_prims ext startup")

    self._window = ui.Window("Spawn Primitives", width=300, height=300)
    with self._window.frame:
        with ui.VStack():

            def on_click():
                pass 

            with ui.HStack():
                ui.Button("Add", clicked_fn=on_click)
```


### Step 3.4: Update the Button Text

Update the `Button` text to "Spawn Cube".

``` python
ui.Button("Spawn Cube", clicked_fn=lambda: on_click())
```

### Step 3.5: Review Your Changes

After making the above changes, your code should read as follows:

``` python
import omni.ext
import omni.ui as ui


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[my.spawn_prims.ext] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MySpawn_primsExtExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[my.spawn_prims.ext] my spawn_prims ext startup")

        self._window = ui.Window("Spawn Primitives", width=300, height=300)
        with self._window.frame:
            with ui.VStack():

                def on_click():
                    pass 

                with ui.HStack():
                    ui.Button("Spawn Cube", clicked_fn=on_click)

    def on_shutdown(self):
        print("[my.spawn_prims.ext] my spawn_prims ext shutdown")

```

Save the file, and return to Omniverse. There, you'll see your new window with a large button saying "Spawn Cube".

![New window](images/spawnprim_tutorial11.png)

### Step 4: Dock the Extension Window

Omniverse allows you to move Extensions and dock them in any location. To do so, click and drag your window to the desired location.

![Drag your Extension](images/spawnprim_tutorial2.gif)

## Step 5: Prepare Your Commands Window

Commands are actions that take place inside of Omniverse. A simple command could be creating an object or changing a color. Commands are composed of a `do` and an `undo` feature. To read more about what commands are and how to create custom commands, read our [documentation](https://docs.omniverse.nvidia.com/kit/docs/omni.kit.commands/latest/Overview.html).

Omniverse allows users and developers to see what commands are being executed as they work in the application. You can find this information in the *Commands* window:

![Commands window](images/commands_window.png)

You'll use this window to quickly build out command-based functionality.

> > **Note:** If you don't see the *Commands* window, make sure it is enabled in the Extension Manager / Extension Window by searching for `omni.kit.window.commands`. Then go to **Window > Commands** :

### Step 5.1: Move Your Commands Window

Move the Commands window to get a better view, or dock it somewhere convenient:

![Move the Commands window](images/spawnprim_tutorial8.gif)

### Step 5.2: Clear Old Commands

Select the **Clear History** button in the *Commands* window. This makes it easier to see what action takes place when you try to create a cube: 

![spawnprim_tut_png12](images/spawnprim_tutorial12.png)

### Step 6: Getting the Command Code

Now that you have the necessary tools, you learn how you can grab one of these commands and use it in the extension. Specifically, you use it create a cube. There are different ways you can create the cube, but for this example, you use **Create** menu in the top bar.

### Step 6.1: Create a Cube

Click **Create > Mesh > Cube** from the top bar:

![Create a cube](images/spawnprim_tutorial3.gif)

In the *Viewport*, you'll see your new cube. In the *Commands Window*, you'll see a new command.

> **Note:** If you cannot see the Cube try adding a light to the stage. **Create > Light > Distant Light**

### Step 6.2: Copy the Create Mesh Command

Select the new line **CreateMeshPrimWithDefaultXform** in the Command Window, then click **Selected Commands** to copy the command to the clipboard:

![spawnprim_tut_png13](images/spawnprim_tutorial13.png)

### Step 6.3: Use the Command in Your Extension

Paste the copied command into the bottom of the `extension.py` file. The whole file looks like this:

``` python
import omni.ext
import omni.ui as ui

# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[my.spawn_prims.ext] some_public_function was called with x: ", x)
    return x ** x

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MySpawn_primsExtExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[my.spawn_prims.ext] my spawn_prims ext startup")

        self._window = ui.Window("Spawn Primitives", width=300, height=300)
        with self._window.frame:
            with ui.VStack():

                def on_click():
                    pass 

                with ui.HStack():
                    ui.Button("Spawn Cube", clicked_fn=on_click)

    def on_shutdown(self):
        print("[my.spawn_prims.ext] my spawn_prims ext shutdown")

import omni.kit.commands

omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
	prim_type='Cube',
	above_ground=True)
```

You added a new import and a command that creates a cube.

### Step 6.4: Group Your Imports

Move the import statement to the top of the module with the other imports:

```python
import omni.ext
import omni.ui as ui
import omni.kit.commands
```

### Step 6.5: Relocate Create Command

Place `omni.kit.commands.execute()` inside the `on_click()` definition and remove `pass`.

``` python
def on_click():
    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
        prim_type='Cube',
        above_ground=True)
```

### Step 6.6: Review and Save

Ensure your code matches ours:

``` python
import omni.ext
import omni.ui as ui
import omni.kit.commands


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[my.spawn_prims.ext] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MySpawn_primsExtExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[my.spawn_prims.ext] my spawn_prims ext startup")

        self._window = ui.Window("Spawn Primitives", width=300, height=300)
        with self._window.frame:
            with ui.VStack():

                def on_click():
                    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
                        prim_type='Cube',
                        above_ground=True)

                with ui.HStack():
                    ui.Button("Spawn Cube", clicked_fn=on_click)

    def on_shutdown(self):
        print("[my.spawn_prims.ext] my spawn_prims ext shutdown")
```

Save your code, and switch back to Omniverse.

### Step 7: Test Your Work 

In Omniverse, test your extension by clicking **Spawn Cube**. You should see that a new Cube prim is created with each button press.
 
![Spawn Cube](images/spawnprim_tutorial4.gif)

Excellent, you now know how to spawn a cube using a function. What's more, you didn't have to reference anything as Omniverse was kind enough to deliver everything you needed.

Continuing on and via same methods, construct a second button that spawns a cone in the same interface.

## Step 8: Spawn a Cone

In this step, you create a new button that spawns a cone.
### Step 8.1: Add a Button

Create a new button below the spawn cube button to spawn a cone: 

```python 
def on_startup(self, ext_id):
    print("[omni.example.spawn_prims] MyExtension startup")

    self._window = ui.Window("Spawn Primitives", width=300, height=300)
    with self._window.frame:
        with ui.VStack():

            def on_click():
                omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
                    prim_type='Cube',
                    above_ground=True)

            ui.Button("Spawn Cube", clicked_fn=lambda: on_click())
            ui.Button("Spawn Cone", clicked_fn=lambda: on_click())
```

### Step 8.2: Save and Review

Save the file, switch back to Omniverse, and test your new button:

![Incorrect mesh](images/spawnprim_tutorial5.gif)

Notice that both buttons use the same function and, therefore, both spawn a `Cube`, despite their labels.

### Step 8.3: Create a Cone from the Menu

Using the same *Create* menu in Omniverse, create a Cone (**Create > Mesh > Cone**).

### Step 8.4: Copy the Commands to your Extension

Copy the command in the *Commands* tab with the **Selected Commands** button.

### Step 8.5: Implement Your New Button

Paste the command into `extensions.py` like you did before:

![Review new button](images/spawnprim_tutorial6.gif)


``` python
def on_click():
    #Create a Cube
    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
        prim_type='Cube',
        above_ground=True)

    #Create a Cone
    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
        prim_type='Cone',
        above_ground=True)
```

Notice the command is the same, and only the `prim_type` is different:

- To spawn cube you pass `'Cube'`
- To spawn a cone you pass `'Cone'`

### Step 8.6: Accept a Prim Type in `on_click()` 

Add a `prim_type` argument to `on_click()`:

``` python
def on_click(prim_type):
```

With this value, you can delete the second `omni.kit.commands.execute()` call. Next, you'll use `prim_type` to determine what shape to create.

### Step 8.7: Use the Prim Type in `on_click()`

Replace `prim_type='Cube'` with `prim_type=prim_type`:

``` python
omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
    prim_type=prim_type,
    above_ground=True)
```

`on_click()` should now look like this:

``` python
def on_click(prim_type):
    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
        prim_type=prim_type,
        above_ground=True)
```

### Step 8.8: Pass the Prim Type to `on_click()`

Update the `clicked_fn` for both UI Buttons to pass the `prim_type`: 

``` python
ui.Button("Spawn Cube", clicked_fn=lambda: on_click("Cube"))
ui.Button("Spawn Cone", clicked_fn=lambda: on_click("Cone"))
```

### Step 8.9: Save and Test

Save the file, and test the updates to your *Spawn Primitives* Extension:

![Correct spawn](images/spawnprim_tutorial7.gif)

## Step 9: Conclusion

Great job! You've successfully created a second button that spawns a second mesh, all within the same Extension. This, of course, can be expanded upon.  

> **Optional Challenge:** Add a button for every mesh type on your own.  
> 
> ![All the buttons](images/spawnprim_tutorial15.png)
> 
> Below you can find a completed "cheat sheet" if you need help or just want to copy it for your own use.
> 
> <details> 
>     <summary><b>Click to show the final code</b></summary>
> 
> ```  
> import omni.ext
> import omni.ui as ui
> import omni.kit.commands
> 
> # Functions and vars are available to other extension as usual in python: `example.python_ext some_public_function(x)`
> def some_public_function(x: int):
>    print("[my.spawn_prims.ext] some_public_function was called with x: ", x)
>    return x ** x
>
> # Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
> # instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
> # on_shutdown() is called.
> class MyExtension(omni.ext.IExt):
>     # ext_id is current extension id. It can be used with extension manager to query additional information, like where
>     # this extension is located on filesystem.
>     def on_startup(self, ext_id):
>         print("[omni.example.spawn_prims] MyExtension startup")
> 
>         self._window = ui.Window("Spawn Primitives", width=300, height=300)
>         with self._window.frame:
>             with ui.VStack():
> 
>                 def on_click(prim_type):
>                     omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
>                         prim_type=prim_type,
>                         above_ground=True)
> 
>                 ui.Button("Spawn Cube", clicked_fn=lambda: on_click("Cube"))
>                 ui.Button("Spawn Cone", clicked_fn=lambda: on_click("Cone"))
>                 ui.Button("Spawn Cylinder", clicked_fn=lambda: on_click("Cylinder"))
>                 ui.Button("Spawn Disk", clicked_fn=lambda: on_click("Disk"))
>                 ui.Button("Spawn Plane", clicked_fn=lambda: on_click("Plane"))
>                 ui.Button("Spawn Sphere", clicked_fn=lambda: on_click("Sphere"))
>                 ui.Button("Spawn Torus", clicked_fn=lambda: on_click("Torus"))
> 
>     def on_shutdown(self):
>         print("[omni.example.spawn_prims] MyExtension shutdown")
> ```
> 
> </details>