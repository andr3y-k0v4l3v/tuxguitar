Name: tuxguitar
Version: 1.5.6
Release: alt1

Summary: A multitrack guitar tablature editor and player
License: LGPL
Group: Sound

Url: http://www.tuxguitar.com.ar/

Source0: %name-%version.tar
Source1: m2-repository-%name-%version.tar
Source2: pluginterfaces-%name-%version.tar
Source3: %name.sh
Source9: %name.desktop

Patch0: tuxguitar-%version-synth-vst-fix.patch

Requires: java-17-openjdk
Requires: javapackages-filesystem
Requires: glibc libfluidsynth pipewire-jack-libs libalsa soundfont2 lilv
BuildRequires: eclipse-swt java-17-openjdk-devel java-headless
BuildRequires: javapackages-filesystem maven glibc libfluidsynth-devel
BuildRequires: libjack-devel libalsa-devel soundfont2-default gcc-c++
BuildRequires: lilv-devel musl-devel libconfig-devel libsuil-devel
BuildRequires: qt5-qtbase qt5-qtbase-gui qt5-base-devel libfreetype-devel
BuildRequires: libxcbutil-devel libXdmcp-devel libxcbutil-cursor-devel
BuildRequires: libxcbutil-keysyms-devel libxkbcommon-x11-devel libpango-devel
BuildRequires: libgtkmm2-devel libgtkmm3-devel libstdc++-devel

%description
TuxGuitar is a guitar tablature editor with player support through midi.
It can display scores and multitrack tabs. It can open GP3, GP3 and GP5
files.

With TuxGuitar, you will be able to compose music using the following features:
* Tablature editor
* Score Viewer
* Multitrack display
* Autoscroll while playing
* Note duration management
* Various effects (bend, slide, vibrato, hammer-on/pull-off)
* Support for triplets (5,6,7,9,10,11,12)
* Repeat open and close
* Time signature management
* Tempo management
* Imports and exports gp3,gp4 and gp5 files

%prep
%setup -n m2-repository-%name-%version -b 1
%setup -n pluginterfaces-%name-%version -b 2
%setup -n %name-%version
echo %buildroot
%patch0 -p1

%build
pushd build-scripts/tuxguitar-linux-x86_64
mvn -P native-modules package -Dmaven.repo.local=../../../m2-repository-%name-%version
popd

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_datadir/%name-%version/
mkdir -p %buildroot/%_libdir/%name-%version/

install -pm 755 %SOURCE3 %buildroot/%_bindir/tuxguitar

cp -r build-scripts/tuxguitar-linux-x86_64/target/%name-%version-linux-x86_64/dist/ %buildroot/%_datadir/%name-%version/
cp -r build-scripts/tuxguitar-linux-x86_64/target/%name-%version-linux-x86_64/share/ %buildroot/%_datadir/%name-%version/
cp -r build-scripts/tuxguitar-linux-x86_64/target/%name-%version-linux-x86_64/lib/ %buildroot/%_libdir/%name-%version/

# desktop files
install -dm 755 %buildroot/%_datadir/applications
install -pm 644 %SOURCE9 %buildroot/%_datadir/applications/

# icons
for dim in 16x16 24x24 32x32 48x48 64x64 96x96; do
 install -dm 755 %buildroot/%_iconsdir/hicolor/$dim/apps/%name.png
 install -pm 644 TuxGuitar/share/skins/Lavender/icon-$dim.png %buildroot/%_iconsdir/hicolor/$dim/apps/%name.png
done

# mime-type icons
install -dm 755 $RPM_BUILD_ROOT/%_iconsdir/hicolor/96x96/mimetypes
install -pm 644 TuxGuitar/share/skins/Lavender/icon-96x96.png %buildroot/%_iconsdir/hicolor/96x96/mimetypes/audio-x-tuxguitar.png
install -pm 644 TuxGuitar/share/skins/Lavender/icon-96x96.png %buildroot/%_iconsdir/hicolor/96x96/mimetypes/audio-x-gtp.png
install -pm 644 TuxGuitar/share/skins/Lavender/icon-96x96.png %buildroot/%_iconsdir/hicolor/96x96/mimetypes/audio-x-ptb.png

