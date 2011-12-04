%define major		0
%define libname		%mklibname json %{major}
%define develname	%mklibname json -d

Name:		json-c
Version:	0.9
Release:	2
Summary:	JSON implementation in C
Group:		System/Libraries
URL:		http://oss.metaparadigm.com/%{name}
Source0:	http://oss.metaparadigm.com/%{name}/json-c-%{version}.tar.gz
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
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/json
%{_libdir}/pkgconfig/*.pc
