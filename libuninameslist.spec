%define major 1
%define libname %mklibname uninameslist %{major}
%define devname %mklibname uninameslist -d
%define _disable_lto 1

Summary:	A Library of Unicode annotation data
Name:		libuninameslist
Version:	20240910
Release:	1
License:	BSD Style
Group:		System/Libraries
Url:		http://libuninameslist.sourceforge.net/
Source0:	https://github.com/fontforge/libuninameslist/archive/%{version}/%{name}-%{version}.tar.gz

%description
The Unicode consortium provides a file containing annotations on many
unicode characters. This library contains a compiled version of this
file so that programs can access these data easily.

%package	-n %{libname}
Summary:	A Library of Unicode annotation data
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description	-n %{libname}
The Unicode consortium provides a file containing annotations on many
unicode characters. This library contains a compiled version of this
file so that programs can access these data easily.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package provides development related files for compiling or
developing any software that make use of this library.

%prep
%setup -q

%build
autoreconf -vfi
%configure2_5x --disable-static
%make_build
	
%install
%make_install

find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc LICENSE
%{_libdir}/lib*.so.%{major}{,.*}
	
%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3.*
