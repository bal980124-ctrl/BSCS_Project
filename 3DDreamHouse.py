"""
================================================================================
3D DREAM HOUSE: INTERACTIVE MODERN TROPICAL ARCHITECTURAL VISUALIZATION
Powered by URSINA Engine
================================================================================
Recreating the exact Modern Two-Storey Tropical Villa from the reference image:
- Modern Minimalist Architecture with Asymmetrical Slanted Roof
- Cantilevered 2nd-Floor Balcony with Slim Black Metal Railings & Furniture
- Ground-Floor Covered Lounge Patio with White Columns & Outdoor Sofa
- Attached Covered Carport with Concrete Driveway on Right Wing
- Decorative Organic Pond / Swimming Pool with River Rocks & Water
- Stepping Stone Path, Traveler's Palms / Banana Plants, Frangipani Trees, Lawn
- Surrounding Green Rice Paddy Fields stretching to the horizon
- Complete Furnished Ground Floor (Living, Dining, Kitchen Island, Powder Room, Stairs)
- Complete Furnished Second Floor (Master Suite, Ensuite, Bedrooms 2 & 3, Lounge, Balcony)
- Full Orbit Camera (Inspect) & First-Person Walkthrough (WASD + Mouse Look)
- Roof Cutaway & Floor Isolation (Ground, 2nd Floor, All)
- Dynamic Time of Day Lighting (Day, Golden Hour, Sunset, Night)
================================================================================
"""

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.models.procedural.cylinder import Cylinder
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader


app = Ursina(
    title="Modern Tropical Villa - 3D Architectural Visualization",
    borderless=False,
    fullscreen=False,
    size=(1280, 720),
    vsync=True
)

Entity.default_shader = lit_with_shadows_shader
window.color = color.rgb(174, 207, 226)
window.fps_counter.enabled = True


COL_WHITE_WALL   = color.hex('#e8e4da')
COL_WOOD_TEAK    = color.hex('#9a582a') 
COL_WOOD_DARK    = color.hex('#543310')
COL_ORANGE_PANEL = color.hex('#a85f3e')
COL_BLACK_METAL  = color.hex('#1e293b')
COL_GLASS        = color.hex('#294550')
COL_CONCRETE     = color.hex('#c9c8bd')
COL_GRASS        = color.hex('#527044')
COL_PADDY        = color.hex('#78934c')
COL_WATER        = color.hex('#287f91')
COL_ROCK         = color.hex('#64748b')
COL_FABRIC       = color.hex('#d6d3d1')
COL_ROOF_SLATE   = color.hex('#334155')
COL_GOLD         = color.hex('#f59e0b')

# Hierarchical Entity Groups for Cutaways
world_group        = Entity()
landscape_group    = Entity(parent=world_group)
ground_floor_group = Entity(parent=world_group)
second_floor_group = Entity(parent=world_group)
roof_group         = Entity(parent=world_group)


Entity(
    parent=landscape_group,
    model='plane',
    scale=(200, 1, 200),
    position=(0, -0.15, 0),
    color=COL_PADDY
)

# Paddy Ridges / Dikes
for offset in range(-80, 90, 40):
    Entity(parent=landscape_group, model='cube', scale=(200, 0.08, 0.4), position=(0, -0.08, offset), color=color.hex('#687646'))
    Entity(parent=landscape_group, model='cube', scale=(0.4, 0.08, 200), position=(offset, -0.08, 0), color=color.hex('#687646'))

# Residential Lot Lawn (Elevated)
lot_ground = Entity(
    parent=landscape_group,
    model='cube',
    scale=(26, 0.3, 38),
    position=(0, 0, 3),
    color=COL_GRASS,
    collider='box'
)

# Break up the lawn's broad flat color without hiding the house foundation.
Entity(
    parent=landscape_group,
    model='plane',
    scale=(25.8, 1, 37.8),
    position=(0, 0.156, 3),
    texture='grass',
    texture_scale=(18, 24),
    color=color.hex('#81936a')
)

# Concrete Driveway leading to Carport (Right side)
Entity(
    parent=landscape_group,
    model='cube',
    scale=(4.2, 0.32, 22),
    position=(4.5, 0.01, 10),
    color=COL_CONCRETE,
    collider='box'
)

for z in range(1, 21, 2):
    Entity(
        parent=landscape_group,
        model='cube',
        scale=(4.0, 0.012, 0.025),
        position=(4.5, 0.174, z),
        color=color.hex('#c5c6b8')
    )

