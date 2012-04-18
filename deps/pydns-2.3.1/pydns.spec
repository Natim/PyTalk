%define name pydns
%define version 2.3.1
%define release 2.4

Summary: Python DNS library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: Python license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Anthony Baxter and others <pydns-developer@lists.sourceforge.net>
Packager: Stuart D. Gathman <stuart@bmsi.com>
Url: http://pydns.sourceforge.net/

%description
Python DNS library

%prep
%setup

%build
python2.4 setup.py build

%install
python2.4 setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Tue May 22 2007 Stuart Gathman <stuart@bmsi.com> 2.3.1-1
- Bug fix release
