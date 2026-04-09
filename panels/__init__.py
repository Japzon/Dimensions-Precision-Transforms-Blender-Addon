import bpy
from . import ui_common
from . import ui_dimensions
def register():
    ui_common.register()
    try: bpy.utils.register_class(ui_dimensions.LSD_PT_Dimensions_And_Precision_Transforms)
    except: pass
    try: bpy.utils.register_class(ui_dimensions.LSD_PT_Dimension_Group_Manager)
    except: pass
def unregister():
    try: bpy.utils.unregister_class(ui_dimensions.LSD_PT_Dimension_Group_Manager)
    except: pass
    try: bpy.utils.unregister_class(ui_dimensions.LSD_PT_Dimensions_And_Precision_Transforms)
    except: pass
    ui_common.unregister()
