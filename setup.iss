[Setup]
AppName=GloveDataHub
AppVersion=1.0
AppPublisher=Giovanni Fanara and Alfredo Gioacchino MariaPio Vecchio
AppPublisherURL=http://yourwebsite.com
AppSupportURL=http://yourwebsite.com/support
AppUpdatesURL=http://yourwebsite.com/updates
DefaultDirName={pf}\GloveDataHub
DefaultGroupName=GloveDataHub
OutputDir=output
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes
SetupIconFile=GUI\images\GDH_icon.ico

[Files]
Source: "dist\glovedatahub\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "GUI\images\GDH_icon.ico"; DestDir: "{app}\GUI\images"; Flags: ignoreversion

[Icons]
Name: "{group}\GloveDataHub"; Filename: "{app}\glovedatahub.exe"; IconFilename: "{app}\GUI\images\GDH_icon.ico"
Name: "{group}\Uninstall GloveDataHub"; Filename: "{uninstallexe}"
Name: "{autodesktop}\GloveDataHub"; Filename: "{app}\glovedatahub.exe"; IconFilename: "{app}\GUI\images\GDH_icon.ico"; Tasks: desktopicon

[Messages]
AppCopyright=Copyright © 2024 Giovanni Fanara and Alfredo Gioacchino MariaPio Vecchio

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Run]
Filename: "{app}\glovedatahub.exe"; Description: "{cm:LaunchProgram,GloveDataHub}"; Flags: nowait postinstall skipifsilent