# Rectangular Stepping Stone Walkway across lawn
for i in range(7):
    Entity(
        parent=landscape_group,
        model='cube',
        scale=(2.4, 0.34, 0.9),
        position=(-1.0, 0.01, 4.5 + i * 1.6),
        color=COL_CONCRETE
    )

# Decorative Pond / Swimming Pool (Front-left)
pool_outer = Entity(
    parent=landscape_group,
    model=Cylinder(),
    scale=(5.5, 0.5, 7.5),
    position=(-6.5, 0.1, 10),
    color=COL_ROCK
)
pool_water = Entity(
    parent=landscape_group,
    model=Cylinder(),
    scale=(5.0, 0.52, 7.0),
    position=(-6.5, 0.15, 10),
    color=COL_WATER
)

# Natural River Boulders around Pond
rock_coords = [
    (-9.5, 0.4, 7), (-9.2, 0.45, 13), (-3.8, 0.35, 7.5), (-3.5, 0.4, 11),
    (-7.5, 0.45, 13.8), (-5.2, 0.35, 13.8), (-6.5, 0.5, 6.5)
]
for rx, ry, rz in rock_coords:
    Entity(
        parent=landscape_group,
        model='sphere',
        scale=(0.9, 0.7, 0.9),
        position=(rx, ry, rz),
        color=COL_ROCK
    )

# Perimeter Fence with White Pillars & Wood Slats
# Front Left Wall
Entity(parent=landscape_group, model='cube', scale=(9, 1.4, 0.25), position=(-8.5, 0.7, 20), color=COL_ORANGE_PANEL, collider='box')
Entity(parent=landscape_group, model='cube', scale=(9.2, 0.4, 0.4), position=(-8.5, 0.2, 20), color=COL_WHITE_WALL)

# Front Wooden Entrance Gate (Slats)
gate_center = Entity(parent=landscape_group, position=(4.5, 0, 20))
Entity(parent=gate_center, model='cube', scale=(4.8, 1.6, 0.1), position=(0, 0.8, 0), color=COL_WOOD_DARK)
for gx in [-1.8, -1.2, -0.6, 0, 0.6, 1.2, 1.8]:
    Entity(parent=gate_center, model='cube', scale=(0.12, 1.5, 0.14), position=(gx, 0.8, 0), color=COL_WOOD_TEAK)

# Gate White Concrete Posts
Entity(parent=landscape_group, model='cube', scale=(0.7, 2.0, 0.7), position=(1.8, 1.0, 20), color=COL_WHITE_WALL, collider='box')
Entity(parent=landscape_group, model='cube', scale=(0.7, 2.0, 0.7), position=(7.2, 1.0, 20), color=COL_WHITE_WALL, collider='box')

# Side Fences
Entity(parent=landscape_group, model='cube', scale=(0.25, 1.4, 34), position=(12, 0.7, 4), color=COL_ORANGE_PANEL, collider='box')
Entity(parent=landscape_group, model='cube', scale=(0.25, 1.4, 34), position=(-12, 0.7, 4), color=COL_ORANGE_PANEL, collider='box')

# Tropical Plants (Traveler's Palms / Banana Plants along Driveway)
def create_banana_plant(x, z, s=1.0):
    plant = Entity(parent=landscape_group, position=(x, 0, z))
    Entity(parent=plant, model=Cylinder(), scale=(0.2*s, 1.8*s, 0.2*s), position=(0, 0.9*s, 0), color=color.hex('#3f6212'))
    for ang in [0, 45, 90, 135, 180, 225, 270, 315]:
        leaf = Entity(parent=plant, model='plane', scale=(0.8*s, 1, 2.2*s), position=(0, 1.5*s, 0), rotation=(35, ang, 0), color=color.hex('#65a30d'))
        leaf.double_sided = True

create_banana_plant(10.5, 16, 1.2)
create_banana_plant(10.8, 13, 1.0)
create_banana_plant(10.6, 9.5, 1.1)
create_banana_plant(10.7, 6, 0.9)

