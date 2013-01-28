%define major		0
%define libname		%mklibname json %{major}
%define develname	%mklibname json -d

Name:		json-c
Version:	0.10
Release:	1
Summary:	JSON implementation in C
Group:		System/Libraries
URL:		https://github.com/json-c/json-c/wiki
Source0:	https://github.com/downloads/json-c/json-c/json-c-%{version}.tar.gz
License:	MIT

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%package -n %{libname}
Summary:	JSON implementation in C
Group:		System/Libraries

%description -n %{libname}
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects. 

%package -n %{develname}
Summary:	Development headers and libraries for %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libjson-devel = %{version}-%{release}

%description -n %{develname}
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/json
%{_libdir}/pkgconfig/*.pc


%changelog
* Sun Dec 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9-2
+ Revision: 737610
- drop the static lib and the libtool *.la file
- various fixes

* Tue Sep 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-1
+ Revision: 701579
- update to new version 0.9

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-4mdv2011.0
+ Revision: 612514
- the mass rebuild of 2010.1 packages

* Sun May 09 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8-3mdv2010.1
+ Revision: 544275
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Feb 22 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdv2009.1
+ Revision: 343849
- 0.8

* Sun Dec 28 2008 Adam Williamson <awilliamson@mandriva.org> 0.7-2mdv2009.1
+ Revision: 320229
- devel requires lib
- import json-c


