import os
import shutil
import arm.assets as assets
import arm.utils
import bpy
from bpy.types import Menu, Panel, UIList
from bpy.props import *

def update_preset(self, context):
    rpdat = arm.utils.get_rp()
    if self.rp_preset == 'Low':
        rpdat.rp_renderer = 'Forward'
        rpdat.rp_depthprepass = False
        rpdat.arm_material_model = 'Full'
        rpdat.rp_shadowmap = '1024'
        rpdat.rp_shadowmap_cascades = '1'
        rpdat.rp_translucency_state = 'Off'
        rpdat.rp_overlays_state = 'Off'
        rpdat.rp_decals_state = 'Off'
        rpdat.rp_sss_state = 'Off'
        rpdat.rp_blending_state = 'Off'
        rpdat.rp_hdr = False
        rpdat.rp_background = 'World'
        rpdat.rp_stereo = False
        # rpdat.rp_greasepencil = False
        rpdat.rp_gi = 'Off'
        rpdat.rp_render_to_texture = False
        rpdat.rp_supersampling = '1'
        rpdat.rp_antialiasing = 'Off'
        rpdat.rp_compositornodes = False
        rpdat.rp_volumetriclight = False
        rpdat.rp_ssgi = 'Off'
        rpdat.rp_ssr = False
        rpdat.rp_dfrs = False
        rpdat.rp_dfao = False
        rpdat.rp_dfgi = False
        rpdat.rp_bloom = False
        rpdat.rp_eyeadapt = False
        rpdat.rp_rendercapture = False
        rpdat.rp_motionblur = 'Off'
        rpdat.arm_rp_resolution = 'Display'
        rpdat.arm_texture_filter = 'Linear'
        rpdat.arm_diffuse_model = 'Lambert'
    elif self.rp_preset == 'Forward':
        rpdat.rp_renderer = 'Forward'
        rpdat.rp_depthprepass = True
        rpdat.arm_material_model = 'Full'
        rpdat.rp_shadowmap = '1024'
        rpdat.rp_shadowmap_cascades = '4'
        rpdat.rp_translucency_state = 'Auto'
        rpdat.rp_overlays_state = 'Auto'
        rpdat.rp_decals_state = 'Auto'
        rpdat.rp_sss_state = 'Auto'
        rpdat.rp_blending_state = 'Off'
        rpdat.rp_hdr = True
        rpdat.rp_background = 'World'
        rpdat.rp_stereo = False
        # rpdat.rp_greasepencil = False
        rpdat.rp_gi = 'Off'
        rpdat.rp_render_to_texture = True
        rpdat.rp_supersampling = '1'
        rpdat.rp_antialiasing = 'SMAA'
        rpdat.rp_compositornodes = True
        rpdat.rp_volumetriclight = False
        rpdat.rp_ssgi = 'SSAO'
        rpdat.rp_ssr = True
        rpdat.rp_dfrs = False
        rpdat.rp_dfao = False
        rpdat.rp_dfgi = False
        rpdat.rp_bloom = False
        rpdat.rp_eyeadapt = False
        rpdat.rp_rendercapture = False
        rpdat.rp_motionblur = 'Off'
        rpdat.arm_rp_resolution = 'Display'
        rpdat.arm_texture_filter = 'Anisotropic'
        rpdat.arm_diffuse_model = 'Lambert'
    elif self.rp_preset == 'Deferred':
        rpdat.rp_renderer = 'Deferred'
        rpdat.arm_material_model = 'Full'
        rpdat.rp_shadowmap = '1024'
        rpdat.rp_shadowmap_cascades = '4'
        rpdat.rp_translucency_state = 'Auto'
        rpdat.rp_overlays_state = 'Auto'
        rpdat.rp_decals_state = 'Auto'
        rpdat.rp_sss_state = 'Auto'
        rpdat.rp_blending_state = 'Off'
        rpdat.rp_hdr = True
        rpdat.rp_background = 'World'
        rpdat.rp_stereo = False
        # rpdat.rp_greasepencil = False
        rpdat.rp_gi = 'Off'
        rpdat.rp_render_to_texture = True
        rpdat.rp_supersampling = '1'
        rpdat.rp_antialiasing = 'FXAA'
        rpdat.rp_compositornodes = True
        rpdat.rp_volumetriclight = False
        rpdat.rp_ssgi = 'SSAO'
        rpdat.rp_ssr = False
        rpdat.rp_dfrs = False
        rpdat.rp_dfao = False
        rpdat.rp_dfgi = False
        rpdat.rp_bloom = False
        rpdat.rp_eyeadapt = False
        rpdat.rp_rendercapture = False
        rpdat.rp_motionblur = 'Off'
        rpdat.arm_rp_resolution = 'Display'
        rpdat.arm_texture_filter = 'Anisotropic'
        rpdat.arm_diffuse_model = 'Lambert'
    elif self.rp_preset == 'Max (Render)':
        rpdat.rp_renderer = 'Deferred'
        rpdat.rp_shadowmap = '8192'
        rpdat.rp_shadowmap_cascades = '1'
        rpdat.rp_translucency_state = 'Auto'
        rpdat.rp_overlays_state = 'Auto'
        rpdat.rp_decals_state = 'Auto'
        rpdat.rp_sss_state = 'Auto'
        rpdat.rp_blending_state = 'Off'
        rpdat.rp_hdr = True
        rpdat.rp_background = 'World'
        rpdat.rp_stereo = False
        # rpdat.rp_greasepencil = False
        rpdat.rp_gi = 'Voxel GI'
        rpdat.rp_voxelgi_resolution = '256'
        rpdat.rp_voxelgi_emission = True
        rpdat.rp_render_to_texture = True
        rpdat.rp_supersampling = '2'
        rpdat.rp_antialiasing = 'TAA'
        rpdat.rp_compositornodes = True
        rpdat.rp_volumetriclight = False
        rpdat.rp_ssgi = 'RTGI'
        rpdat.rp_ssr = True
        rpdat.arm_ssr_half_res = False
        rpdat.rp_dfrs = False
        rpdat.rp_dfao = False
        rpdat.rp_dfgi = False
        rpdat.rp_bloom = True
        rpdat.rp_eyeadapt = False
        rpdat.rp_rendercapture = True
        rpdat.rp_motionblur = 'Off'
        rpdat.arm_rp_resolution = 'Display'
        rpdat.arm_material_model = 'Full'
        rpdat.arm_texture_filter = 'Anisotropic'
        rpdat.arm_diffuse_model = 'OrenNayar'
    elif self.rp_preset == 'VR':
        rpdat.rp_renderer = 'Forward'
        rpdat.rp_depthprepass = False
        rpdat.arm_material_model = 'Mobile'
        rpdat.rp_shadowmap = '1024'
        rpdat.rp_shadowmap_cascades = '1'
        rpdat.rp_translucency_state = 'Off'
        rpdat.rp_overlays_state = 'Off'
        rpdat.rp_decals_state = 'Off'
        rpdat.rp_sss_state = 'Off'
        rpdat.rp_blending_state = 'Off'
        rpdat.rp_hdr = False
        rpdat.rp_background = 'World'
        rpdat.rp_stereo = True
        # rpdat.rp_greasepencil = False
        rpdat.rp_gi = 'Off'
        rpdat.rp_render_to_texture = False
        rpdat.rp_supersampling = '1'
        rpdat.rp_antialiasing = 'Off'
        rpdat.rp_compositornodes = False
        rpdat.rp_volumetriclight = False
        rpdat.rp_ssgi = 'Off'
        rpdat.rp_ssr = False
        rpdat.rp_dfrs = False
        rpdat.rp_dfao = False
        rpdat.rp_dfgi = False
        rpdat.rp_bloom = False
        rpdat.rp_eyeadapt = False
        rpdat.rp_rendercapture = False
        rpdat.rp_motionblur = 'Off'
        rpdat.arm_rp_resolution = 'Display'
        rpdat.arm_texture_filter = 'Point'
        rpdat.arm_diffuse_model = 'Lambert'
    elif self.rp_preset == 'Mobile':
        rpdat.rp_renderer = 'Forward'
        rpdat.rp_depthprepass = False
        rpdat.arm_material_model = 'Mobile'
        rpdat.rp_shadowmap = '1024'
        rpdat.rp_shadowmap_cascades = '1'
        rpdat.rp_translucency_state = 'Off'
        rpdat.rp_overlays_state = 'Off'
        rpdat.rp_decals_state = 'Off'
        rpdat.rp_sss_state = 'Off'
        rpdat.rp_blending_state = 'Off'
        rpdat.rp_hdr = False
        rpdat.rp_background = 'Clear'
        rpdat.rp_stereo = False
        # rpdat.rp_greasepencil = False
        rpdat.rp_gi = 'Off'
        rpdat.rp_render_to_texture = False
        rpdat.rp_supersampling = '1'
        rpdat.rp_antialiasing = 'Off'
        rpdat.rp_compositornodes = False
        rpdat.rp_volumetriclight = False
        rpdat.rp_ssgi = 'Off'
        rpdat.rp_ssr = False
        rpdat.rp_dfrs = False
        rpdat.rp_dfao = False
        rpdat.rp_dfgi = False
        rpdat.rp_bloom = False
        rpdat.rp_eyeadapt = False
        rpdat.rp_rendercapture = False
        rpdat.rp_motionblur = 'Off'
        rpdat.arm_rp_resolution = 'Display'
        rpdat.arm_texture_filter = 'Linear'
        rpdat.arm_diffuse_model = 'Lambert'
    elif self.rp_preset == 'Max (Game)':
        rpdat.rp_renderer = 'Deferred'
        rpdat.rp_shadowmap = '4096'
        rpdat.rp_shadowmap_cascades = '4'
        rpdat.rp_translucency_state = 'Auto'
        rpdat.rp_overlays_state = 'Auto'
        rpdat.rp_decals_state = 'Auto'
        rpdat.rp_sss_state = 'Auto'
        rpdat.rp_blending_state = 'Off'
        rpdat.rp_hdr = True
        rpdat.rp_background = 'World'
        rpdat.rp_stereo = False
        # rpdat.rp_greasepencil = False
        rpdat.rp_gi = 'Voxel GI'
        rpdat.rp_voxelgi_resolution = '128'
        rpdat.arm_voxelgi_revoxelize = False
        rpdat.arm_voxelgi_camera = False
        rpdat.rp_voxelgi_emission = False
        rpdat.rp_render_to_texture = True
        rpdat.rp_supersampling = '1'
        rpdat.rp_antialiasing = 'TAA'
        rpdat.rp_compositornodes = True
        rpdat.rp_volumetriclight = False
        rpdat.rp_ssgi = 'RTGI'
        rpdat.arm_ssrs = False
        rpdat.rp_ssr = True
        rpdat.rp_dfrs = False
        rpdat.rp_dfao = False
        rpdat.rp_dfgi = False
        rpdat.rp_bloom = True
        rpdat.rp_eyeadapt = False
        rpdat.rp_rendercapture = False
        rpdat.rp_motionblur = 'Off'
        rpdat.arm_rp_resolution = 'Display'
        rpdat.arm_material_model = 'Full'
        rpdat.arm_texture_filter = 'Anisotropic'
        rpdat.arm_diffuse_model = 'Lambert'
    update_renderpath(self, context)

