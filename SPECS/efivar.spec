Name:           efivar
Version:        35
Release:        4%{?dist}
Summary:        Tools to manage UEFI variables
License:        LGPLv2.1
URL:            https://github.com/rhboot/efivar
Requires:       %{name}-libs = %{version}-%{release}
ExclusiveArch:	%{ix86} x86_64 aarch64

BuildRequires:  popt-devel popt-static git glibc-static
Source0:        https://github.com/rhinstaller/efivar/releases/download/efivar-%{version}/efivar-%{version}.tar.bz2

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package libs
Summary: Library to manage UEFI variables

%description libs
Library to allow for the simple manipulation of UEFI variables.

%package devel
Summary: Development headers for libefivar
Requires: %{name}-libs = %{version}-%{release}

%description devel
development headers required to use libefivar.

%prep
%setup -q -n %{name}-%{version}

%build
make libdir=%{_libdir} bindir=%{_bindir} CFLAGS="$RPM_OPT_FLAGS -flto" LDFLAGS="$RPM_LD_FLAGS -flto"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md
%{_bindir}/efivar
%exclude %{_bindir}/efivar-static
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files libs
%{_libdir}/*.so.*

%changelog
* Mon Oct 17 2016 Peter Jones <pjones@redhat.com> - 30-4
- Handle NVMe device attributes paths moving around in sysfs.

* Wed Sep 28 2016 Peter Jones <pjones@redhat.com> - 30-3
- Maybe even provide the *right* old linker deps.

* Tue Sep 27 2016 Peter Jones <pjones@redhat.com> - 30-2
- Try not to screw up SONAME stuff quite so badly.

* Tue Sep 27 2016 Peter Jones <pjones@redhat.com> - 30-1
- Fix efidp_*() functions with __pure__ that break with some optimizations
- Fix NVMe EUI parsing.

* Tue Sep 27 2016 Peter Jones <pjones@redhat.com> - 29-1
- Use -pie not -PIE in our linker config
- Fix some overflow checks for gcc < 5.x
- Make variable class probes other than the first one actually work
- Move -flto to CFLAGS
- Pack all of the efi device path headers
- Fix redundant decl of efi_guid_zero()

* Wed Aug 17 2016 Peter Jones <pjones@redhat.com> - 28-1
- Make our sonames always lib$FOO.1 , not lib$FOO.$VERSION .

* Tue Aug 16 2016 Peter Jones <pjones@redhat.com> - 27-1
- Bug fix for 086eeb17 in efivar 26.

* Wed Aug 10 2016 Peter Jones <pjones@redhat.com> - 26-1
- Update to efivar-26 .

* Thu Jun 30 2016 Peter Jones <pjones@redhat.com> - 0.24-1
- Update to 0.24

* Mon Feb 15 2016 Peter Jones <pjones@redhat.com> - 0.23-1
- Update to 0.23

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Peter Jones <pjones@redhat.com> - 0.21-2
- Bump the release here so f22->f23->f24 updates work.

* Mon Jul 13 2015 Peter Jones <pjones@redhat.com> - 0.21-1
- Rename "make test" so packagers don't think it's a good idea to run it
  during builds.
- Error check sizes in vars_get_variable()
- Fix some file size comparisons
- make SONAME reflect the correct values.
- Fix some uses of "const"
- Compile with -O2 by default
- Fix some strict-aliasing violations
- Fix some of the .pc files and how we do linking to work better.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Peter Jones <pjones@redhat.com> - 0.20-1
- Update to 0.20
- Make sure tester is build with the right link order for libraries.
- Adjust linker order for pkg-config
- Work around LocateDevicePath() not grokking PcieRoot() devices properly.
- Rectify some missing changelog entries

* Thu May 28 2015 Peter Jones <pjones@redhat.com> - 0.19-1
- Update to 0.19
- add API from efibootmgr so fwupdate and other tools can use it.

* Wed Oct 15 2014 Peter Jones <pjones@redhat.com> - 0.15-1
- Update to 0.15
- Make 32-bit builds set variables' DataSize correctly.

* Wed Oct 08 2014 Peter Jones <pjones@redhat.com> - 0.14-1
- Update to 0.14
- add efi_id_guid_to_guid() and efi_guid_to_id_guid(), which support {ID GUID}
  as a concept.
- Add some vendor specific guids to our guid list.
- Call "empty" "zero" now, as many other places do.  References to
  efi_guid_is_empty() and efi_guid_empty still exist for ABI compatibility.
- add "efivar -L" to the man page.

* Tue Oct 07 2014 Peter Jones <pjones@redhat.com> - 0.13-1
- Update to 0.13:
- add efi_symbol_to_guid()
- efi_name_to_guid() will now fall back on efi_symbol_to_guid() as a last
  resort
- "efivar -L" to list all the guids we know about
- better namespacing on libefivar.so (rename well_known_* -> efi_well_known_*)

* Thu Sep 25 2014 Peter Jones <pjones@redhat.com> - 0.12-1
- Update to 0.12

* Wed Aug 20 2014 Peter Jones <pjones@redhat.com> - 0.11-1
- Update to 0.11

* Fri May 02 2014 Peter Jones <pjones@redhat.com> - 0.10-1
- Update package to 0.10.
- Fixes a build error due to different cflags in the builders vs updstream
  makefile.

* Fri May 02 2014 Peter Jones <pjones@redhat.com> - 0.9-0.1
- Update package to 0.9.

* Tue Apr 01 2014 Peter Jones <pjones@redhat.com> - 0.8-0.1
- Update package to 0.8 as well.

* Fri Oct 25 2013 Peter Jones <pjones@redhat.com> - 0.7-1
- Update package to 0.7
- adds --append support to the binary.

* Fri Sep 06 2013 Peter Jones <pjones@redhat.com> - 0.6-1
- Update package to 0.6
- fixes to documentation from lersek
- more validation of uefi guids
- use .xz for archives

* Thu Sep 05 2013 Peter Jones <pjones@redhat.com> - 0.5-0.1
- Update to 0.5

* Mon Jun 17 2013 Peter Jones <pjones@redhat.com> - 0.4-0.2
- Fix ldconfig invocation

* Mon Jun 17 2013 Peter Jones <pjones@redhat.com> - 0.4-0.1
- Initial spec file
