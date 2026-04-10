import bpy
from . import ui_common
from . import ui_dimensions
from .. import properties, core, operators

def register():
    # Check if core toolkit is already registered (by another module or main addon)
    # This prevents 'already registered' warnings and registration conflicts.
    core_registered = hasattr(bpy.ops.lsd, 'select_object_by_name')
    if not core_registered:
        properties.register()
        core.register()
        operators.register()
    
    ui_common.register()
    try: ui_dimensions.register()
    except: pass
    try: bpy.utils.register_class(ui_dimensions.LSD_PT_Dimensions_And_Precision_Transforms)
    except Exception as e: print(f'[LSD Standalone] Panel class registration failed: {e}')

def unregister():
    try: bpy.utils.unregister_class(ui_dimensions.LSD_PT_Dimensions_And_Precision_Transforms)
    except: pass
    try: ui_dimensions.unregister()
    except: pass
    ui_common.unregister()
    # We don't unregister core/operators here because they might be in use
    # by the main toolkit or other standalone panels. Blender handles cleanup
    # on exit or when the last module that actually registered them is disabled.