def update_renderpath(self, context):
    if assets.invalidate_enabled == False:
        return
    assets.invalidate_shader_cache(self, context)
    bpy.data.worlds['Arm'].arm_recompile = True

def udpate_shadowmap_cascades(self, context):
    bpy.data.worlds['Arm'].arm_recompile = True
    update_renderpath(self, context)

def update_material_model(self, context):
    assets.invalidate_shader_cache(self, context)
    update_renderpath(self, context)

def update_translucency_state(self, context):
    if self.rp_translucency_state == 'On':
        self.rp_translucency = True
    elif self.rp_translucency_state == 'Off':
        self.rp_translucency = False
    else: # Auto - updates rp at build time if translucent mat is used
        return
    update_renderpath(self, context)

def update_decals_state(self, context):
    if self.rp_decals_state == 'On':
        self.rp_decals = True
    elif self.rp_decals_state == 'Off':
        self.rp_decals = False
    else: # Auto - updates rp at build time if decal mat is used
        return
    update_renderpath(self, context)

def update_overlays_state(self, context):
    if self.rp_overlays_state == 'On':
        self.rp_overlays = True
    elif self.rp_overlays_state == 'Off':
        self.rp_overlays = False
    else: # Auto - updates rp at build time if x-ray mat is used
        return
    update_renderpath(self, context)