desktop-file-install --dir %buildroot/%_datadir/applications --delete-original %buildroot/%_datadir/applications/%name.desktop

# mime-type file
install -dm 755 %buildroot/%_datadir/mime/packages
install -pm 644 misc/%name.xml %buildroot/%_datadir/mime/packages/

%files
%doc AUTHORS LICENSE README

%_libdir/%name-%version
%_datadir/%name-%version
%_datadir/icons/hicolor/*/*/*
%_datadir/applications/%name.desktop
%_datadir/mime/packages/*.xml

%_bindir/%name

%changelog
* Fri Sep 08 2023 Andrey Kovalev <ded@altlinux.ru> 1.5.6-alt1
- update to 1.5.6

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt6
- fix build: add rpm-build-xdg

* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt5
- fix build: drop libgcj-devel

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt4
- fix build: add libalsa-devel, libjack-devel

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.4
- NMU: corrected java dependencies

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.3
- NMU: corrected java dependencies

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.2
- NMU: corrected java dependencies

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.1
- NMU: corrected java dependencies

* Mon Mar 19 2012 Michael Shigorin <mike@altlinux.org> 1.2-alt3
- rebuilt in current environment (closes: #21801)
- minor spec cleanup

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- fix CVE-2010-3385: insecure library loading (ALT bug #24333)

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for tuxguitar

* Thu Jan 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- new version 1.2 (with rpmrb script)
- add requires to eclipse-swt (ALT #24865)
- use Fedora's spec

* Thu Oct 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- subst /usr/lib with %_libdir (fix #21799)
- remove jpackage utils (fix #21521)

* Fri Sep 11 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script)

* Sat Jun 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version (1.0)
- rewrote spec, use external itext

* Sat May 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0rc4-alt1
- initial build for ALT Linux Sisyphus (thanks to SUSE for spec)

* Fri Apr 04 2008 Toni Graffy <toni@links2linux.de> - 1.0rc3-0.pm.1
- update to 1.0rc3
- changed BuildArch as this package contains two shared libs
- TuxGuitar-alsa is obsoleted now
* Mon Oct 29 2007 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.2
- rebuild with new eclipse-swt-gtk2 package
* Wed Jan 31 2007 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.1
- update to 0.9.1
* Tue Jan 30 2007 Toni Graffy <toni@links2linux.de> - 0.9-0.pm.1
- update to 0.9
* Wed Sep 27 2006 Toni Graffy <toni@links2linux.de> - 0.8-0.pm.1
- build for packman
- added itext.jar as internal lib
* Sat Sep 02 2006 oc2pus <oc2pus@arcor.de> - 0.8-0.oc2pus.2
- rebuild, change in start-script for alsa-plugin
* Thu Aug 24 2006 oc2pus <oc2pus@arcor.de> - 0.8-0.oc2pus.1
- update to 0.8
* Mon Jul 17 2006 oc2pus <oc2pus@arcor.de> - 0.7-0.oc2pus.1
- update to 0.7
- switched to ant-build
- repacked without lib/* as tar.gz2
* Sun Jun 10 2006 oc2pus <oc2pus@arcor.de> - 0.6-0.oc2pus.2
- corrected desktop-entry
* Sun May 28 2006 oc2pus <oc2pus@arcor.de> - 0.6-0.oc2pus.1
- update to 0.6
- added itext to dependencies
* Sat Apr 08 2006 oc2pus <oc2pus@arcor.de> - 0.5-0.oc2pus.1
- First packaged release 0.5
- repacked without swt.jar and native libs (jameica-swt3-gtk)
