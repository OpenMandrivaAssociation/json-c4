%define oldmaj 0
%define major 4
%define libname %mklibname json-c %{major}
%bcond_with crosscompile

Summary:	JSON implementation in C
Name:		json-c4
Version:	0.13.1
Release:	6
Group:		System/Libraries
License:	MIT
Url:		https://github.com/json-c/json-c/wiki
Source0:	https://s3.amazonaws.com/json-c_releases/releases/json-c-%{version}.tar.gz
# Cherry-picked from upstream.
# https://github.com/json-c/json-c/commit/da4b34355da023c439e96bc6ca31886cd69d6bdb
Patch0:         json-c-0.13.1-parse_test_UTF8_BOM.patch
# https://github.com/json-c/json-c/commit/f8c632f579c71012f9aca81543b880a579f634fc
Patch1:         json-c-0.13.1-fix_incorrect_casts_in_calls_to_ctype_functions.patch
# https://github.com/json-c/json-c/commit/8bd62177e796386fb6382db101c90b57b6138afe
Patch2:         json-c-0.13.1-fix_typos.patch
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

%prep
%autosetup -p1 -n json-c-%{version}

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
# No -devel files for compat packages
rm -rf %{buildroot}%{_libdir}/*.so %{buildroot}%{_includedir} %{buildroot}%{_libdir}/pkgconfig

%files -n %{libname}
%{_libdir}/libjson-c.so.%{major}*
