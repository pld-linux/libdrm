Summary:	Userspace interface to kernel DRM services
Summary(pl):	Interfejs przestrzeni u¿ytkownika do us³ug DRM j±dra
Name:		libdrm
Version:	1.0.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://people.freedesktop.org/~ajax/libdrm/%{name}-%{version}.tar.gz
# Source0-md5:	2fd32375b17fa80e3a962276f98d6440
URL:		http://dri.freedesktop.org/
# currently uses <X11/Xlibint.h>
#BuildRequires:	XFree86-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Userspace interface to kernel DRM services.

%description -l pl
Interfejs przestrzeni u¿ytkownika do us³ug DRM j±dra.

%package devel
Summary:	Header files for libdrm library
Summary(pl):	Pliki nag³ówkowe biblioteki libdrm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdrm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libdrm.

%package static
Summary:	Static libdrm library
Summary(pl):	Statyczna biblioteka libdrm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdrm library.

%description static -l pl
Statyczna biblioteka libdrm.

%prep
%setup -q

%build
%configure
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdrm.so
%{_libdir}/libdrm.la
%{_includedir}/xf86drm.h
%{_includedir}/drm
%{_pkgconfigdir}/libdrm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdrm.a
