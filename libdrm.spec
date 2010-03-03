Summary:	Userspace interface to kernel DRM services
Summary(pl.UTF-8):	Interfejs przestrzeni użytkownika do usług DRM jądra
Name:		libdrm
Version:	2.4.19
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
# Source0-md5:	c2699b5d8ebc9e47fb56da15f460107f
Patch0:		%{name}-kms.patch
URL:		http://dri.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libpthread-stubs
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Userspace interface to kernel DRM services.

%description -l pl.UTF-8
Interfejs przestrzeni użytkownika do usług DRM jądra.

%package devel
Summary:	Header files for libdrm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdrm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdrm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdrm.

%package static
Summary:	Static libdrm library
Summary(pl.UTF-8):	Statyczna biblioteka libdrm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdrm library.

%description static -l pl.UTF-8
Statyczna biblioteka libdrm.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-nouveau-experimental-api \
	--enable-radeon-experimental-api \
	--enable-vmwgfx-experimental-api \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdrm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm.so.2
%attr(755,root,root) %{_libdir}/libdrm_intel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_intel.so.1
%attr(755,root,root) %{_libdir}/libdrm_nouveau.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_nouveau.so.1
%attr(755,root,root) %{_libdir}/libdrm_radeon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_radeon.so.1
%attr(755,root,root) %{_libdir}/libkms.so.*.*.*                                                                                                       
%attr(755,root,root) %ghost %{_libdir}/libkms.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdrm.so
%attr(755,root,root) %{_libdir}/libdrm_intel.so
%attr(755,root,root) %{_libdir}/libdrm_nouveau.so
%attr(755,root,root) %{_libdir}/libdrm_radeon.so
%attr(755,root,root) %{_libdir}/libkms.so
%{_libdir}/libdrm.la
%{_libdir}/libdrm_intel.la
%{_libdir}/libdrm_nouveau.la
%{_libdir}/libdrm_radeon.la
%{_libdir}/libkms.la
%{_includedir}/drm
%{_includedir}/nouveau
%{_includedir}/intel_bufmgr.h
%{_includedir}/libkms
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h
%{_pkgconfigdir}/libdrm.pc
%{_pkgconfigdir}/libdrm_intel.pc
%{_pkgconfigdir}/libdrm_nouveau.pc
%{_pkgconfigdir}/libdrm_radeon.pc
%{_pkgconfigdir}/libkms.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdrm.a
%{_libdir}/libdrm_intel.a
%{_libdir}/libdrm_nouveau.a
%{_libdir}/libdrm_radeon.a
%{_libdir}/libkms.a