# Frangipani Trees near Pond & Carport
def create_frangipani(x, z):
    tree = Entity(parent=landscape_group, position=(x, 0, z))
    Entity(parent=tree, model=Cylinder(), scale=(0.25, 2.2, 0.25), position=(0, 1.1, 0), rotation=(0, 0, 8), color=color.hex('#78716c'))
    for canopy_x, canopy_y, canopy_z, canopy_scale, canopy_color in [
        (-0.35, 2.65, 0.0, 1.15, '#477a43'),
        (0.45, 2.85, 0.15, 1.2, '#56894a'),
        (0.05, 3.25, -0.2, 1.0, '#629153'),
        (0.75, 2.55, -0.15, 0.85, '#4d8146'),
    ]:
        Entity(
            parent=tree,
            model='sphere',
            scale=(canopy_scale, canopy_scale * 0.75, canopy_scale),
            position=(canopy_x, canopy_y, canopy_z),
            color=color.hex(canopy_color)
        )

create_frangipani(-8, 5)
create_frangipani(8.5, 4)

def create_planter(x, z):
    planter = Entity(parent=landscape_group, position=(x, 0, z))
    Entity(parent=planter, model='cube', scale=(1.1, 0.38, 0.62), position=(0, 0.28, 0), color=color.hex('#5b5144'))
    for leaf_x, leaf_scale in ((-0.28, 0.62), (0.25, 0.7), (0.0, 0.8)):
        Entity(
            parent=planter,
            model='sphere',
            scale=(leaf_scale, leaf_scale * 0.9, leaf_scale),
            position=(leaf_x, 0.75, 0),
            color=color.hex('#52764a')
        )

create_planter(-4.15, 3.1)
create_planter(2.45, 3.0)

# =============================================================================
# 2. HOUSE GROUND FLOOR
# =============================================================================

# Ground Floor Foundation Slab
Entity(
    parent=ground_floor_group,
    model='cube',
    scale=(9.0, 0.3, 11.5),
    position=(-0.5, 0.15, -1.5),
    color=color.hex('#f1f5f9'),
    collider='box'
)

# Covered Lounge Porch Slab (beneath balcony)
Entity(
    parent=ground_floor_group,
    model='cube',
    scale=(8.0, 0.28, 4.0),
    position=(-1.0, 0.14, 2.5),
    color=color.hex('#f1f5f9'),
    collider='box'
)

# White Support Columns (Front corners under balcony)
Entity(parent=ground_floor_group, model='cube', scale=(0.5, 3.4, 0.5), position=(-3.7, 1.85, 3.8), color=COL_WHITE_WALL, collider='box')
Entity(parent=ground_floor_group, model='cube', scale=(0.5, 3.4, 0.5), position=(1.5, 1.85, 3.8), color=COL_WHITE_WALL, collider='box')
for x in (-3.7, 1.5):
    Entity(parent=ground_floor_group, model='cube', scale=(0.22, 0.34, 0.12), position=(x, 2.45, 4.07), color=COL_BLACK_METAL)
    Entity(parent=ground_floor_group, model='cube', scale=(0.12, 0.18, 0.14), position=(x, 2.45, 4.15), color=color.hex('#f2c982'), unlit=True)

# Outdoor Lounge Furniture (Under Balcony)
lounge_grp = Entity(parent=ground_floor_group, position=(-1.0, 0.3, 2.8))
Entity(parent=lounge_grp, model='cube', scale=(2.4, 0.25, 0.9), position=(0, 0.2, 0), color=COL_WOOD_DARK)
Entity(parent=lounge_grp, model='cube', scale=(2.3, 0.2, 0.8), position=(0, 0.42, 0), color=COL_FABRIC)
Entity(parent=lounge_grp, model='cube', scale=(2.3, 0.5, 0.2), position=(0, 0.65, -0.32), color=COL_FABRIC)
Entity(parent=lounge_grp, model='cube', scale=(1.0, 0.3, 0.6), position=(0, 0.15, 0.9), color=COL_WOOD_DARK)

# Front Floor-to-Ceiling Glass Sliding Doors & Black Frames
Entity(parent=ground_floor_group, model='cube', scale=(5.2, 3.1, 0.08), position=(-1.1, 1.85, 0.8), color=COL_GLASS)
Entity(parent=ground_floor_group, model='cube', scale=(5.3, 0.08, 0.12), position=(-1.1, 3.4, 0.8), color=COL_BLACK_METAL)
Entity(parent=ground_floor_group, model='cube', scale=(5.3, 0.08, 0.12), position=(-1.1, 0.3, 0.8), color=COL_BLACK_METAL)
for fx in [-3.7, -1.9, -0.2, 1.5]:
    Entity(parent=ground_floor_group, model='cube', scale=(0.08, 3.2, 0.12), position=(fx, 1.85, 0.8), color=COL_BLACK_METAL)
