Summary:	Userspace interface to kernel DRM services
Summary(pl.UTF-8):	Interfejs przestrzeni użytkownika do usług DRM jądra
Name:		libdrm
Version:	2.4.54
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
# Source0-md5:	56e98a9c2073c3fab7f95e003b657f46
URL:		http://dri.freedesktop.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	libpthread-stubs
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
Requires:	xorg-lib-libpciaccess >= 0.10
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static \
%ifarch arm
	--enable-exynos-experimental-api \
	--enable-freedreno-experimental-api \
	--enable-omap-experimental-api \
%endif
	--enable-vmwgfx-experimental-api
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
%attr(755,root,root) %ghost %{_libdir}/libdrm_nouveau.so.2
%attr(755,root,root) %{_libdir}/libdrm_radeon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_radeon.so.1
%ifarch arm
%attr(755,root,root) %{_libdir}/libdrm_exynos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_exynos.so.1
%attr(755,root,root) %{_libdir}/libdrm_freedreno.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_freedreno.so.1
%attr(755,root,root) %{_libdir}/libdrm_omap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_omap.so.1
%endif
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
%{_includedir}/libdrm
%{_includedir}/libkms
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h
%{_pkgconfigdir}/libdrm.pc
%{_pkgconfigdir}/libdrm_intel.pc
%{_pkgconfigdir}/libdrm_nouveau.pc
%{_pkgconfigdir}/libdrm_radeon.pc
%{_pkgconfigdir}/libkms.pc
%ifarch arm
%attr(755,root,root) %{_libdir}/libdrm_exynos.so
%attr(755,root,root) %{_libdir}/libdrm_freedreno.so
%attr(755,root,root) %{_libdir}/libdrm_omap.so
%{_libdir}/libdrm_exynos.la
%{_libdir}/libdrm_freedreno.la
%{_libdir}/libdrm_omap.la
%{_includedir}/exynos
%{_includedir}/freedreno
%{_includedir}/omap
%{_pkgconfigdir}/libdrm_exynos.pc
%{_pkgconfigdir}/libdrm_freedreno.pc
%{_pkgconfigdir}/libdrm_omap.pc
%endif
%{_mandir}/man3/drm*.3*
%{_mandir}/man7/drm*.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdrm.a
%{_libdir}/libdrm_intel.a
%{_libdir}/libdrm_nouveau.a
%{_libdir}/libdrm_radeon.a
%ifarch arm
%{_libdir}/libdrm_exynos.a
%{_libdir}/libdrm_freedreno.a
%{_libdir}/libdrm_omap.a
%endif
%{_libdir}/libkms.a
