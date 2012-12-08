%define	version 20091231
%define release %mkrel 4

%define major 0
%define libname %mklibname uninameslist %{major}
%define develname %mklibname uninameslist -d

Summary:	A Library of Unicode annotation data
Name:		libuninameslist
Version:	%{version}
Release:	%{release}
License:	BSD Style
Group:		System/Libraries
URL:		http://libuninameslist.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
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

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{_lib}uninameslist0-devel

%description -n	%{develname}
The Unicode consortium provides a file containing annotations on many
unicode characters. This library contains a compiled version of this
file so that programs can access these data easily.

This package provides development related files for compiling or
developing any software that make use of this library.

%prep
%setup -q -n %{name}

%build
%configure2_5x --enable-static
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
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a



%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 20091231-2mdv2011.0
+ Revision: 660288
- mass rebuild

* Sun Aug 15 2010 Emmanuel Andry <eandry@mandriva.org> 20091231-1mdv2011.0
+ Revision: 569841
- New version 20091231

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 20080409-3mdv2010.1
+ Revision: 520914
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 20080409-2mdv2010.0
+ Revision: 425854
- rebuild

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 20080409-1mdv2009.1
+ Revision: 365693
- use configure2_5x

* Fri Sep 05 2008 Emmanuel Andry <eandry@mandriva.org> 20080409-1mdv2009.0
+ Revision: 281375
- New version
- apply devel policy
- check major

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 20060907-2mdv2009.0
+ Revision: 223014
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20060907-1mdv2008.1
+ Revision: 129169
- kill re-definition of %%buildroot on Pixel's request

* Thu May 03 2007 Adam Williamson <awilliamson@mandriva.org> 20060907-1mdv2008.0
+ Revision: 20864
- 20060907, rebuild for new era


* Sun Jan 16 2005 Abel Cheung <deaddog@mandrake.org> 040707-1mdk
- First Mandrakelinux package
- P0: Add DESTDIR support and add missing --mode=* to libtool calls

