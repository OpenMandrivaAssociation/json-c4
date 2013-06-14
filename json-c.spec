%define major 0
%define libname %mklibname json %{major}
%define devname %mklibname json -d
%bcond_with crosscompile

Name:		json-c
Version:	0.11
Release:	1
Summary:	JSON implementation in C
Group:		System/Libraries
License:	MIT
Url:		https://github.com/json-c/json-c/wiki
Source0:	https://github.com/downloads/json-c/json-c/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

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

%package -n %{devname}
Summary:	Development headers and libraries for %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	json-devel = %{version}-%{release}

%description -n %{devname}
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%prep
%setup -q

%if %{with crosscompile}
export ac_cv_func_malloc_0_nonnull=yes
%endif

%build
autoreconf -fi
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libjson.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/json
%{_libdir}/pkgconfig/*.pc

