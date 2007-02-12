Summary:	Userspace interface to kernel DRM services
Summary(pl.UTF-8):   Interfejs przestrzeni użytkownika do usług DRM jądra
Name:		libdrm
Version:	2.3.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
# Source0-md5:	01a1e1ee0268a2403db42fa630036ab2
URL:		http://dri.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Userspace interface to kernel DRM services.

%description -l pl.UTF-8
Interfejs przestrzeni użytkownika do usług DRM jądra.

%package devel
Summary:	Header files for libdrm library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libdrm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdrm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdrm.

%package static
Summary:	Static libdrm library
Summary(pl.UTF-8):   Statyczna biblioteka libdrm
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdrm.so
%{_libdir}/libdrm.la
%{_includedir}/*.h
%{_includedir}/drm
%{_pkgconfigdir}/libdrm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdrm.a
