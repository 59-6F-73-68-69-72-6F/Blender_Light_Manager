# Blender Light Manager 💡

<img width="1903" height="964" alt="image" src="https://github.com/user-attachments/assets/7ebbba36-bc74-4644-9817-7961dc074aaa" />

## 1. Overview

The Blender Light Manager is an add-on designed to streamline the lighting workflow within Blender. It provides a compact and intuitive user interface to manage, create, and modify all standard light types in your scene directly from a single, persistent panel. This tool is perfect for lighting artists, 3D generalists, and level designers who need to quickly iterate on lighting setups without constantly navigating the Outliner and the Object Data Properties panel.

Built with PySide6, it offers a responsive interface that integrates smoothly with your Blender workspace.

## 2. Features

*   **Comprehensive Light Listing:** Automatically lists all lights (`Point`, `Sun`, `Spot`, `Area`) in the current scene.
*   **Light Creation:** Quickly create any standard light type with a consistent, automatic naming convention (`LGT_LightName.001`).
*   **Direct Attribute Editing:** Modify common light properties directly from the UI table with real-time updates:
    *   Visibility (**Mute**/**Solo**)
    *   **Color** (via a color picker)
    *   **Exposure**
    *   **Use Temperature** & **Temperature** Value
    *   **Radius** (`shadow_soft_size`)
    *   **Shadow** visibility
*   **Live Scene Interaction:**
    *   Select a light in the UI to select it in the Blender viewport.
    *   Changes made in Blender's properties panel are reflected back in the Light Manager UI instantly.
    *   Rename and delete lights directly from the manager.
*   **Efficient Workflow Tools:**
    *   **Search:** Instantly filter the light list by name.
    *   **Refresh:** Manually update the list to reflect the current state of the scene.
    *   **Solo/Mute:** Quickly isolate a single light's contribution or toggle the visibility of multiple lights.

## 3. How to Use

### 3.1. Main Interface

The interface is divided into two main sections: creation/renaming controls at the top and the interactive light list below.

### 3.2. Creating and Managing Lights

*   **Create Light:**
    1.  Optionally, enter a base name in the **Light Name** field. If left blank, the light type will be used as the base name.
    2.  Select the desired light type from the **Light Type** dropdown (`POINT`, `SUN`, `SPOT`, `AREA`).
    3.  Click **Create Light**. A new light will be added to the scene at the 3D cursor's location with a unique name (e.g., `LGT_POINT.001`) and will appear in the list.

*   **Rename Light:**
    1.  Select a light in the table.
    2.  Enter the new base name in the **Light Name** field.
    3.  Click **Rename Light**. The light object in the scene will be renamed.

*   **Delete Light:**
    1.  Select a light in the table.
    2.  Click the **Delete** button. The light will be permanently removed from the scene.

*   **Refresh:**
    *   Click the **Refresh** button to reload the list with all lights currently in the scene. This is useful if you've made changes outside the tool, such as duplicating lights in the viewport.

*   **Search:**
    *   Type in the **Search by name** field to dynamically filter the list. The search is case-insensitive. Clear the field to see all lights again.

### 3.3. The Light Table

The core of the tool is the table, which gives you an at-a-glance view and control over your lights.

| Column | Description |
|---|---|
| **Name** | The name of the light object in Blender. Clicking a name selects the light in the scene. |
| **V (Visible)** | A checkbox to toggle the light's visibility in the viewport and render (Mute). Unchecked means hidden. |
| **S (Solo)** | A checkbox to solo a light. When checked, all other lights become invisible, allowing you to isolate its contribution. Only one light can be soloed at a time. |
| **Type** | An icon representing the light's type. |
| **Color** | A color swatch showing the light's current color. Click it to open a color picker and change the color. |
| **Exposure** | A numeric field for the light's exposure value. You can type a value or use the **mouse wheel** to adjust it. |
| **Use Temp.** | A checkbox to enable or disable temperature-based color. |
| **Temperature**| A numeric field for the light's color temperature in Kelvin. This is only active if "Use Temp." is checked. |
| **Radius** | A numeric field for the light's `shadow_soft_size`. Not applicable for Sun or Area lights. |
| **Shadow** | A checkbox to toggle the light's ability to cast shadows. |

> **Note:** Some attributes like `Radius` may show "N/A" if they are not applicable to the selected light type (e.g., a Sun Light).

## 4. Installation

### 4.1. Prerequisites

1.  **Blender**: Version 3.0 or newer.
2.  **PySide6**: This tool requires the PySide6 Python library to run its interface.

### 4.2. Installing Dependencies (PySide6)

Blender comes with its own Python environment. You need to install PySide6 into that specific environment.

1.  **Find Blender's Python Executable:**
    *   **Windows:** `C:\Program Files\Blender Foundation\Blender <version>\<version>\python\bin\python.exe`
    *   **macOS:** `/Applications/Blender.app/Contents/Resources/<version>/python/bin/python<version>`
    *   **Linux:** `/<path_to_blender>/<version>/python/bin/python<version>`

2.  **Open a Command Prompt or Terminal** as an **Administrator** (on Windows) or using `sudo` (on macOS/Linux).

3.  **Run the Installation Command:**
    Navigate to your Blender's python directory or use the full path to the python executable.

    **Example for Windows:**
    ```sh
    "C:\Program Files\Blender Foundation\Blender 4.1\4.1\python\bin\python.exe" -m pip install PySide6
    ```

    **Example for macOS:**
    ```sh
    sudo /Applications/Blender.app/Contents/Resources/4.1/python/bin/python4.1 -m pip install PySide6
    ```

    This will download and install PySide6 into Blender's Python site-packages.

### 4.3. Installing the Add-on

There are two methods to install the Blender Light Manager add-on.

#### Method 1: Install from .zip file (Recommended)

1.  Zip the entire `Blender_Light_Manager` folder (ensure the `__init__.py`, `blm_main.py`, etc., are at the root of the zip file).
2.  In Blender, go to `Edit > Preferences > Add-ons`.
3.  Click the **Install...** button at the top.
4.  Navigate to your newly created `.zip` file and select it.
5.  Find "Light Manager" in the add-on list and enable the checkbox next to it.

#### Method 2: Manual Installation

1.  Navigate to Blender's script/add-on directory. You can find the path in `Edit > Preferences > File Paths > Scripts`.
2.  Inside that directory, open the `addons` folder.
3.  Copy the entire `Blender_Light_Manager` folder into the `addons` directory.
4.  Restart Blender or go to `Edit > Preferences > Add-ons` and click "Refresh".
5.  Find "Light Manager" in the add-on list and enable the checkbox next to it.

### 4.4. How to Launch the Tool

Once the add-on is installed and enabled:

1.  Open the 3D Viewport.
2.  Press `N` to open the Sidebar (if it's not already open).
3.  Find and click on the **"Light Manager"** tab.
4.  Click the **"Open Light Manager"** button.

The Light Manager window will appear and remain on top of Blender for easy access.