Entity(parent=ground_floor_group, model='cube', scale=(5.25, 0.06, 0.14), position=(-1.1, 1.85, 0.8), color=COL_BLACK_METAL)

# Exterior Walls (Ground Floor)
Entity(parent=ground_floor_group, model='cube', scale=(0.25, 3.3, 11.5), position=(-4.9, 1.95, -1.5), color=COL_WHITE_WALL, collider='box')
Entity(parent=ground_floor_group, model='cube', scale=(9.0, 3.3, 0.25), position=(-0.5, 1.95, -7.2), color=COL_WHITE_WALL, collider='box')
Entity(parent=ground_floor_group, model='cube', scale=(0.25, 3.3, 11.5), position=(3.9, 1.95, -1.5), color=COL_WHITE_WALL, collider='box')

# Interior Partition (Powder room)
Entity(parent=ground_floor_group, model='cube', scale=(2.4, 3.3, 0.15), position=(2.6, 1.95, -1.0), color=COL_WHITE_WALL, collider='box')

# Living Room (Sofa, Coffee Table, Wood Slat TV Feature Wall, TV)
liv = Entity(parent=ground_floor_group, position=(-2.2, 0.3, -1.2))
Entity(parent=liv, model='cube', scale=(0.1, 3.0, 3.2), position=(-2.55, 1.5, 0), color=COL_WOOD_TEAK) # Wood slat wall
Entity(parent=liv, model='cube', scale=(0.06, 1.1, 2.0), position=(-2.45, 1.7, 0), color=color.hex('#0a0a0a')) # TV
Entity(parent=liv, model='cube', scale=(0.4, 0.35, 2.6), position=(-2.3, 0.5, 0), color=COL_BLACK_METAL) # Console
Entity(parent=liv, model='cube', scale=(1.0, 0.45, 2.8), position=(0.5, 0.25, 0), color=COL_FABRIC) # Sofa
Entity(parent=liv, model='cube', scale=(0.25, 0.5, 2.8), position=(1.0, 0.6, 0), color=COL_FABRIC)
Entity(parent=liv, model=Cylinder(), scale=(1.3, 0.35, 1.3), position=(-0.8, 0.2, 0), color=color.hex('#f8fafc')) # Table
Entity(parent=liv, model='cube', scale=(2.4, 0.02, 3.2), position=(-0.8, 0.01, 0), color=color.hex('#cbd5e1')) # Rug

# Dining Area
din = Entity(parent=ground_floor_group, position=(-2.2, 0.3, -4.5))
Entity(parent=din, model='cube', scale=(1.4, 0.08, 2.4), position=(0, 0.75, 0), color=COL_WOOD_DARK)
Entity(parent=din, model='cube', scale=(0.2, 0.08, 1.8), position=(0, 2.7, 0), color=COL_GOLD) # Chandelier
for dx in [-0.9, 0.9]:
    for dz in [-0.7, 0, 0.7]:
        Entity(parent=din, model='cube', scale=(0.42, 0.45, 0.42), position=(dx, 0.22, dz), color=COL_FABRIC)

# Kitchen with Island
kit = Entity(parent=ground_floor_group, position=(1.0, 0.3, -5.2))
Entity(parent=kit, model='cube', scale=(1.4, 0.9, 2.8), position=(0, 0.45, 0), color=COL_WHITE_WALL) # Waterfall island
Entity(parent=kit, model='cube', scale=(0.7, 2.8, 2.8), position=(2.4, 1.4, 0), color=COL_WOOD_TEAK) # Cabinets
for kz in [-0.8, 0, 0.8]:
    Entity(parent=kit, model=Cylinder(), scale=(0.44, 0.65, 0.44), position=(-0.95, 0.32, kz), color=COL_WOOD_DARK)

# Floating Staircase (Interior)
stairs = Entity(parent=ground_floor_group, position=(2.6, 0.3, -1.8))
for i in range(16):
    Entity(
        parent=stairs,
        model='cube',
        scale=(1.1, 0.08, 0.3),
        position=(0, i * 0.2, i * 0.24),
        color=COL_WOOD_DARK,
        collider='box'
    )

# Exterior Staircase on Left Side (Matching Photo!)
ext_stairs = Entity(parent=ground_floor_group, position=(-4.4, 0.3, 0.5))
for i in range(15):
    Entity(
        parent=ext_stairs,
        model='cube',
        scale=(0.9, 0.06, 0.28),
        position=(0, i * 0.21, 2.8 - i * 0.22),
        color=COL_WOOD_DARK,
        collider='box'
    )

