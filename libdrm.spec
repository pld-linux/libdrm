#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_with	valgrind	# valgrind support in libdrm
%bcond_without	arch_arm	# ARM specific libraries (libdrm_{etnaviv,exynos,freedreno,omap,tegra,vc4})
%bcond_without	arch_x86	# x86 specific libraries (libdrm_intel)

%ifnarch %{arm} aarch64
%undefine	with_arch_arm
%endif
%ifnarch %{ix86} %{x8664} x32
%undefine	with_arch_x86
%endif
Summary:	Userspace interface to kernel DRM services
Summary(pl.UTF-8):	Interfejs przestrzeni użytkownika do usług DRM jądra
Name:		libdrm
Version:	2.4.128
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.xz
# Source0-md5:	77845fa800823a24243bfc771ceb4297
URL:		https://dri.freedesktop.org/
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	docutils
BuildRequires:	gcc >= 6:4.9
%ifarch i386
BuildRequires:	libatomic_ops-devel
%endif
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_valgrind:BuildRequires:	valgrind >= 3.10.0}
%if %{with arch_x86}
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
%endif
BuildRequires:	xz
%if %{with arch_x86}
Requires:	xorg-lib-libpciaccess%{?_isa} >= 0.10
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Userspace interface to kernel DRM services.

%description -l pl.UTF-8
Interfejs przestrzeni użytkownika do usług DRM jądra.

%package devel
Summary:	Header files for libdrm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdrm
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
%if %{with arch_x86}
Requires:	xorg-lib-libpciaccess-devel%{?_isa} >= 0.10
%endif

%description devel
Header files for libdrm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdrm.

%package static
Summary:	Static libdrm library
Summary(pl.UTF-8):	Statyczna biblioteka libdrm
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libdrm library.

%description static -l pl.UTF-8
Statyczna biblioteka libdrm.

%prep
%setup -q

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Damdgpu=enabled \
	-Detnaviv=%{__enabled_disabled arch_arm} \
	-Dexynos=%{__enabled_disabled arch_arm} \
	-Dfreedreno=%{__enabled_disabled arch_arm} \
	-Dintel=%{__enabled_disabled arch_x86} \
	-Dman-pages=enabled \
	-Domap=%{__enabled_disabled arch_arm} \
	-Dradeon=enabled \
	-Dtegra=%{__enabled_disabled arch_arm} \
	-Dvalgrind=%{__enabled_disabled valgrind} \
	-Dvc4=%{__enabled_disabled arch_arm} \
	-Dvmwgfx=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%if %{with arch_x86}
%attr(755,root,root) %{_libdir}/libdrm_intel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_intel.so.1
%endif
%attr(755,root,root) %{_libdir}/libdrm_nouveau.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_nouveau.so.2
%attr(755,root,root) %{_libdir}/libdrm_radeon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdrm_radeon.so.1
%if %{with arch_arm}
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
%{_datadir}/libdrm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdrm.so
%attr(755,root,root) %{_libdir}/libdrm_amdgpu.so
%attr(755,root,root) %{_libdir}/libdrm_nouveau.so
%attr(755,root,root) %{_libdir}/libdrm_radeon.so
%{_includedir}/libdrm
%{_includedir}/libsync.h
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h
%{_pkgconfigdir}/libdrm.pc
%{_pkgconfigdir}/libdrm_amdgpu.pc
%{_pkgconfigdir}/libdrm_nouveau.pc
%{_pkgconfigdir}/libdrm_radeon.pc
%if %{with arch_x86}
%attr(755,root,root) %{_libdir}/libdrm_intel.so
%{_pkgconfigdir}/libdrm_intel.pc
%endif
%if %{with arch_arm}
%attr(755,root,root) %{_libdir}/libdrm_etnaviv.so
%attr(755,root,root) %{_libdir}/libdrm_exynos.so
%attr(755,root,root) %{_libdir}/libdrm_freedreno.so
%attr(755,root,root) %{_libdir}/libdrm_omap.so
%attr(755,root,root) %{_libdir}/libdrm_tegra.so
%{_includedir}/exynos
%{_includedir}/freedreno
%{_includedir}/omap
%{_pkgconfigdir}/libdrm_etnaviv.pc
%{_pkgconfigdir}/libdrm_exynos.pc
%{_pkgconfigdir}/libdrm_freedreno.pc
%{_pkgconfigdir}/libdrm_omap.pc
%{_pkgconfigdir}/libdrm_tegra.pc
%{_pkgconfigdir}/libdrm_vc4.pc
%endif
%{_mandir}/man3/drm*.3*
%{_mandir}/man7/drm*.7*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdrm.a
%{_libdir}/libdrm_amdgpu.a
%if %{with arch_x86}
%{_libdir}/libdrm_intel.a
%endif
%{_libdir}/libdrm_nouveau.a
%{_libdir}/libdrm_radeon.a
%if %{with arch_arm}
%{_libdir}/libdrm_etnaviv.a
%{_libdir}/libdrm_exynos.a
%{_libdir}/libdrm_freedreno.a
%{_libdir}/libdrm_omap.a
%{_libdir}/libdrm_tegra.a
%endif
%endif
