Summary:	Video DVD creation tool
Name:		2mandvd
Version:	1.4
Release:	1%{?dist}

URL:		http://2mandvd.tuxfamily.org/
License:	GPLv2 and LGPL
Group:		Applications/Multimedia
Source:		http://download.tuxfamily.org/2mandvd/2ManDVD-%{version}.tar.gz
Source1:	2ManDVD.desktop

BuildRequires:  qt-devel >= 4.6
%if 0%{?fedora} >= 14
BuildRequires:  qt-webkit-devel >= 4.6
%endif

Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	ffmpeg >= 0.5
Requires:	ffmpegthumbnailer
Requires:	mencoder
Requires:	mjpegtools
Requires:	mkisofs
Requires:	mplayer
Requires:	netpbm
Requires:	sox

%description
ManDVD is a graphical tool for creating Video DVDs, including menus.

%prep
%setup -q -n 2ManDVD

%build
qmake-qt4 2ManDVD.pro
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

# put the executable in %{_datadir}/%{name} and symlink it to %_bindir
# otherwise the UI localizations don't work
install -D -m 755 2ManDVD %{buildroot}%{_datadir}/2ManDVD/2ManDVD

mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
	ln -s %{_datadir}/2ManDVD/2ManDVD 2ManDVD
popd

install -m 644 2mandvd_*.qm %{buildroot}%{_datadir}/2ManDVD
install -m 644 fake.pl %{buildroot}%{_datadir}/2ManDVD

install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/2ManDVD.desktop
install -D -m 644 Interface/mandvd.png %{buildroot}%{_datadir}/pixmaps/2ManDVD.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/2ManDVD
%dir %{_datadir}/2ManDVD
%{_datadir}/2ManDVD/2ManDVD
%{_datadir}/2ManDVD/2mandvd_*.qm
%{_datadir}/2ManDVD/fake.pl
%{_datadir}/applications/2ManDVD.desktop
%{_datadir}/pixmaps/2ManDVD.png


%changelog
* Mon Oct  4 2010 Arkady L. Shane <ashejn@yandex-team.ru> 1.4-1
- update to 1.4.0

* Thu Aug 12 2010 Arkady L. Shane <ashejn@yandex-team.ru> 1.3.5-2
- added BR qt-webkit-devel for qt 4.7 in Fedora 14

* Mon Jun  7 2010 Arkady L. Shane <ashejn@yandex-team.ru> 1.3.5-1
- rebuilt for Fedora
- update to 1.3.5

* Mon Apr 19 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.3-4mdv2010.1
+ Revision: 536759
- Adjust ppegtopnm detection, fixes #58695

* Mon Apr 19 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.3-3mdv2010.1
+ Revision: 536729
- Add missing fake.pl script

* Sun Mar 28 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.3-2mdv2010.1
+ Revision: 528474
- rebuild
- Update to 1.3.3

* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 1.3.2-1mdv2010.1
+ Revision: 518684
- new version 1.3.2

* Mon Mar 08 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.1-2mdv2010.1
+ Revision: 515906
- Correct growisofs requires

* Mon Mar 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.1-1mdv2010.1
+ Revision: 513035
- Update to 1.3.1

* Thu Feb 25 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3-2mdv2010.1
+ Revision: 511190
- Forgot to bump rel
- Add missing Requires
- Transform trancode requires into suggests since this package is not available in official mandriva repositories

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - 1.3 now requires qt >= 4.6

* Wed Feb 24 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.3-1mdv2010.1
+ Revision: 510789
- rename back the symlink in bindir, otherwise it doesn't work??
- adapt spec for package renaming
- rename to lowercase
- clean spec
- fix license
- update to 1.3
- name the executable 2mandvd, more robust this way
- use "EXEC=2mandvd -graphicssystem raster" as per upstream's recomendation
- fix requires (again)
- fix requires

* Wed Jan 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2-3mdv2010.1
+ Revision: 497157
- only suggest transcode

* Wed Jan 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2-2mdv2010.1
+ Revision: 496931
- use %%qmake_qt4 and %%make macors (the latter to enable parallel build
  which seems to work)
- make .desktop file compliant with xdg specs

* Mon Jan 18 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.2-1mdv2010.1
+ Revision: 493378
- import 2ManDVD