# Attached Carport (Right Side)
carport = Entity(parent=ground_floor_group, position=(5.5, 0, 0))
Entity(parent=carport, model='cube', scale=(4.8, 0.35, 8.5), position=(0, 3.45, 0), color=COL_WHITE_WALL)
Entity(parent=carport, model='cube', scale=(4.85, 0.08, 8.55), position=(0, 3.25, 0), color=COL_WOOD_TEAK)
Entity(parent=carport, model='cube', scale=(0.4, 3.3, 0.4), position=(2.1, 1.65, 3.8), color=COL_WHITE_WALL, collider='box')
Entity(parent=carport, model='cube', scale=(0.4, 3.3, 0.4), position=(2.1, 1.65, -3.8), color=COL_WHITE_WALL, collider='box')
Entity(parent=carport, model='cube', scale=(0.08, 2.3, 1.2), position=(-1.5, 1.25, -2.5), color=COL_WOOD_DARK)

# =============================================================================
# 3. HOUSE SECOND FLOOR
# =============================================================================

# Second Floor Intermediate Slab
Entity(
    parent=second_floor_group,
    model='cube',
    scale=(9.0, 0.35, 11.5),
    position=(-0.5, 3.45, -1.5),
    color=color.hex('#f1f5f9'),
    collider='box'
)

# Cantilevered Front Balcony
Entity(
    parent=second_floor_group,
    model='cube',
    scale=(8.0, 0.35, 4.0),
    position=(-1.0, 3.45, 2.5),
    color=color.hex('#f1f5f9'),
    collider='box'
)

# Teak deck boards add visible material scale to the cantilevered balcony.
for board in range(12):
    Entity(
        parent=second_floor_group,
        model='cube',
        scale=(7.75, 0.035, 0.24),
        position=(-1.0, 3.65, 1.0 + board * 0.28),
        color=color.hex('#79502f') if board % 2 else color.hex('#8a6038')
    )

# Balcony Black Metal Railings
Entity(parent=second_floor_group, model='cube', scale=(7.8, 0.05, 0.05), position=(-1.0, 4.45, 4.3), color=COL_BLACK_METAL)
for bx in range(-45, 28, 4):
    Entity(parent=second_floor_group, model='cube', scale=(0.03, 1.0, 0.03), position=(bx * 0.1, 3.95, 4.3), color=COL_BLACK_METAL)
Entity(parent=second_floor_group, model='cube', scale=(0.05, 0.05, 3.5), position=(-4.8, 4.45, 2.5), color=COL_BLACK_METAL)
Entity(parent=second_floor_group, model='cube', scale=(0.05, 0.05, 3.5), position=(2.8, 4.45, 2.5), color=COL_BLACK_METAL)

# Balcony Furniture & Ceiling Fan (visible in photo)
Entity(parent=second_floor_group, model='cube', scale=(0.6, 0.6, 0.6), position=(-0.3, 3.8, 2.8), color=COL_WOOD_DARK)
Entity(parent=second_floor_group, model='cube', scale=(0.6, 0.6, 0.6), position=(-1.7, 3.8, 2.8), color=COL_WOOD_DARK)
Entity(parent=second_floor_group, model=Cylinder(), scale=(0.6, 0.45, 0.6), position=(-1.0, 3.75, 2.8), color=COL_BLACK_METAL)
fan = Entity(parent=second_floor_group, position=(-1.0, 6.4, 2.2))
Entity(parent=fan, model=Cylinder(), scale=(0.36, 0.15, 0.36), color=COL_BLACK_METAL)
for r in [0, 90, 180, 270]:
    Entity(parent=fan, model='cube', scale=(0.16, 0.02, 1.0), position=(0, 0, 0.5), rotation=(0, r, 0), color=COL_BLACK_METAL)

# Cantilevered White Architectural Framing Box
Entity(parent=second_floor_group, model='cube', scale=(8.2, 0.4, 4.2), position=(-1.0, 6.7, 2.5), color=COL_WHITE_WALL)
Entity(parent=second_floor_group, model='cube', scale=(0.4, 3.2, 4.2), position=(-4.9, 5.1, 2.5), color=COL_WHITE_WALL, collider='box')

