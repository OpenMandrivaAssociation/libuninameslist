%define major 1
%define libname %mklibname uninameslist %{major}
%define devname %mklibname uninameslist -d
%define _disable_lto 1

Summary:	A Library of Unicode annotation data
Name:		libuninameslist
Version:	20190701
Release:	16
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
%setup -qn %{name}

%build
47 	autoreconf -vfi
48 	%configure2_5x --disable-static
49 	%make_build
50 	
51 	%install
52 	%make_install
53 	
54 	find %{buildroot} -name '*.la' -delete
55 	
56 	%files -n %{libname}
57 	%doc LICENSE
58 	%{_libdir}/lib*.so.%{major}{,.*}
59 	
60 	%files -n %{devname}
61 	%{_includedir}/*
62 	%{_libdir}/lib*.so
63 	%{_libdir}/pkgconfig/%{name}.pc
64 	%{_mandir}/man3/%{name}.3.*

