# Author-Patrick Rainsberry
# Expended with new functions for GeoSIG BOM handling
# Description-Set of Utilities for Managing Fusion 360 Projects

from .CloseAllCommand import CloseAllCommand

from .UpdateTitleBoxCommand import UpdateTitleBoxCommand
from .NewMinorVersionCommand import NewMinorVersionCommand
from .NewMajorVersionCommand import NewMajorVersionCommand
from .UpdateComponentsCommand import UpdateComponentsCommand
from .MakeAllPdfCommand import MakeAllPdfCommand


from .ArchiveCommand import ArchiveCommand
from .StatsCommand import StatsCommand

commands = []
command_definitions = []

# Define parameters for command #1
cmd = {
    'cmd_name': 'Close All Documents',
    'cmd_description': 'NOTE: This closes all documents WITHOUT prompting to save',
    'cmd_id': 'cmdID_Close_Docs',
    'cmd_resources': './resources/Icons',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'command_visible': True,
    'class': CloseAllCommand
}
command_definitions.append(cmd)

# Define parameters for command #2
cmd = {
    'cmd_name': 'Update drawing title box',
    'cmd_description': 'This will update P/N, version, project tile, ...',
    'cmd_id': 'cmdID_Update_DwgBox',
    'cmd_resources': './resources/GS_LogoMinimal',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': UpdateTitleBoxCommand
}
command_definitions.append(cmd)

# Define parameters for command #3
cmd = {
    'cmd_name': 'New Minor Version',
    'cmd_description': 'Export All files from Current Fusion 360 Project',
    'cmd_id': 'cmdID_New_Minor_Ver',
    'cmd_resources': './resources/GS_LogoMinimal',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': NewMinorVersionCommand
}
command_definitions.append(cmd)

# Define parameters for command #4
cmd = {
    'cmd_name': 'New Major Version',
    'cmd_description': 'Export All files from Current Fusion 360 Project',
    'cmd_id': 'cmdID_New_Major_Ver',
    'cmd_resources': './resources/GS_LogoMinimal',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': NewMajorVersionCommand
}
command_definitions.append(cmd)

# Define parameters for command #5
cmd = {
    'cmd_name': 'Update all assemblies and drawings',
    'cmd_description': 'Update linked components',
    'cmd_id': 'cmdID_Update_Linked_Comp',
    'cmd_resources': './resources/GS_LogoMinimal',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': UpdateComponentsCommand
}
command_definitions.append(cmd)

# Define parameters for command #6
cmd = {
    'cmd_name': 'Generate all pdf of project',
    'cmd_description': 'Export All files from Current Fusion 360 Project',
    'cmd_id': 'cmdID_Make_All_Pdf',
    'cmd_resources': './resources/GS_LogoMinimal',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': MakeAllPdfCommand
}
command_definitions.append(cmd)

# Define parameters for command #7
cmd = {
    'cmd_name': 'Archive Project',
    'cmd_description': 'Export All files from Current Fusion 360 Project',
    'cmd_id': 'cmdID_ProjectUtilities_Archive',
    'cmd_resources': './resources/Archive',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': ArchiveCommand
}
command_definitions.append(cmd)

# Define parameters for command #8
cmd = {
    'cmd_name': 'Project Statistics',
    'cmd_description': 'Get Statistics about current Fusion 360 Project',
    'cmd_id': 'cmdID_ProjectUtilities_Statistics',
    'cmd_resources': './resources/Xvm',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': StatsCommand
}
command_definitions.append(cmd)


# Set to True to display various useful messages when debugging your app
debug = False


# Don't change anything below here:
for cmd_def in command_definitions:
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)


def run(context):
    for run_command in commands:
        run_command.on_run()


def stop(context):
    for stop_command in commands:
        stop_command.on_stop()
