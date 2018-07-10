%define major 0
%define libname %mklibname uninameslist %{major}
%define devname %mklibname uninameslist -d
%define _disable_lto 1

Summary:	A Library of Unicode annotation data
Name:		libuninameslist
Version:	20091231
Release:	15
License:	BSD Style
Group:		System/Libraries
Url:		http://libuninameslist.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

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
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libuninameslist.so.%{major}*
%{_libdir}/libuninameslist-fr.so.%{major}*

%files -n %{devname}
%doc LICENSE
%{_includedir}/*
%{_libdir}/lib*.so

