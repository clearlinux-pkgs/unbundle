#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unbundle
Version  : 0.1.6
Release  : 35
URL      : https://github.com/clearlinux/unbundle/releases/download/v0.1.6/unbundle-0.1.6.tar.gz
Source0  : https://github.com/clearlinux/unbundle/releases/download/v0.1.6/unbundle-0.1.6.tar.gz
Summary  : UNKNOWN
Group    : Development/Tools
License  : GPL-3.0
Requires: unbundle-bin = %{version}-%{release}
Requires: unbundle-license = %{version}-%{release}
Requires: unbundle-python = %{version}-%{release}
Requires: unbundle-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# unbundle
unbundle parses bundle and pundle definition files to recursively resolve
a complete list of all packages in a bundle.

%package bin
Summary: bin components for the unbundle package.
Group: Binaries
Requires: unbundle-license = %{version}-%{release}

%description bin
bin components for the unbundle package.


%package license
Summary: license components for the unbundle package.
Group: Default

%description license
license components for the unbundle package.


%package python
Summary: python components for the unbundle package.
Group: Default
Requires: unbundle-python3 = %{version}-%{release}

%description python
python components for the unbundle package.


%package python3
Summary: python3 components for the unbundle package.
Group: Default
Requires: python3-core

%description python3
python3 components for the unbundle package.


%prep
%setup -q -n unbundle-0.1.6
cd %{_builddir}/unbundle-0.1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582906821
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/unbundle
cp %{_builddir}/unbundle-0.1.6/LICENSE %{buildroot}/usr/share/package-licenses/unbundle/8624bcdae55baeef00cd11d5dfcfa60f68710a02
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unbundle

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/unbundle/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
