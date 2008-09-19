%define	snap	20080814
Summary:	Userspace interface to kernel DRM services
Summary(pl.UTF-8):	Interfejs przestrzeni użytkownika do usług DRM jądra
Name:		libdrm
Version:	2.4.0
Release:	0.%{snap}.1
License:	MIT
Group:		Libraries
# Source0:	http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	2af5325c8ae923a7cbaea3671bc7b969
URL:		http://dri.freedesktop.org/
Patch0:		%{name}-make-dri-perms-okay.patch
Patch1:		%{name}-2.4.0-no-bc.patch
Patch2:		%{name}-wait-udev.patch
Patch3:		%{name}-2.4.0-no-freaking-mknod.patch
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
%setup -q -n libdrm-%{snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1

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
install libdrm/xf86mm.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %attr(755,root,root) %{_libdir}/libdrm.so.2
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
