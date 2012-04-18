%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-pydns
Version:        2.3.1
Release:        1%{?dist}
Summary:        Python module for DNS (Domain Name Service).

Group:          Development/Languages
License:        Python Software Foundation License
URL:            http://pydns.sourceforge.net/
Source0:        pydns-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
#BuildRequires:  python-setuptools

%description
This is a another release of the pydns code, as originally written by
Guido van Rossum, and with a hopefully nicer API bolted over the
top of it by Anthony Baxter <anthony@interlink.com.au>.

This package contains a module (dnslib) that implements a DNS
(Domain Name Server) client, plus additional modules that define some
symbolic constants used by DNS (dnstype, dnsclass, dnsopcode).

%define namewithoutpythonprefix %(echo %{name} | sed 's/^python-//')
%prep
%setup -q -n %{namewithoutpythonprefix}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CREDITS.txt PKG-INFO README-guido.txt README.txt
%{python_sitelib}/DNS/*.py*

%changelog
* Tue May 22 2007 Stuart Gathman <stuart@bmsi.com> 2.3.1-1
- Bug fix release
* Tue Aug 29 2006 Sean Reifschneider <jafo@tummy.com> 2.3.0-1
- Initial RPM spec file.
