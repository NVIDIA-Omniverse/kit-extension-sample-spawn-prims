import omni.ext
import omni.ui as ui
import omni.kit.commands

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.example.spawn_prims] MyExtension startup")

        self._window = ui.Window("Spawn Primitives", width=300, height=300)
        with self._window.frame:
            with ui.VStack():

                def on_click(prim_type):
                    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
                        prim_type=prim_type)

                    print("clicked!")

                ui.Button("Spawn Cube", clicked_fn=lambda: on_click("Cube"))
                ui.Button("Spawn Cone", clicked_fn=lambda: on_click("Cone"))
                ui.Button("Spawn Cylinder", clicked_fn=lambda: on_click("Cylinder"))
                ui.Button("Spawn Disk", clicked_fn=lambda: on_click("Disk"))
                ui.Button("Spawn Plane", clicked_fn=lambda: on_click("Plane"))
                ui.Button("Spawn Sphere", clicked_fn=lambda: on_click("Sphere"))
                ui.Button("Spawn Torus", clicked_fn=lambda: on_click("Torus"))

    def on_shutdown(self):
        print("[omni.example.spawn_prims] MyExtension shutdown")
