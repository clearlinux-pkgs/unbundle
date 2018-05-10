#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unbundle
Version  : 0.1.2
Release  : 5
URL      : https://github.com/clearlinux/unbundle/releases/download/v0.1.2/unbundle-0.1.2.tar.gz
Source0  : https://github.com/clearlinux/unbundle/releases/download/v0.1.2/unbundle-0.1.2.tar.gz
Summary  : UNKNOWN
Group    : Development/Tools
License  : GPL-3.0
Requires: unbundle-bin
Requires: unbundle-python3
Requires: unbundle-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# unbundle
unbundle parses bundle and pundle definition files to recursively resolve
a complete list of all packages in a bundle.

%package bin
Summary: bin components for the unbundle package.
Group: Binaries

%description bin
bin components for the unbundle package.


%package python
Summary: python components for the unbundle package.
Group: Default
Requires: unbundle-python3

%description python
python components for the unbundle package.


%package python3
Summary: python3 components for the unbundle package.
Group: Default
Requires: python3-core

%description python3
python3 components for the unbundle package.


%prep
%setup -q -n unbundle-0.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523997405
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unbundle

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
