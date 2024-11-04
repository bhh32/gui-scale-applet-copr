Name:           gui-scale-applet
Version:        2.0.0
Release:        1%{?dist}
Summary:        COSMIC Tailscale Applet

License:        BSDv3.0
URL:            https://github.com/cosmic-utils/gui-scale-applet/
Source0:        %{name}-%{version}.tar.gz

%description
COMSIC Applet for Tailscale

%prep
%autosetup

%global debug_package %{nil}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/applications/ $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/

install -Dm755 %{name} %{buildroot}%{_bindir}
install -Dm755 com.github.bhh32.GUIScaleApplet.desktop %{buildroot}%{_datadir}/applications/ 
cp tailscale-icon.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%files
%{_bindir}/%{name}
%{_datadir}/applications/com.github.bhh32.GUIScaleApplet.desktop
%{_datadir}/icons/hicolor/scalable/apps/tailscale-icon.png

%changelog
* Sun Nov 3 2024 Bryan Hyland <bryan.hyland32@gmail.com>
- Implemented TailDrop and exit node features. Updated version number to 2.0.0.
* Sat Nov 2 2024 Bryan Hyland <bryan.hyland32@gmail.com>
- Fixed bug with getting devices from updated Tailscale status command output.
* Tue Oct 8 2024 Bryan Hyland <bryan.hyland32@gmail.com>
- Updated spec file to use _buildroot macro instead of variable.
* Mon Oct 07 2024 Bryan Hyland <bryan.hyland32@gmail.com>
- Applet now has Tail Drop feature implemented
* Thu Oct 03 2024 Bryan Hyland <bryan.hyland32@gmail.com>
- Initial rpm build
