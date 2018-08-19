Name:           xbill
Version:        2.1
Release:        11%{?dist}
Summary:        Stop Bill from loading his OS into all the computers

Group:          Amusements/Games
License:        GPL+
URL:            http://www.xbill.org/
Source0:        http://www.xbill.org/download/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# Gentoo 201214
Patch0:         %{name}-2.1-gtk2.patch
# Debian
Patch1:         %{name}-2.1-hurd_logos.patch
# Andrea Musuruane
Patch2:         %{name}-2.1-score.patch
Patch3:         %{name}-2.1-dropsgid.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libtool

BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
Requires:       hicolor-icon-theme


%description
The xbill game tests your reflexes as you seek out and destroy all
forms of Bill, establish a new operating system throughout the
universe, and boldly go where no geek has gone before.  Xbill has
become an increasingly attractive option as the Linux Age progresses,
and it is very popular at Red Hat.


%prep
%setup -q
%patch0 -p0
%patch1 -p1
# Patch2 must be applied before patch3
%patch2 -p1
%patch3 -p1



%build
autoreconf
%configure --disable-motif \
  --localstatedir=%{_localstatedir}/games
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#install man page
install -d %{buildroot}%_mandir/man6
install -m 644 %{name}.6 %{buildroot}%{_mandir}/man6

# install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor '' \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
convert -resize x48 %{name}.gif \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%attr(2755,root,games) %{_bindir}/%{name}
%{_localstatedir}/games/%{name}
%attr(0664,root,games) %config(noreplace) %{_localstatedir}/games/%{name}/scores
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc ChangeLog README


%changelog
* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.1-11
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 21 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1-5
- Add BR for autoreconf

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.1-4
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 26 2009 Andrea Musuruane <musuruan@gmail.com> 2.1-2
- Updated icon cache scriptlets to be compliant to new guidelines

* Sat Dec 27 2008 Andrea Musuruane <musuruan@gmail.com> 2.1-1
- Reworked to meet Fedora guidelines
- Used a patch to use gtk-2 (Gentoo BZ #201214)
- Used a patch to use an updated hurd logo (Debian)
- Made a patch to fix highscore view when compiling with FORTIFY_SOURCE=2
- Made a patch to drop setgid privileges after opening the score file

* Sun Oct 28 2001 Brian Wellington <bwelling@xbill.org>
- Updated to 2.1

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Apr 27 2001 Bill Nottingham <notting@redhat.com>
- rebuild for C++ exception handling on ia64

* Wed Oct 18 2000 Than Ngo <than@redhat.com>
- rebuilt against gcc-2.96-60

* Tue Jul 18 2000 Than Ngo <than@redhat.de>
- rebuilt with gcc-2.96-4.0

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul  2 2000 Jakub Jelinek <jakub@redhat.com>
- Rebuild with new C++

* Sun Jun 18 2000 Than Ngo <than@redhat.de>
- rebuilt in the new build environment
- use RPM maccros

* Mon May 08 2000 Preston Brown <pbrown@redhat.com>
- fix for gcc 2.95 from t-matsuu@protein.osaka-u.ac.jp.

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- rebuild with config(noreplace) score file, new description
- replace wmconfig with desktop file

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built pacakge for 6.0

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

