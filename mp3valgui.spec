%define name mp3valgui
%define version 0.1.1
%define release %mkrel 4

Summary: Tool to validate and fix MPEG audio files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Sound
Url: http://mp3val.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: pygtk2.0-libglade
Requires: mp3val

%description
MP3val is a small, high-speed tool for MPEG audio files validation and
(optionally) fixing problems. It was primarily designed for
verification of MPEG 1 Layer III (MP3) files, but supports also other
MPEG versions and layers.

This is a GUI for MP3val.

%prep
%setup -q -n %name

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d %buildroot%_datadir/%name
install -m 755 mp3valgui.py %buildroot%_datadir/%name
install -m 644 mp3valgui.glade %buildroot%_datadir/%name
install -d %buildroot%_bindir
cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
exec %_datadir/%name/mp3valgui.py "\$*"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=MP3val
Comment=Validate and fix MPEG audio files
Exec=%{name}
Icon=sound_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Sound;GTK;Audio;
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS
%attr(755,root,root) %_bindir/%name
%_datadir/%name
%_datadir/applications/mandriva-%name.desktop


%changelog
* Tue Aug 02 2011 Götz Waschk <waschk@mandriva.org> 0.1.1-4mdv2012.0
+ Revision: 692726
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.1.1-3mdv2011.0
+ Revision: 252950
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.1.1-1mdv2008.1
+ Revision: 136608
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 0.1.1-1mdv2007.1
+ Revision: 13557
- Import mp3valgui



* Tue Apr 10 2007 Götz Waschk <waschk@mandriva.org> 0.1.1-1mdv2007.1
- initial package