def update_sss_state(self, context):
    if self.rp_sss_state == 'On':
        self.rp_sss = True
    elif self.rp_sss_state == 'Off':
        self.rp_sss = False
    else: # Auto - updates rp at build time if sss mat is used
        return
    update_renderpath(self, context)

class ArmRPListItem(bpy.types.PropertyGroup):
    name = StringProperty(
           name="Name",
           description="A name for this item",
           default="Path")

    rp_driver_list = CollectionProperty(type=bpy.types.PropertyGroup)
    rp_driver = StringProperty(name="Driver", default="Armory", update=assets.invalidate_compiled_data)
    rp_renderer = EnumProperty(
        items=[('Forward', 'Forward', 'Forward'),
               ('Deferred', 'Deferred', 'Deferred'),
               # ('Deferred Plus', 'Deferred Plus', 'Deferred Plus'),
               ],
        name="Renderer", description="Renderer type", default='Deferred', update=update_renderpath)
    rp_depthprepass = BoolProperty(name="Depth Prepass", description="Depth Prepass for mesh context", default=True, update=update_renderpath)
    rp_hdr = BoolProperty(name="HDR", description="Render in HDR Space", default=True, update=update_renderpath)
    rp_render_to_texture = BoolProperty(name="Post Process", description="Render scene to texture for further processing", default=True, update=update_renderpath)
    rp_background = EnumProperty(
      items=[('World', 'World', 'World'),
             ('Clear', 'Clear', 'Clear'),
             ('Off', 'Off', 'Off'),
      ],
      name="Background", description="Background type", default='World', update=update_renderpath)    
    rp_autoexposure = BoolProperty(name="Auto Exposure", description="Adjust exposure based on luminance", default=False, update=update_renderpath)
    rp_compositornodes = BoolProperty(name="Compositor", description="Draw compositor nodes", default=True, update=update_renderpath)
    rp_shadowmap = EnumProperty(
        items=[('Off', 'Off', 'Off'),
               ('512', '512', '512'),
               ('1024', '1024', '1024'),
               ('2048', '2048', '2048'),
               ('4096', '4096', '4096'),
               ('8192', '8192', '8192'),
               ('16384', '16384', '16384'),],
        name="Shadow Map", description="Shadow map resolution", default='1024', update=update_renderpath)
    rp_shadowmap_cascades = EnumProperty(
        items=[('1', '1', '1'),
               ('2', '2', '2'),
               # ('3', '3', '3'),
               ('4', '4', '4')],
        name="Cascades", description="Shadow map cascades", default='4', update=udpate_shadowmap_cascades)
    rp_supersampling = EnumProperty(
        items=[('1', '1', '1'),
               ('1.5', '1.5', '1.5'),
               ('2', '2', '2'),
               ('4', '4', '4')],
        name="Super Sampling", description="Screen resolution multiplier", default='1', update=update_renderpath)
    rp_antialiasing = EnumProperty(
        items=[('Off', 'Off', 'Off'),
               ('FXAA', 'FXAA', 'FXAA'),
               ('SMAA', 'SMAA', 'SMAA'),
               ('TAA', 'TAA', 'TAA')],
        name="Anti Aliasing", description="Post-process anti aliasing technique", default='SMAA', update=update_renderpath)
    rp_volumetriclight = BoolProperty(name="Volumetric Light", description="Use volumetric lighting", default=False, update=update_renderpath)
    rp_ssr = BoolProperty(name="SSR", description="Screen space reflections", default=False, update=update_renderpath)
    rp_ssgi = EnumProperty(
        items=[('Off', 'Off', 'Off'),
               ('SSAO', 'SSAO', 'Screen space ambient occlusion'),
               ('RTAO', 'Ray-traced AO', 'Ray-traced ambient occlusion'),
               ('RTGI', 'Ray-traced GI', 'Ray-traced global illumination')
               ],
        name="SSGI", description="Screen space global illumination", default='SSAO', update=update_renderpath)
    rp_dfao = BoolProperty(name="DFAO", description="Distance field ambient occlusion", default=False)
    rp_dfrs = BoolProperty(name="DFRS", description="Distance field ray-traced shadows", default=False)
    rp_dfgi = BoolProperty(name="DFGI", description="Distance field global illumination", default=False)
    rp_bloom = BoolProperty(name="Bloom", description="Bloom processing", default=False, update=update_renderpath)
    rp_eyeadapt = BoolProperty(name="Eye Adaptation", description="Auto-exposure based on histogram", default=False, update=update_renderpath)
    rp_rendercapture = BoolProperty(name="Render Capture", description="Save output as render result", default=False, update=update_renderpath)
    rp_motionblur = EnumProperty(
        items=[('Off', 'Off', 'Off'),
               ('Camera', 'Camera', 'Camera'),
               ('Object', 'Object', 'Object')],
        name="Motion Blur", description="Velocity buffer is used for object based motion blur", default='Off', update=update_renderpath)
    rp_translucency = BoolProperty(name="Translucency", description="Current render-path state", default=False)
    rp_translucency_state = EnumProperty(
        items=[('On', 'On', 'On'),
               ('Off', 'Off', 'Off'), 
               ('Auto', 'Auto', 'Auto')],
        name="Translucency", description="Order independent translucency", default='Auto', update=update_translucency_state)
    rp_decals = BoolProperty(name="Decals", description="Current render-path state", default=False)
    rp_decals_state = EnumProperty(
        items=[('On', 'On', 'On'),
               ('Off', 'Off', 'Off'), 
               ('Auto', 'Auto', 'Auto')],
        name="Decals", description="Decals pass", default='Auto', update=update_decals_state)
    rp_overlays = BoolProperty(name="Overlays", description="Current render-path state", default=False)
    rp_overlays_state = EnumProperty(
        items=[('On', 'On', 'On'),
               ('Off', 'Off', 'Off'), 
               ('Auto', 'Auto', 'Auto')],
        name="Overlays", description="X-Ray pass", default='Auto', update=update_overlays_state)
    rp_sss = BoolProperty(name="SSS", description="Current render-path state", default=False)
    rp_sss_state = EnumProperty(
        items=[('On', 'On', 'On'),
               ('Off', 'Off', 'Off'),
               ('Auto', 'Auto', 'Auto')],
        name="SSS", description="Sub-surface scattering pass", default='Auto', update=update_sss_state)
    rp_blending_state = EnumProperty(
        items=[('On', 'On', 'On'),
               ('Off', 'Off', 'Off')],
        name="Blending", description="Additive blending pass", default='Off', update=update_renderpath)
    rp_stereo = BoolProperty(name="Stereo", description="Stereo rendering", default=False, update=update_renderpath)
    rp_greasepencil = BoolProperty(name="Grease Pencil", description="Render Grease Pencil data", default=False, update=update_renderpath)
    rp_ocean = BoolProperty(name="Ocean", description="Ocean pass", default=False, update=update_renderpath)
    
    rp_gi = EnumProperty(
        items=[('Off', 'Off', 'Off'),
               ('Voxel GI', 'Voxel GI', 'Voxel GI'),
               ('Voxel AO', 'Voxel AO', 'Voxel AO')
               ],
        name="Global Illumination", description="Dynamic global illumination", default='Off', update=update_renderpath)
    rp_voxelgi_resolution = EnumProperty(
        items=[('32', '32', '32'),
               ('64', '64', '64'),
               ('128', '128', '128'),
               ('256', '256', '256'),
               ('512', '512', '512')],
        name="Resolution", description="3D texture resolution", default='128', update=update_renderpath)
    rp_voxelgi_resolution_z = EnumProperty(
        items=[('1.0', '1.0', '1.0'),
               ('0.5', '0.5', '0.5'),
               ('0.25', '0.25', '0.25')],
        name="Resolution Z", description="3D texture z resolution multiplier", default='1.0', update=update_renderpath)
    arm_clouds = BoolProperty(name="Clouds", default=False, update=assets.invalidate_shader_cache)
    arm_soft_shadows = EnumProperty(
        items=[('On', 'On', 'On'),
               ('Off', 'Off', 'Off'), 
               ('Auto', 'Auto', 'Auto')],
        name="Soft Shadows", description="Soft shadows with variable penumbra (spot and non-cascaded sun lamp supported)", default='Off', update=assets.invalidate_shader_cache)
    arm_soft_shadows_penumbra = IntProperty(name="Penumbra", description="Variable penumbra scale", default=1, min=0, max=10, update=assets.invalidate_shader_cache)
    arm_soft_shadows_distance = FloatProperty(name="Distance", description="Variable penumbra distance", default=1.0, min=0, max=10, update=assets.invalidate_shader_cache)
    arm_ssrs = BoolProperty(name="SSRS", description="Screen-space ray-traced shadows", default=False, update=assets.invalidate_shader_cache)
    arm_texture_filter = EnumProperty(
        items=[('Anisotropic', 'Anisotropic', 'Anisotropic'),
               ('Linear', 'Linear', 'Linear'), 
               ('Point', 'Closest', 'Point'), 
               ('Manual', 'Manual', 'Manual')],
        name="Texture Filtering", description="Set Manual to honor interpolation setting on Image Texture node", default='Anisotropic')
    arm_material_model = EnumProperty(
        items=[('Full', 'Full', 'Full'),
               ('Mobile', 'Mobile', 'Mobile'),
               ('Solid', 'Solid', 'Solid'),
               ],
        name="Materials", description="Material builder", default='Full', update=update_material_model)
    arm_diffuse_model = EnumProperty(
        items=[('Lambert', 'Lambert', 'Lambert'),
               ('OrenNayar', 'OrenNayar', 'OrenNayar'),
               ],
        name="Diffuse", description="Diffuse model", default='Lambert', update=assets.invalidate_shader_cache)
    arm_displacement = BoolProperty(name="Displacement", description="Enable tessellated displacement for height maps", default=True, update=assets.invalidate_shader_cache)
    arm_rp_resolution = EnumProperty(
        items=[('Display', 'Display', 'Display'),
               ('480', '480p', '480p'),
               ('720', '720p', '720p'),
               ('1080', '1080p', '1080p'),
               ('1440', '1440p', '1440p'),
               ('2160', '2160p', '2160p')],
        name="Resolution", description="Render at specific resolution, regardless of display resolution", default='Display', update=update_renderpath)
    rp_dynres = BoolProperty(name="Dynamic Resolution", description="Dynamic resolution scaling for performance", default=False, update=update_renderpath)
    arm_ssr_half_res = BoolProperty(name="Half Res", description="Trace in half resolution", default=True, update=update_renderpath)
    rp_voxelgi_hdr = BoolProperty(name="HDR Voxels", description="Store voxels in RGBA64 instead of RGBA32", default=False, update=update_renderpath)
    arm_voxelgi_dimensions = FloatProperty(name="Dimensions", description="Voxelization bounds",default=16, update=assets.invalidate_shader_cache)
    arm_voxelgi_revoxelize = BoolProperty(name="Revoxelize", description="Revoxelize scene each frame", default=False, update=assets.invalidate_shader_cache)
    arm_voxelgi_temporal = BoolProperty(name="Temporal Filter", description="Use temporal filtering to stabilize voxels", default=False, update=assets.invalidate_shader_cache)
    arm_voxelgi_bounces = EnumProperty(
        items=[('1', '1', '1'),
               ('2', '2', '2')],
        name="Bounces", description="Trace multiple light bounces", default='1', update=update_renderpath)
    arm_voxelgi_camera = BoolProperty(name="Dynamic Camera", description="Use camera as voxelization origin", default=False, update=assets.invalidate_shader_cache)
    # arm_voxelgi_anisotropic = BoolProperty(name="Anisotropic", description="Use anisotropic voxels", default=False, update=update_renderpath)
    arm_voxelgi_shadows = BoolProperty(name="Trace Shadows", description="Use voxels to render shadows", default=False, update=update_renderpath)
    arm_voxelgi_refraction = BoolProperty(name="Trace Refraction", description="Use voxels to render refraction", default=False, update=update_renderpath)
    arm_voxelgi_emission = BoolProperty(name="Emission Voxels", description="Encode emission into voxelized data", default=False, update=update_renderpath)
    arm_samples_per_pixel = EnumProperty(
        items=[('1', '1', '1'),
               ('2', '2', '2'),
               ('4', '4', '4'),
               ('8', '8', '8'),
               ('16', '16', '16')],
        name="MSAA", description="Samples per pixel usable for render paths drawing directly to framebuffer", default='1')  
    arm_ssao_half_res = BoolProperty(name="Half Res", description="Trace in half resolution", default=False, update=assets.invalidate_shader_cache)

