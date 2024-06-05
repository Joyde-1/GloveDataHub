[Setup]
AppName=GloveDataHub
AppVersion=1.0
AppPublisher=Giovanni Fanara and Alfredo Gioacchino MariaPio Vecchio
AppPublisherURL=http://glovedatahub.it
DefaultDirName={pf}\GloveDataHub
DefaultGroupName=GloveDataHub
OutputDir=Application
OutputBaseFilename=GloveDataHub-installer
Compression=lzma
SolidCompression=yes
SetupIconFile=GUI\images\GDH_icon.ico
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "dist\glovedatahub\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "GUI\images\GDH_icon.ico"; DestDir: "{app}\GUI\images"; Flags: ignoreversion

[Icons]
Name: "{group}\GloveDataHub"; Filename: "{app}\glovedatahub.exe"; IconFilename: "{app}\GUI\images\GDH_icon.ico"
Name: "{group}\Uninstall GloveDataHub"; Filename: "{uninstallexe}"
Name: "{autodesktop}\GloveDataHub"; Filename: "{app}\glovedatahub.exe"; IconFilename: "{app}\GUI\images\GDH_icon.ico"; Tasks: desktopicon

[Messages]
AppCopyright=Copyright © GloveDataHub 2024 | All rights reserved

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Run]
Filename: "{app}\glovedatahub.exe"; Description: "{cm:LaunchProgram,GloveDataHub}"; Flags: nowait postinstall skipifsilent