# Upper Front Facade: Warm Teak Wood Slat Box
Entity(parent=second_floor_group, model='cube', scale=(7.6, 3.0, 0.15), position=(-1.1, 5.1, 0.8), color=COL_WOOD_TEAK)
Entity(parent=second_floor_group, model='cube', scale=(5.2, 2.6, 0.08), position=(-1.5, 4.95, 0.85), color=COL_GLASS)
for x in (-3.95, 1.05):
    Entity(parent=second_floor_group, model='cube', scale=(0.08, 2.75, 0.12), position=(x, 5.0, 0.72), color=COL_BLACK_METAL)
for x in (-3.6, -2.35, -1.1, 0.15):
    Entity(parent=second_floor_group, model='cube', scale=(0.045, 2.5, 0.1), position=(x, 4.95, 0.75), color=color.hex('#60777b'))
for side_x in (-4.65, 1.35, 1.65, 1.95, 2.25, 2.55):
    Entity(parent=second_floor_group, model='cube', scale=(0.055, 2.85, 0.12), position=(side_x, 5.1, 0.68), color=color.hex('#70401f'))
for pane_y in (5.95, 2.8):
    Entity(
        parent=second_floor_group if pane_y > 4 else ground_floor_group,
        model='cube',
        scale=(4.8 if pane_y > 4 else 4.9, 0.045, 0.025),
        position=(-1.5 if pane_y > 4 else -1.1, pane_y, 0.68),
        color=color.hex('#7895a0')
    )

# Right Side Facade: Distinctive Orange-Brown / Terracotta Accent Panel with Casement Windows
Entity(parent=second_floor_group, model='cube', scale=(0.3, 2.4, 4.0), position=(3.95, 5.2, 1.2), color=COL_ORANGE_PANEL, collider='box')
Entity(parent=second_floor_group, model='cube', scale=(0.35, 1.4, 1.6), position=(3.95, 5.2, 1.2), color=COL_BLACK_METAL)
Entity(parent=second_floor_group, model='cube', scale=(0.38, 1.25, 1.45), position=(3.95, 5.2, 1.2), color=COL_GLASS)

# Exterior Walls (2nd Floor)
Entity(parent=second_floor_group, model='cube', scale=(0.25, 3.1, 11.5), position=(-4.9, 5.1, -1.5), color=COL_WHITE_WALL, collider='box')
Entity(parent=second_floor_group, model='cube', scale=(9.0, 3.1, 0.25), position=(-0.5, 5.1, -7.2), color=COL_WHITE_WALL, collider='box')
Entity(parent=second_floor_group, model='cube', scale=(0.25, 3.1, 7.5), position=(3.9, 5.1, -3.5), color=COL_WHITE_WALL, collider='box')

# Side windows bring detail to the otherwise blank carport-side wall.
for z in (-5.0, -2.35):
    Entity(parent=ground_floor_group, model='cube', scale=(0.08, 1.35, 1.65), position=(4.04, 2.0, z), color=COL_BLACK_METAL)
    Entity(parent=ground_floor_group, model='cube', scale=(0.045, 1.2, 1.5), position=(4.09, 2.0, z), color=COL_GLASS)
    Entity(parent=ground_floor_group, model='cube', scale=(0.035, 1.32, 0.045), position=(4.12, 2.0, z), color=color.hex('#70858a'))

# Master Bedroom Suite (Bed, Nightstands, Bathtub)
master = Entity(parent=second_floor_group, position=(-2.2, 3.65, -1.2))
Entity(parent=master, model='cube', scale=(2.3, 0.4, 2.5), position=(0, 0.2, 0), color=COL_WOOD_DARK)
Entity(parent=master, model='cube', scale=(2.1, 0.35, 2.3), position=(0, 0.5, 0.05), color=color.white)
Entity(parent=master, model='cube', scale=(2.3, 1.1, 0.15), position=(0, 0.9, -1.15), color=COL_FABRIC)
Entity(parent=master, model='cube', scale=(0.5, 0.45, 0.5), position=(-1.35, 0.25, -1.0), color=COL_WOOD_DARK)
Entity(parent=master, model='cube', scale=(0.5, 0.45, 0.5), position=(1.35, 0.25, -1.0), color=COL_WOOD_DARK)
Entity(parent=master, model=Cylinder(), scale=(1.4, 0.6, 0.85), position=(1.4, 0.35, 0.2), color=color.white) # Bathtub

