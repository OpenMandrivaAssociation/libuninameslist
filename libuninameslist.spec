%define	version 20060907
%define release %mkrel 2

%define major 0
%define libname %mklibname uninameslist %{major}

Summary:	A Library of Unicode annotation data
Name:		libuninameslist
Version:	%{version}
Release:	%{release}
License:	BSD Style
Group:		System/Libraries
URL:		http://libuninameslist.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}_src-%{version}.tar.bz2
Patch0:		libuninameslist-destdir.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{libname}-devel
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
The Unicode consortium provides a file containing annotations on many
unicode characters. This library contains a compiled version of this
file so that programs can access these data easily.

This package provides development related files for compiling or
developing any software that make use of this library.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .destdir

%build
%configure --enable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la

