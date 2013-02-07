%define major		0
%define libname		%mklibname json %{major}
%define develname	%mklibname json -d

Name:		json-c
Version:	0.10
Release:	3
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

# Hack from Fedora to get json_object_iterator.c compiled
sed -e 's/json_object.c/json_object.c json_object_iterator.c/' \
    -e 's/json_object.h/json_object.h json_object_iterator.h/' \
    -e 's/json_object.lo/json_object.lo json_object_iterator.lo/' \
    -i Makefile.in

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/json
%{_libdir}/pkgconfig/*.pc