# Bedrooms 2 & 3
Entity(parent=second_floor_group, model='cube', scale=(1.7, 0.4, 2.1), position=(-2.8, 3.85, -5.2), color=COL_WOOD_DARK)
Entity(parent=second_floor_group, model='cube', scale=(1.6, 0.3, 2.0), position=(-2.8, 4.1, -5.2), color=color.white)
Entity(parent=second_floor_group, model='cube', scale=(1.7, 0.4, 2.1), position=(1.8, 3.85, -5.2), color=COL_WOOD_DARK)
Entity(parent=second_floor_group, model='cube', scale=(1.6, 0.3, 2.0), position=(1.8, 4.1, -5.2), color=color.white)

# =============================================================================
# 4. HOUSE ROOF (Asymmetrical Overhanging Shed Roof)
# =============================================================================
roof = Entity(parent=roof_group, position=(-0.8, 7.15, -1.5), rotation=(-1.7, 0, -2.3))

# Slate Dark Grey Top
Entity(parent=roof, model='cube', scale=(10.2, 0.28, 14.5), position=(0, 0, 0), color=COL_ROOF_SLATE)

# Warm Wood Slat Soffit (Underside of roof)
Entity(parent=roof, model='cube', scale=(10.15, 0.05, 14.45), position=(0, -0.16, 0), color=COL_WOOD_TEAK)
for slat in range(25):
    Entity(
        parent=roof,
        model='cube',
        scale=(0.035, 0.035, 14.2),
        position=(-4.8 + slat * 0.4, -0.205, 0),
        color=color.hex('#80502c') if slat % 2 else color.hex('#96643a')
    )

# Upper Front Clerestory Box in Teak Slats
Entity(parent=roof, model='cube', scale=(7.2, 0.9, 0.2), position=(-0.2, -0.6, 5.6), color=COL_WOOD_TEAK)

# =============================================================================
# 5. LIGHTING & ENVIRONMENT
# =============================================================================
lit_with_shadows_shader.default_input['shadow_color'] = color.rgba(36, 39, 45, 230)
sun = DirectionalLight(shadow_map_resolution=(2048, 2048), y=45, z=25, x=35, shadows=True)
sun.look_at(Vec3(0, 4, 1))

# Ambient lighting
ambient = AmbientLight(color=color.rgba(90, 96, 104, 255))

# Sky
sky = Sky(color=color.white)

# =============================================================================
# 6. CAMERA MODES & CONTROLLER
# =============================================================================

# Mode 1: House-centered orbit camera (arrow keys rotate around the villa)
orbit_pivot = Entity(position=(0, 4, 1), rotation=(12, 160, 0))
orbit_distance = 42

# Mode 2: First Person Walkthrough Controller
player = FirstPersonController(
    position=(4.5, 1.7, 21.5),
    speed=6,
    mouse_sensitivity=Vec2(40, 40),
    enabled=False
)
player.cursor.enabled = False

# The controller resets the shared camera, so restore the orbit view after initialization.
camera.parent = orbit_pivot
camera.position = (0, 0, -orbit_distance)
camera.rotation = Vec3.zero
camera.fov = 38

# State Management
CURRENT_MODE = "ORBIT" # "ORBIT" or "WALK"
CURRENT_TOD  = 0       # 0: Noon, 1: Golden, 2: Sunset, 3: Night
ROOF_VISIBLE = True

# =============================================================================
# 7. ON-SCREEN UI & CONTROLS HUD
# =============================================================================
title_text = Text(
    text="3D DREAM HOUSE: MODERN TROPICAL VILLA",
    position=(-0.85, 0.47),
    scale=1.2,
    color=color.hex('#ea580c')
)

status_text = Text(
    text="ORBIT: Arrow keys rotate 360° | Mouse wheel zooms",
    position=(-0.85, 0.43),
    scale=0.9,
    color=color.white
)

help_panel = Text(
    text="CONTROLS:\n[ARROWS] Rotate house view 360°\n[Mouse Wheel] Zoom in / out\n[TAB] Switch Walk / Orbit\n[R] Toggle Roof\n[1] Ground Floor | [2] 2nd Floor | [3] All\n[L] Time of Day | [H] Reset View",
    position=(-0.85, 0.20),
    scale=0.75,
    color=color.rgba(255, 255, 255, 220),
    background=True
)

