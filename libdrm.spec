Summary:	Userspace interface to kernel DRM services
Summary(pl.UTF-8):	Interfejs przestrzeni użytkownika do usług DRM jądra
Name:		libdrm
Version:	2.4.88
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
# Source0-md5:	fe4d5c77f1468ee73d0bbb30d76945d7
URL:		https://dri.freedesktop.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	libpthread-stubs >= 0.4
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	valgrind
%ifarch %{ix86} %{x8664} x32
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
%endif
BuildRequires:	xorg-util-util-macros >= 1.12
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
%ifarch %{arm} aarch64
	--enable-etnaviv-experimental-api \
	--enable-exynos-experimental-api \
	--enable-freedreno-experimental-api \
	--enable-omap-experimental-api \
	--enable-tegra-experimental-api
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdrm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm.so.2
%attr(755,root,root) %{_libdir}/libdrm_amdgpu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_amdgpu.so.1
%ifarch %{ix86} %{x8664} x32
%attr(755,root,root) %{_libdir}/libdrm_intel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_intel.so.1
%endif
%attr(755,root,root) %{_libdir}/libdrm_nouveau.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_nouveau.so.2
%attr(755,root,root) %{_libdir}/libdrm_radeon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_radeon.so.1
%ifarch %{arm} aarch64
%attr(755,root,root) %{_libdir}/libdrm_etnaviv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_etnaviv.so.1
%attr(755,root,root) %{_libdir}/libdrm_exynos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_exynos.so.1
%attr(755,root,root) %{_libdir}/libdrm_freedreno.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_freedreno.so.1
%attr(755,root,root) %{_libdir}/libdrm_omap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_omap.so.1
%attr(755,root,root) %{_libdir}/libdrm_tegra.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_tegra.so.0
%endif
%attr(755,root,root) %{_libdir}/libkms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkms.so.1
%{_datadir}/libdrm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdrm.so
%attr(755,root,root) %{_libdir}/libdrm_amdgpu.so
%attr(755,root,root) %{_libdir}/libdrm_nouveau.so
%attr(755,root,root) %{_libdir}/libdrm_radeon.so
%attr(755,root,root) %{_libdir}/libkms.so
%{_includedir}/libdrm
%{_includedir}/libkms
%{_includedir}/libsync.h
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h
%{_pkgconfigdir}/libdrm.pc
%{_pkgconfigdir}/libdrm_amdgpu.pc
%{_pkgconfigdir}/libdrm_nouveau.pc
%{_pkgconfigdir}/libdrm_radeon.pc
%{_pkgconfigdir}/libkms.pc
%ifarch %{ix86} %{x8664} x32
%attr(755,root,root) %{_libdir}/libdrm_intel.so
%{_pkgconfigdir}/libdrm_intel.pc
%endif
%ifarch %{arm} aarch64
%attr(755,root,root) %{_libdir}/libdrm_etnaviv.so
%attr(755,root,root) %{_libdir}/libdrm_exynos.so
%attr(755,root,root) %{_libdir}/libdrm_freedreno.so
%attr(755,root,root) %{_libdir}/libdrm_omap.so
%attr(755,root,root) %{_libdir}/libdrm_tegra.so
%{_includedir}/exynos
%{_includedir}/freedreno
%{_includedir}/omap
# already included above
#%{_includedir}/libdrm/etnaviv_drmif.h
#%{_includedir}/libdrm/tegra.h
#%{_includedir}/libdrm/vc4_packet.h
#%{_includedir}/libdrm/vc4_qpu_defines.h
%{_pkgconfigdir}/libdrm_etnaviv.pc
%{_pkgconfigdir}/libdrm_exynos.pc
%{_pkgconfigdir}/libdrm_freedreno.pc
%{_pkgconfigdir}/libdrm_omap.pc
%{_pkgconfigdir}/libdrm_tegra.pc
%{_pkgconfigdir}/libdrm_vc4.pc
%endif
%{_mandir}/man3/drm*.3*
%{_mandir}/man7/drm*.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdrm.a
%{_libdir}/libdrm_amdgpu.a
%ifarch %{ix86} %{x8664} x32
%{_libdir}/libdrm_intel.a
%endif
%{_libdir}/libdrm_nouveau.a
%{_libdir}/libdrm_radeon.a
%ifarch %{arm} aarch64
%{_libdir}/libdrm_etnaviv.a
%{_libdir}/libdrm_exynos.a
%{_libdir}/libdrm_freedreno.a
%{_libdir}/libdrm_omap.a
%{_libdir}/libdrm_tegra.a
%endif
%{_libdir}/libkms.a
