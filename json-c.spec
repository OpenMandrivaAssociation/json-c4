%define oldmaj 0
%define major 4
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%bcond_with crosscompile

Summary:	JSON implementation in C
Name:		json-c
Version:	0.13.1
Release:	4
Group:		System/Libraries
License:	MIT
Url:		https://github.com/json-c/json-c/wiki
Source0:	https://s3.amazonaws.com/json-c_releases/releases/%{name}-%{version}.tar.gz
# Cherry-picked from upstream.
# https://github.com/json-c/json-c/commit/da4b34355da023c439e96bc6ca31886cd69d6bdb
Patch0:         %{name}-0.13.1-parse_test_UTF8_BOM.patch
# https://github.com/json-c/json-c/commit/f8c632f579c71012f9aca81543b880a579f634fc
Patch1:         %{name}-0.13.1-fix_incorrect_casts_in_calls_to_ctype_functions.patch
# https://github.com/json-c/json-c/commit/8bd62177e796386fb6382db101c90b57b6138afe
Patch2:         %{name}-0.13.1-fix_typos.patch
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
Obsoletes:	%{_lib}json-devel < 0.11-2

%description -n %{devname}
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%prep
%autosetup -p1

%if %{with crosscompile}
export ac_cv_func_malloc_0_nonnull=yes
%endif

%build
sed -i -e "s:-Werror::" configure.ac
autoreconf -fiv
%configure \
	--disable-static \
	--enable-rdrand \
	--enable-shared \
	--enable-threading

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libjson-c.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
