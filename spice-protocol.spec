Name:           spice-protocol
Version:        0.8.0
Release:        1%{?dist}
Summary:        Spice protocol header files
Group:          Development/Libraries
# Main headers are BSD, controller / foreign menu are LGPL
License:        BSD and LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root,-)
%doc COPYING NEWS
%{_includedir}/spice-1
%{_datadir}/pkgconfig/spice-protocol.pc

%changelog
* Wed Mar  2 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.0-1
- Update to upstream 0.8.0 release
  Related: rhbz#662992

* Mon Feb 14 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.1-1
- Update to upstream 0.7.1 release
  Related: rhbz#662992

* Wed Jan 12 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.0-2
- Update License tag (controller and foreign menu headers are LGPL)
  Related: rhbz#662992

* Fri Dec 17 2010 Hans de Goede <hdegoede@redhat.com> - 0.7.0-1
- Update to upstream 0.7.0 release
  Related: rhbz#662992

* Thu Dec 16 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-3
- Build for RHEL-6
  Resolves: rhbz#662992

* Wed Dec 15 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-2
- Add utf8 controller menu text patch from upstream git
- Add smartcard channel patch from upstream git

* Mon Oct 18 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Thu Sep 30 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.6.1-1
- Update to 0.6.1.

* Tue Aug 31 2010 Alexander Larsson <alexl@redhat.com> - 0.6.0-1
- Update to 0.6.0 (stable release)

* Tue Jul 20 2010 Alexander Larsson <alexl@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Mon Jul 12 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-2
- Fix license: It is BSD, not GPL.
- Cleanup specfile, drop bits not needed any more with
  recent rpm versions (F13+).

* Fri Jul 9 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-1
- initial package.

