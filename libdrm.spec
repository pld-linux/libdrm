Summary:	Userspace interface to kernel DRM services
Summary(pl):	Interfejs przestrzeni u¿ytkownika do us³ug DRM j±dra
Name:		libdrm
Version:	1.0.4
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://people.freedesktop.org/~ajax/libdrm/%{name}-%{version}.tar.bz2
# Source0-md5:	a1979e2b94801c0b35f552e30a93c2f5
URL:		http://dri.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