def toggle_camera_mode():
    global CURRENT_MODE
    if CURRENT_MODE == "ORBIT":
        CURRENT_MODE = "WALK"
        orbit_pivot.enabled = False
        player.position = (4.5, 1.7, 21.5)
        player.look_at((4.5, 1.7, 10))
        player.enabled = True
        mouse.locked = True
        status_text.text = "Camera Mode: WALKTHROUGH (WASD: Move | Mouse: Look | Shift: Run | TAB: Exit)"
        status_text.color = color.hex('#22c55e')
    else:
        CURRENT_MODE = "ORBIT"
        player.enabled = False
        mouse.locked = False
        orbit_pivot.enabled = True
        camera.parent = orbit_pivot
        camera.position = (0, 0, -orbit_distance)
        camera.rotation = Vec3.zero
        camera.fov = 38
        status_text.text = "ORBIT: Arrow keys rotate 360° | Mouse wheel zooms"
        status_text.color = color.white

def toggle_roof():
    global ROOF_VISIBLE
    ROOF_VISIBLE = not ROOF_VISIBLE
    roof_group.enabled = ROOF_VISIBLE

def set_floor(floor_num):
    if floor_num == 1:
        ground_floor_group.enabled = True
        second_floor_group.enabled = False
        roof_group.enabled = False
    elif floor_num == 2:
        ground_floor_group.enabled = False
        second_floor_group.enabled = True
        roof_group.enabled = False
    else:
        ground_floor_group.enabled = True
        second_floor_group.enabled = True
        roof_group.enabled = ROOF_VISIBLE

def cycle_lighting():
    global CURRENT_TOD
    CURRENT_TOD = (CURRENT_TOD + 1) % 4
    if CURRENT_TOD == 0: # Tropical Noon
        sky.color = color.rgb(160, 200, 240)
        sun.color = color.white
        sun.position = (35, 45, 25)
    elif CURRENT_TOD == 1: # Golden Hour
        sky.color = color.rgb(251, 146, 60)
        sun.color = color.rgb(255, 140, 40)
        sun.position = (40, 18, 20)
    elif CURRENT_TOD == 2: # Sunset
        sky.color = color.rgb(124, 45, 18)
        sun.color = color.rgb(225, 29, 72)
        sun.position = (45, 8, 15)
    elif CURRENT_TOD == 3: # Night
        sky.color = color.rgb(5, 10, 25)
        sun.color = color.rgb(60, 90, 150)
        sun.position = (-20, 30, -20)

# On-screen Quick Action Buttons
btn_walk = Button(text="Toggle Walk/Orbit [TAB]", scale=(0.22, 0.05), position=(0.75, 0.44), color=color.hex('#ea580c'))
btn_walk.on_click = toggle_camera_mode

btn_roof = Button(text="Toggle Roof [R]", scale=(0.22, 0.05), position=(0.75, 0.37), color=color.hex('#0284c7'))
btn_roof.on_click = toggle_roof

btn_tod = Button(text="Lighting [L]", scale=(0.22, 0.05), position=(0.75, 0.30), color=color.hex('#d97706'))
btn_tod.on_click = cycle_lighting

# =============================================================================
# 8. KEYBOARD INPUT EVENT HANDLER
# =============================================================================
def input(key):
    global orbit_distance
    if key == 'tab':
        toggle_camera_mode()
    elif key == 'r':
        toggle_roof()
    elif key == '1':
        set_floor(1)
    elif key == '2':
        set_floor(2)
    elif key == '3':
        set_floor(3)
    elif key == 'l':
        cycle_lighting()
    elif key == 'h':
        if CURRENT_MODE == "ORBIT":
            orbit_pivot.rotation = (12, 160, 0)
            orbit_distance = 42
            camera.position = (0, 0, -orbit_distance)
            camera.fov = 38
        else:
            player.position = (4.5, 1.7, 21.5)
            player.look_at((4.5, 1.7, 10))
    elif CURRENT_MODE == "ORBIT" and key in ("scroll up", "scroll down"):
        orbit_distance = clamp(orbit_distance + (3 if key == "scroll down" else -3), 16, 50)
        camera.z = -orbit_distance

# Gentle water animation
def update():
    pool_water.rotation_y += time.dt * 4
    if CURRENT_MODE == "ORBIT":
        orbit_pivot.rotation_y += (held_keys["right arrow"] - held_keys["left arrow"]) * 60 * time.dt
        orbit_pivot.rotation_x = clamp(
            orbit_pivot.rotation_x + (held_keys["up arrow"] - held_keys["down arrow"]) * 40 * time.dt,
            5,
            75,
        )


app.run()
