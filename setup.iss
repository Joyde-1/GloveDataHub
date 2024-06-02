[Setup]
AppName=GloveDataHub
AppVersion=1.0
DefaultDirName={pf}\GloveDataHub
DefaultGroupName=GloveDataHub
OutputDir=output
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\GloveDataHub"; Filename: "{app}\glovedatahub.exe"; IconFilename: "{app}\\GUI\\images\\GDH.ico"
Name: "{group}\Uninstall GloveDataHub"; Filename: "{uninstallexe}"
