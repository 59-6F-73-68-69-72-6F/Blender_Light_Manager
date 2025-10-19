    ######################################################
    # - BLENDER LIGHT MANAGER -
    # AUTHOR : RUDY LETI
    # DATE : 2025/10/09
    # DESIGNED TO SPEED UP LIGHTING PRODUCTION PROCESS
    #
    # .LIST THE MOST COMMON BLENDER ENGINE LIGHTS
    # . NAMING CONVENTION INTEGRATED
    # . LIGHTS SELECTABLE FROM THE UI
    # . ALLOW TO MUTE OR SOLO LIGHTS
    # . ALLOW TO SEARCH LIGHTS BY NAME
    # . ALLOW TO CREATE AND RENAME LIGHTS FROM THE UI
    # . ALLOW TO DELETE LIGHTS FROM THE UI
    # . ALLOW TO MODIFY THE MOST COMMON ATTRIBUTES FROM THE UI
    ######################################################

import os
import sys

directory = r"C:\Users\Yoshi\Documents\project_python\Blender_Light_Manager"
if directory not in sys.path:
    sys.path.append(directory)

import bpy
from PySide6.QtGui import QPixmap, QColor, QPalette
from PySide6.QtWidgets import QApplication


import BlenderLightLogic as bll
import LightManagerUI as lmui

bl_info = {
    "name": "Light Manager",
    "author": "Rudy Leti",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Light Manager",
    "description": "A tool to manage lights in the scene.",
    "category": "Lighting",
}

# --- Globals to hold UI instance ---
main_window_instance = None
app_instance = None


class LaunchLightManagerOperator(bpy.types.Operator):
    """An operator to launch the Light Manager UI."""
    bl_idname = "wm.launch_light_manager"
    bl_label = "Launch Light Manager"

    def execute(self, context):
        global main_window_instance, app_instance, directory

        # Get or create the QApplication instance
        app_instance = QApplication.instance()
        if not app_instance:
            app_instance = QApplication([])

        # If window already exists, just show and activate it
        if main_window_instance and main_window_instance.isVisible():
            main_window_instance.activateWindow()
            self.report({'INFO'}, "Light Manager is already open.")
            return {'FINISHED'}

        # Create the UI and Logic instances
        ui = lmui.LightManagerUI()
        logic = bll.BlenderLightLogic(ui)

        # Store the instance globally
        main_window_instance = ui

        # LOAD LOGO IMAGE
        logo_path = os.path.join(directory, "img", "logo.png")
        if os.path.exists(logo_path):
            img = QPixmap(logo_path)
            ui.logo.setPixmap(img)
            
            
        # Apply a dark theme to the application
        app_instance.setStyle("Fusion")
        dark_palette = app_instance.palette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        app_instance.setPalette(dark_palette)
        app_instance.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

        # SET SIGNALS
        ui.signal_table_selection.connect(logic.light_table_selection)
        ui.signal_light_created.connect(logic.create_light)
        ui.signal_light_renamed.connect(logic.rename_light)
        ui.signal_light_search.connect(logic.search_light)
        ui.button_render.clicked.connect(logic.render)
        ui.signal_light_deleted.connect(logic.delete)
        ui.signal_refresh.connect(logic.refresh)
        
        # Initial refresh to populate the UI
        logic.refresh(ui.light_table)

        main_window_instance.show()
        return {'FINISHED'}

class LIGHTMAN_PT_Panel(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport sidebar"""
    bl_label = "Light Manager"
    bl_idname = "OBJECT_PT_light_manager"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Light Manager'

    def draw(self, context):
        layout = self.layout
        layout.operator(LaunchLightManagerOperator.bl_idname, text="Open Light Manager", icon='LIGHT')

def register():
    bpy.utils.register_class(LaunchLightManagerOperator)
    bpy.utils.register_class(LIGHTMAN_PT_Panel)

def unregister():
    global main_window_instance
    if main_window_instance:
        main_window_instance.close()
        main_window_instance = None
    bpy.utils.unregister_class(LaunchLightManagerOperator)
    bpy.utils.unregister_class(LIGHTMAN_PT_Panel)

if __name__ == "__main__":
    register()