class ArmRPList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        custom_icon = 'OBJECT_DATAMODE'

        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            row = layout.row()
            row.prop(item, "name", text="", emboss=False, icon=custom_icon)

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label("", icon = custom_icon)

class ArmRPListNewItem(bpy.types.Operator):
    # Add a new item to the list
    bl_idname = "arm_rplist.new_item"
    bl_label = "Add a new item"

    def execute(self, context):
        mdata = bpy.data.worlds['Arm']
        mdata.arm_rplist.add()
        mdata.arm_rplist_index = len(mdata.arm_rplist) - 1
        return{'FINISHED'}


class ArmRPListDeleteItem(bpy.types.Operator):
    # Delete the selected item from the list
    bl_idname = "arm_rplist.delete_item"
    bl_label = "Deletes an item"

    @classmethod
    def poll(self, context):
        """ Enable if there's something in the list """
        mdata = bpy.data.worlds['Arm']
        return len(mdata.arm_rplist) > 0

    def execute(self, context):
        mdata = bpy.data.worlds['Arm']
        list = mdata.arm_rplist
        index = mdata.arm_rplist_index

        list.remove(index)

        if index > 0:
            index = index - 1

        mdata.arm_rplist_index = index
        return{'FINISHED'}

def register():
    bpy.utils.register_class(ArmRPListItem)
    bpy.utils.register_class(ArmRPList)
    bpy.utils.register_class(ArmRPListNewItem)
    bpy.utils.register_class(ArmRPListDeleteItem)

    bpy.types.World.arm_rplist = CollectionProperty(type=ArmRPListItem)
    bpy.types.World.arm_rplist_index = IntProperty(name="Index for my_list", default=0, update=update_renderpath)

def unregister():
    bpy.utils.unregister_class(ArmRPListItem)
    bpy.utils.unregister_class(ArmRPList)
    bpy.utils.unregister_class(ArmRPListNewItem)
    bpy.utils.unregister_class(ArmRPListDeleteItem)
